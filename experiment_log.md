# Optimization Experiment Log

**Target:** Exotel Resume Screener — evaluation prompt & scoring logic
**Editable files:** `frameworks.py` (prompt, dimensions, context), `app.py` (API params)
**Metric:** Composite quality score (direction: higher is better)
**Baseline score:** 85.9
**Started:** 2026-04-01

### Baseline Metrics
| Metric | Score | Weight |
|---|---|---|
| JSON parse success | 100.0 | 20% |
| Score discrimination | 57.4 | 20% |
| Evidence specificity | 100.0 | 20% |
| Name accuracy | 100.0 | 15% |
| Completeness | 100.0 | 15% |
| Calibration | 43.9 | 10% |
| **Composite** | **85.9** | |

### Baseline Ranking
| # | Name | Score | Verdict |
|---|------|-------|---------|
| 1 | Divya Singh Thakur | 6.42 | Maybe |
| 2 | Aviral Jain | 5.78 | Maybe |
| 3 | Shubham Goyal | 5.47 | Maybe |
| 4 | Syed Akrama Irshad | 5.10 | Maybe |
| 5 | Rachel Priyadharshini K | 4.70 | No |
| 6 | Susatya Sinha | 4.30 | No |
| 7 | Maddipudi Shiri Koushik | 3.73 | No |
| 8 | Akash Salode | 3.08 | No |
| 9 | Danish Nabi | 1.45 | No |
| 10 | Gaurav Kumar | 1.45 | No |

### Key Observations
- JSON parse, evidence, name, completeness all at 100% — already strong
- **Discrimination (57.4)** and **Calibration (43.9)** are the weak spots
- Scores cluster too tightly (5.10-6.42 for top 4) — not differentiating well
- Per-dimension scores lack spread — model gives similar scores across dimensions
- No "Strong Yes" or "Yes" verdicts — may be too harsh or scores too compressed

## Experiments

| # | Hypothesis | Change | Score | Delta | Status |
|---|-----------|--------|-------|-------|--------|
| 1 | Stronger calibration instructions | Detailed 1-10 scale anchors + differentiation rule in prompt | 86.9 | +1.0 | **KEPT** |
| 2 | Per-dimension reasoning field | Added dimension_reasoning JSON field | 85.6 | -0.3 | REVERTED |
| 3 | Increase max_tokens 1500→2000 | More room for detailed evidence | 86.9 | +1.0 | **KEPT** |
| 4 | Temperature 0.1→0.0 | Fully deterministic scoring | 87.1 | +1.2 | **KEPT** |
| 5 | Resume text limit 3500→4000 | More resume content for evaluation | 86.5 | +0.6 | REVERTED |
| 6 | Concrete anchor examples in context | Added score=3 vs score=8 examples | 84.3 | -1.6 | REVERTED |
| 7 | System + user message split | Separate persona from data | 87.0 | +1.1 | REVERTED (noise) |
| 8 | Force 3 strengths + 3 concerns | More evidence items in template | 86.7 | +0.8 | REVERTED |
| 9 | Score weakest dimension first | Scoring order instruction | 86.6 | +0.7 | REVERTED (calibration↑ but discrimination↓) |
| 10 | Min 2-point spread requirement | Soft floor on per-candidate dimension spread | 87.0 | +1.1 | **KEPT** |

## Final Results

| Metric | Baseline | Final | Delta |
|---|---|---|---|
| JSON parse success | 100.0 | 100.0 | — |
| Score discrimination | 57.4 | 60.3 | +2.9 |
| Evidence specificity | 100.0 | 100.0 | — |
| Name accuracy | 100.0 | 100.0 | — |
| Completeness | 100.0 | 100.0 | — |
| Calibration | 43.9 | 49.4 | +5.5 |
| **Composite** | **85.9** | **87.0** | **+1.1** |

### Final Ranking
| # | Name | Score | Verdict |
|---|------|-------|---------|
| 1 | Divya Singh Thakur | 6.83 | **Yes** (was Maybe) |
| 2 | Aviral Jain | 5.98 | Maybe |
| 3 | Syed Akrama Irshad | 5.60 | Maybe |
| 4 | Shubham Goyal | 5.58 | Maybe |
| 5 | Rachel Priyadharshini K | 5.08 | Maybe |
| 6 | Susatya Sinha | 4.35 | No |
| 7 | Maddipudi Shiri Koushik | 3.50 | No |
| 8 | Akash Salode | 3.30 | No |
| 9 | Gaurav Kumar | 1.75 | No |
| 10 | Danish Nabi | 1.45 | No |
