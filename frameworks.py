"""
Exotel Resume Evaluation Frameworks
All role-specific scoring dimensions, weights, and evaluation prompts.
"""

# ─────────────────────────────────────────────
# FRAMEWORK DEFINITIONS
# ─────────────────────────────────────────────

FRAMEWORKS = {

    # ── BACKEND: SE-1 ────────────────────────
    "Backend — SE-1 (0-2 YOE)": {
        "description": "Junior Backend Engineer — fundamentals + learning ability",
        "dimensions": {
            "backend_fundamentals": "Backend fundamentals — REST API development, basic DB usage (SQL, schema design), backend frameworks, server-side logic. Go/Java/Python preferred but any strong backend language acceptable.",
            "learning_ability": "Learning ability & curiosity — internship backend work, deployed projects, personal projects, hackathons, open-source contributions, hands-on exposure beyond coursework. Important: demonstrates self-driven learning.",
            "tech_exposure": "Tech exposure — Linux familiarity, Git workflows, basic Docker usage, SQL understanding, any cloud exposure (AWS). Strong: has actually deployed something. Weak: only tutorials/certifications.",
            "ownership": "Ownership signals — did they OWN something (even small)? Built a feature end-to-end, owned a module, deployed to production. Weak: only assisted, only followed tutorials, resume filled with tools but no work.",
            "communication_clarity": "Resume quality & communication — clear description of what they did vs what the team did, specific technologies mentioned with context, structured resume. Weak: buzzword-heavy, vague descriptions.",
            "genai_expertise": "GenAI signals — LangChain, LangGraph, agent workflows, RAG systems, vector databases, prompt orchestration, evaluation pipelines, production AI systems",
            "leadership": "Leadership signals — college tech lead, organized events, mentored peers, led project teams",
        },
        "weights": {
            "backend_fundamentals": 0.30,
            "learning_ability": 0.25,
            "tech_exposure": 0.20,
            "ownership": 0.15,
            "communication_clarity": 0.10,
            "genai_expertise": 0.0,
            "leadership": 0.0,
        },
        "context": """Exotel builds high reliability, real-time, distributed backend systems.
Primary tech: Go (Platform), Java/PostgreSQL/Citus (Contact Center), Python (GenAI).

SE-1 (0-2 YOE): Strong fundamentals + learning ability. Candidate is expected to be implementation-focused.
Expected: REST API dev, basic DB, backend frameworks, Linux, Git. Go/Java/Python preferred.
Good signals: internship backend work, deployed projects, basic Docker, SQL understanding, API development, basic concurrency, DB schema usage.
NOT expected: architecture design, distributed systems expertise — do NOT penalize for missing these.
Red flags: only tutorials, no backend ownership, resume filled with tools but no actual work, only frontend/scripting.
Red flags (general): frontend-heavy, only scripting/automation, QA/DevOps without backend.""",
    },

    # ── BACKEND: SE-2 ────────────────────────
    "Backend — SE-2 (2-4 YOE)": {
        "description": "Mid-level Backend Engineer — independent feature ownership",
        "dimensions": {
            "backend_depth": "Backend engineering depth — API design, microservices, DB optimization, concurrency, async processing, caching, system performance. Must show production backend experience, not just side projects.",
            "feature_ownership": "End-to-end feature ownership — built and shipped features independently without handholding. Look for: E2E ownership, DB understanding, performance awareness. Weak: only implementation tickets, no impact statements.",
            "performance_awareness": "Performance & optimization — caching implementation, queue usage, async workflows, API optimization, DB indexing. Strong: 'improved API latency by introducing Redis caching'. Weak: no mention of performance.",
            "tech_stack_fit": "Tech stack fit — Go, Java, Python, Kafka, Redis, MongoDB, PostgreSQL/Citus, AWS, Docker/K8s. Production usage required, not just listed.",
            "ownership": "Ownership level — impact statements, measurable outcomes, 'I built/designed/improved X'. Weak: vague team contributions, no specific impact.",
            "genai_expertise": "GenAI signals — LangChain, LangGraph, agent workflows, RAG systems, vector databases, prompt orchestration, evaluation pipelines, production AI systems",
            "leadership": "Leadership signals — mentoring juniors, code reviews, onboarding new team members",
        },
        "weights": {
            "backend_depth": 0.30,
            "feature_ownership": 0.25,
            "performance_awareness": 0.15,
            "tech_stack_fit": 0.15,
            "ownership": 0.15,
            "genai_expertise": 0.0,
            "leadership": 0.0,
        },
        "context": """Exotel builds high reliability, real-time, distributed backend systems.
Primary tech: Go (Platform), Java/PostgreSQL/Citus (Contact Center), Python (GenAI).

SE-2 (2-4 YOE): Independent feature ownership. Engineer should execute without handholding. Production backend exposure required.
Must show: end-to-end feature ownership, database understanding, performance awareness.
Strong signals: caching implementation, queue usage, async workflows, API optimization, DB indexing.
Good example: 'Improved API latency by introducing Redis caching.'
Weak signals: only implementation tickets, no impact statements, no production exposure.
Red flags: frontend-heavy, only scripting/automation, QA/DevOps without backend, buzzword-heavy without depth, service company background without strong eng signals.""",
    },

    # ── BACKEND: SE-3 / TECH LEAD ────────────
    "Backend — SE-3 / Tech Lead (4-5+ YOE)": {
        "description": "Senior Backend / Tech Lead — system-level contributor, Exotel hiring bar increases significantly",
        "dimensions": {
            "backend_depth": "Core backend depth — API design, microservices, distributed systems, concurrency, async processing, DB optimization, caching, system performance at scale.",
            "system_design": "System design & architecture — MANDATORY at this level. Design participation, distributed systems exposure, scalability thinking. Strong: event-driven architecture, Kafka/messaging, service decomposition, HA design, load handling. Common rejection reason: senior title but execution-level work only.",
            "scale_complexity": "Scale & complexity — high throughput, low latency, real-time systems, event-driven, horizontal scaling, large data volumes. Must show evidence of operating at scale.",
            "advanced_system_thinking": "Advanced system thinking — tradeoff awareness (latency vs consistency, perf vs cost), failure handling (retries, timeouts, circuit breakers), load management (rate limiting, backpressure, queue buffering), data safety (idempotency, exactly-once processing), graceful degradation. Presence is a strong positive at this level.",
            "ownership": "Ownership level — designed/owned systems, led implementation, migrated architecture, reduced latency/cost, improved throughput. Must show 'designed' or 'owned', not just 'assisted'.",
            "tech_stack_fit": "Tech stack fit — Go, Java, Python, Kafka, Redis, MongoDB, PostgreSQL/Citus, AWS, Docker/K8s.",
            "genai_expertise": "GenAI signals — LangChain, LangGraph, agent workflows, RAG systems, vector databases, prompt orchestration, evaluation pipelines, production AI systems",
            "leadership": "Leadership signals — mentoring juniors, code reviews, technical decision-making, architecture involvement, cross-team collaboration",
        },
        "weights": {
            "backend_depth": 0.20,
            "system_design": 0.20,
            "scale_complexity": 0.15,
            "advanced_system_thinking": 0.15,
            "ownership": 0.15,
            "tech_stack_fit": 0.10,
            "genai_expertise": 0.0,
            "leadership": 0.05,
        },
        "context": """Exotel builds high reliability, real-time, distributed backend systems.
Primary tech: Go (Platform), Java/PostgreSQL/Citus (Contact Center), Python (GenAI).

SE-3 / Tech Lead (4-5+ YOE): System-level contributor. Exotel hiring bar increases SIGNIFICANTLY here.
MANDATORY signals: design participation, distributed systems exposure, scalability thinking.
Strong technical signals: event-driven architecture, Kafka or messaging systems, service decomposition, high availability design, load handling improvements, retry strategies, timeout management, rate limiting, system observability design.
Expected exposure: performance bottlenecks, service ownership, reliability improvements.
Additional signals: mentoring juniors, code reviews, technical decision involvement.

ADVANCED SYSTEM THINKING (strong positive at this level):
- Tradeoff awareness: latency vs consistency, performance vs cost, simplicity vs scalability
- Failure handling: partial failures, retry mechanisms, timeout strategies, circuit breakers
- Load management: rate limiting, backpressure handling, queue buffering, traffic shaping
- Data safety: idempotency, duplicate event protection, safe retries, exactly-once awareness
- Graceful degradation: reduced capacity during failures, feature fallbacks

Common rejection reason: senior title but execution-level work only — no design, no system thinking.
Red flags: frontend-heavy, only scripting/automation, buzzword-heavy without depth, service company without strong eng signals.""",
    },

    # ── BACKEND: PRINCIPAL ENGINEER ──────────
    "Backend — Principal Engineer (7+ YOE)": {
        "description": "Principal Engineer — key tech choices, cross-system impact, drives decisions",
        "dimensions": {
            "technical_direction": "Technical direction & decision-making — makes key technology choices, establishes patterns other engineers follow, evaluates tradeoffs with reasoning. They DRIVE decisions, not just contribute. Look for: 'defined system architecture', 'led technical direction', 'introduced new architecture patterns'.",
            "system_impact": "Cross-system impact — system redesign, scaling architecture, migration initiatives, DB scaling strategies, reliability improvements. Must show impact beyond a single service. Strong: reduced infra cost, improved throughput, eliminated bottlenecks, multi-service ownership.",
            "advanced_system_thinking": "Advanced system thinking — tradeoff awareness, failure handling & reliability (retries, circuit breakers, fail-safe), load management (rate limiting, backpressure), data safety (idempotency, exactly-once), graceful degradation. Expected to be strong at this level.",
            "backend_depth": "Core backend depth — deep expertise in API design, distributed systems, concurrency, DB optimization, caching, system performance at scale.",
            "ownership": "Ownership — writes most critical/complex components, reviews designs from other engineers for coherence. Must show 'designed' and 'drove', not 'contributed'.",
            "tech_stack_fit": "Tech stack fit — Go, Java, Python, Kafka, Redis, MongoDB, PostgreSQL/Citus, AWS, Docker/K8s.",
            "genai_expertise": "GenAI signals — LangChain, LangGraph, agent workflows, RAG systems, vector databases, prompt orchestration, evaluation pipelines, production AI systems",
            "leadership": "Leadership signals — technical mentoring across teams, architecture reviews, establishing engineering standards, hiring bar-raiser",
        },
        "weights": {
            "technical_direction": 0.25,
            "system_impact": 0.20,
            "advanced_system_thinking": 0.15,
            "backend_depth": 0.15,
            "ownership": 0.10,
            "tech_stack_fit": 0.05,
            "genai_expertise": 0.0,
            "leadership": 0.10,
        },
        "context": """Exotel builds high reliability, real-time, distributed backend systems.
Primary tech: Go (Platform), Java/PostgreSQL/Citus (Contact Center), Python (GenAI).

Principal Engineer (7+ YOE): Makes key technology choices, establishes patterns that other engineers follow, writes the most critical or complex components, reviews designs from other engineers to ensure coherence.
They make technical tradeoffs and decide 'how things should be built.'

Required resume signals: system redesign, scaling architecture, migration initiatives, database scaling strategies, reliability improvements.
Strong indicators: reduced infra cost, improved throughput, eliminated bottlenecks, multi-service ownership.
Important distinction: they DRIVE decisions, not just contribute to them.

Red flag: title inflation without cross-system impact — senior title but no evidence of architectural influence.
Red flags (general): buzzword-heavy without depth, no measurable outcomes, repeated short tenures.""",
    },

    # ── BACKEND: ENGINEERING MANAGER ─────────
    "Backend — Engineering Manager": {
        "description": "Backend EM — hands-on technical leader, managed 4-6 engineers",
        "dimensions": {
            "backend_depth": "Backend engineering depth — strong backend past, architecture involvement, system design. Must have been a credible engineer before managing.",
            "team_management": "Team management — managed 4-6 engineers (ideal for Exotel), mentoring, hiring, team building. Red flag: managed 15+ directly (too far from hands-on), pure delivery/PM with no eng depth.",
            "delivery_execution": "Delivery & execution — project delivery, sprint planning, scope-quality-time tradeoffs, stakeholder management. Breaking down large initiatives, coordinating across teams, managing dependencies.",
            "technical_credibility": "Technical credibility — still technically involved. Look for: 'code review practices', 'provided technical guidance', 'unblocked complex technical challenges', architecture involvement. Positive: '50% coding, 50% people management'. Negative: complete absence of technical work.",
            "engineering_maturity": "Engineering maturity — code review practices, engineering process improvements, unblocking complex challenges, production debugging involvement.",
            "tech_stack_fit": "Tech stack fit — Go, Java, Python, Kafka, Redis, MongoDB, PostgreSQL/Citus, AWS, Docker/K8s.",
            "genai_expertise": "GenAI signals — LangChain, LangGraph, agent workflows, RAG systems, vector databases, prompt orchestration, evaluation pipelines, production AI systems",
            "leadership": "Leadership depth — people management maturity, hiring involvement, conflict resolution, performance management, cross-functional collaboration",
        },
        "weights": {
            "backend_depth": 0.15,
            "team_management": 0.25,
            "delivery_execution": 0.15,
            "technical_credibility": 0.20,
            "engineering_maturity": 0.10,
            "tech_stack_fit": 0.05,
            "genai_expertise": 0.0,
            "leadership": 0.10,
        },
        "context": """Exotel builds high reliability, real-time, distributed backend systems.
Primary tech: Go (Platform), Java/PostgreSQL/Citus (Contact Center), Python (GenAI).

Engineering Manager: Exotel wants hands-on technical leaders. Ideal profile = Lead Software Engineers in good product companies (Fintech, E-commerce, etc.) who managed small teams while staying technically involved.
Target: managed 4-6 engineers, still technically credible, architecture involvement.
Must show: strong backend past, architecture involvement, team management, mentoring, delivery ownership, sprint planning, stakeholder alignment.
Positive signals: 'managed team of 5 while contributing to architecture', 'balanced 50% coding with 50% people management', 'established code review practices', 'unblocked team on complex technical challenges'.
Red flags: pure delivery/project managers with no engineering depth, managed very large teams (15+ directly — suggests beyond hands-on level, typically second-level managers who don't code).""",
    },

    # ── BACKEND: SR. ENGINEERING MANAGER ─────
    "Backend — Sr. Engineering Manager": {
        "description": "Sr. EM — manages 15-20, cross-functional, technical direction",
        "dimensions": {
            "team_scale": "Team scale & org management — managed 15-20 people, potentially managing managers. Cross-functional collaboration with Product, QA, and other engineering teams to deliver larger initiatives.",
            "technical_direction": "Technical direction — defining technical strategy, driving architectural evolution. Should still have recent technical contributions (less than first-level EMs). Look for: architectural reviews, unblocking complex challenges, contributing to critical system designs.",
            "engineering_process": "Engineering process — engineering process improvements, quality bar-setting, incident response maturity, release management, tech debt management.",
            "delivery_execution": "Delivery & execution — delivered larger cross-team initiatives, managed dependencies across teams, stakeholder management at senior level.",
            "backend_depth": "Backend engineering depth — strong backend past. Complete absence of technical involvement in recent roles is concerning.",
            "tech_stack_fit": "Tech stack fit — Go, Java, Python, Kafka, Redis, MongoDB, PostgreSQL/Citus, AWS, Docker/K8s.",
            "genai_expertise": "GenAI signals — LangChain, LangGraph, agent workflows, RAG systems, vector databases, prompt orchestration, evaluation pipelines, production AI systems",
            "leadership": "Leadership depth — managing managers, hiring, org design, people development, cross-functional influence, conflict resolution at org level",
        },
        "weights": {
            "team_scale": 0.20,
            "technical_direction": 0.20,
            "engineering_process": 0.15,
            "delivery_execution": 0.15,
            "backend_depth": 0.10,
            "tech_stack_fit": 0.05,
            "genai_expertise": 0.0,
            "leadership": 0.15,
        },
        "context": """Exotel builds high reliability, real-time, distributed backend systems.
Primary tech: Go (Platform), Java/PostgreSQL/Citus (Contact Center), Python (GenAI).

Senior Engineering Manager: Influences technical direction of the team. Should still have recent technical contributions, although less than first-level EMs. Look for: involvement in architectural reviews, unblocking complex technical challenges, contributing to critical system designs.
Expected: managed 15-20 people, cross-functional collaboration (Product, QA, other eng teams), engineering process improvements, technical direction setting.
Complete absence of technical involvement in recent roles is concerning.
Red flags: pure people manager with zero technical awareness, no engineering process improvements, only operational/delivery focus without strategic technical involvement.""",
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
