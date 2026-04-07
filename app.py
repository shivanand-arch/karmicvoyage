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
from resume_processor import (
    extract_resumes_from_zip, extract_text_from_uploaded_file, extract_text_from_bytes,
)
from excel_generator import generate_excel
from trakstar_client import (
    create_session, fetch_openings, fetch_candidates,
    deduplicate, get_unique_stages, fetch_resume_bytes,
    get_opening_name, is_active_opening,
)


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
# TRAKSTAR CONFIG (from secrets/env)
# ─────────────────────────────────────────────

def _get_secret(key, default=""):
    """Read from Streamlit secrets or env var. Handles flat keys and [section] nesting."""
    # Try top-level st.secrets[key]
    try:
        val = st.secrets[key]
        if val:
            return str(val)
    except (KeyError, FileNotFoundError, AttributeError):
        pass
    # Try nested under common sections (in case TOML ordering put them under [auth] etc.)
    for section in ("auth", "trakstar", "default"):
        try:
            val = st.secrets[section][key]
            if val:
                return str(val)
        except (KeyError, FileNotFoundError, AttributeError, TypeError):
            pass
    # Fallback to env var
    return os.environ.get(key, default)

TRAKSTAR_API_KEY = _get_secret("TRAKSTAR_API_KEY")
TRAKSTAR_COOKIE = _get_secret("TRAKSTAR_COOKIE")
TRAKSTAR_SUBDOMAIN = _get_secret("TRAKSTAR_SUBDOMAIN", "exotel")


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

    st.subheader("2. Job Description")
    jd_file = st.file_uploader("Upload JD (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])
    jd_text = ""
    if jd_file:
        jd_text = extract_text_from_uploaded_file(jd_file)
        if jd_text:
            st.success(f"Extracted {len(jd_text)} chars from JD")
            with st.expander("Preview JD text"):
                st.text(jd_text[:500] + "...")

with col2:
    st.subheader("3. Resumes")
    resume_source = st.radio(
        "Resume source",
        ["Upload ZIP", "Pull from Trakstar"],
        horizontal=True,
        help="Upload a ZIP of resumes, or pull directly from Trakstar Hire",
    )

    if resume_source == "Upload ZIP":
        resume_zip = st.file_uploader(
            "Upload ZIP file containing resumes",
            type=["zip"],
            help="ZIP containing PDF, DOCX, or TXT resume files",
        )

        if resume_zip:
            with st.spinner("Extracting resumes..."):
                resumes, failed_extract = extract_resumes_from_zip(resume_zip)
            st.success(f"Extracted {len(resumes)} resumes")
            if failed_extract:
                st.warning(
                    f"{len(failed_extract)} files could not be read: "
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
    else:
        # ── Trakstar Pull ────────────────────────
        tk_has_auth = bool(TRAKSTAR_API_KEY or TRAKSTAR_COOKIE)

        if not tk_has_auth:
            st.warning(
                "Trakstar credentials not configured. "
                "Set `TRAKSTAR_API_KEY` in `.streamlit/secrets.toml` or environment variables."
            )
        else:
            try:
                tk_session, tk_base = create_session(
                    TRAKSTAR_SUBDOMAIN, TRAKSTAR_API_KEY, TRAKSTAR_COOKIE
                )

                # Cache openings in session state
                if "tk_openings" not in st.session_state:
                    with st.spinner("Fetching positions from Trakstar..."):
                        st.session_state.tk_openings = fetch_openings(tk_session, tk_base)

                tk_openings = st.session_state.tk_openings
                tk_published = [o for o in tk_openings if is_active_opening(o)]

                if not tk_published:
                    st.error("No active openings found. Check your credentials.")
                else:
                    # Build display names for all active openings
                    tk_display_names = [
                        get_opening_name(o) for o in tk_published
                    ]

                    tk_selected_name = st.selectbox(
                        f"Select or type a position ({len(tk_published)} published)",
                        options=[""] + tk_display_names,
                        format_func=lambda x: "Type or select a position..." if x == "" else x,
                        key="tk_position",
                    )

                    # If nothing selected from dropdown, allow free-text search
                    if not tk_selected_name:
                        tk_keyword = st.text_input(
                            "Or search by keyword",
                            placeholder="e.g. backend, success, sales, CSM",
                            key="tk_search",
                        )
                        if tk_keyword:
                            matched = [
                                o for o in tk_published
                                if tk_keyword.lower() in get_opening_name(o).lower()
                            ]
                            if not matched:
                                st.warning(f"No positions match \"{tk_keyword}\"")
                            elif len(matched) == 1:
                                tk_selected_name = get_opening_name(matched[0])
                                st.success(f"Matched: **{tk_selected_name}**")
                            else:
                                match_names = [
                                    get_opening_name(o) for o in matched
                                ]
                                tk_selected_name = st.selectbox(
                                    f"{len(matched)} matches — pick one",
                                    match_names,
                                    key="tk_match_pick",
                                )

                    # Resolve selection to opening object
                    tk_selected = None
                    if tk_selected_name:
                        tk_selected = next(
                            (o for o in tk_published
                             if get_opening_name(o) == tk_selected_name),
                            None,
                        )

                    if tk_selected:
                        # Fetch candidates for stage filter
                        tk_cache_key = f"tk_cands_{tk_selected['id']}"
                        if tk_cache_key not in st.session_state:
                            with st.spinner("Loading candidates..."):
                                raw_cands = fetch_candidates(tk_session, tk_base, tk_selected["id"])
                                st.session_state[tk_cache_key] = deduplicate(raw_cands)

                        tk_all_cands = st.session_state[tk_cache_key]
                        tk_stages = get_unique_stages(tk_all_cands)

                        tk_stage = st.selectbox("Filter by stage", ["All stages"] + tk_stages, key="tk_stage")
                        tk_limit = st.number_input("Max candidates (0 = all)", min_value=0, value=0, step=10, key="tk_limit")

                        # Apply filters
                        tk_cands = tk_all_cands
                        if tk_stage != "All stages":
                            sl = tk_stage.lower()
                            tk_cands = [
                                c for c in tk_cands
                                if sl in ((c.get("current_stage") or {}).get("name", "").lower()
                                          or (c.get("stage") or "").lower())
                            ]
                        if tk_limit > 0:
                            tk_cands = tk_cands[:tk_limit]

                        st.info(f"**{len(tk_cands)}** candidates ready (out of {len(tk_all_cands)} total)")

                        if st.button(f"Pull {len(tk_cands)} Resumes from Trakstar", key="tk_pull"):
                            progress = st.progress(0)
                            status = st.empty()
                            downloaded = 0
                            skipped = 0

                            for i, c in enumerate(tk_cands):
                                cand_name = f"{c.get('first_name', '')} {c.get('last_name', '')}".strip() or str(c["id"])
                                progress.progress((i + 1) / len(tk_cands))
                                status.text(f"Downloading {i + 1}/{len(tk_cands)}: {cand_name}")

                                try:
                                    fname, data = fetch_resume_bytes(tk_session, tk_base, c["id"])
                                    if fname and data:
                                        safe_name = "".join(ch for ch in cand_name if ch not in r'\/:*?"<>|')
                                        display_name = f"{safe_name} - {fname}"
                                        text = extract_text_from_bytes(fname, data)
                                        if len(text.strip()) > 20:
                                            resumes[display_name] = text
                                            downloaded += 1
                                        else:
                                            failed_extract.append(display_name)
                                            skipped += 1
                                    else:
                                        skipped += 1
                                except Exception:
                                    skipped += 1

                            progress.progress(1.0)
                            status.empty()
                            st.success(f"Pulled **{downloaded}** resumes ({skipped} skipped — no resume or unreadable)")

                            if resumes:
                                with st.expander(f"Preview pulled resumes ({len(resumes)})"):
                                    for fname, text in list(resumes.items())[:5]:
                                        st.markdown(f"**{fname}** ({len(text)} chars)")
                                        st.text(text[:150] + "...")
                                        st.markdown("---")

            except Exception as e:
                st.error(f"Trakstar error: {e}")

st.markdown("---")


# ─────────────────────────────────────────────
# EVALUATION ENGINE
# ─────────────────────────────────────────────

def evaluate_single_resume(api_key, model, framework_key, jd_text, filename, resume_text, custom_notes=""):
    """Evaluate a single resume via Claude API. Returns parsed result dict.
    Creates its own Anthropic client per call for thread safety.
    """
    client = anthropic.Anthropic(api_key=api_key)
    prompt = build_evaluation_prompt(framework_key, jd_text, resume_text, filename)
    if custom_notes:
        prompt += f"\n\nADDITIONAL EVALUATION INSTRUCTIONS FROM HIRING MANAGER:\n{custom_notes}"
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
    disabled=not (api_key and jd_text and len(resumes) > 0),
    use_container_width=True,
):
    if not api_key:
        st.error("Please enter your Anthropic API key in the sidebar")
        st.stop()
    if not jd_text:
        st.error("Please provide a Job Description")
        st.stop()
    if not len(resumes) > 0:
        st.error("Please provide resumes (upload a ZIP or pull from Trakstar)")
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

    # Store results + context in session state for post-evaluation refinement
    st.session_state["eval_results"] = all_results
    st.session_state["eval_framework_name"] = framework_name
    st.session_state["eval_resumes"] = dict(resumes)
    st.session_state["eval_jd_text"] = jd_text
    st.session_state["eval_model"] = model_choice
    st.session_state["eval_api_key"] = api_key

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
        "Adjust how much each dimension matters. "
        "**Total score and ranking order update instantly** — per-dimension AI scores stay fixed."
    )

    # Initialize adjusted weights from framework defaults
    if "adjusted_weights" not in st.session_state or st.session_state.get("_weights_fw") != stored_fw_name:
        st.session_state["adjusted_weights"] = dict(stored_fw["weights"])
        st.session_state["_weights_fw"] = stored_fw_name

    # Apply leadership weight from the setup toggle (section 1)
    ldr_weight = st.session_state.get("leadership_weight")
    if ldr_weight is not None and "leadership" in st.session_state["adjusted_weights"]:
        st.session_state["adjusted_weights"]["leadership"] = ldr_weight

    adjusted_weights = {}
    weight_cols = st.columns(min(len(dimensions), 4))
    for idx, dim in enumerate(dimensions):
        col = weight_cols[idx % len(weight_cols)]
        label = dim.replace("_", " ").title()
        current_val = int(st.session_state["adjusted_weights"].get(dim, stored_fw["weights"][dim]) * 100)
        adjusted_weights[dim] = col.slider(
            f"{label} (%)",
            min_value=0,
            max_value=100,
            value=current_val,
            step=5,
            key=f"w_{dim}",
            help=stored_fw["dimensions"][dim][:120],
        ) / 100.0

    # Show total and warn if not 100%
    weight_total_pct = int(round(sum(adjusted_weights.values()) * 100))
    if weight_total_pct == 100:
        st.success(f"Total: **{weight_total_pct}%**")
    elif weight_total_pct > 100:
        st.error(f"Total: **{weight_total_pct}%** — exceeds 100%. Please reduce some weights.")
    elif weight_total_pct == 0:
        st.error("Total: **0%** — at least one dimension must have weight.")
    else:
        st.warning(f"Total: **{weight_total_pct}%** — does not add up to 100%.")

    # Use weights as-is (percentages), normalize only for calculation
    st.session_state["adjusted_weights"] = adjusted_weights
    weight_sum = sum(adjusted_weights.values())
    if weight_sum > 0:
        normalized_weights = {k: v / weight_sum for k, v in adjusted_weights.items()}
    else:
        normalized_weights = {k: 1.0 / len(adjusted_weights) for k in adjusted_weights}

    reset_col, _ = st.columns([1, 3])
    with reset_col:
        if st.button("Reset to defaults", key="reset_weights"):
            st.session_state["adjusted_weights"] = dict(stored_fw["weights"])
            st.rerun()

    # ── Refine evaluation criteria text box ──
    st.markdown("**Update evaluation criteria**")
    refine_notes = st.text_area(
        "Add or change evaluation instructions",
        height=100,
        placeholder="e.g. 'Prefer candidates with startup experience', 'Must have Kubernetes knowledge', 'Penalize job-hoppers with <1yr stints', 'Bonus for open-source contributions'...",
        help="These notes will be sent to the AI along with the original JD to re-score all resumes.",
        key="refine_notes",
    )

    if st.button(
        "🔄 Re-evaluate with updated criteria",
        disabled=not refine_notes.strip(),
        help="Re-runs AI evaluation on all resumes with your updated instructions. This uses API calls.",
        key="re_evaluate_btn",
    ):
        stored_resumes = st.session_state.get("eval_resumes", {})
        stored_jd = st.session_state.get("eval_jd_text", "")
        stored_model = st.session_state.get("eval_model", "claude-sonnet-4-6")
        stored_api_key = st.session_state.get("eval_api_key", "")

        if not stored_resumes or not stored_api_key:
            st.error("Missing evaluation context. Please run the initial evaluation first.")
        else:
            re_progress = st.progress(0)
            re_status = st.empty()
            re_results = []
            total = len(stored_resumes)
            completed = 0

            with concurrent.futures.ThreadPoolExecutor(max_workers=max_parallel) as executor:
                future_to_file = {
                    executor.submit(
                        evaluate_single_resume,
                        stored_api_key, stored_model, stored_fw_name,
                        stored_jd, fname, text, refine_notes.strip()
                    ): fname
                    for fname, text in stored_resumes.items()
                }
                for future in concurrent.futures.as_completed(future_to_file):
                    fname = future_to_file[future]
                    completed += 1
                    try:
                        result = future.result()
                        re_results.append(result)
                    except Exception as e:
                        re_results.append({
                            "name": fname, "file": fname,
                            "current_role": "Error", "yoe": 0,
                            "scores": {k: 0 for k in stored_fw["dimensions"]},
                            "total_score": 0, "verdict": "No",
                            "key_strengths": [],
                            "key_concerns": [str(e)[:100]],
                            "evidence_summary": f"Error: {str(e)[:100]}",
                        })
                    re_progress.progress(completed / total)
                    re_status.text(f"Re-evaluated {completed}/{total} resumes")

            re_results.sort(key=lambda x: x.get("total_score", 0), reverse=True)
            st.session_state["eval_results"] = re_results
            raw_results = re_results
            st.success("✅ Re-evaluation complete with updated criteria!")
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

    # ── Quick-glance ranking table (updates live with slider changes) ──
    verdict_icons = {"Strong Yes": "🟢", "Yes": "🟡", "Maybe": "🟠", "No": "🔴"}
    table_rows = []
    for i, r in enumerate(display_results):
        v = r.get("verdict", "No")
        table_rows.append({
            "Rank": i + 1,
            "Candidate": r.get("name", "Unknown"),
            "Weighted Total": round(r.get("total_score", 0), 2),
            "Verdict": f"{verdict_icons.get(v, '⚪')} {v}",
            "Role": r.get("current_role", "N/A"),
            "YOE": r.get("yoe", "?"),
        })
    st.dataframe(table_rows, use_container_width=True, hide_index=True)

    # ── Detailed cards ──
    for i, r in enumerate(display_results):
        verdict = r.get("verdict", "No")
        icon = verdict_icons.get(verdict, "⚪")

        with st.expander(
            f"{icon} #{i+1} — {r.get('name', 'Unknown')} | "
            f"Weighted Total: {r.get('total_score', 0):.2f} | {verdict} | "
            f"{r.get('current_role', 'N/A')} | {r.get('yoe', '?')} YOE",
            expanded=(i < 3),
        ):
            # Show weighted contribution per dimension
            scores = r.get("scores", {})
            active_dims = [d for d in scores if normalized_weights.get(d, 0) > 0]
            inactive_dims = [d for d in scores if normalized_weights.get(d, 0) == 0]

            if active_dims:
                score_cols = st.columns(min(len(active_dims), 4))
                for j, dim in enumerate(active_dims):
                    col = score_cols[j % len(score_cols)]
                    val = scores[dim]
                    weight = normalized_weights.get(dim, 0)
                    contribution = val * weight
                    label = dim.replace("_", " ").title()
                    col.metric(
                        f"{label} ({weight:.0%})",
                        f"{val:.1f}",
                        delta=f"→ {contribution:.2f} weighted",
                        delta_color="off",
                    )

            if inactive_dims:
                with st.expander("Dimensions with 0% weight (scored but not counted)"):
                    zero_cols = st.columns(min(len(inactive_dims), 4))
                    for j, dim in enumerate(inactive_dims):
                        col = zero_cols[j % len(zero_cols)]
                        val = scores[dim]
                        label = dim.replace("_", " ").title()
                        col.metric(f"{label} (0%)", f"{val:.1f}")

            # Bonus dimensions — with clear labeling
            if "bonus_scores" in r:
                st.markdown("**Bonus Dimensions** *(scored separately — NOT included in total score)*")
                for bd, val in r["bonus_scores"].items():
                    note = r.get("bonus_notes", {}).get(bd, "")
                    label = bd.replace("_", " ").title()
                    st.markdown(f"- **{label}**: {val}/10 — {note}")

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
