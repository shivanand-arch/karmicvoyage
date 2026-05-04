"""Quality regression: compare cached-split prompt vs the original mega-prompt.

Run this with your real Anthropic key on a small sample BEFORE merging changes
to the prompt structure. If verdict-agreement drops below ~90% or rank
correlation drops below ~0.85, do not merge — the split has shifted scoring.

Usage:
  ANTHROPIC_API_KEY=sk-ant-... \\
    python3 scripts/eval_compare.py \\
      --framework "Backend — SE-2 (2-4 YOE)" \\
      --jd path/to/jd.txt \\
      --resumes-dir path/to/resumes_folder \\
      --max 10

Output: prints a per-resume diff and summary stats. Exits non-zero if quality
agreement is below the configured threshold.
"""

from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
import time
from pathlib import Path
from typing import Iterable

# Make the parent dir importable so we can use the in-repo modules
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import anthropic

from frameworks import (
    FRAMEWORKS,
    build_evaluation_prompt,
    build_evaluation_prompt_split,
    calculate_total,
    get_verdict,
)
from resume_processor import extract_text_from_bytes


VERDICT_AGREEMENT_THRESHOLD = 0.90
RANK_CORRELATION_THRESHOLD = 0.85


def _evaluate_old(client: anthropic.Anthropic, model: str, framework_key: str,
                  jd: str, filename: str, resume_text: str) -> dict:
    """Original single-message prompt — no caching."""
    prompt = build_evaluation_prompt(framework_key, jd, resume_text, filename)
    resp = client.messages.create(
        model=model,
        max_tokens=2000,
        temperature=0.0,
        messages=[{"role": "user", "content": prompt}],
    )
    return _parse_response(resp, framework_key, filename)


def _evaluate_new(client: anthropic.Anthropic, model: str, framework_key: str,
                  jd: str, filename: str, resume_text: str) -> dict:
    """Split prompt + cache_control — what PR #17 ships."""
    system_text, jd_block, resume_block = build_evaluation_prompt_split(
        framework_key, jd, resume_text, filename
    )
    resp = client.messages.create(
        model=model,
        max_tokens=2000,
        temperature=0.0,
        system=[{"type": "text", "text": system_text, "cache_control": {"type": "ephemeral"}}],
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": jd_block, "cache_control": {"type": "ephemeral"}},
                    {"type": "text", "text": resume_block},
                ],
            }
        ],
    )
    return _parse_response(resp, framework_key, filename)


def _parse_response(resp, framework_key: str, filename: str) -> dict:
    text = resp.content[0].text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text[3:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()
    result = json.loads(text)
    fw = FRAMEWORKS[framework_key]
    result["total_score"] = calculate_total(result.get("scores", {}), fw["weights"])
    result["verdict"] = get_verdict(result["total_score"])
    result["file"] = filename
    return result


def _spearman(a: list[float], b: list[float]) -> float:
    """Spearman rank correlation. Returns 0.0 on degenerate inputs."""
    if len(a) != len(b) or len(a) < 2:
        return 0.0

    def rank(xs: list[float]) -> list[float]:
        order = sorted(range(len(xs)), key=lambda i: xs[i])
        ranks = [0.0] * len(xs)
        i = 0
        while i < len(xs):
            j = i
            while j + 1 < len(xs) and xs[order[j + 1]] == xs[order[i]]:
                j += 1
            avg = (i + j) / 2 + 1
            for k in range(i, j + 1):
                ranks[order[k]] = avg
            i = j + 1
        return ranks

    ra, rb = rank(a), rank(b)
    n = len(a)
    mean_a, mean_b = sum(ra) / n, sum(rb) / n
    num = sum((ra[i] - mean_a) * (rb[i] - mean_b) for i in range(n))
    den_a = (sum((ra[i] - mean_a) ** 2 for i in range(n))) ** 0.5
    den_b = (sum((rb[i] - mean_b) ** 2 for i in range(n))) ** 0.5
    if den_a == 0 or den_b == 0:
        return 0.0
    return num / (den_a * den_b)


def _load_resumes(resumes_dir: Path, limit: int) -> Iterable[tuple[str, str]]:
    files = sorted(p for p in resumes_dir.iterdir() if p.is_file())
    files = files[:limit]
    for p in files:
        try:
            text = extract_text_from_bytes(p.read_bytes(), p.name)
        except Exception as e:
            print(f"  ! skip {p.name}: {e}", file=sys.stderr)
            continue
        if text.strip():
            yield p.name, text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--framework", required=True, help="Framework name (must match FRAMEWORKS key)")
    ap.add_argument("--jd", required=True, type=Path, help="Path to JD .txt")
    ap.add_argument("--resumes-dir", required=True, type=Path,
                    help="Folder of resume PDFs/DOCX")
    ap.add_argument("--max", type=int, default=10, help="Max resumes to compare")
    ap.add_argument("--model", default="claude-sonnet-4-6")
    args = ap.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(2)

    if args.framework not in FRAMEWORKS:
        print(f"Unknown framework: {args.framework}\nAvailable: {list(FRAMEWORKS)}", file=sys.stderr)
        sys.exit(2)

    jd_text = args.jd.read_text()
    client = anthropic.Anthropic(api_key=api_key)

    rows = []
    for filename, resume_text in _load_resumes(args.resumes_dir, args.max):
        print(f"  → {filename}", file=sys.stderr)
        try:
            old = _evaluate_old(client, args.model, args.framework, jd_text, filename, resume_text)
            time.sleep(0.5)
            new = _evaluate_new(client, args.model, args.framework, jd_text, filename, resume_text)
        except Exception as e:
            print(f"    ! {filename}: {e}", file=sys.stderr)
            continue
        rows.append({
            "file": filename,
            "old_score": old.get("total_score", 0),
            "new_score": new.get("total_score", 0),
            "old_verdict": old.get("verdict", ""),
            "new_verdict": new.get("verdict", ""),
            "delta": (new.get("total_score", 0) - old.get("total_score", 0)),
        })

    if not rows:
        print("no rows to compare", file=sys.stderr)
        sys.exit(2)

    print(f"\n{'file':<40} {'old':>6} {'new':>6} {'Δ':>6}  old→new verdict")
    print("-" * 90)
    for r in rows:
        same = "✓" if r["old_verdict"] == r["new_verdict"] else "✗"
        print(f"{r['file'][:39]:<40} {r['old_score']:>6.2f} {r['new_score']:>6.2f} "
              f"{r['delta']:>+6.2f}  {r['old_verdict']:>12} → {r['new_verdict']:<12} {same}")

    agreement = sum(1 for r in rows if r["old_verdict"] == r["new_verdict"]) / len(rows)
    rho = _spearman([r["old_score"] for r in rows], [r["new_score"] for r in rows])
    mean_delta = statistics.mean(r["delta"] for r in rows)
    stdev_delta = statistics.pstdev(r["delta"] for r in rows)

    print("\nSummary")
    print(f"  resumes:               {len(rows)}")
    print(f"  verdict agreement:     {agreement:.0%}  (threshold {VERDICT_AGREEMENT_THRESHOLD:.0%})")
    print(f"  Spearman ρ on scores:  {rho:.3f}  (threshold {RANK_CORRELATION_THRESHOLD:.2f})")
    print(f"  mean Δ (new - old):    {mean_delta:+.2f}")
    print(f"  stdev Δ:               {stdev_delta:.2f}")

    failed = []
    if agreement < VERDICT_AGREEMENT_THRESHOLD:
        failed.append(f"verdict agreement {agreement:.0%} < {VERDICT_AGREEMENT_THRESHOLD:.0%}")
    if rho < RANK_CORRELATION_THRESHOLD:
        failed.append(f"rank correlation {rho:.3f} < {RANK_CORRELATION_THRESHOLD:.2f}")
    if failed:
        print("\nFAIL — do not merge:")
        for f in failed:
            print(f"  - {f}")
        sys.exit(1)
    print("\nOK — quality preserved within thresholds.")


if __name__ == "__main__":
    main()
