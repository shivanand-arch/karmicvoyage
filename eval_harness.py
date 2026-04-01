"""
Evaluation harness for the resume screener optimization loop.
Extracts resumes from a ZIP, runs evaluations, and computes a composite quality score.

Metrics:
  1. JSON parse success rate (0-100)
  2. Score discrimination — std dev of total scores (higher = better differentiation)
  3. Evidence specificity — avg tech keywords in evidence_summary
  4. Name extraction accuracy — does extracted name match filename hints?
  5. Completeness — all required fields present, non-empty lists
  6. Calibration — per-candidate score spread across dimensions (not all same value)

Composite = weighted sum, scaled 0-100.
"""

import json
import os
import re
import statistics
import sys
import time
import zipfile
import tempfile

import anthropic
import pdfplumber

# Add project root to path
sys.path.insert(0, os.path.dirname(__file__))
from frameworks import FRAMEWORKS, build_evaluation_prompt, build_evaluation_prompt_split, calculate_total, get_verdict


# ── Config ────────────────────────────────────
FRAMEWORK_KEY = "Backend Engineer (SE-1 to Sr. EM)"
MODEL = "claude-sonnet-4-6"
MAX_RETRIES = 2

# Metric weights (sum to 1.0)
METRIC_WEIGHTS = {
    "json_parse":       0.20,
    "discrimination":   0.20,
    "evidence":         0.20,
    "name_accuracy":    0.15,
    "completeness":     0.15,
    "calibration":      0.10,
}


# ── Resume extraction (standalone, no Streamlit) ────
def extract_resumes_from_zip_path(zip_path: str) -> dict:
    """Extract {filename: text} from a ZIP file on disk."""
    resumes = {}
    with tempfile.TemporaryDirectory() as tmpdir:
        extract_dir = os.path.join(tmpdir, "extracted")
        os.makedirs(extract_dir)
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(extract_dir)
        for root, dirs, files in os.walk(extract_dir):
            if "__MACOSX" in root:
                continue
            for fname in sorted(files):
                if fname.startswith(".") or fname.startswith("._"):
                    continue
                ext = os.path.splitext(fname)[1].lower()
                if ext != ".pdf":
                    continue
                fpath = os.path.join(root, fname)
                text = ""
                try:
                    with pdfplumber.open(fpath) as pdf:
                        for page in pdf.pages:
                            text += (page.extract_text() or "") + "\n"
                except Exception:
                    pass
                if len(text.strip()) > 20:
                    resumes[fname] = text[:4000]
    return resumes


def extract_jd_from_pdf(pdf_path: str) -> str:
    """Extract text from a JD PDF."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += (page.extract_text() or "") + "\n"
    return text.strip()


# ── Single resume evaluation ────────────────
def evaluate_resume(client, jd_text, framework_key, filename, resume_text):
    """Evaluate a single resume. Returns (result_dict, was_parsed_ok)."""
    prompt = build_evaluation_prompt(framework_key, jd_text, resume_text, filename)
    fw = FRAMEWORKS[framework_key]

    for attempt in range(MAX_RETRIES + 1):
        try:
            response = client.messages.create(
                model=MODEL,
                max_tokens=2000,
                temperature=0.0,
                messages=[{"role": "user", "content": prompt}],
            )
            text = response.content[0].text.strip()
            if text.startswith("```"):
                text = text.split("\n", 1)[1] if "\n" in text else text[3:]
                if text.endswith("```"):
                    text = text[:-3]
                text = text.strip()

            result = json.loads(text)
            scores = result.get("scores", {})
            result["total_score"] = calculate_total(scores, fw["weights"])
            result["verdict"] = get_verdict(result["total_score"])
            result["file"] = filename
            return result, True

        except json.JSONDecodeError:
            if attempt < MAX_RETRIES:
                time.sleep(1)
                continue
            return {"file": filename, "parse_error": True}, False
        except Exception as e:
            if attempt < MAX_RETRIES:
                time.sleep(2)
                continue
            return {"file": filename, "api_error": str(e)[:100]}, False


# ── Metric calculators ──────────────────────
def metric_json_parse(results, parsed_flags):
    """% of resumes that returned valid JSON."""
    if not parsed_flags:
        return 0
    return (sum(parsed_flags) / len(parsed_flags)) * 100


def metric_discrimination(results):
    """Std dev of total scores, normalized to 0-100. Higher = better spread."""
    scores = [r.get("total_score", 0) for r in results if "total_score" in r]
    if len(scores) < 2:
        return 0
    sd = statistics.stdev(scores)
    # Max realistic std dev for 1-10 scale is ~3.0; normalize
    return min(sd / 3.0 * 100, 100)


def metric_evidence(results):
    """Avg count of tech keywords in evidence_summary, normalized 0-100."""
    tech_keywords = {
        "python", "go", "golang", "java", "kafka", "redis", "aws", "docker",
        "kubernetes", "k8s", "postgresql", "mongodb", "mysql", "langchain",
        "langgraph", "rag", "llm", "microservices", "api", "rest", "distributed",
        "agent", "vector", "elasticsearch", "aerospike", "voicebot", "asr", "tts",
    }
    counts = []
    for r in results:
        summary = (r.get("evidence_summary", "") + " ".join(r.get("key_strengths", []))).lower()
        count = sum(1 for kw in tech_keywords if kw in summary)
        counts.append(count)
    if not counts:
        return 0
    avg = statistics.mean(counts)
    # 8+ keywords is excellent
    return min(avg / 8.0 * 100, 100)


def metric_name_accuracy(results, filenames):
    """% of results where extracted name roughly matches filename."""
    if not results:
        return 0
    matches = 0
    for r, fname in zip(results, filenames):
        name = r.get("name", "").lower().replace(" ", "")
        # Extract name hint from filename like "Naukri_ShubhamGoyal[4y_5m].pdf"
        fname_clean = fname.replace("Naukri_", "").replace("Updated_Resume ", "")
        fname_clean = re.sub(r"\[.*?\]", "", fname_clean).replace(".pdf", "").replace("_", "").lower()
        # Check if there's meaningful overlap
        if len(fname_clean) > 3 and (fname_clean[:5] in name or name[:5] in fname_clean):
            matches += 1
        elif len(name) > 2 and name != "unknown" and name != "full name":
            matches += 0.5  # Got a name, just doesn't match filename pattern
    return (matches / len(results)) * 100


def metric_completeness(results):
    """% of required fields present and non-empty."""
    required = ["name", "current_role", "yoe", "scores", "key_strengths", "key_concerns", "evidence_summary"]
    if not results:
        return 0
    total_checks = 0
    passed = 0
    for r in results:
        for field in required:
            total_checks += 1
            val = r.get(field)
            if val is None:
                continue
            if isinstance(val, list) and len(val) == 0:
                continue
            if isinstance(val, str) and len(val.strip()) == 0:
                continue
            if isinstance(val, dict) and len(val) == 0:
                continue
            passed += 1
    return (passed / total_checks) * 100 if total_checks else 0


def metric_calibration(results):
    """Avg per-candidate score spread across dimensions. Higher = not all same value."""
    spreads = []
    fw = FRAMEWORKS[FRAMEWORK_KEY]
    for r in results:
        scores = r.get("scores", {})
        vals = [scores.get(d, 0) for d in fw["dimensions"]]
        if len(vals) >= 2:
            spreads.append(statistics.stdev(vals))
    if not spreads:
        return 0
    avg_spread = statistics.mean(spreads)
    # Good calibration: avg spread of 1.5+; max realistic ~3.0
    return min(avg_spread / 2.5 * 100, 100)


def compute_composite(metrics: dict) -> float:
    """Weighted composite score 0-100."""
    return sum(metrics[k] * METRIC_WEIGHTS[k] for k in METRIC_WEIGHTS)


# ── Main eval runner ────────────────────────
def run_eval(zip_path: str, jd_path: str, verbose: bool = True) -> dict:
    """Run full evaluation. Returns metrics dict with composite score."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: Set ANTHROPIC_API_KEY environment variable")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    if verbose:
        print("Extracting resumes...")
    resumes = extract_resumes_from_zip_path(zip_path)
    jd_text = extract_jd_from_pdf(jd_path)

    if verbose:
        print(f"Found {len(resumes)} resumes, JD: {len(jd_text)} chars")

    results = []
    parsed_flags = []
    filenames = []

    for i, (fname, text) in enumerate(resumes.items()):
        if verbose:
            print(f"  [{i+1}/{len(resumes)}] Evaluating {fname}...")
        result, parsed = evaluate_resume(client, jd_text, FRAMEWORK_KEY, fname, text)
        results.append(result)
        parsed_flags.append(parsed)
        filenames.append(fname)

    # Only compute metrics on successfully parsed results
    good_results = [r for r, p in zip(results, parsed_flags) if p]

    metrics = {
        "json_parse":     metric_json_parse(results, parsed_flags),
        "discrimination": metric_discrimination(good_results),
        "evidence":       metric_evidence(good_results),
        "name_accuracy":  metric_name_accuracy(good_results, [f for f, p in zip(filenames, parsed_flags) if p]),
        "completeness":   metric_completeness(good_results),
        "calibration":    metric_calibration(good_results),
    }
    metrics["composite"] = compute_composite(metrics)

    if verbose:
        print("\n" + "=" * 60)
        print("EVALUATION RESULTS")
        print("=" * 60)
        for k, v in metrics.items():
            w = METRIC_WEIGHTS.get(k, 0)
            prefix = f"  ({w:.0%})" if w else "      "
            print(f"  {prefix} {k:20s}: {v:6.1f}")
        print("=" * 60)

        # Show ranking
        good_results.sort(key=lambda x: x.get("total_score", 0), reverse=True)
        print("\nRANKING:")
        for i, r in enumerate(good_results):
            print(f"  #{i+1} {r.get('name', '?'):30s} | {r.get('total_score', 0):5.2f} | {r.get('verdict', '?')}")

    return {
        "metrics": metrics,
        "results": good_results,
        "all_results": results,
        "parsed_flags": parsed_flags,
    }


if __name__ == "__main__":
    ZIP_PATH = "/Users/shivanand/Downloads/SE-3(Gen AI).zip"
    JD_PATH = "/Users/shivanand/Downloads/JD- SE-3 (Gen AI).pdf"
    run_eval(ZIP_PATH, JD_PATH)
