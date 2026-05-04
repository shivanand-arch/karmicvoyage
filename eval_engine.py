"""Evaluation engine — pure logic, no Streamlit dependency.

Extracted from app.py so it can be unit-tested without spinning up Streamlit
and so the eval logic stays decoupled from the UI.
"""

from __future__ import annotations

import json
import time
import random
import logging
from typing import Optional

import anthropic

from frameworks import FRAMEWORKS, build_evaluation_prompt_split, calculate_total, get_verdict


MAX_RETRIES = 2

logger = logging.getLogger("exotel.resume_screener.eval")


def categorize_error(msg: str) -> str:
    """Bucket a raw error string into a coarse category for aggregation."""
    if not msg:
        return "other"
    m = msg.lower()
    if any(s in m for s in ("authentication", "invalid api key", "401", "403", "permission")):
        return "auth_error"
    if any(s in m for s in ("credit", "billing", "payment", "balance", "402")):
        return "billing"
    if any(s in m for s in ("rate", "429", "quota")):
        return "rate_limit"
    if any(s in m for s in ("timeout", "timed out", "504", "522")):
        return "timeout"
    if "parse" in m or "json" in m:
        return "parse_error"
    if any(s in m for s in ("connection", "network", "dns")):
        return "network"
    return "other"


def evaluate_single_resume(
    api_key: str,
    model: str,
    framework_key: str,
    jd_text: str,
    filename: str,
    resume_text: str,
    custom_notes: str = "",
    *,
    client: Optional[anthropic.Anthropic] = None,
) -> dict:
    """Evaluate a single resume via Claude API. Returns parsed result dict.

    Uses prompt caching: framework rubric (system) and JD are marked with
    cache_control so they are billed at ~10% on reads. Per-resume content
    (resume text + JSON template) stays uncached.

    A client may be passed in for testing; otherwise a fresh client is created
    per call (the SDK is thread-safe per-call but a fresh client avoids any
    shared connection-pool surprises in the parallel path).
    """
    if client is None:
        client = anthropic.Anthropic(api_key=api_key)
    system_text, jd_block, resume_block = build_evaluation_prompt_split(
        framework_key, jd_text, resume_text, filename
    )
    if custom_notes:
        resume_block += f"\n\nADDITIONAL EVALUATION INSTRUCTIONS FROM HIRING MANAGER:\n{custom_notes}"
    fw = FRAMEWORKS[framework_key]

    for attempt in range(MAX_RETRIES + 1):
        try:
            response = client.messages.create(
                model=model,
                max_tokens=2000,
                temperature=0.0,
                system=[
                    {
                        "type": "text",
                        "text": system_text,
                        "cache_control": {"type": "ephemeral"},
                    }
                ],
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": jd_block,
                                "cache_control": {"type": "ephemeral"},
                            },
                            {
                                "type": "text",
                                "text": resume_block,
                            },
                        ],
                    }
                ],
            )
            usage = getattr(response, "usage", None)
            if usage is not None:
                logger.info(
                    "cache filename=%s input=%d cache_write=%d cache_read=%d output=%d",
                    filename,
                    getattr(usage, "input_tokens", 0),
                    getattr(usage, "cache_creation_input_tokens", 0),
                    getattr(usage, "cache_read_input_tokens", 0),
                    getattr(usage, "output_tokens", 0),
                )
            text = response.content[0].text.strip()

            # Strip markdown fences if present
            if text.startswith("```"):
                text = text.split("\n", 1)[1] if "\n" in text else text[3:]
                if text.endswith("```"):
                    text = text[:-3]
                text = text.strip()

            result = json.loads(text)

            # Recompute total with our own weights so verdicts are consistent
            scores = result.get("scores", {})
            result["total_score"] = calculate_total(scores, fw["weights"])
            result["verdict"] = get_verdict(result["total_score"])
            result["file"] = filename

            return result

        except json.JSONDecodeError:
            if attempt < MAX_RETRIES:
                time.sleep(1)
                continue
            logger.warning("parse failure after %d retries filename=%s", MAX_RETRIES, filename)
            return _failure_result(fw, filename, "Parse error", "AI evaluation failed to parse",
                                   "Evaluation failed after retries")
        except Exception as e:
            if attempt < MAX_RETRIES:
                # exponential backoff with jitter — avoids 5 workers retrying in lockstep after a 429
                backoff = (2 ** attempt) + random.uniform(0, 1)
                logger.warning(
                    "api error attempt=%d filename=%s sleeping=%.2fs error=%s",
                    attempt, filename, backoff, str(e)[:200],
                )
                time.sleep(backoff)
                continue
            logger.error("api failure after %d retries filename=%s error=%s",
                         MAX_RETRIES, filename, str(e)[:300])
            return _failure_result(fw, filename, "API error",
                                   f"API error: {str(e)[:100]}",
                                   f"Evaluation failed: {str(e)[:100]}")


def _failure_result(fw: dict, filename: str, current_role: str,
                    concern: str, evidence: str) -> dict:
    return {
        "name": filename.replace(".pdf", "").replace("_", " "),
        "file": filename,
        "current_role": current_role,
        "yoe": 0,
        "scores": {k: 0 for k in fw["dimensions"]},
        "total_score": 0,
        "verdict": "No",
        "key_strengths": [],
        "key_concerns": [concern],
        "evidence_summary": evidence,
    }
