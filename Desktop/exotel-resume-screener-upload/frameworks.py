"""
Exotel Resume Evaluation Frameworks
All role-specific scoring dimensions, weights, and evaluation prompts.
"""

# ─────────────────────────────────────────────
# FRAMEWORK DEFINITIONS
# ─────────────────────────────────────────────

FRAMEWORKS = {

    # ── BACKEND ENGINEERING ──────────────────
    "Backend Engineer (SE-1 to Sr. EM)": {
        "description": "Backend engineering roles at Exotel across levels",
        "dimensions": {
            "backend_depth": "Core backend engineering depth — API design, microservices, distributed systems, concurrency, async processing, DB optimization, caching, system performance",
            "scale_complexity": "Scale & complexity signals — high throughput, low latency, real-time systems, event-driven, Kafka, horizontal scaling, large data volumes",
            "ownership": "Ownership level — designed/owned systems vs assisted/supported. Look for: designed service, owned system, led implementation, migrated architecture, reduced latency/cost",
            "engineering_maturity": "Engineering maturity — production debugging, incident resolution, monitoring, on-call, reliability improvements, root cause analysis, observability",
            "genai_expertise": "GenAI signals — LangChain, LangGraph, agent workflows, RAG systems, vector databases, prompt orchestration, evaluation pipelines, production AI systems",
            "tech_stack_fit": "Tech stack fit for Exotel — Go, Java, Python, Kafka, Redis, MongoDB, PostgreSQL/Citus, AWS, Docker/K8s",
            "leadership": "Leadership signals — mentoring, code reviews, technical decision-making, team management, architecture involvement, cross-team collaboration",
        },
        "weights": {
            "backend_depth": 0.20,
            "scale_complexity": 0.15,
            "ownership": 0.15,
            "engineering_maturity": 0.10,
            "genai_expertise": 0.15,
            "tech_stack_fit": 0.10,
            "leadership": 0.15,
        },
        "context": """Exotel builds high reliability, real-time, distributed backend systems with low latency expectations.
Primary tech: Go (Platform), Java/PostgreSQL/Citus (Contact Center), Python/LangChain/LangGraph (GenAI).
Ownership-driven engineering culture. Production sensitivity is critical.
Red flags: frontend-heavy, only scripting/automation, QA/DevOps without backend, buzzword-heavy without depth, service company background without strong eng signals.""",
    },

    # ── SALES MANAGER ────────────────────────
    "Sales Manager": {
        "description": "Enterprise Sales roles — Mid-Market, Enterprise, International",
        "dimensions": {
            "hunter_mindset": "Hunter validation — new logo acquisition, outbound pipeline creation, greenfield acquisition, self-generated pipeline. Deprioritize if revenue from existing accounts/renewals only.",
            "solution_selling": "Solution selling — sold platform/AI/technical/consultative offerings. Strong: AI products, automation platforms, CX platforms, enterprise SaaS. Weak: feature/price/catalogue selling.",
            "multi_threading": "Multi-threading — engaged multiple stakeholders, CXO conversations, cross-functional alignment, business + technical selling simultaneously.",
            "influence_ownership": "Influence without authority — drove deals forward despite dependencies, coordinated internal stakeholders, owned outcomes beyond formal scope.",
            "field_sales": "Field sales — in-person meetings, customer visits. Weak: pure inside sales, only remote selling.",
            "company_context": "Company context — SaaS, enterprise software, AI/automation platforms, CX/contact center tools = high signal. Transactional/hardware/channel/distributor = low signal.",
            "numbers_metrics": "Numbers & ownership — quota achievement, revenue numbers, deal sizes, pipeline ownership, growth metrics. RED FLAG: sales resume without numbers.",
        },
        "weights": {
            "hunter_mindset": 0.20,
            "solution_selling": 0.20,
            "multi_threading": 0.15,
            "influence_ownership": 0.15,
            "field_sales": 0.05,
            "company_context": 0.15,
            "numbers_metrics": 0.10,
        },
        "bonus_dimensions": {
            "ai_first_selling": "AI-First Solution Selling — has the candidate sold AI-first solutions? Conversational AI, GenAI, Voice AI/Bots, NLP, AI automation platforms, AI-first SaaS. Score 1-10 but report SEPARATELY.",
        },
        "context": """Exotel sells communication infrastructure, contact center platforms, and AI-led solutions (Voice Bots, Conversational AI, CCaaS, CPaaS).
Selling requires solution-led conversations, technical understanding, multi-stakeholder alignment, long cycles, internal coordination.
Successful sellers: influence without authority, navigate eng/product/biz stakeholders, drive deals despite ambiguity, end-to-end ownership.
This is for individual contributor hunter roles, NOT account management or customer success.
Red flags: no revenue metrics, pure account management, channel-only, small ticket, inside-sales heavy.""",
    },

    # ── SDR ───────────────────────────────────
    "SDR (Sales Development Representative)": {
        "description": "Outbound SDR roles — Scaleup, Enterprise, International",
        "dimensions": {
            "outbound_ownership": "Outbound ownership — did they GENERATE pipeline or only handle inbound? Cold calling, account research, multi-channel outreach (LinkedIn+Email+Calls), self-generated meetings. Hard deprioritize: no outbound exposure.",
            "funnel_metrics": "Funnel & metric thinking — call-to-meeting ratios, conversion rates, monthly targets, activity metrics (calls/day, emails/day), pipeline contribution. RED FLAG: SDR resume with zero metrics.",
            "qualification_depth": "Qualification depth — discovery questioning, BANT/MEDDIC awareness, pain-point identification, qualification before handoff. Strong: qualified on budget/timeline/use-case. Weak: booked demos without qualification.",
            "technical_curiosity": "Technical curiosity — SaaS exposure, API/SDK familiarity, automation tools, CRM usage (HubSpot/Salesforce), GenAI for research. Strong: sold SaaS, used Apollo/Sales Navigator. Weak: pure non-tech B2B.",
            "industry_persona": "Industry & persona awareness — persona-based messaging (CXOs, Founders, Product Heads), industry pain points (BFSI, D2C, FMCG), contextualized value props. Weak: generic mass messaging.",
            "self_discipline": "Self-discipline & ownership — consistency in target achievement, self-driven prospecting, independent pipeline generation, long tenure in outbound roles. Red flags: frequent switches (<1yr), heavy dependence on marketing.",
        },
        "weights": {
            "outbound_ownership": 0.25,
            "funnel_metrics": 0.20,
            "qualification_depth": 0.15,
            "technical_curiosity": 0.15,
            "industry_persona": 0.10,
            "self_discipline": 0.15,
        },
        "context": """Exotel SDR is not a generic cold-calling role. It requires structured outbound prospecting, persona-based outreach (CXOs, Founders, Product Heads), discovery-driven qualification, technical curiosity (APIs, automation, contact center tools), funnel math understanding, and collaboration with AEs.
SDRs generate qualified opportunities, not just meetings.
Platform: communication APIs, contact centers, AI-led solutions. 10B+ conversations/year for brands like Swiggy, Ola, Zerodha, Flipkart.
Tier 1 (Strong SDR Fit): Clear outbound, metric-driven, consultative, tech-curious.
Tier 2 (Potential Fit): Outbound exposure but lacks structure or metrics.
Tier 3 (Low Fit): Primarily inbound, no metrics, no qualification depth.""",
    },

    # ── CHIEF OF STAFF ───────────────────────
    "Chief of Staff": {
        "description": "CoS for CEO's Office — Strategy & Ops",
        "dimensions": {
            "strategic_thinking": "Strategic thinking — strategy consulting, business planning, CEO-level thinking, board prep, competitive analysis, M&A support, long-range planning",
            "execution_ops": "Execution & ops — operational excellence, program management, process design, operating cadence, OKR/KPI management, cross-functional delivery",
            "cross_functional": "Cross-functional leadership — cross-team coordination, stakeholder management across eng/product/sales/ops, breaking silos, driving alignment",
            "communication": "Communication & presentation — executive communication, board decks, written clarity, ability to synthesize complex info for leadership (assessed from resume quality)",
            "domain_fit": "Domain fit — B2B SaaS, CPaaS, CX tech, telecom experience. Nice-to-have: worked with founders/CEO directly",
            "leadership_eq": "Leadership & EQ — people leadership, emotional intelligence, executive presence, managing up, navigating ambiguity, influence without authority",
            "company_pedigree": "Company pedigree — brand value of companies worked at. FAANG/Big Tech=10, Unicorn=9, Global brand=8, Recognized mid-tier=7, Established niche=6, Small known=5, Unknown=3-4",
        },
        "weights": {
            "strategic_thinking": 0.20,
            "execution_ops": 0.20,
            "cross_functional": 0.15,
            "communication": 0.10,
            "domain_fit": 0.10,
            "leadership_eq": 0.15,
            "company_pedigree": 0.10,
        },
        "context": """Chief of Staff for CEO's Office at Exotel. 8-12 YOE preferred. Strategy & Ops / Consulting / BizOps / Product Ops background.
Key responsibilities: CEO priorities, operating cadence, cross-functional programs, decision support, special projects.
Nice-to-have: MBA Tier-1, B2B SaaS/CPaaS/CX domain, worked with founders/CEO.
The role requires someone who can toggle between strategy and execution, manage up to the CEO while driving down through the org.""",
    },

    # ── ENGINEERING MANAGER (GenAI) ──────────
    "Engineering Manager (GenAI)": {
        "description": "EM for GenAI product team",
        "dimensions": {
            "backend_depth": "Backend engineering depth — strong backend past, architecture involvement, system design",
            "scale_complexity": "Scale & complexity — distributed systems, high throughput, production-grade systems",
            "ownership": "Ownership & delivery — project delivery, sprint planning, scope-quality-time tradeoffs, stakeholder management",
            "engineering_maturity": "Engineering maturity — code review practices, technical guidance, unblocking complex challenges, engineering process improvements",
            "genai_expertise": "GenAI expertise — LangChain, LangGraph, RAG, agent workflows, LLM orchestration, production AI systems (not demos)",
            "leadership": "Leadership — team management (ideally 4-6 engineers), mentoring, hiring, still technically credible. Red flag: managed 15+ directly (too senior), pure PM without eng depth",
            "tech_stack_fit": "Tech stack fit — Python, LangChain/LangGraph, vector DBs, AWS, relevant AI/ML tools",
        },
        "weights": {
            "backend_depth": 0.10,
            "scale_complexity": 0.10,
            "ownership": 0.15,
            "engineering_maturity": 0.10,
            "genai_expertise": 0.20,
            "leadership": 0.25,
            "tech_stack_fit": 0.10,
        },
        "context": """Exotel wants hands-on technical leaders — ideal profile is Lead Software Engineers in good product companies who've managed small teams while staying technically involved.
Target: managed 4-6 engineers, still technically credible, architecture involvement.
Red flags: pure delivery/project managers, no engineering depth, managed very large teams (15+ directly — suggests beyond hands-on level).
GenAI product uses Python, LangChain, LangGraph, RAG pipelines, agent workflows, LLM orchestration.""",
    },
}


VERDICT_THRESHOLDS = {
    "Strong Yes": 8.0,
    "Yes": 6.5,
    "Maybe": 5.0,
    "No": 0.0,
}

# Highest band first; everything below Maybe is "No".
_VERDICT_ORDER = [
    ("Strong Yes", VERDICT_THRESHOLDS["Strong Yes"]),
    ("Yes", VERDICT_THRESHOLDS["Yes"]),
    ("Maybe", VERDICT_THRESHOLDS["Maybe"]),
]


def get_verdict(score: float) -> str:
    for label, threshold in _VERDICT_ORDER:
        if score >= threshold:
            return label
    return "No"


def calculate_total(scores: dict, weights: dict) -> float:
    total = sum(scores.get(k, 0) * weights.get(k, 0) for k in weights)
    return round(total, 2)


def build_evaluation_prompt(framework_key: str, jd_text: str, resume_text: str, filename: str) -> str:
    """Build the full evaluation prompt for a single resume."""
    fw = FRAMEWORKS[framework_key]

    dimensions_desc = "\n".join(
        f"- **{k}** (weight {fw['weights'][k]:.0%}): {v}"
        for k, v in fw["dimensions"].items()
    )

    bonus_section = ""
    if "bonus_dimensions" in fw:
        bonus_desc = "\n".join(
            f"- **{k}**: {v}" for k, v in fw["bonus_dimensions"].items()
        )
        bonus_section = f"""
BONUS DIMENSIONS (score separately, NOT included in total):
{bonus_desc}
"""

    prompt = f"""You are an expert resume screener for Exotel. Evaluate this resume against the job description.

ROLE CONTEXT:
{fw['context']}

JOB DESCRIPTION:
{jd_text}

SCORING DIMENSIONS (each 1-10):
{dimensions_desc}
{bonus_section}
VERDICT THRESHOLDS: Strong Yes (≥8.0), Yes (6.5-7.9), Maybe (5.0-6.4), No (<5.0)
Total score = weighted sum of dimension scores (the app recomputes total_score and verdict from your dimension scores).

RESUME (filename: {filename}):
{resume_text[:3500]}

INSTRUCTIONS:
- Read the resume carefully. Extract specific evidence for each dimension.
- SCORING CALIBRATION (use the full 1-10 range — do NOT cluster all scores around 5-6):
  1-2: No evidence at all for this dimension
  3-4: Weak/tangential evidence, mostly unrelated experience
  5: Average — meets basic expectations but nothing notable
  6-7: Good — clear, specific evidence of competence in this area
  8: Strong — multiple concrete achievements with measurable impact
  9-10: Exceptional — rare, standout evidence (e.g., built systems at scale, published work, led major migrations)
- DIFFERENTIATE across dimensions: A candidate strong in backend but weak in GenAI should show a 3+ point gap between those scores. Do not give flat scores. Your highest and lowest dimension scores for any candidate should differ by at least 2 points.
- If evidence is missing for a dimension, score 1-3. Do not assume competence without evidence.
- Extract the candidate's full name, current role/company, and estimated YOE.
- You may omit total_score and verdict — they will be recomputed from dimension scores.

Respond with ONLY valid JSON (no markdown, no explanation):
"""

    # Build the JSON template
    score_fields = ", ".join(f'"{k}": 0.0' for k in fw["dimensions"])
    json_template = f"""{{
  "name": "Full Name",
  "file": "{filename}",
  "current_role": "Current Title @ Company",
  "yoe": 0,
  "scores": {{
    {score_fields}
  }},"""

    if "bonus_dimensions" in fw:
        bonus_score_fields = ", ".join(f'"{k}": 0.0' for k in fw["bonus_dimensions"])
        bonus_note_fields = ", ".join(f'"{k}": "brief note"' for k in fw["bonus_dimensions"])
        json_template += f"""
  "bonus_scores": {{{bonus_score_fields}}},
  "bonus_notes": {{{bonus_note_fields}}},"""

    json_template += """
  "total_score": 0.00,
  "verdict": "Maybe",
  "key_strengths": ["strength1", "strength2"],
  "key_concerns": ["concern1", "concern2"],
  "evidence_summary": "2-3 sentence summary with specific resume evidence"
}"""

    prompt += json_template
    return prompt


def build_evaluation_prompt_split(framework_key: str, jd_text: str, resume_text: str, filename: str) -> tuple:
    """Build system + user message pair for evaluation. Returns (system_text, user_text)."""
    fw = FRAMEWORKS[framework_key]

    dimensions_desc = "\n".join(
        f"- **{k}** (weight {fw['weights'][k]:.0%}): {v}"
        for k, v in fw["dimensions"].items()
    )

    bonus_section = ""
    if "bonus_dimensions" in fw:
        bonus_desc = "\n".join(
            f"- **{k}**: {v}" for k, v in fw["bonus_dimensions"].items()
        )
        bonus_section = f"""
BONUS DIMENSIONS (score separately, NOT included in total):
{bonus_desc}
"""

    system_text = f"""You are an expert resume screener for Exotel. You evaluate resumes against job descriptions with rigorous, evidence-based scoring.

ROLE CONTEXT:
{fw['context']}

SCORING DIMENSIONS (each 1-10):
{dimensions_desc}
{bonus_section}
VERDICT THRESHOLDS: Strong Yes (≥8.0), Yes (6.5-7.9), Maybe (5.0-6.4), No (<5.0)
Total score = weighted sum of dimension scores (the app recomputes total_score and verdict from your dimension scores).

SCORING CALIBRATION (use the full 1-10 range — do NOT cluster all scores around 5-6):
  1-2: No evidence at all for this dimension
  3-4: Weak/tangential evidence, mostly unrelated experience
  5: Average — meets basic expectations but nothing notable
  6-7: Good — clear, specific evidence of competence in this area
  8: Strong — multiple concrete achievements with measurable impact
  9-10: Exceptional — rare, standout evidence (e.g., built systems at scale, published work, led major migrations)

DIFFERENTIATE across dimensions: A candidate strong in backend but weak in GenAI should show a 3+ point gap between those scores. Do not give flat scores.
If evidence is missing for a dimension, score 1-3. Do not assume competence without evidence.

Respond with ONLY valid JSON (no markdown, no explanation)."""

    # Build the JSON template
    score_fields = ", ".join(f'"{k}": 0.0' for k in fw["dimensions"])
    json_template = f"""\n{{\n  "name": "Full Name",\n  "file": "{filename}",\n  "current_role": "Current Title @ Company",\n  "yoe": 0,\n  "scores": {{\n    {score_fields}\n  }},"""

    if "bonus_dimensions" in fw:
        bonus_score_fields = ", ".join(f'"{k}": 0.0' for k in fw["bonus_dimensions"])
        bonus_note_fields = ", ".join(f'"{k}": "brief note"' for k in fw["bonus_dimensions"])
        json_template += f"""\n  "bonus_scores": {{{bonus_score_fields}}},\n  "bonus_notes": {{{bonus_note_fields}}},"""

    json_template += """\n  "total_score": 0.00,\n  "verdict": "Maybe",\n  "key_strengths": ["strength1", "strength2"],\n  "key_concerns": ["concern1", "concern2"],\n  "evidence_summary": "2-3 sentence summary with specific resume evidence"\n}"""

    user_text = f"""Evaluate this resume against the job description below.

JOB DESCRIPTION:
{jd_text}

RESUME (filename: {filename}):
{resume_text[:3500]}

Extract the candidate's full name, current role/company, and estimated YOE. Score each dimension with specific evidence. Return JSON in this format:
{json_template}"""

    return system_text, user_text


def get_framework_names() -> list:
    return list(FRAMEWORKS.keys())
