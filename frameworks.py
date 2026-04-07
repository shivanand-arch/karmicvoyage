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
            "backend_depth": 0.25,
            "scale_complexity": 0.20,
            "ownership": 0.20,
            "engineering_maturity": 0.10,
            "genai_expertise": 0.0,
            "tech_stack_fit": 0.10,
            "leadership": 0.15,
        },
        "context": """Exotel builds high reliability, real-time, distributed backend systems with low latency expectations.
Primary tech: Go (Platform — distributed services, async/event-driven, Kafka, Redis, MongoDB, AWS, high concurrency), Java/PostgreSQL/Citus (Contact Center — scalable APIs, multi-tenant, data-heavy), Python/LangChain/LangGraph (GenAI — RAG, agent workflows, LLM orchestration).
Ownership-driven engineering culture. Production sensitivity is critical.

LEVEL-WISE EXPECTATIONS (calibrate scoring based on candidate's YOE):

SE-1 (0-2 YOE): Strong fundamentals + learning. Go/Java/Python preferred. Expected: REST API dev, basic DB, frameworks, Linux, Git. Good: internship backend, deployed projects, Docker, SQL. NOT expected: architecture, distributed systems. Red flags: only tutorials, no backend ownership.

SE-2 (2-4 YOE): Independent feature ownership. Production backend required. Must show: E2E feature ownership, DB understanding, performance awareness. Strong: caching implementation, queue usage, async workflows, API optimization, DB indexing. Weak: only implementation tickets, no impact statements.

SE-3/Tech Lead (4-5+ YOE): System-level contributor — Exotel hiring bar increases significantly here. MANDATORY: design participation, distributed systems exposure, scalability thinking. Strong: event-driven architecture, Kafka/messaging, service decomposition, HA design, load handling, retry/timeout/rate limiting, observability. Also: mentoring, code reviews, technical decisions. Common rejection: senior title but execution-level work only.

Principal Engineer (7+ YOE): Makes key tech choices, establishes patterns, writes most critical components, reviews designs. Signals: system redesign, scaling architecture, migration initiatives, DB scaling, reliability improvements. They DRIVE decisions, not just contribute. Red flag: title inflation without cross-system impact.

Engineering Manager: Ideal = Lead SWE from product companies who managed 4-6 engineers while staying technical. Must show: strong backend past, architecture involvement, team management, mentoring, delivery ownership, sprint planning, stakeholder alignment. Red flags: pure delivery/PM, no engineering depth, managed 15+ directly (too far from hands-on).

Sr. Engineering Manager: Managed 15-20 people, cross-functional collaboration with Product/QA/other eng teams, engineering process improvements, technical direction setting. Should still have recent technical contributions. Complete absence of technical involvement is concerning.

ADVANCED SYSTEM THINKING SIGNALS (important for SE-3 and above — increase score confidence):
- Tradeoff Awareness: latency vs consistency, performance vs cost, simplicity vs scalability, technology evaluation with reasoning
- Failure Handling & Reliability: partial failures, retry mechanisms, timeout strategies, circuit breakers, fail-safe design
- Load Management & System Protection: rate limiting, backpressure handling, queue buffering, traffic shaping
- Data & Request Safety: idempotency handling, duplicate event protection, safe retries, exactly-once/at-least-once awareness
- Graceful Degradation: system continues in reduced capacity during failures, feature fallbacks instead of total outages
Absence of these signals is acceptable for SE-1 and early SE-2. For SE-3+ their presence is a strong positive.

Red flags: frontend-heavy, only scripting/automation, QA/DevOps without backend, buzzword-heavy without depth, service company background without strong eng signals, too many technologies listed without ownership, repeated short tenures.""",
    },

    # ── SALES: MID-MARKET ─────────────────────
    "Sales — Mid-Market": {
        "description": "Mid-Market Sales Manager — faster cycles, multi-industry, pipeline creation",
        "dimensions": {
            "hunter_mindset": "Hunter validation — new logo acquisition, outbound pipeline creation, greenfield acquisition, self-generated pipeline. Deprioritize if revenue from existing accounts/renewals only.",
            "solution_selling": "Solution selling — sold platform/AI/technical/consultative offerings. Strong: AI products, automation platforms, CX platforms, enterprise SaaS. Weak: feature/price/catalogue selling.",
            "multi_threading": "Multi-threading — engaged multiple stakeholders, CXO conversations, cross-functional alignment, business + technical selling simultaneously.",
            "influence_ownership": "Influence without authority — drove deals forward despite dependencies, coordinated internal stakeholders, owned outcomes beyond formal scope.",
            "field_sales": "Field sales — in-person meetings, customer visits. Weak: pure inside sales, only remote selling.",
            "company_context": "Company context — SaaS, enterprise software, AI/automation platforms, CX/contact center tools = high signal. Transactional/hardware/channel/distributor = low signal.",
            "numbers_metrics": "Numbers & ownership — quota achievement, revenue numbers, deal sizes, pipeline ownership, growth metrics. RED FLAG: sales resume without numbers.",
            "leadership": "Leadership signals — team management, mentoring junior reps, sales playbook creation, hiring involvement, cross-functional coordination, regional/segment ownership",
        },
        "weights": {
            "hunter_mindset": 0.20,
            "solution_selling": 0.20,
            "multi_threading": 0.15,
            "influence_ownership": 0.15,
            "field_sales": 0.05,
            "company_context": 0.15,
            "numbers_metrics": 0.10,
            "leadership": 0.0,
        },
        "bonus_dimensions": {
            "ai_first_selling": "AI-First Solution Selling — has the candidate sold AI-first solutions? Conversational AI, GenAI, Voice AI/Bots, NLP, AI automation platforms, AI-first SaaS. Score 1-10 but report SEPARATELY.",
        },
        "context": """Exotel sells communication infrastructure, contact center platforms, and AI-led solutions (Voice Bots, Conversational AI, CCaaS, CPaaS).

MID-MARKET SEGMENT: Faster sales cycles, caters across industries (industry-agnostic), multiple concurrent opportunities, strong discovery and qualification needed.
Key success signals: pipeline creation ability, efficient deal progression, handling multiple stakeholders quickly, strong qualification.
Strong signals: outbound prospecting, full-cycle sales ownership, demo to closure, solution mapping.

Levels: Sales Manager (5-8/11 yrs) = independent solution hunter, new logo, pipeline creation, full-cycle ownership. Senior Sales Manager (8-14 yrs) = complex deal closer, larger deals, stronger solutioning. Principal Sales Manager (14+ yrs) = high-trust complex seller, ambiguous deals, senior stakeholder influence, E2E outcome ownership. Red flag at Principal: only leadership without individual selling.

This is for individual contributor hunter roles, NOT account management or customer success.
Red flags: no revenue metrics, pure account management, channel-only, small ticket, inside-sales heavy.""",
    },

    # ── SALES: ENTERPRISE ────────────────────
    "Sales — Enterprise": {
        "description": "Enterprise Sales Manager — long cycles, complex stakeholders, industry-specific",
        "dimensions": {
            "hunter_mindset": "Hunter validation — new logo acquisition, outbound pipeline creation, greenfield acquisition, self-generated pipeline. Deprioritize if revenue from existing accounts/renewals only.",
            "solution_selling": "Solution selling — sold platform/AI/technical/consultative offerings. Strong: AI products, automation platforms, CX platforms, enterprise SaaS. Weak: feature/price/catalogue selling.",
            "multi_threading": "Multi-threading — engaged multiple stakeholders, CXO conversations, cross-functional alignment, business + technical selling simultaneously. Critical: ability to understand what to sell to which persona (CTO=architecture/integration, Ops=efficiency/workflow, Business=ROI/outcomes).",
            "influence_ownership": "Influence without authority — drove deals forward despite dependencies, coordinated internal stakeholders, owned outcomes beyond formal scope.",
            "field_sales": "Field sales — in-person meetings, customer visits. Weak: pure inside sales, only remote selling.",
            "company_context": "Company & industry context — SaaS, enterprise software, AI/automation, CX/contact center = high signal. Industry match weighting: same vertical=high, similar buyer environment (regulated/large enterprise)=medium, different industry but strong solution selling=neutral. Transactional/hardware/channel=low.",
            "numbers_metrics": "Numbers & ownership — quota achievement, revenue numbers, deal sizes, pipeline ownership, growth metrics. RED FLAG: sales resume without numbers.",
            "leadership": "Leadership signals — team management, mentoring junior reps, sales playbook creation, hiring involvement, cross-functional coordination, regional/segment ownership",
        },
        "weights": {
            "hunter_mindset": 0.20,
            "solution_selling": 0.20,
            "multi_threading": 0.15,
            "influence_ownership": 0.15,
            "field_sales": 0.05,
            "company_context": 0.15,
            "numbers_metrics": 0.10,
            "leadership": 0.0,
        },
        "bonus_dimensions": {
            "ai_first_selling": "AI-First Solution Selling — has the candidate sold AI-first solutions? Conversational AI, GenAI, Voice AI/Bots, NLP, AI automation platforms, AI-first SaaS. Score 1-10 but report SEPARATELY.",
        },
        "context": """Exotel sells communication infrastructure, contact center platforms, and AI-led solutions (Voice Bots, Conversational AI, CCaaS, CPaaS).

ENTERPRISE SEGMENT: Long sales cycles, complex stakeholder structures, technical solutioning required, industry-specific.
Strong signals: enterprise account selling, CXO engagement, technical discovery, complex negotiations, RFP participation.
Critical success indicator: ability to understand WHAT to sell to WHICH persona — CTO=architecture/integration value, Ops=efficiency & workflow, Business=ROI & outcomes.
Industry match weighting: same vertical=high weight, similar buyer environment (regulated industries, large enterprises)=medium, different industry but strong enterprise solution selling=neutral.

Levels: Sales Manager (5-8/11 yrs) = independent solution hunter, new logo, pipeline creation, full-cycle ownership. Senior Sales Manager (8-14 yrs) = complex deal closer, larger deals, stronger solutioning, negotiation maturity. Principal Sales Manager (14+ yrs) = high-trust complex seller, ambiguous deals, senior stakeholder influence, consensus driving. Red flag at Principal: only leadership without individual selling.

This is for individual contributor hunter roles, NOT account management or customer success.
Red flags: no revenue metrics, pure account management, channel-only, small ticket, inside-sales heavy.""",
    },

    # ── SALES: INTERNATIONAL ─────────────────
    "Sales — International": {
        "description": "International Sales Manager — Africa/ME/SEA markets, cross-border selling",
        "dimensions": {
            "hunter_mindset": "Hunter validation — new logo acquisition, outbound pipeline creation, greenfield acquisition, self-generated pipeline. Deprioritize if revenue from existing accounts/renewals only.",
            "solution_selling": "Solution selling — sold platform/AI/technical/consultative offerings. Strong: AI products, automation platforms, CX platforms, enterprise SaaS. Weak: feature/price/catalogue selling.",
            "multi_threading": "Multi-threading — engaged multiple stakeholders, CXO conversations, cross-functional alignment, business + technical selling simultaneously.",
            "influence_ownership": "Influence without authority — drove deals forward despite dependencies, coordinated internal stakeholders, owned outcomes beyond formal scope.",
            "international_selling": "International selling — selling into Africa/ME/SEA markets, handling remote stakeholders, working across time zones, global procurement processes, understanding regional buying patterns and decision cycles, adapting to cultural and communication differences. Strong: closing large deals with international customers, prior experience in same region. Weak: only outbound calling to international prospects.",
            "company_context": "Company context — SaaS, enterprise software, AI/automation platforms, CX/contact center tools = high signal. Transactional/hardware/channel/distributor = low signal.",
            "numbers_metrics": "Numbers & ownership — quota achievement, revenue numbers, deal sizes, pipeline ownership, growth metrics. RED FLAG: sales resume without numbers.",
            "leadership": "Leadership signals — team management, mentoring junior reps, sales playbook creation, hiring involvement, cross-functional coordination, regional/segment ownership",
        },
        "weights": {
            "hunter_mindset": 0.20,
            "solution_selling": 0.15,
            "multi_threading": 0.10,
            "influence_ownership": 0.10,
            "international_selling": 0.15,
            "company_context": 0.10,
            "numbers_metrics": 0.10,
            "leadership": 0.10,
        },
        "bonus_dimensions": {
            "ai_first_selling": "AI-First Solution Selling — has the candidate sold AI-first solutions? Conversational AI, GenAI, Voice AI/Bots, NLP, AI automation platforms, AI-first SaaS. Score 1-10 but report SEPARATELY.",
        },
        "context": """Exotel sells communication infrastructure, contact center platforms, and AI-led solutions (Voice Bots, Conversational AI, CCaaS, CPaaS).

INTERNATIONAL SEGMENT: Selling into Africa/ME/SEA markets with remote stakeholders across time zones.
Additional signals: closing large deals with international customers, handling cultural and communication differences, understanding regional buying patterns and decision cycles, prior experience selling into the same region the role is focused on.
Strong: named international deal closures, region-specific pipeline. Weak: only outbound calling to international prospects.

Levels: Sales Manager (5-8/11 yrs) = independent solution hunter, new logo, pipeline creation, full-cycle ownership. Senior Sales Manager (8-14 yrs) = complex deal closer, larger deals, stronger solutioning. Principal Sales Manager (14+ yrs) = high-trust complex seller, ambiguous deals, senior stakeholder influence.

This is for individual contributor hunter roles, NOT account management or customer success.
Red flags: no revenue metrics, pure account management, channel-only, small ticket, inside-sales heavy.""",
    },

    # ── SDR: SCALEUP ─────────────────────────
    "SDR — Scaleup": {
        "description": "Scaleup SDR — high-volume outreach, multi-industry, fast experimentation",
        "dimensions": {
            "outbound_ownership": "Outbound ownership — did they GENERATE pipeline or only handle inbound? Cold calling, account research, multi-channel outreach (LinkedIn+Email+Calls), self-generated meetings. Hard deprioritize: no outbound exposure.",
            "funnel_metrics": "Funnel & metric thinking — call-to-meeting ratios, conversion rates, monthly targets, activity metrics (calls/day, emails/day), pipeline contribution. RED FLAG: SDR resume with zero metrics.",
            "qualification_depth": "Qualification depth — discovery questioning, BANT/MEDDIC awareness, pain-point identification, qualification before handoff. Strong: qualified on budget/timeline/use-case. Weak: booked demos without qualification.",
            "technical_curiosity": "Technical curiosity — SaaS exposure, API/SDK familiarity, automation tools, CRM usage (HubSpot/Salesforce), GenAI for research. Strong: sold SaaS, used Apollo/Sales Navigator. Weak: pure non-tech B2B.",
            "industry_persona": "Industry & persona awareness — persona-based messaging (CXOs, Founders, Product Heads), industry pain points (BFSI, D2C, FMCG), contextualized value props. Weak: generic mass messaging.",
            "self_discipline": "Self-discipline & ownership — consistency in target achievement, self-driven prospecting, independent pipeline generation, long tenure in outbound roles. Red flags: frequent switches (<1yr), heavy dependence on marketing.",
            "leadership": "Leadership signals — mentoring junior SDRs, training new hires, creating outreach playbooks, SDR team lead experience, process improvements",
        },
        "weights": {
            "outbound_ownership": 0.25,
            "funnel_metrics": 0.20,
            "qualification_depth": 0.15,
            "technical_curiosity": 0.15,
            "industry_persona": 0.10,
            "self_discipline": 0.15,
            "leadership": 0.0,
        },
        "context": """Exotel SDR is not a generic cold-calling role. SDRs generate qualified opportunities, not just meetings.
Platform: communication APIs, contact centers, AI-led solutions. 10B+ conversations/year for brands like Swiggy, Ola, Zerodha, Flipkart.

SCALEUP SEGMENT: Faster sales cycles, high-volume outreach, multi-industry coverage.
Strong signals: handling multiple verticals, fast experimentation in messaging, high activity volume with structured tracking.

Tier 1 (Strong Fit): Clear outbound ownership, metric-driven, consultative, tech-curious.
Tier 2 (Potential Fit): Outbound exposure but lacks structure or metrics.
Tier 3 (Low Fit): Primarily inbound, no metrics, no qualification depth.
Hard red flags: no outbound, no metrics, pure inbound/support. Soft: only volume focus without funnel awareness, generic resume.""",
    },

    # ── SDR: ENTERPRISE ──────────────────────
    "SDR — Enterprise": {
        "description": "Enterprise SDR — account-based, research-heavy, quality over quantity",
        "dimensions": {
            "outbound_ownership": "Outbound ownership — did they GENERATE pipeline or only handle inbound? Account-based prospecting, named account targeting, research-heavy outreach. Hard deprioritize: no outbound exposure.",
            "funnel_metrics": "Funnel & metric thinking — call-to-meeting ratios, conversion rates, monthly targets, pipeline contribution. Focus on quality metrics over volume. RED FLAG: SDR resume with zero metrics.",
            "qualification_depth": "Qualification depth — discovery questioning, BANT/MEDDIC awareness, pain-point identification, qualification before handoff. Critical for enterprise: quality over quantity mindset. Strong: qualified on budget/timeline/use-case, worked with AEs on enterprise accounts. Weak: booked demos without qualification.",
            "technical_curiosity": "Technical curiosity — SaaS exposure, API/SDK familiarity, automation tools, CRM usage (HubSpot/Salesforce), GenAI for research. Strong: sold SaaS, used Apollo/Sales Navigator. Weak: pure non-tech B2B.",
            "industry_persona": "Industry & persona awareness — persona-based messaging (CXOs, Founders, Product Heads), multi-threading outreach within one account, industry pain points, contextualized value props. Weak: generic mass messaging.",
            "self_discipline": "Self-discipline & ownership — consistency in target achievement, self-driven prospecting, independent pipeline generation, long tenure in outbound roles. Red flags: frequent switches (<1yr), heavy dependence on marketing.",
            "leadership": "Leadership signals — mentoring junior SDRs, training new hires, creating outreach playbooks, SDR team lead experience, process improvements",
        },
        "weights": {
            "outbound_ownership": 0.20,
            "funnel_metrics": 0.15,
            "qualification_depth": 0.20,
            "technical_curiosity": 0.15,
            "industry_persona": 0.15,
            "self_discipline": 0.15,
            "leadership": 0.0,
        },
        "context": """Exotel SDR is not a generic cold-calling role. SDRs generate qualified opportunities, not just meetings.
Platform: communication APIs, contact centers, AI-led solutions. 10B+ conversations/year for brands like Swiggy, Ola, Zerodha, Flipkart.

ENTERPRISE SEGMENT: Account-based prospecting, research-heavy outreach, fewer but high-value meetings.
Strong signals: named account targeting, multi-threading outreach within one account, working with AEs on enterprise accounts.
Critical indicator: QUALITY over quantity mindset. Booking 3 well-qualified enterprise meetings > 20 spray-and-pray demos.

Tier 1 (Strong Fit): Clear outbound ownership, metric-driven, consultative, tech-curious, account-based approach.
Tier 2 (Potential Fit): Outbound exposure but lacks structure or enterprise focus.
Tier 3 (Low Fit): Primarily inbound, no metrics, no qualification depth, only volume-based outreach.
Hard red flags: no outbound, no metrics, pure inbound/support.""",
    },

    # ── SDR: INTERNATIONAL ───────────────────
    "SDR — International": {
        "description": "International SDR — US/MEA/SEA markets, cross-timezone prospecting",
        "dimensions": {
            "outbound_ownership": "Outbound ownership — did they GENERATE pipeline or only handle inbound? Cold calling, account research, multi-channel outreach (LinkedIn+Email+Calls), self-generated meetings. Hard deprioritize: no outbound exposure.",
            "funnel_metrics": "Funnel & metric thinking — call-to-meeting ratios, conversion rates, monthly targets, activity metrics, pipeline contribution. RED FLAG: SDR resume with zero metrics.",
            "qualification_depth": "Qualification depth — discovery questioning, BANT/MEDDIC awareness, pain-point identification, qualification before handoff. Strong: qualified on budget/timeline/use-case. Weak: booked demos without qualification.",
            "international_prospecting": "International prospecting — experience prospecting into US/MEA/SEA markets, working across time zones, handling remote stakeholders, adapting messaging to regional nuances. Strong: booking qualified meetings with international buyers. Weak: only bulk cold emailing internationally, no ownership of qualification.",
            "technical_curiosity": "Technical curiosity — SaaS exposure, API/SDK familiarity, automation tools, CRM usage (HubSpot/Salesforce), GenAI for research. Strong: sold SaaS, used Apollo/Sales Navigator. Weak: pure non-tech B2B.",
            "self_discipline": "Self-discipline & ownership — consistency in target achievement, self-driven prospecting, independent pipeline generation, long tenure in outbound roles. Red flags: frequent switches (<1yr), heavy dependence on marketing.",
            "leadership": "Leadership signals — mentoring junior SDRs, training new hires, creating outreach playbooks, SDR team lead experience, process improvements",
        },
        "weights": {
            "outbound_ownership": 0.20,
            "funnel_metrics": 0.20,
            "qualification_depth": 0.15,
            "international_prospecting": 0.15,
            "technical_curiosity": 0.10,
            "self_discipline": 0.15,
            "leadership": 0.05,
        },
        "context": """Exotel SDR is not a generic cold-calling role. SDRs generate qualified opportunities, not just meetings.
Platform: communication APIs, contact centers, AI-led solutions. 10B+ conversations/year for brands like Swiggy, Ola, Zerodha, Flipkart.

INTERNATIONAL SEGMENT: Prospecting into US/MEA/SEA markets, working across time zones, handling remote stakeholders.
Strong signals: booking qualified meetings with international buyers, adapting messaging to regional nuances, experience in target region.
Weak signals: only bulk cold emailing internationally, no ownership of qualification.

Tier 1 (Strong Fit): Clear outbound ownership, metric-driven, international experience, consultative.
Tier 2 (Potential Fit): Outbound exposure but no international experience.
Tier 3 (Low Fit): Primarily inbound, no metrics, no qualification depth.
Hard red flags: no outbound, no metrics, pure inbound/support.""",
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
            "leadership": "Leadership signals — direct team management, hiring, building functions/teams, driving org-level initiatives, managing managers, program ownership across departments",
        },
        "weights": {
            "strategic_thinking": 0.20,
            "execution_ops": 0.20,
            "cross_functional": 0.15,
            "communication": 0.10,
            "domain_fit": 0.10,
            "leadership_eq": 0.15,
            "company_pedigree": 0.10,
            "leadership": 0.0,
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

    # ── CX: SMB CSM ───────────────────────────
    "CX — SMB CSM": {
        "description": "SMB Customer Success Manager — high-volume portfolio ownership",
        "dimensions": {
            "portfolio_scale": "Portfolio scale — has the candidate managed 50+ accounts? Look for: SMB portfolios, high-volume account ownership, pooled/segmented customer bases. Deprioritize: only enterprise (5-10 accounts), no multi-account evidence.",
            "segmentation_structure": "Segmentation & structured thinking — customer tiering (top/mid/long-tail), engagement playbooks, prioritization frameworks, scalable engagement models. Weak: attempting 1:1 for all accounts, no structured approach.",
            "scalability_automation": "Scalability & automation mindset — email campaigns, lifecycle workflows, self-serve enablement (FAQs, guides), automation workflows, scalable customer journeys. Weak: purely manual account handling.",
            "retention_adoption": "Retention & adoption ownership — product adoption metrics, churn reduction, onboarding/activation ownership. Look for: 'reduced churn by X%', 'increased product usage'. Red flag: no mention of retention or adoption.",
            "expansion": "Expansion (upsell/cross-sell/renewals) — revenue influence within accounts, identifying growth opportunities, renewal ownership. Weak: no commercial awareness.",
            "technical_curiosity": "API & product understanding — basic API understanding, SaaS platform experience, ability to explain product workflows. Weak: no exposure to technical products.",
            "communication_execution": "Communication & execution — clear outcome-driven communication, handling multiple stakeholders, structured thinking, ownership mindset.",
            "leadership": "Leadership signals — team management, mentoring junior CSMs, building CS processes/playbooks, hiring involvement, regional/segment ownership",
        },
        "weights": {
            "portfolio_scale": 0.25,
            "segmentation_structure": 0.20,
            "scalability_automation": 0.10,
            "retention_adoption": 0.20,
            "expansion": 0.10,
            "technical_curiosity": 0.05,
            "communication_execution": 0.10,
            "leadership": 0.0,
        },
        "context": """Exotel SMB CSM is a high-volume, high-ownership role — NOT a relationship-only role.
The SMB CSM owns ~700-800 accounts, drives product adoption/retention/expansion at scale, segments accounts and prioritizes effectively, uses structured engagement and automation.
Requires structured thinking, prioritization, and scalable execution — not just relationship management.
Experience: CSM 2-5 YOE (50+ accounts), Senior CSM 5-8 YOE (100+, strong KPI ownership, segmentation).
Red flags: no multi-account ownership, pure support/onboarding-only role, only enterprise experience (low volume), no metrics, no expansion or retention ownership.""",
    },

    # ── CX: MID-MARKET CSM ────────────────────
    "CX — Mid-Market CSM": {
        "description": "Mid-Market Customer Success Manager — balanced scale and depth",
        "dimensions": {
            "portfolio_complexity": "Portfolio size & complexity — managed 20-100 accounts with recurring engagement, balanced multiple accounts. Enterprise experience (5-10 accounts) is acceptable if structured ownership is demonstrated. Weak: only SMB high-volume (500+, no depth), no clear account ownership.",
            "account_management": "Account management & structured thinking — account plans/playbooks, regular cadence (QBRs, reviews), defined success metrics per account. Weak: reactive customer handling, no structured approach.",
            "retention_adoption": "Retention & adoption ownership — product adoption, churn mitigation, onboarding/lifecycle management. Look for: improved usage/engagement, reduced churn. Weak: no measurable impact.",
            "expansion": "Expansion ownership — upsell/cross-sell contribution, renewal ownership, revenue growth within accounts, identifying expansion opportunities. Weak: no commercial involvement.",
            "stakeholder_management": "Stakeholder management — multi-threaded engagement, working with business + operational stakeholders, managing decision-makers. Weak: single point of contact only.",
            "technical_product": "Technical/product understanding — SaaS/product understanding, basic API awareness, mapping product to use cases. Weak: no technical curiosity.",
            "problem_solving": "Problem-solving & execution — driving outcomes, resolving customer issues end-to-end, cross-functional collaboration.",
            "leadership": "Leadership signals — team management, mentoring junior CSMs, building CS processes/playbooks, hiring involvement, segment ownership",
        },
        "weights": {
            "portfolio_complexity": 0.20,
            "account_management": 0.20,
            "retention_adoption": 0.20,
            "expansion": 0.15,
            "stakeholder_management": 0.10,
            "technical_product": 0.05,
            "problem_solving": 0.10,
            "leadership": 0.0,
        },
        "context": """Exotel Mid-Market CSM is a balanced role between scale and depth.
Owns ~20-100 accounts, drives adoption/retention/expansion, engages multiple stakeholders per account, requires structured account planning.
Enterprise experience (5-10 accounts) is NOT a dealbreaker if candidate demonstrates: structured account management, retention/expansion ownership, ability to handle multiple accounts.
Experience: CSM 2-6 YOE (20-100 accounts, adoption/retention), Senior CSM 6-10 YOE (larger portfolios, strong KPIs, stakeholder influence).
Red flags: no account ownership, pure support roles, only SMB volume without structure, no metrics, no expansion involvement.""",
    },

    # ── CX: ENTERPRISE CSM ────────────────────
    "CX — Enterprise CSM": {
        "description": "Enterprise Customer Success Manager — high-impact strategic ownership",
        "dimensions": {
            "account_value": "Account value & complexity — managed 5-20 enterprise accounts, high ARR ownership, named enterprise accounts, long-term engagement. Weak: only SMB high-volume, no complexity or stakeholder depth.",
            "strategic_management": "Strategic account management — account plans, QBRs/EBRs, defined success metrics, business outcome alignment, strategic roadmap discussions. Weak: reactive engagement, no structured planning.",
            "renewals_retention": "Renewals & retention ownership — renewal ownership, multi-year retention, managing contract cycles. Look for: 'managed renewals worth $X', '95%+ retention'. Weak: no renewal ownership.",
            "expansion": "Expansion (upsell/cross-sell) — large upsell/cross-sell deals, expansion strategy, revenue growth within accounts. Weak: no revenue influence.",
            "stakeholder_cxo": "CXO-level stakeholder management — engagement with CTO/Product Heads/Business Leaders, multi-threaded relationships, influence across functions. Weak: single-threaded relationships.",
            "consultative_approach": "Problem-solving & consultative approach — understanding customer business goals, mapping product to outcomes, business problem-solving, use-case driven engagement.",
            "technical_understanding": "Technical/product understanding — APIs and integrations, technical workflows, comfort with product/engineering teams. Weak: no technical exposure.",
            "leadership": "Leadership signals — CS team management, mentoring, hiring, building enterprise CS function, managing managers, defining CS strategy",
        },
        "weights": {
            "account_value": 0.20,
            "strategic_management": 0.20,
            "renewals_retention": 0.20,
            "expansion": 0.15,
            "stakeholder_cxo": 0.10,
            "consultative_approach": 0.10,
            "technical_understanding": 0.05,
            "leadership": 0.0,
        },
        "context": """Exotel Enterprise CSM is a high-impact, strategic ownership role — closer to consultative sales + program management, NOT support or SMB CS.
Owns ~5-20 high-value accounts, drives long-term retention and large renewals, influences expansion, engages CXOs/Product/Business leaders, navigates complex stakeholder environments, acts as strategic advisor.
Experience: CSM 3-6 YOE (enterprise account ownership, renewal/retention, stakeholder management), Senior CSM 6-9 YOE (larger/strategic accounts, CXO influence, strong expansion).
Red flags: no enterprise account ownership, pure support or SMB-only roles, no renewal ownership, no expansion involvement, weak stakeholder depth, no strategic thinking.""",
    },

    # ── SUPPORT: L1 PRODUCT SUPPORT ───────────
    "Support — L1 Product Support Engineer": {
        "description": "L1 Product Support Engineer — technical troubleshooting & customer handling",
        "dimensions": {
            "linux_fundamentals": "Linux fundamentals — commands (grep, awk, ps, top), log analysis, file system navigation, process-level understanding. This is a primary filter — no Linux exposure is a hard disqualifier.",
            "networking_fundamentals": "Networking fundamentals — DNS, DHCP, OSI model, TCP/IP basics, basic connectivity troubleshooting. If networking is limited but Linux + DB are strong, candidate can still be Potential Fit.",
            "database_querying": "Database querying — experience with any relational DB (PostgreSQL, MySQL, MariaDB, Oracle), SQL queries (joins, filters, aggregations), query-based debugging. No database knowledge is a hard disqualifier.",
            "debugging_approach": "Debugging approach — step-by-step troubleshooting, logical thinking, ability to isolate issues. Look for: 'checked logs and identified...', 'resolved issue by...'. Weak: vague or generic explanations.",
            "customer_communication": "Customer handling & communication — clarity of communication, ability to explain technical issues simply, client/stakeholder interaction. For freshers, strong communication can compensate for lack of experience.",
            "ownership": "Ownership — end-to-end issue handling, closure responsibility, independent work. Weak: only assisting roles.",
            "learning_ability": "Learning ability — curiosity, projects/internships, hands-on exposure. Important especially for freshers.",
            "leadership": "Leadership signals — team lead experience, mentoring junior engineers, shift management, creating runbooks/SOPs, process improvements",
        },
        "weights": {
            "linux_fundamentals": 0.25,
            "networking_fundamentals": 0.10,
            "database_querying": 0.20,
            "debugging_approach": 0.20,
            "customer_communication": 0.10,
            "ownership": 0.10,
            "learning_ability": 0.05,
            "leadership": 0.0,
        },
        "context": """Exotel L1 Support is NOT a ticket-routing role. The L1 Product Support Engineer troubleshoots issues across Linux, networking, and databases on production systems impacting real-time communication.
Owns issues end-to-end within defined scope, communicates clearly with customers and internal teams, operates in an SLA-driven environment.
Experience: Freshers (strong fundamentals + communication + learning mindset), 1-3 YOE (real troubleshooting, production systems, basic customer handling).
Hard disqualifiers: no Linux exposure, no database querying ability.
Soft red flags: no debugging examples, generic resume, poor communication signals.""",
    },

    # ── SUPPORT: L3 PRODUCT SUPPORT LEAD ──────
    "Support — L3 Product Support Lead": {
        "description": "L3 Product Support Lead — senior ownership, RCA, escalation handling",
        "dimensions": {
            "linux_advanced": "Advanced Linux expertise — load average analysis, system bottleneck analysis, advanced grep/awk usage, deep log analysis, performance debugging.",
            "database_advanced": "Advanced database debugging — experience with relational DBs (PostgreSQL, MySQL, MariaDB, Oracle), connection pool issues, replication lag debugging, query optimization, indexing.",
            "networking": "Networking depth — DNS, TCP/IP, latency/debugging issues, network-related RCA.",
            "rca_ownership": "RCA ownership — end-to-end root cause analysis, cross-system debugging, preventive solutions, long-term fixes. No RCA ownership is a hard disqualifier.",
            "escalation_handling": "Escalation handling — high-severity incidents, customer escalations, communication under pressure.",
            "mentorship_leadership": "Mentorship & team contribution — mentoring junior engineers, knowledge sharing, creating playbooks/runbooks.",
            "cross_functional": "Ownership & collaboration — driving issues end-to-end, working with engineering/product, accountability beyond scope.",
            "leadership": "Leadership signals — support team management, hiring, defining escalation processes, managing shifts/on-call, building support org structure",
        },
        "weights": {
            "linux_advanced": 0.20,
            "database_advanced": 0.20,
            "networking": 0.10,
            "rca_ownership": 0.20,
            "escalation_handling": 0.10,
            "mentorship_leadership": 0.10,
            "cross_functional": 0.10,
            "leadership": 0.0,
        },
        "context": """Exotel L3 Support Lead is a senior ownership role requiring deep technical expertise + ownership + leadership + customer handling.
Handles complex production issues, performs end-to-end RCA, manages customer escalations, mentors L1/L2 engineers, works across systems (Linux, DB, networking, application), drives resolution across teams.
Experience: 5+ years with advanced troubleshooting, RCA ownership, escalation handling, mentorship.
Hard disqualifiers: no RCA ownership, no advanced technical depth.
Soft red flags: no mentoring experience, only repetitive support work, only ticket handling without depth.""",
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
