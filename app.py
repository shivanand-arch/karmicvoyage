"""
Exotel Resume Screener — Internal Tool
Upload JDs + Resume ZIPs → Get ranked Excel output.
Powered by Claude API with Exotel's evaluation frameworks baked in.
"""

import os
import json
import time
import concurrent.futures
import streamlit as st
import anthropic

from frameworks import (
    FRAMEWORKS, get_framework_names, build_evaluation_prompt,
    calculate_total, get_verdict,
)
from resume_processor import extract_resumes_from_zip, extract_text_from_uploaded_file
from excel_generator import generate_excel


# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────

MODEL = "claude-sonnet-4-5-20250929"  # or claude-opus-4-5-20251101 for higher quality
MAX_CONCURRENT = 5  # parallel API calls
MAX_RETRIES = 2

st.set_page_config(
    page_title="Exotel Resume Screener",
    page_icon="📋",
    layout="wide",
)


# ─────────────────────────────────────────────
# SIDEBAR: API KEY + SETTINGS
# ─────────────────────────────────────────────

with st.sidebar:
    st.image("https://www.exotel.com/wp-content/themes/flavor-jeera/assets/images/logo.svg", width=150)
    st.title("⚙️ Settings")

    api_key = st.text_input(
        "Anthropic API Key",
        type="password",
        value=os.environ.get("ANTHROPIC_API_KEY", ""),
        help="Get yours at console.anthropic.com",
    )

    model_choice = st.selectbox(
        "Model",
        ["claude-sonnet-4-5-20250929", "claude-opus-4-5-20251101"],
        index=0,
        help="Opus = higher quality but slower & more expensive. Sonnet = recommended for most uses.",
    )

    max_parallel = st.slider("Parallel evaluations", 1, 10, MAX_CONCURRENT)

    st.markdown("---")
    st.markdown("**Evaluation Frameworks**")
    for name in get_framework_names():
        fw = FRAMEWORKS[name]
        with st.expander(name, expanded=False):
            st.caption(fw["description"])
            for dim, desc in fw["dimensions"].items():
                weight = fw["weights"][dim]
                st.markdown(f"- **{dim.replace('_', ' ').title()}** ({weight:.0%}): {desc[:80]}...")


# ─────────────────────────────────────────────
# MAIN UI
# ─────────────────────────────────────────────

st.title("📋 Exotel Resume Screener")
st.caption("Upload a JD + resume ZIP → Get AI-powered ranked Excel output")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Select Role Framework")
    framework_name = st.selectbox(
        "Choose evaluation framework",
        get_framework_names(),
        help="This determines the scoring dimensions and weights",
    )
    framework = FRAMEWORKS[framework_name]

    st.subheader("2. Job Description")
    jd_source = st.radio("JD source", ["Paste text", "Upload file"], horizontal=True)

    if jd_source == "Paste text":
        jd_text = st.text_area(
            "Paste JD here",
            height=200,
            placeholder="Paste the full job description...",
        )
    else:
        jd_file = st.file_uploader("Upload JD (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])
        jd_text = ""
        if jd_file:
            jd_text = extract_text_from_uploaded_file(jd_file)
            if jd_text:
                st.success(f"Extracted {len(jd_text)} chars from JD")
                with st.expander("Preview JD text"):
                    st.text(jd_text[:500] + "...")

with col2:
    st.subheader("3. Upload Resumes")
    resume_zip = st.file_uploader(
        "Upload ZIP file containing resumes",
        type=["zip"],
        help="ZIP containing PDF, DOCX, or TXT resume files",
    )

    if resume_zip:
        with st.spinner("Extracting resumes..."):
            resumes, failed = extract_resumes_from_zip(resume_zip)
        st.success(f"✅ Extracted {len(resumes)} resumes")
        if failed:
            st.warning(f"⚠️ {len(failed)} files could not be read: {', '.join(failed[:5])}")

        with st.expander(f"Preview extracted resumes ({len(resumes)})"):
            for fname, text in list(resumes.items())[:5]:
                st.markdown(f"**{fname}** ({len(text)} chars)")
                st.text(text[:150] + "...")
                st.markdown("---")

st.markdown("---")


# ─────────────────────────────────────────────
# EVALUATION ENGINE
# ─────────────────────────────────────────────

def evaluate_single_resume(client, model, framework_key, jd_text, filename, resume_text):
    """Evaluate a single resume via Claude API. Returns parsed result dict."""
    prompt = build_evaluation_prompt(framework_key, jd_text, resume_text, filename)
    fw = FRAMEWORKS[framework_key]

    for attempt in range(MAX_RETRIES + 1):
        try:
            response = client.messages.create(
                model=model,
                max_tokens=1500,
                temperature=0.1,
                messages=[{"role": "user", "content": prompt}],
            )
            text = response.content[0].text.strip()

            # Clean potential markdown wrapping
            if text.startswith("```"):
                text = text.split("\n", 1)[1] if "\n" in text else text[3:]
                if text.endswith("```"):
                    text = text[:-3]
                text = text.strip()

            result = json.loads(text)

            # Recalculate total with correct weights for consistency
            scores = result.get("scores", {})
            result["total_score"] = calculate_total(scores, fw["weights"])
            result["verdict"] = get_verdict(result["total_score"])
            result["file"] = filename

            return result

        except json.JSONDecodeError:
            if attempt < MAX_RETRIES:
                time.sleep(1)
                continue
            return {
                "name": filename.replace(".pdf", "").replace("_", " "),
                "file": filename,
                "current_role": "Parse error",
                "yoe": 0,
                "scores": {k: 0 for k in fw["dimensions"]},
                "total_score": 0,
                "verdict": "No",
                "key_strengths": [],
                "key_concerns": ["AI evaluation failed to parse"],
                "evidence_summary": "Evaluation failed after retries",
            }
        except Exception as e:
            if attempt < MAX_RETRIES:
                time.sleep(2)
                continue
            return {
                "name": filename.replace(".pdf", "").replace("_", " "),
                "file": filename,
                "current_role": "API error",
                "yoe": 0,
                "scores": {k: 0 for k in fw["dimensions"]},
                "total_score": 0,
                "verdict": "No",
                "key_strengths": [],
                "key_concerns": [f"API error: {str(e)[:100]}"],
                "evidence_summary": f"Evaluation failed: {str(e)[:100]}",
            }


# ─────────────────────────────────────────────
# RUN EVALUATION
# ─────────────────────────────────────────────

can_run = (
    api_key
    and jd_text
    and resume_zip
    and "resumes" in dir()
    and len(resumes) > 0
)

# Check if we have resumes loaded
has_resumes = resume_zip is not None and "resumes" in dir() and len(locals().get("resumes", {})) > 0

if st.button(
    "🚀 Evaluate & Rank Resumes",
    type="primary",
    disabled=not (api_key and jd_text and has_resumes),
    use_container_width=True,
):
    if not api_key:
        st.error("Please enter your Anthropic API key in the sidebar")
        st.stop()
    if not jd_text:
        st.error("Please provide a Job Description")
        st.stop()
    if not has_resumes:
        st.error("Please upload a resume ZIP file")
        st.stop()

    client = anthropic.Anthropic(api_key=api_key)

    st.subheader("Evaluating...")
    progress_bar = st.progress(0)
    status_text = st.empty()
    results_container = st.empty()

    all_results = []
    total = len(resumes)
    completed = 0
    errors = 0

    # Evaluate in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_parallel) as executor:
        future_to_file = {
            executor.submit(
                evaluate_single_resume,
                client, model_choice, framework_name, jd_text, fname, text
            ): fname
            for fname, text in resumes.items()
        }

        for future in concurrent.futures.as_completed(future_to_file):
            fname = future_to_file[future]
            completed += 1
            try:
                result = future.result()
                all_results.append(result)
                if result.get("current_role") in ("Parse error", "API error"):
                    errors += 1
            except Exception as e:
                errors += 1
                all_results.append({
                    "name": fname,
                    "file": fname,
                    "current_role": "Error",
                    "yoe": 0,
                    "scores": {k: 0 for k in framework["dimensions"]},
                    "total_score": 0,
                    "verdict": "No",
                    "key_strengths": [],
                    "key_concerns": [str(e)[:100]],
                    "evidence_summary": f"Error: {str(e)[:100]}",
                })

            progress_bar.progress(completed / total)
            status_text.text(
                f"Evaluated {completed}/{total} resumes "
                f"({errors} errors)"
            )

    # Sort by score
    all_results.sort(key=lambda x: x.get("total_score", 0), reverse=True)

    st.success(f"✅ Evaluation complete! {len(all_results)} candidates ranked.")

    # ── Display results table ────────────────
    st.subheader("Rankings")

    # Quick stats
    from collections import Counter
    verdicts = Counter(r["verdict"] for r in all_results)

    stat_cols = st.columns(4)
    stat_cols[0].metric("Strong Yes", verdicts.get("Strong Yes", 0))
    stat_cols[1].metric("Yes", verdicts.get("Yes", 0))
    stat_cols[2].metric("Maybe", verdicts.get("Maybe", 0))
    stat_cols[3].metric("No", verdicts.get("No", 0))

    # Results table
    for i, r in enumerate(all_results):
        verdict = r.get("verdict", "No")
        color_map = {
            "Strong Yes": "🟢", "Yes": "🟡", "Maybe": "🟠", "No": "🔴"
        }
        icon = color_map.get(verdict, "⚪")

        with st.expander(
            f"{icon} #{i+1} — {r.get('name', 'Unknown')} | "
            f"Score: {r.get('total_score', 0):.2f} | {verdict} | "
            f"{r.get('current_role', 'N/A')} | {r.get('yoe', '?')} YOE",
            expanded=(i < 3),  # Auto-expand top 3
        ):
            # Scores
            scores = r.get("scores", {})
            score_cols = st.columns(len(scores))
            for j, (dim, val) in enumerate(scores.items()):
                weight = framework["weights"].get(dim, 0)
                label = dim.replace("_", " ").title()
                score_cols[j].metric(f"{label} ({weight:.0%})", f"{val:.1f}")

            # Bonus scores
            if "bonus_scores" in r:
                st.markdown("**Bonus Dimensions:**")
                for bd, val in r["bonus_scores"].items():
                    note = r.get("bonus_notes", {}).get(bd, "")
                    st.markdown(f"- **{bd.replace('_', ' ').title()}**: {val}/10 — {note}")

            # Strengths & concerns
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("**Strengths:**")
                for s in r.get("key_strengths", []):
                    st.markdown(f"- {s}")
            with col_b:
                st.markdown("**Concerns:**")
                for c in r.get("key_concerns", []):
                    st.markdown(f"- {c}")

            st.caption(r.get("evidence_summary", ""))

    # ── Generate Excel download ──────────────
    st.subheader("📥 Download Results")
    excel_buffer = generate_excel(all_results, framework, framework_name)

    safe_name = framework_name.replace(" ", "_").replace("(", "").replace(")", "")
    filename = f"Exotel_{safe_name}_Screening_Results.xlsx"

    st.download_button(
        label=f"📥 Download Excel ({len(all_results)} candidates)",
        data=excel_buffer,
        file_name=filename,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        type="primary",
        use_container_width=True,
    )

    # Also save raw JSON for debugging
    json_data = json.dumps(all_results, indent=2, ensure_ascii=False)
    st.download_button(
        label="📋 Download raw JSON",
        data=json_data,
        file_name=f"Exotel_{safe_name}_raw_results.json",
        mime="application/json",
    )


# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────

st.markdown("---")
st.caption(
    "Exotel Resume Screener v1.0 · Powered by Claude API · "
    "Evaluation frameworks maintained by Exotel HR"
)
