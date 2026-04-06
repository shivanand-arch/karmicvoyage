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

    # API key: read from secrets/env only, never show in UI
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if hasattr(st, "secrets"):
        api_key = st.secrets.get("ANTHROPIC_API_KEY", api_key)
    if api_key:
        st.success("API key configured", icon="🔑")
    else:
        st.error("API key not configured. Set ANTHROPIC_API_KEY in Streamlit secrets.")

    model_choice = st.selectbox(
        "Model",
        ["claude-sonnet-4-6", "claude-opus-4-6"],
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

resumes = {}
failed_extract = []

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Select Role Framework")
    framework_name = st.selectbox(
        "Choose evaluation framework",
        get_framework_names(),
        help="This determines the scoring dimensions and weights",
    )
    framework = FRAMEWORKS[framework_name]

    # Leadership toggle — shown inline for frameworks that have the dimension
    has_leadership_dim = "leadership" in framework["dimensions"]
    if has_leadership_dim:
        is_leadership_role = st.toggle(
            "Leadership position?",
            value=True,
            key="leadership_toggle_setup",
            help="Turn off for IC roles (SE-1, SE-2, Sr. Engineer). Leadership weight goes to 0%.",
        )
        if is_leadership_role:
            leadership_level = st.select_slider(
                "How much leadership?",
                options=["Light (tech lead)", "Moderate (lead + mentoring)", "Heavy (EM / people mgr)"],
                value="Moderate (lead + mentoring)",
                key="leadership_level_setup",
            )
            leadership_weight_map = {
                "Light (tech lead)": 0.10,
                "Moderate (lead + mentoring)": 0.20,
                "Heavy (EM / people mgr)": 0.30,
            }
            st.session_state["leadership_weight"] = leadership_weight_map[leadership_level]
        else:
            st.caption("Leadership weight → 0% — ranking based on IC skills only")
            st.session_state["leadership_weight"] = 0.0
    else:
        st.session_state["leadership_weight"] = None  # not applicable

    # GenAI toggle — shown for frameworks that have the dimension
    has_genai_dim = "genai_expertise" in framework["dimensions"]
    if has_genai_dim:
        is_genai_role = st.toggle(
            "GenAI role? (CQA / Chatbot / Voice AI team)",
            value=framework["weights"].get("genai_expertise", 0) > 0,
            key="genai_toggle_setup",
            help="Turn on for GenAI team roles. Off for ECC, Platform, and other backend teams.",
        )
        if is_genai_role:
            st.session_state["genai_weight"] = 0.15
        else:
            st.caption("GenAI expertise weight → 0%")
            st.session_state["genai_weight"] = 0.0
    else:
        st.session_state["genai_weight"] = None  # not applicable

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
            resumes, failed_extract = extract_resumes_from_zip(resume_zip)
        st.success(f"✅ Extracted {len(resumes)} resumes")
        if failed_extract:
            st.warning(
                f"⚠️ {len(failed_extract)} files could not be read: "
                f"{', '.join(failed_extract[:5])}"
            )

        with st.expander(f"Preview extracted resumes ({len(resumes)})"):
            st.caption(
                "First ~3,500 characters of each resume are sent to the model for scoring."
            )
            for fname, text in list(resumes.items())[:5]:
                st.markdown(f"**{fname}** ({len(text)} chars)")
                st.text(text[:150] + "...")
                st.markdown("---")

st.markdown("---")


# ─────────────────────────────────────────────
# EVALUATION ENGINE
# ─────────────────────────────────────────────

def evaluate_single_resume(api_key, model, framework_key, jd_text, filename, resume_text):
    """Evaluate a single resume via Claude API. Returns parsed result dict.
    Creates its own Anthropic client per call for thread safety.
    """
    client = anthropic.Anthropic(api_key=api_key)
    prompt = build_evaluation_prompt(framework_key, jd_text, resume_text, filename)
    fw = FRAMEWORKS[framework_key]

    for attempt in range(MAX_RETRIES + 1):
        try:
            response = client.messages.create(
                model=model,
                max_tokens=2000,
                temperature=0.0,
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

if st.button(
    "🚀 Evaluate & Rank Resumes",
    type="primary",
    disabled=not (api_key and jd_text and resume_zip and len(resumes) > 0),
    use_container_width=True,
):
    if not api_key:
        st.error("Please enter your Anthropic API key in the sidebar")
        st.stop()
    if not jd_text:
        st.error("Please provide a Job Description")
        st.stop()
    if not len(resumes) > 0:
        st.error("Please upload a resume ZIP file")
        st.stop()

    st.subheader("Evaluating...")
    progress_bar = st.progress(0)
    status_text = st.empty()

    all_results = []
    total = len(resumes)
    completed = 0
    errors = 0

    # Evaluate in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_parallel) as executor:
        future_to_file = {
            executor.submit(
                evaluate_single_resume,
                api_key, model_choice, framework_name, jd_text, fname, text
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

    # Store results in session state for post-evaluation refinement
    st.session_state["eval_results"] = all_results
    st.session_state["eval_framework_name"] = framework_name

    st.success(f"✅ Evaluation complete! {len(all_results)} candidates ranked.")


# ─────────────────────────────────────────────
# DISPLAY RESULTS (from session state)
# ─────────────────────────────────────────────

if "eval_results" in st.session_state and st.session_state["eval_results"]:
    stored_fw_name = st.session_state.get("eval_framework_name", framework_name)
    stored_fw = FRAMEWORKS.get(stored_fw_name, framework)
    raw_results = st.session_state["eval_results"]
    dimensions = list(stored_fw["dimensions"].keys())

    # ── Refine Criteria Panel ────────────────
    st.markdown("---")
    st.subheader("5. Refine Criteria (adjust weights in real-time)")
    st.caption(
        "Drag the sliders to change dimension weights. "
        "Rankings recalculate instantly — no re-evaluation needed."
    )

    # Initialize adjusted weights from framework defaults
    if "adjusted_weights" not in st.session_state or st.session_state.get("_weights_fw") != stored_fw_name:
        st.session_state["adjusted_weights"] = dict(stored_fw["weights"])
        st.session_state["_weights_fw"] = stored_fw_name

    # Apply leadership weight from the setup toggle (section 1)
    ldr_weight = st.session_state.get("leadership_weight")
    if ldr_weight is not None and "leadership" in st.session_state["adjusted_weights"]:
        st.session_state["adjusted_weights"]["leadership"] = ldr_weight

    # Apply GenAI weight from the setup toggle (section 1)
    genai_weight = st.session_state.get("genai_weight")
    if genai_weight is not None and "genai_expertise" in st.session_state["adjusted_weights"]:
        st.session_state["adjusted_weights"]["genai_expertise"] = genai_weight

    adjusted_weights = {}
    weight_cols = st.columns(min(len(dimensions), 4))
    for idx, dim in enumerate(dimensions):
        col = weight_cols[idx % len(weight_cols)]
        label = dim.replace("_", " ").title()
        default_val = int(stored_fw["weights"][dim] * 100)
        current_val = int(st.session_state["adjusted_weights"].get(dim, stored_fw["weights"][dim]) * 100)
        adjusted_weights[dim] = col.slider(
            f"{label}",
            min_value=0,
            max_value=50,
            value=current_val,
            step=5,
            key=f"w_{dim}",
            help=stored_fw["dimensions"][dim][:120],
        ) / 100.0

    # Normalize weights so they sum to 1.0
    weight_sum = sum(adjusted_weights.values())
    if weight_sum > 0:
        normalized_weights = {k: v / weight_sum for k, v in adjusted_weights.items()}
    else:
        normalized_weights = {k: 1.0 / len(adjusted_weights) for k in adjusted_weights}

    st.session_state["adjusted_weights"] = adjusted_weights

    # Show normalized weights
    norm_summary = " · ".join(
        f"**{k.replace('_', ' ').title()}** {v:.0%}"
        for k, v in normalized_weights.items() if v > 0
    )
    st.caption(f"Normalized weights: {norm_summary}")

    reset_col, _ = st.columns([1, 3])
    with reset_col:
        if st.button("Reset to defaults", key="reset_weights"):
            st.session_state["adjusted_weights"] = dict(stored_fw["weights"])
            st.rerun()

    # ── Recalculate scores with adjusted weights ──
    display_results = []
    for r in raw_results:
        r_copy = dict(r)
        scores = r_copy.get("scores", {})
        r_copy["total_score"] = calculate_total(scores, normalized_weights)
        r_copy["verdict"] = get_verdict(r_copy["total_score"])
        display_results.append(r_copy)

    display_results.sort(key=lambda x: x.get("total_score", 0), reverse=True)

    # Build a modified framework dict with the adjusted weights for Excel export
    display_fw = dict(stored_fw)
    display_fw["weights"] = normalized_weights

    # ── Rankings ─────────────────────────────
    st.markdown("---")
    st.subheader("Rankings")

    from collections import Counter
    verdicts = Counter(r.get("verdict", "No") for r in display_results)

    stat_cols = st.columns(4)
    stat_cols[0].metric("Strong Yes", verdicts.get("Strong Yes", 0))
    stat_cols[1].metric("Yes", verdicts.get("Yes", 0))
    stat_cols[2].metric("Maybe", verdicts.get("Maybe", 0))
    stat_cols[3].metric("No", verdicts.get("No", 0))

    for i, r in enumerate(display_results):
        verdict = r.get("verdict", "No")
        color_map = {
            "Strong Yes": "🟢", "Yes": "🟡", "Maybe": "🟠", "No": "🔴"
        }
        icon = color_map.get(verdict, "⚪")

        with st.expander(
            f"{icon} #{i+1} — {r.get('name', 'Unknown')} | "
            f"Score: {r.get('total_score', 0):.2f} | {verdict} | "
            f"{r.get('current_role', 'N/A')} | {r.get('yoe', '?')} YOE",
            expanded=(i < 3),
        ):
            scores = r.get("scores", {})
            score_cols = st.columns(len(scores))
            for j, (dim, val) in enumerate(scores.items()):
                weight = normalized_weights.get(dim, 0)
                label = dim.replace("_", " ").title()
                score_cols[j].metric(f"{label} ({weight:.0%})", f"{val:.1f}")

            if "bonus_scores" in r:
                st.markdown("**Bonus Dimensions:**")
                for bd, val in r["bonus_scores"].items():
                    note = r.get("bonus_notes", {}).get(bd, "")
                    st.markdown(f"- **{bd.replace('_', ' ').title()}**: {val}/10 — {note}")

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

    # ── Download ─────────────────────────────
    st.subheader("📥 Download Results")
    excel_buffer = generate_excel(display_results, display_fw, stored_fw_name)

    safe_name = stored_fw_name.replace(" ", "_").replace("(", "").replace(")", "")
    filename = f"Exotel_{safe_name}_Screening_Results.xlsx"

    st.download_button(
        label=f"📥 Download Excel ({len(display_results)} candidates)",
        data=excel_buffer,
        file_name=filename,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        type="primary",
        use_container_width=True,
    )

    json_data = json.dumps(display_results, indent=2, ensure_ascii=False)
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
