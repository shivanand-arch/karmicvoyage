"""
Exotel Resume Evaluation Frameworks
All role-specific scoring dimensions, weights, and evaluation prompts.
"""

# ─────────────────────────────────────────────
# FRAMEWORK DEFINITIONS
# ─────────────────────────────────────────────

FRAMEWORKS = {

    # ── BACKEND: SE-1 ────────────────────────────
    "Backend — SE-1 (0-2 YOE)": {
        "description": "Junior backend engineer with strong fundamentals and learning ability, expected to be implementation-focused.",
        "dimensions": {
            "backend_fundamentals": "Proficiency in core backend languages (Go, Java, Python or similar). Evidence of REST API development, basic database usage (SQL understanding, DB schema usage), backend frameworks, Linux familiarity, and Git workflows. Look for internship backend work, deployed projects, basic Docker usage. Evaluate whether the candidate has hands-on experience writing server-side logic, not just tutorials or tool listings.",
            "code_and_implementation_quality": "Ability to write clean, functional backend code and deliver working features. Look for evidence of building backend services, API development, basic concurrency handling. Assess whether projects show real implementation effort vs. copy-paste or tutorial-following. Strong signals include deployed projects with actual backend logic, contributions to production codebases.",
            "database_and_storage": "Basic understanding of databases and data storage. Evidence of SQL usage, DB schema design or interaction, basic query writing. At this level, deep optimization is not expected, but the candidate should demonstrate they can work with databases beyond trivial CRUD. Look for PostgreSQL, MongoDB, or similar database interaction in projects or work experience.",
            "learning_ability_and_potential": "Signals of growth trajectory, curiosity, and adaptability. Strong academic background, relevant side projects, open-source contributions, hackathon participation with backend focus, certifications in relevant technologies. For fresh graduates, quality of internships and project complexity matters. Look for progression from academic to practical backend work.",
            "company_and_career_context": "Quality of companies and environments worked in. Product companies, funded startups, SaaS platforms are stronger signals than service companies or maintenance roles. For freshers, quality of internships and university project context matters. Tenure stability is less critical at this level but multiple very short stints are still a concern.",
            "genai_expertise": "Experience with GenAI/LLM technologies: LangChain, LangGraph, RAG pipelines, agent workflows, vector databases, prompt orchestration, evaluation pipelines. Production GenAI deployment is the strongest signal. Weak signals include OpenAI API wrappers, demo chatbots, or hackathon-only projects.",
            "leadership": "Leadership signals such as mentoring, team coordination, technical decision-making, or people management. Not expected at SE-1 level.",
        },
        "weights": {
            "backend_fundamentals": 0.35,
            "code_and_implementation_quality": 0.25,
            "database_and_storage": 0.15,
            "learning_ability_and_potential": 0.15,
            "company_and_career_context": 0.10,
            "genai_expertise": 0.0,
            "leadership": 0.0,
        },
        "context": """Exotel backend context: High-throughput, event-driven, reliability-sensitive systems with low-latency expectations. Tech stacks include Golang (platform/voice/messaging), Java with PostgreSQL/Citus (contact center), and Python (GenAI product). Production ownership is expected from all engineers.

SE-1 expectations: Implementation-focused. Should demonstrate strong fundamentals and ability to learn. Not expected to have architecture design, distributed systems expertise, or leadership/mentoring experience.

Strong signals: Backend internship work, deployed projects, API development experience, basic concurrency understanding, SQL proficiency, Git workflow familiarity, basic Docker usage.

Weak signals: Only CRUD services with no depth, tool-heavy but impact-light resumes, no scale or performance discussion (acceptable at this level but noted).

Red flags: Only tutorials with no real projects, no backend ownership evidence, resume filled with tools/buzzwords but no actual work, frontend-heavy with no backend, only scripting/automation, QA/DevOps without backend history, academic-only projects with no practical application.""",
    },

    # ── BACKEND: SE-2 ────────────────────────────
    "Backend — SE-2 (2-4 YOE)": {
        "description": "Mid-level backend engineer capable of independent feature ownership, expected to execute without handholding.",
        "dimensions": {
            "backend_engineering_depth": "Production backend experience in Go, Java, Python or equivalent. Must show end-to-end feature ownership, not just ticket implementation. Look for API development and optimization, microservices experience, async processing, concurrency handling. Evidence of building and maintaining backend services in production. Strong signals: caching implementation (Redis), queue usage (Kafka, RabbitMQ), async workflows, API optimization, service ownership.",
            "database_and_performance": "Database understanding beyond basic CRUD. Look for DB indexing knowledge, query optimization, schema design decisions, caching strategies to reduce latency. Performance awareness is critical — candidate should show they understand how to make systems faster. Strong signal: 'Improved API latency by introducing Redis caching' or similar impact statements. Weak signal: no mention of performance or optimization.",
            "scale_and_reliability": "Early signals of working in environments with scale considerations. Look for exposure to high-throughput systems, event-driven patterns, queue-based architectures, basic monitoring and observability. Production debugging and incident awareness are positive signals. Not expected to design these systems but should have worked within them.",
            "ownership_and_impact": "Evidence of owning features end-to-end with measurable outcomes. Language like 'designed', 'owned', 'built', 'improved' vs. 'assisted', 'supported'. Must show impact statements — latency reduced, throughput improved, cost savings. Weak signals: only implementation tickets with no impact, no ownership language, no measurable outcomes.",
            "company_and_career_context": "Quality of engineering environments. Product companies, funded startups, SaaS platforms, scale-heavy companies are stronger signals. Tenure of 1.5-3 years with increasing responsibility is ideal. Multiple short stints without explanation are concerning. Service company experience with strong engineering roles is acceptable but weighted lower.",
            "genai_expertise": "Experience with GenAI/LLM technologies: LangChain, LangGraph, RAG pipelines, agent workflows, vector databases, prompt orchestration, evaluation pipelines. Production GenAI deployment is the strongest signal. Weak signals include OpenAI API wrappers, demo chatbots, or hackathon-only projects.",
            "leadership": "Leadership signals such as mentoring, team coordination, technical decision-making, or people management. Not a primary expectation at SE-2 but early signals are positive.",
        },
        "weights": {
            "backend_engineering_depth": 0.30,
            "database_and_performance": 0.25,
            "scale_and_reliability": 0.20,
            "ownership_and_impact": 0.15,
            "company_and_career_context": 0.10,
            "genai_expertise": 0.0,
            "leadership": 0.0,
        },
        "context": """Exotel backend context: High-throughput, event-driven, reliability-sensitive systems with low-latency expectations. Tech stacks include Golang (platform/voice/messaging), Java with PostgreSQL/Citus (contact center), and Python (GenAI product). Production ownership is expected from all engineers.

SE-2 expectations: Independent feature ownership. Should execute without handholding. Must demonstrate production backend experience with measurable impact. Performance awareness and database depth are differentiators at this level.

Strong signals: Caching implementation (Redis), queue usage (Kafka), async workflows, API optimization, DB indexing, end-to-end feature delivery with impact metrics, production debugging experience, service ownership.

Weak signals: Only implementation tickets without impact statements, no performance or optimization discussion, no ownership language, tool-heavy but impact-light resumes.

Red flags: No production backend exposure after 2+ years, only frontend or scripting work, buzzword-heavy with no depth, no measurable outcomes, repeated short tenures, senior title at service company with only CRUD work.""",
    },

    # ── BACKEND: SE-3 ────────────────────────────
    "Backend — SE-3/Tech Lead (4-5+ YOE)": {
        "description": "System-level contributor with distributed systems exposure and design participation; Exotel hiring bar increases significantly at this level.",
        "dimensions": {
            "system_design_and_architecture": "Design participation and architectural thinking. Must show distributed systems exposure, service decomposition, event-driven architecture design. Look for: Kafka or messaging system usage, high availability design, load handling improvements, system observability design. Candidates should demonstrate tradeoff awareness — latency vs consistency, performance vs cost, simplicity vs scalability. Strong signals include technology evaluation with reasoning, migration initiatives, architecture pattern introduction.",
            "scale_and_reliability_engineering": "Deep experience with scale and reliability challenges. Must demonstrate: retry strategies, timeout management, rate limiting, circuit breakers, backpressure handling, idempotency, graceful degradation. Look for failure handling patterns — partial failure management, fail-safe design, fallback mechanisms. Evidence of handling production incidents, root cause analysis, on-call ownership. This is critical for Exotel's reliability-sensitive environment.",
            "backend_technical_depth": "Strong backend engineering fundamentals at senior level. Proficiency in Go, Java, or Python with production distributed systems. Concurrency expertise, async processing at scale, performance bottleneck identification and resolution. Look for: event-driven processing, queue-based architectures, caching strategies at scale, database performance tuning, horizontal scaling experience.",
            "ownership_and_impact": "High ownership signals — 'designed service', 'owned system', 'led implementation', 'migrated architecture', 'reduced latency/cost', 'improved throughput'. Must show system-level impact, not just feature-level. Service ownership across the full lifecycle. Impact should be quantified where possible. Common rejection reason at this level: senior title but execution-level work only.",
            "mentoring_and_technical_leadership": "Evidence of mentoring juniors, conducting code reviews, involvement in technical decisions. This differentiates SE-3 from strong SE-2. Look for team guidance, design review participation, establishing engineering practices. Should be an informal leader even without a manager title.",
            "company_and_career_context": "Quality and relevance of engineering environments. Product companies with scale challenges are ideal. Career trajectory should show increasing scope and responsibility. Tenure of 1.5-3 years per role with progression. Strong concern if candidate has senior title but only worked in low-scale or maintenance environments.",
            "genai_expertise": "Experience with GenAI/LLM technologies: LangChain, LangGraph, RAG pipelines, agent workflows, vector databases, prompt orchestration, evaluation pipelines. Production GenAI deployment is the strongest signal. Weak signals include OpenAI API wrappers, demo chatbots, or hackathon-only projects.",
            "leadership": "Formal or informal leadership beyond mentoring — driving technical direction, leading cross-team initiatives, project leadership. Positive signal at SE-3 but not the primary evaluation criterion.",
        },
        "weights": {
            "system_design_and_architecture": 0.25,
            "scale_and_reliability_engineering": 0.25,
            "backend_technical_depth": 0.20,
            "ownership_and_impact": 0.15,
            "mentoring_and_technical_leadership": 0.10,
            "company_and_career_context": 0.05,
            "genai_expertise": 0.0,
            "leadership": 0.0,
        },
        "context": """Exotel backend context: High-throughput, event-driven, reliability-sensitive systems with low-latency expectations. Tech stacks include Golang (platform/voice/messaging), Java with PostgreSQL/Citus (contact center), and Python (GenAI product). Production ownership is expected from all engineers.

SE-3/Tech Lead expectations: System-level contributor. This is where Exotel's hiring bar increases significantly. Must demonstrate design participation, distributed systems exposure, and scalability thinking. Should show advanced system thinking — tradeoff awareness, failure handling, load management, data safety (idempotency), and graceful degradation.

Strong signals: Event-driven architecture design, Kafka/messaging systems expertise, service decomposition, high availability design, retry/timeout/rate-limiting strategies, circuit breakers, backpressure handling, idempotent API design, system observability, mentoring juniors, code review leadership, technical decision involvement, quantified impact on latency/throughput/cost.

Weak signals: Senior title but only execution-level work, no design participation, no distributed systems evidence, no system-level thinking, no mentoring signals, only CRUD or simple microservices.

Red flags: Title inflation without cross-system impact, no reliability or failure-handling experience after 4+ years, inability to articulate tradeoffs, no evidence of owning systems end-to-end, buzzword-heavy resume with no architectural depth, multiple short stints at this seniority level.""",
    },

    # ── BACKEND: Principal ────────────────────────
    "Backend — Principal Engineer (7+ YOE)": {
        "description": "Makes key technology choices, establishes patterns for other engineers, writes the most critical components, and reviews designs for coherence across systems.",
        "dimensions": {
            "architecture_and_technical_vision": "Drives architectural decisions, not just contributes to them. Must show: system redesign, scaling architecture, migration initiatives, database scaling strategies. Look for evidence of defining system architecture, leading technical direction, evaluating tradeoffs at org level, introducing new architecture patterns. Should demonstrate choosing 'how things should be built' for the engineering organization.",
            "cross_system_impact": "Impact spanning multiple services, teams, or systems. Must show multi-service ownership, eliminated bottlenecks across systems, infrastructure cost reduction, throughput improvements at platform level. Principal Engineers set patterns that other engineers follow — look for evidence of establishing engineering standards, reusable frameworks, or platform-level improvements.",
            "reliability_and_scale_mastery": "Deep mastery of reliability and scale challenges. Production-proven experience with: high availability at scale, disaster recovery, capacity planning, performance engineering, zero-downtime migrations. Should demonstrate sophisticated failure handling, load management, and system protection patterns. Evidence of handling the most complex technical challenges in the organization.",
            "technical_decision_making": "Makes technical tradeoffs with business awareness. Technology evaluation with clear reasoning, build-vs-buy decisions, technical debt management at strategic level. Should show evidence of influencing technology roadmap, defining technical standards, and making decisions that shape engineering culture.",
            "ownership_and_impact": "Writes the most critical or complex components. Quantified impact at system or organizational level — reduced infra cost significantly, improved throughput at platform scale, led critical migrations. Reviews designs from other engineers to ensure coherence. Must demonstrate driving decisions, not just participating.",
            "company_and_career_context": "Career trajectory showing increasing scope from system to organization level. Strong product company experience, ideally at companies facing real scale challenges. Progressive responsibility growth. Long enough tenures to show deep impact (2+ years in senior roles).",
            "genai_expertise": "Experience with GenAI/LLM technologies: LangChain, LangGraph, RAG pipelines, agent workflows, vector databases, prompt orchestration, evaluation pipelines. Production GenAI deployment is the strongest signal. Weak signals include OpenAI API wrappers, demo chatbots, or hackathon-only projects.",
            "leadership": "Technical leadership at organizational level — setting technical direction, influencing engineering culture, mentoring senior engineers, representing engineering in cross-functional decisions.",
        },
        "weights": {
            "architecture_and_technical_vision": 0.25,
            "cross_system_impact": 0.20,
            "reliability_and_scale_mastery": 0.20,
            "technical_decision_making": 0.15,
            "ownership_and_impact": 0.15,
            "company_and_career_context": 0.05,
            "genai_expertise": 0.0,
            "leadership": 0.0,
        },
        "context": """Exotel backend context: High-throughput, event-driven, reliability-sensitive systems with low-latency expectations. Tech stacks include Golang (platform/voice/messaging), Java with PostgreSQL/Citus (contact center), and Python (GenAI product). Production ownership is expected from all engineers.

Principal Engineer expectations: Makes key technology choices and establishes patterns that other engineers follow. Writes the most critical or complex components. Reviews designs from other engineers to ensure coherence. Drives decisions — does not just contribute to them.

Strong signals: System redesign initiatives, scaling architecture across multiple services, migration leadership, database scaling strategies, reduced infra cost at significant scale, eliminated cross-system bottlenecks, multi-service ownership, introduced architecture patterns adopted by the org, defined technical direction for teams, technology evaluation with clear tradeoff reasoning.

Weak signals: Senior title but scope limited to single service, no cross-system impact, no architecture or design leadership, only execution even at high quality, no evidence of establishing patterns for others.

Red flags: Title inflation without cross-system impact, 7+ years but scope equivalent to SE-3, no evidence of driving (vs participating in) technical decisions, no reliability or migration experience, career spent entirely in low-scale environments, buzzword-heavy without architectural depth, no measurable organizational-level impact.""",
    },

    # ── BACKEND: Engineering Manager ──────────────
    "Backend — Engineering Manager": {
        "description": "Hands-on technical leader managing 4-6 engineers while staying technically credible; Exotel needs EMs who code and architect, not pure people managers.",
        "dimensions": {
            "technical_credibility": "Strong backend engineering past with continued technical involvement. Must show architecture involvement, code review and technical guidance, unblocking teams on complex technical challenges. Look for: 'managed team while contributing to architecture decisions', 'hands-on coding for critical components', 'balanced coding with people management'. Established code review practices and provided technical guidance to team.",
            "people_management": "Team management experience with 4-6 engineers (ideal for Exotel's needs). Evidence of mentoring, career development support, hiring involvement, performance management. Look for building and growing engineering teams, not just inheriting large organizations. Managing small teams while staying hands-on is the target profile.",
            "delivery_and_execution": "Ability to deliver projects on time with quality. Evidence of managing sprint planning, balancing technical debt with features, making scope-quality-time tradeoffs, managing stakeholder expectations. Breaking down large initiatives, coordinating across teams, managing dependencies. Project management skills complementing people management.",
            "engineering_process": "Establishing and improving engineering processes — code review practices, CI/CD, testing standards, on-call rotations, incident management. Look for evidence of process improvement that increased team velocity or quality without adding bureaucracy.",
            "stakeholder_management": "Stakeholder alignment, cross-functional collaboration, communicating technical concepts to non-technical stakeholders. Evidence of managing expectations, providing visibility into engineering progress, influencing product direction with technical perspective.",
            "genai_expertise": "Experience with GenAI/LLM technologies: LangChain, LangGraph, RAG pipelines, agent workflows, vector databases, prompt orchestration, evaluation pipelines. Production GenAI deployment is the strongest signal. Weak signals include OpenAI API wrappers, demo chatbots, or hackathon-only projects.",
            "leadership": "Broader leadership beyond direct team — influencing engineering culture, driving organizational improvements, cross-team collaboration, strategic thinking about engineering direction.",
        },
        "weights": {
            "technical_credibility": 0.30,
            "people_management": 0.25,
            "delivery_and_execution": 0.20,
            "engineering_process": 0.15,
            "stakeholder_management": 0.10,
            "genai_expertise": 0.0,
            "leadership": 0.0,
        },
        "context": """Exotel backend context: High-throughput, event-driven, reliability-sensitive systems with low-latency expectations. Tech stacks include Golang (platform/voice/messaging), Java with PostgreSQL/Citus (contact center), and Python (GenAI product). Production ownership is expected from all engineers.

Engineering Manager expectations: Exotel wants hands-on technical leaders. The ideal profile is Lead Software Engineers from good product companies (fintech, ecommerce, etc.) who have managed small teams while staying technically involved. Continued technical involvement is critical. Target: managed 4-6 engineers while still being technically credible.

Strong signals: 'Managed team of 5 engineers while contributing to architecture decisions', 'led team building payment platform with hands-on coding for critical components', 'balanced 50% coding with 50% people management', 'established code review practices', 'provided technical guidance to team', 'unblocked team on complex technical challenges', sprint planning and delivery ownership, stakeholder alignment.

Weak signals: Pure people management with no recent technical involvement, managed only through project management tools without technical depth, no architecture or code review involvement.

Red flags: Pure delivery/project managers with no engineering depth, has managed very large teams (15+ engineers) directly — suggests they are beyond the hands-on level Exotel needs (typically second-level managers who do not code), no backend engineering history, no technical credibility signals in recent roles, career trajectory away from technology.""",
    },

    # ── BACKEND: Sr. Engineering Manager ──────────
    "Backend — Sr. Engineering Manager": {
        "description": "Senior engineering leader managing 15-20 people with cross-functional collaboration, engineering process improvements, and technical direction setting while maintaining technical involvement.",
        "dimensions": {
            "technical_direction_and_strategy": "Influences technical direction of the team/org. Evidence of defining technical strategy, driving architectural evolution, involvement in architectural reviews, unblocking complex technical challenges, contributing to critical system designs. Should still have recent technical contributions although less than first-level EMs. Complete absence of technical involvement in recent roles is concerning.",
            "organizational_leadership": "Managing teams of 15-20 people effectively. Cross-functional collaboration with Product, QA, and other engineering teams to deliver larger initiatives. Evidence of building engineering organizations, not just managing existing teams. Ability to scale teams, hire senior talent, and develop engineering leaders.",
            "engineering_process_and_culture": "Engineering process improvements at organizational level. Driving engineering excellence — quality standards, reliability practices, development velocity improvements. Building engineering culture that attracts and retains talent. Evidence of initiatives that improved engineering maturity across multiple teams.",
            "delivery_at_scale": "Delivering large, cross-team initiatives successfully. Managing dependencies across teams, coordinating releases, balancing multiple workstreams. Evidence of shipping complex projects involving multiple teams and stakeholders. Strategic prioritization and resource allocation.",
            "stakeholder_and_cross_functional_management": "Senior stakeholder management — working with product leadership, business teams, and executive leadership. Translating business needs to engineering strategy. Managing expectations at leadership level. Evidence of influencing product and business direction with engineering perspective.",
            "genai_expertise": "Experience with GenAI/LLM technologies: LangChain, LangGraph, RAG pipelines, agent workflows, vector databases, prompt orchestration, evaluation pipelines. Production GenAI deployment is the strongest signal. Weak signals include OpenAI API wrappers, demo chatbots, or hackathon-only projects.",
            "leadership": "Executive-level leadership — organizational strategy, talent strategy, engineering vision, cross-functional influence at company level.",
        },
        "weights": {
            "technical_direction_and_strategy": 0.25,
            "organizational_leadership": 0.25,
            "engineering_process_and_culture": 0.20,
            "delivery_at_scale": 0.15,
            "stakeholder_and_cross_functional_management": 0.15,
            "genai_expertise": 0.0,
            "leadership": 0.0,
        },
        "context": """Exotel backend context: High-throughput, event-driven, reliability-sensitive systems with low-latency expectations. Tech stacks include Golang (platform/voice/messaging), Java with PostgreSQL/Citus (contact center), and Python (GenAI product). Production ownership is expected from all engineers.

Sr. Engineering Manager expectations: Manages 15-20 people with cross-functional collaboration. Should influence technical direction and still maintain some technical involvement (architectural reviews, unblocking complex challenges, contributing to critical system designs). Expected to drive engineering process improvements and set technical direction at organizational level.

Strong signals: Managed 15-20 person engineering org, cross-functional collaboration with Product/QA/other engineering teams, engineering process improvements at org level, technical strategy definition, architectural evolution leadership, recent technical contributions (even if reduced), delivered large cross-team initiatives, built and scaled engineering teams.

Weak signals: Only people management with no technical involvement, managed through layers with no direct engineering impact, no evidence of process improvement or engineering culture building.

Red flags: Complete absence of technical involvement in recent roles, pure project/program management without engineering depth, managed 50+ people (too senior/removed for Exotel's needs), no cross-functional collaboration evidence, no engineering process improvement signals, career entirely in service companies with no product engineering depth.""",
    },

    # ── SALES: Mid-Market ────────────────────────
    "Sales — Mid-Market": {
        "description": "Mid-Market sales IC hunter roles at Exotel — faster cycles, industry-agnostic, high pipeline velocity",
        "dimensions": {
            "hunter_mindset": "Hunter validation — new logo acquisition, outbound pipeline creation, greenfield territory development, self-generated pipeline. Must show evidence of CREATING business, not just managing it. Strong: outbound prospecting, full-cycle sales ownership, demo to closure. Deprioritize heavily if revenue comes primarily from existing accounts, renewals, or customer success.",
            "solution_selling": "Solution selling ability — has the candidate sold platform products, AI products, technical solutions, or configurable/consultative offerings? Strong: AI product selling, automation platforms, CX platforms, enterprise SaaS, solution mapping, use-case driven selling. Weak: feature selling, price-driven selling, catalogue-based selling.",
            "pipeline_velocity": "Pipeline creation and velocity — ability to manage multiple concurrent opportunities efficiently, strong discovery and qualification skills, efficient deal progression from prospecting to close. Look for: outbound prospecting volume, full-cycle ownership, qualification frameworks, pipeline-to-close ratios, ability to handle high deal volume simultaneously.",
            "multi_threading": "Multi-threading and stakeholder navigation — ability to handle multiple stakeholders quickly in shorter cycles. Engaged CXO + technical + operations personas. Cross-functional alignment, business + technical selling simultaneously. Must show ability to quickly identify and engage decision-makers.",
            "company_context": "Company and selling environment fit — SaaS companies, enterprise software, AI/automation platforms, CX/contact center tools, CRM companies, infrastructure or platform sales = high signal. These environments create sellers comfortable with ambiguity and solutioning. Low signal: transactional product selling, hardware-only, channel-led, distributor-driven sales.",
            "numbers_metrics": "Numbers and ownership validation — quota achievement percentages, revenue numbers, deal sizes, pipeline ownership metrics, growth metrics. Strong: '120% quota for 3 consecutive years', 'built pipeline worth 3X quota'. RED FLAG: sales resume without any numbers or revenue metrics.",
            "influence_ownership": "Influence without authority and deal ownership — drove deals forward despite dependencies on presales/product/engineering, coordinated internal stakeholders, resolved customer blockers, owned outcomes beyond formal scope. Weak: only passed leads downstream, heavy reliance on presales for deal movement.",
        },
        "weights": {
            "hunter_mindset": 0.20,
            "solution_selling": 0.20,
            "pipeline_velocity": 0.15,
            "multi_threading": 0.15,
            "company_context": 0.10,
            "numbers_metrics": 0.10,
            "influence_ownership": 0.10,
        },
        "context": """Exotel Mid-Market sales involves relatively faster sales cycles, catering across industries (industry-agnostic), managing multiple concurrent opportunities, and strong discovery/qualification skills.

Company context: Exotel sells communication infrastructure (CPaaS), contact center platforms (CCaaS), and AI-led solutions (Voice Bots, Conversational AI). 10B+ conversations/year for brands like Swiggy, Ola, Zerodha, Flipkart.

What to look for: Pipeline creation ability is paramount. Mid-market sellers must demonstrate high throughput — managing many deals simultaneously while maintaining quality discovery. Full-cycle ownership from prospecting to close. Solution mapping to customer pain points rather than feature pitching.

Strong signals: Outbound prospecting, full-cycle sales ownership, demo-to-closure experience, solution mapping, SaaS/platform selling background, clear quota attainment numbers, multiple concurrent deal management.

Weak signals: Pure renewals/account management, inside-sales only, feature/price-driven selling, no revenue metrics, channel-only sales.

Red flags: No revenue metrics on resume, pure account management background, channel-only or distributor-driven sales, small ticket size accounts, inside-sales heavy profiles, only passed leads downstream without owning closure.

Level expectations:
- Sales Manager (5-8 yrs): Independent solution hunter. Must show new logo acquisition, pipeline creation, full-cycle ownership, stakeholder navigation.
- Sr Sales Manager (8-14 yrs): Complex deal closer. Larger deal ownership, strong solutioning, negotiation maturity, stakeholder influence.
- Principal Sales Manager (14+ yrs): High-trust complex seller. Handles ambiguous deals, influences senior stakeholders, drives consensus, end-to-end outcome ownership. Red flag if only leadership without individual selling.""",
    },

    # ── SALES: Enterprise ────────────────────────
    "Sales — Enterprise": {
        "description": "Enterprise sales IC hunter roles at Exotel — long cycles, complex stakeholder structures, industry-specific, technical solutioning",
        "dimensions": {
            "hunter_mindset": "Hunter validation — new logo acquisition in enterprise accounts, greenfield enterprise territory development, self-generated pipeline in large accounts. Must show evidence of CREATING new enterprise business. Strong: new enterprise account acquisition, outbound into large organizations. Deprioritize if revenue comes primarily from farming existing accounts or renewals.",
            "solution_selling": "Solution selling depth — has the candidate sold complex platform products, AI solutions, or deeply technical/consultative offerings to enterprises? Very strong: AI product selling, automation platforms, CX platforms, enterprise SaaS with long implementation cycles. Must demonstrate ability to tailor solutions to enterprise requirements. Weak: feature/price/catalogue selling, transactional product sales.",
            "stakeholder_complexity": "Stakeholder complexity and persona-based selling — ability to understand what to sell to which persona: CTO (architecture/integration value), Ops (efficiency/workflow), Business (ROI/outcomes). CXO engagement, technical discovery, complex negotiations, RFP participation. Must show evidence of managing deal across engineering, operations, and procurement stakeholders.",
            "multi_threading": "Multi-threading across complex org structures — engaged multiple stakeholders simultaneously, navigated enterprise procurement processes, managed technical objections across functions, coordinated internal teams for deal closure. Must show ability to drive deals through organizational complexity with long decision cycles.",
            "industry_alignment": "Industry and vertical alignment — High weight: same vertical enterprise selling experience (e.g., BFSI for BFSI role, healthcare for healthcare). Medium weight: similar buyer environment (regulated industries, large enterprises). Neutral: different industry but strong enterprise solution selling capability. Look for depth of understanding in specific verticals.",
            "company_context": "Company and selling environment fit — SaaS companies, enterprise software, AI/automation platforms, CX/contact center tools, infrastructure or platform sales = high signal. Enterprise B2B background with complex sales motions preferred. Low signal: transactional selling, hardware-only, channel-led, SMB-focused backgrounds.",
            "numbers_metrics": "Numbers, deal sizes, and ownership — quota achievement, revenue numbers, enterprise deal sizes (look for large ACV), pipeline ownership, growth metrics. Strong: 'Closed enterprise deals worth X Cr', multi-year contract values, strategic account growth. RED FLAG: enterprise sales resume without revenue numbers or deal sizes.",
        },
        "weights": {
            "hunter_mindset": 0.15,
            "solution_selling": 0.20,
            "stakeholder_complexity": 0.20,
            "multi_threading": 0.15,
            "industry_alignment": 0.10,
            "company_context": 0.10,
            "numbers_metrics": 0.10,
        },
        "context": """Exotel Enterprise sales involves long sales cycles, complex stakeholder structures, technical solutioning requirements, and industry-specific depth.

Company context: Exotel sells communication infrastructure (CPaaS), contact center platforms (CCaaS), and AI-led solutions (Voice Bots, Conversational AI) to large enterprises. Customers include major brands across BFSI, e-commerce, healthcare, and more.

What to look for: The critical success indicator is the ability to understand what to sell to which persona — CTO gets architecture/integration value, Ops gets efficiency/workflow, Business gets ROI/outcomes. Enterprise sellers must demonstrate deep solutioning capability, long-cycle deal management, and multi-stakeholder navigation. Industry vertical experience is weighted based on match to the specific role.

Strong signals: Enterprise account selling, CXO engagement, technical discovery, complex negotiations, RFP participation, strategic enterprise accounts, persona-based selling, multi-year contracts, large deal closures.

Weak signals: Pure SMB/mid-market experience without enterprise complexity, feature/price selling, single-stakeholder deals, channel-only, transactional backgrounds.

Red flags: No revenue metrics or deal sizes, pure account management, channel-only sales, inside-sales heavy, only leadership roles without individual selling (especially at Principal level), small ticket sizes, no evidence of stakeholder complexity.

Industry Match Weighting:
- High Weight: Same vertical enterprise selling experience (e.g., BFSI for BFSI role)
- Medium Weight: Similar buyer environment (regulated industries, large enterprises)
- Neutral: Different industry but strong enterprise solution selling capability

Level expectations:
- Sales Manager (5-8 yrs): Independent solution hunter in enterprise accounts. New logo acquisition, pipeline creation, full-cycle ownership, stakeholder navigation.
- Sr Sales Manager (8-14 yrs): Complex deal closer. Larger enterprise deal ownership, strong solutioning, negotiation maturity, stakeholder influence, handling objections across functions.
- Principal Sales Manager (14+ yrs): High-trust complex seller. Handles ambiguous enterprise deals, influences senior/CXO stakeholders, drives consensus, strategic account ownership. Red flag if only leadership without individual selling.""",
    },

    # ── SALES: International ─────────────────────
    "Sales — International": {
        "description": "International sales IC hunter roles at Exotel — cross-border selling into Africa, ME, SEA markets with regional and cultural complexity",
        "dimensions": {
            "hunter_mindset": "Hunter validation — new logo acquisition in international markets, greenfield market development, self-generated pipeline across borders. Must show evidence of CREATING new business in international territories. Strong: new market entry, outbound into foreign markets. Deprioritize if revenue comes primarily from existing accounts or domestic-only experience.",
            "solution_selling": "Solution selling ability — has the candidate sold platform products, AI products, or technical/consultative offerings to international customers? Must demonstrate ability to adapt solution positioning to regional market needs and pain points. Strong: AI products, automation platforms, CX platforms, enterprise SaaS sold internationally. Weak: feature/price selling, catalogue-based selling.",
            "regional_market_expertise": "Regional market expertise — selling into Africa, Middle East, or SEA markets depending on role requirement. Understanding of regional buying patterns, decision cycles, market-specific pain points, cultural and communication differences. Prior experience selling into the same region the role is focused on is a strong signal. Handling remote stakeholders, working across time zones, global procurement processes.",
            "multi_threading": "Multi-threading with international stakeholders — engaged multiple stakeholders across geographies, handled remote stakeholder management, navigated cross-border procurement processes, managed cultural and communication nuances in deal progression. Must show ability to close large deals with international customers.",
            "influence_ownership": "Influence without authority and deal ownership — drove international deals forward despite geographic dependencies, coordinated internal teams across time zones, resolved cross-border customer blockers, owned outcomes end-to-end despite remote complexity. Weak: only outbound calling to international prospects without deal ownership.",
            "company_context": "Company and selling environment fit — SaaS companies, enterprise software, AI/automation platforms, CX/contact center tools with international operations = high signal. Global or multi-geography sales experience preferred. Low signal: purely domestic experience, transactional selling, hardware-only, channel-led, distributor-driven sales.",
            "numbers_metrics": "Numbers, deal sizes, and ownership — quota achievement in international territories, revenue numbers in international markets, deal sizes with cross-border customers, pipeline ownership metrics. Strong: 'Closed international deals worth $X', multi-country account management, regional revenue growth. RED FLAG: international sales resume without revenue numbers.",
        },
        "weights": {
            "hunter_mindset": 0.15,
            "solution_selling": 0.15,
            "regional_market_expertise": 0.20,
            "multi_threading": 0.15,
            "influence_ownership": 0.15,
            "company_context": 0.10,
            "numbers_metrics": 0.10,
        },
        "context": """Exotel International sales involves selling communication infrastructure, contact center platforms, and AI-led solutions into Africa, Middle East, and Southeast Asia markets. This requires cross-border deal management, cultural adaptability, and regional market understanding on top of all core Exotel sales competencies.

Company context: Exotel is expanding internationally and needs sellers who can navigate unfamiliar markets, handle remote stakeholder relationships, work across time zones, and understand global procurement processes. The role requires matching regional experience to the specific market the role targets (Africa experience for Africa roles, Middle East for ME roles, etc.).

What to look for: Regional market expertise is the key differentiator for international roles. Candidates must show understanding of regional buying patterns, decision cycles, market-specific pain points, and cultural/communication differences. Closing large deals with international customers is a critical signal. Remote stakeholder management and cross-timezone coordination are essential.

Strong signals: Selling into Africa/ME/SEA markets (matching role requirement), closing large deals with international customers, handling cultural and communication differences, understanding regional buying patterns and decision cycles, prior experience in the same target region, global procurement process navigation, multi-geography pipeline management.

Weak signals: Only outbound calling to international prospects without deal closure, purely domestic experience, no evidence of cross-cultural selling, only remote/inside sales to international markets without field engagement.

Red flags: No revenue metrics, pure account management, domestic-only selling experience with no international exposure, channel-only sales, inside-sales heavy, no evidence of cultural adaptability or regional market understanding.

Level expectations:
- Sales Manager (5-8 yrs): Independent international hunter. New logo acquisition in target markets, pipeline creation across borders, full-cycle ownership, stakeholder navigation across geographies.
- Sr Sales Manager (8-14 yrs): Complex international deal closer. Larger deal ownership across regions, strong cross-cultural solutioning, negotiation maturity in international contexts, multi-stakeholder influence across borders.
- Principal Sales Manager (14+ yrs): High-trust complex international seller. Handles ambiguous cross-border deals, influences senior stakeholders across cultures, drives consensus in multi-geography contexts, owns end-to-end regional outcomes. Red flag if only leadership without individual selling.""",
    },

    # ── SDR: Scaleup ─────────────────────────────
    "SDR — Scaleup": {
        "description": "SDR for Exotel's scaleup segment — high-volume outbound prospecting across multiple verticals with fast sales cycles.",
        "dimensions": {
            "outbound_ownership": "Evidence of self-driven outbound prospecting: cold calling, account research before outreach, identifying decision-makers, multi-channel outreach (LinkedIn + Email + Calls), self-generated meetings. Strong signals include building own target account lists, creating messaging sequences, A/B testing outreach, and improving conversion rates. Penalize candidates who only handled inbound/MQLs or had no outbound exposure.",
            "funnel_metrics": "Quantitative evidence of funnel thinking and metric-driven execution: call-to-meeting ratios, meeting-to-opportunity conversion, monthly targets, activity metrics (calls/day, emails/day), pipeline contribution. Look for specific numbers like '20+ qualified meetings per month', '12% email reply rate', '3X pipeline vs quota'. Resume with zero metrics is a red flag.",
            "qualification_depth": "Ability to qualify prospects beyond surface level: discovery questioning, BANT/MEDDIC awareness, pain-point identification, understanding decision-making processes, qualification before handoff to AEs. Strong signals include qualifying on budget/timeline/use case, disqualifying poor-fit leads, and collaborating with AEs on account strategy. Penalize if only booking demos without qualification.",
            "technical_curiosity": "Familiarity with SaaS, APIs, automation tools, and CRM platforms relevant to Exotel's product suite (APIs, contact center, AI solutions). Strong signals include experience selling SaaS, using tools like Apollo/Sales Navigator/HubSpot, leveraging GenAI for research/personalization, and understanding how APIs or platforms work. Penalize pure non-tech B2B sales background.",
            "high_volume_execution": "Evidence of managing high-volume outbound activity across multiple verticals with structured tracking. Strong signals include handling multiple industry verticals simultaneously, fast experimentation in messaging and sequences, and maintaining high activity volume without sacrificing quality. This is the key differentiator for the scaleup motion vs enterprise.",
            "discipline_and_ownership": "Consistency in target achievement, self-driven prospecting, independent pipeline generation, and tenure stability in outbound-heavy roles. Red flags include frequent job switches (<1 year without performance context) and heavy dependence on marketing-generated leads.",
        },
        "weights": {
            "outbound_ownership": 0.25,
            "funnel_metrics": 0.20,
            "qualification_depth": 0.15,
            "technical_curiosity": 0.10,
            "high_volume_execution": 0.20,
            "discipline_and_ownership": 0.10,
        },
        "context": """Exotel SDR — Scaleup segment. The scaleup SDR motion involves faster sales cycles, high-volume outreach, and multi-industry coverage. This is NOT a generic cold-calling role — it requires structured outbound prospecting, persona-based outreach to CXOs/Founders/Product Heads, and discovery-driven qualification.

Exotel sells APIs, contact center solutions, and AI products. SDRs are expected to generate qualified opportunities, not just meetings. The scaleup SDR must balance volume with quality across multiple verticals (BFSI, D2C, FMCG, etc.).

PRIMARY SIGNALS (must-have): Outbound prospecting ownership, funnel & conversion thinking, qualification ability, target ownership.
SECONDARY SIGNALS: SaaS/tech exposure, industry awareness, CRM usage (HubSpot/Salesforce), GenAI or automation tool usage.
SUPPORTING SIGNALS: Multi-industry experience.

HARD DISQUALIFIERS: No outbound exposure, no metrics mentioned, pure inbound or support roles.
SOFT RED FLAGS: Only volume focus without qualification, no funnel awareness, extremely generic resume.

TIERING: Tier 1 (Strong Fit) — clear outbound ownership, metric-driven, consultative, tech-curious. Tier 2 (Potential Fit) — outbound exposure but lacks structure or metrics. Tier 3 (Low Fit) — primarily inbound, no metrics, no qualification depth.""",
    },

    # ── SDR: Enterprise ──────────────────────────
    "SDR — Enterprise": {
        "description": "SDR for Exotel's enterprise segment — account-based prospecting with research-heavy outreach targeting high-value named accounts.",
        "dimensions": {
            "outbound_ownership": "Evidence of self-driven outbound prospecting: cold calling, account research before outreach, identifying decision-makers, multi-channel outreach (LinkedIn + Email + Calls), self-generated meetings. Strong signals include building own target account lists, creating messaging sequences, A/B testing outreach, and improving conversion rates. Penalize candidates who only handled inbound/MQLs or had no outbound exposure.",
            "account_based_prospecting": "Evidence of account-based, research-heavy outreach targeting named enterprise accounts. Strong signals include named account targeting, multi-threading outreach within a single account (reaching multiple stakeholders), working closely with AEs on enterprise account strategy, and maintaining a quality-over-quantity mindset. This is the critical differentiator for the enterprise SDR motion.",
            "qualification_depth": "Ability to qualify enterprise prospects with depth and rigor: discovery questioning, BANT/MEDDIC awareness, pain-point identification, understanding complex decision-making processes and buying committees, qualification before handoff to AEs. Strong signals include qualifying on budget/timeline/use case, disqualifying poor-fit leads, and collaborating with AEs on enterprise account strategy.",
            "funnel_metrics": "Quantitative evidence of funnel thinking and metric-driven execution: call-to-meeting ratios, meeting-to-opportunity conversion, monthly targets, pipeline contribution. For enterprise SDRs, fewer but higher-quality meetings are expected. Look for pipeline value generated, not just meeting volume. Resume with zero metrics is a red flag.",
            "technical_curiosity": "Familiarity with SaaS, APIs, automation tools, and CRM platforms relevant to Exotel's product suite (APIs, contact center, AI solutions). Strong signals include experience selling SaaS to enterprise buyers, using tools like Apollo/Sales Navigator/HubSpot, leveraging GenAI for research/personalization, and understanding how APIs or platforms work. Penalize pure non-tech B2B sales background.",
            "industry_persona_awareness": "Understanding of enterprise buyer personas (CXOs, Founders, department heads) and ability to contextualize Exotel's value proposition by industry. Strong signals include persona-based messaging, understanding industry pain points (BFSI, D2C, FMCG), vertical-specific outreach, and customized messaging by industry. Penalize generic mass messaging approaches.",
            "discipline_and_ownership": "Consistency in target achievement, self-driven prospecting, independent pipeline generation, and tenure stability in outbound-heavy roles. Red flags include frequent job switches (<1 year without performance context) and heavy dependence on marketing-generated leads.",
        },
        "weights": {
            "outbound_ownership": 0.20,
            "account_based_prospecting": 0.25,
            "qualification_depth": 0.20,
            "funnel_metrics": 0.10,
            "technical_curiosity": 0.10,
            "industry_persona_awareness": 0.10,
            "discipline_and_ownership": 0.05,
        },
        "context": """Exotel SDR — Enterprise segment. The enterprise SDR motion involves account-based prospecting, research-heavy outreach, and fewer but high-value meetings. The critical indicator is a quality-over-quantity mindset.

Exotel sells APIs, contact center solutions, and AI products to large enterprise buyers. SDRs are expected to generate qualified opportunities with named accounts, not just volume meetings. Enterprise SDRs must multi-thread within accounts, work closely with AEs, and deeply understand buyer personas and pain points.

PRIMARY SIGNALS (must-have): Outbound prospecting ownership, account-based targeting, qualification ability, target ownership.
SECONDARY SIGNALS: SaaS/tech exposure, industry awareness, CRM usage (HubSpot/Salesforce), GenAI or automation tool usage.
SUPPORTING SIGNALS: Multi-industry experience, persona-based messaging.

HARD DISQUALIFIERS: No outbound exposure, no metrics mentioned, pure inbound or support roles.
SOFT RED FLAGS: Only volume focus without qualification, no funnel awareness, extremely generic resume, spray-and-pray outreach approach.

TIERING: Tier 1 (Strong Fit) — clear outbound ownership with named account targeting, metric-driven, consultative, tech-curious, multi-threading evidence. Tier 2 (Potential Fit) — outbound exposure but lacks enterprise account-based approach or metrics. Tier 3 (Low Fit) — primarily inbound, no metrics, no qualification depth, no enterprise prospecting evidence.""",
    },

    # ── SDR: International ───────────────────────
    "SDR — International": {
        "description": "SDR for Exotel's international markets (US/MEA/SEA) — outbound prospecting across geographies with cross-timezone execution and region-adapted messaging.",
        "dimensions": {
            "outbound_ownership": "Evidence of self-driven outbound prospecting: cold calling, account research before outreach, identifying decision-makers, multi-channel outreach (LinkedIn + Email + Calls), self-generated meetings. Strong signals include building own target account lists, creating messaging sequences, A/B testing outreach, and improving conversion rates. Penalize candidates who only handled inbound/MQLs or had no outbound exposure.",
            "international_market_experience": "Evidence of prospecting into international markets — US, MEA, SEA, or other non-domestic geographies. Strong signals include booking qualified meetings with international buyers, adapting messaging to regional nuances, working across time zones, and handling remote stakeholders. Penalize if only bulk cold emailing internationally with no ownership of qualification.",
            "qualification_depth": "Ability to qualify international prospects with depth: discovery questioning, BANT/MEDDIC awareness, pain-point identification, understanding decision-making processes across different market contexts. Strong signals include qualifying on budget/timeline/use case, disqualifying poor-fit leads, and collaborating with AEs on international account strategy.",
            "funnel_metrics": "Quantitative evidence of funnel thinking and metric-driven execution: call-to-meeting ratios, meeting-to-opportunity conversion, monthly targets, activity metrics, pipeline contribution. Look for specific numbers. International context may show different conversion benchmarks. Resume with zero metrics is a red flag.",
            "technical_curiosity": "Familiarity with SaaS, APIs, automation tools, and CRM platforms relevant to Exotel's product suite (APIs, contact center, AI solutions). Strong signals include experience selling SaaS to international buyers, using tools like Apollo/Sales Navigator/HubSpot, leveraging GenAI for research/personalization, and understanding how APIs or platforms work. Penalize pure non-tech B2B sales background.",
            "industry_persona_awareness": "Understanding of buyer personas (CXOs, Founders, department heads) across international markets and ability to contextualize Exotel's value proposition by region and industry. Strong signals include persona-based messaging, understanding regional pain points, vertical-specific outreach, and customized messaging by geography and industry. Penalize generic mass messaging.",
            "discipline_and_ownership": "Consistency in target achievement, self-driven prospecting, independent pipeline generation, and ability to work autonomously across time zones. Red flags include frequent job switches (<1 year without performance context), heavy dependence on marketing-generated leads, and only bulk cold emailing internationally without qualification ownership.",
        },
        "weights": {
            "outbound_ownership": 0.20,
            "international_market_experience": 0.25,
            "qualification_depth": 0.15,
            "funnel_metrics": 0.15,
            "technical_curiosity": 0.10,
            "industry_persona_awareness": 0.10,
            "discipline_and_ownership": 0.05,
        },
        "context": """Exotel SDR — International segment. The international SDR must prospect into US, MEA, and SEA markets, working across time zones and adapting messaging to regional nuances. This requires all core SDR competencies plus international market exposure.

Exotel sells APIs, contact center solutions, and AI products. SDRs are expected to generate qualified opportunities with international buyers, not just volume meetings or bulk cold emails. International SDRs must demonstrate cultural adaptability, timezone discipline, and ability to handle remote stakeholders.

PRIMARY SIGNALS (must-have): Outbound prospecting ownership, international market prospecting experience, qualification ability, target ownership.
SECONDARY SIGNALS: SaaS/tech exposure, industry awareness, CRM usage (HubSpot/Salesforce), GenAI or automation tool usage, cross-timezone work experience.
SUPPORTING SIGNALS: Multi-industry experience, regional messaging adaptation.

HARD DISQUALIFIERS: No outbound exposure, no metrics mentioned, pure inbound or support roles.
SOFT RED FLAGS: Only volume focus without qualification, no funnel awareness, extremely generic resume, only bulk cold emailing internationally with no qualification ownership.

TIERING: Tier 1 (Strong Fit) — clear outbound ownership with international prospecting, metric-driven, consultative, tech-curious, region-adapted messaging. Tier 2 (Potential Fit) — outbound exposure but lacks international experience or metrics. Tier 3 (Low Fit) — primarily inbound, no metrics, no qualification depth, no international market evidence.""",
    },

    # ── CX: SMB CSM ──────────────────────────────
    "CX — SMB CSM": {
        "description": "SMB Customer Success Manager owning high-volume portfolios (~700-800 accounts) with scalable engagement, segmentation, and retention at Exotel.",
        "dimensions": {
            "portfolio_scale": "Has the candidate managed high-volume account portfolios (50+ accounts minimum, ideally 100-500+)? Look for SMB or scaled customer environments, pooled or segmented customer bases. Deprioritize candidates with only enterprise accounts (5-10) or no evidence of multi-account ownership.",
            "segmentation_and_structured_thinking": "Does the candidate demonstrate customer segmentation (high-value vs mid-tier vs long-tail), structured engagement models, prioritization frameworks, tiering strategies, and engagement playbooks? Penalize attempts at 1:1 engagement for all accounts or lack of any structured approach.",
            "scalability_and_automation": "Does the candidate show an automation and scalable engagement mindset — email campaigns, lifecycle communication, playbooks, workflows, self-serve enablement (FAQs, help content, guides), scalable customer journeys? Penalize purely manual account handling at scale.",
            "retention_and_adoption": "Does the candidate own product adoption, customer retention, and churn mitigation outcomes? Look for improved adoption metrics, reduced churn percentages, onboarding and activation ownership. Penalize no mention of retention or adoption KPIs.",
            "expansion_ownership": "Does the candidate demonstrate upsell, cross-sell, or renewal ownership? Look for revenue influence within accounts, identifying growth opportunities, and commercial awareness. Penalize no commercial awareness.",
            "api_and_product_understanding": "Does the candidate have basic API understanding, ability to understand product workflows, technical curiosity? Look for experience with APIs or SaaS platforms and ability to explain product usage. Penalize no exposure to technical products.",
            "communication_and_execution": "Does the candidate communicate clearly at scale with structured thinking and an ownership mindset? Look for outcome-driven communication and handling multiple stakeholders effectively.",
        },
        "weights": {
            "portfolio_scale": 0.25,
            "segmentation_and_structured_thinking": 0.20,
            "scalability_and_automation": 0.15,
            "retention_and_adoption": 0.15,
            "expansion_ownership": 0.10,
            "api_and_product_understanding": 0.08,
            "communication_and_execution": 0.07,
        },
        "context": """Exotel SMB CSM Evaluation Context:

ROLE NATURE: This is a high-volume, high-ownership role — NOT a relationship-only role. The SMB CSM at Exotel owns ~700-800 accounts, drives product adoption, retention, and expansion at scale. They cannot provide high-touch support to all customers and must segment accounts and prioritize effectively using structured engagement and automation.

WHAT EXOTEL OPTIMIZES FOR: Ability to manage high-volume account portfolios, structured thinking and segmentation capability, ownership of customer outcomes (adoption, churn, expansion), ability to drive engagement at scale (not just 1:1), commercial awareness (upsell, cross-sell, renewals), strong communication and problem-solving, basic API/product understanding.

NOT MANDATORY: Enterprise account experience, telecom domain experience.

EXPERIENCE EXPECTATIONS:
- CSM (2-5 years): Handling 50+ accounts, adoption and retention exposure, some level of structured execution.
- Senior CSM (5-8 years): Larger portfolios (100+ / scaled environments), strong KPI ownership, segmentation and process thinking, expansion contribution.

CONFIDENCE BOOSTERS: Portfolio size (50+, 100+), segmentation/tiering, automation/playbooks/lifecycle, adoption/churn/retention metrics, upsell/cross-sell/renewals, API/SaaS/product usage, competitor company or similar industry domain.

CONFIDENCE REDUCERS: Generic "handled customers" with no scale indicators, no metrics, enterprise-only exposure.

HARD DISQUALIFIERS: No multi-account ownership, pure support role or onboarding-heavy role.

SOFT RED FLAGS: Only enterprise account experience (low volume), no segmentation or structure, no metrics, no expansion or retention ownership.

CLASSIFICATION:
- Tier 1 (Strong Fit): High-volume ownership, structured segmentation, strong KPI ownership (adoption, churn, expansion).
- Tier 2 (Potential Fit): Customer-facing but lacks scale or structured thinking.
- Tier 3 (Low Fit): Low-volume account handling, no ownership, no metrics.""",
    },

    # ── CX: Mid-Market CSM ───────────────────────
    "CX — Mid-Market CSM": {
        "description": "Mid-Market Customer Success Manager balancing scale and depth across 20-100 accounts with structured account management, retention, and expansion at Exotel.",
        "dimensions": {
            "portfolio_size_and_complexity": "Has the candidate managed a meaningful number of accounts with moderate complexity (20-100 accounts)? Look for portfolio with recurring engagement, balancing multiple accounts. Enterprise experience (5-10 accounts) is acceptable if candidate demonstrates structured account management, retention/expansion ownership, and willingness to handle higher volume. Deprioritize candidates with only SMB high-volume exposure (500+ accounts, no depth) or no clear account ownership.",
            "account_management_and_planning": "Does the candidate demonstrate structured account management — account plans, playbooks, regular engagement cadence (QBRs, reviews), defined success metrics per account, and prioritization across accounts? Penalize reactive customer handling or no structured approach.",
            "retention_and_adoption": "Does the candidate own product adoption, customer retention, and churn mitigation? Look for improved usage/engagement, reduced churn, onboarding and lifecycle management. Penalize no measurable impact on these KPIs.",
            "expansion_ownership": "Does the candidate demonstrate upsell/cross-sell contribution and renewal ownership? Mid-Market CSMs are expected to influence revenue — look for revenue growth within accounts and identifying expansion opportunities. Penalize no commercial involvement.",
            "stakeholder_management": "Does the candidate work with multiple stakeholders — business and operational? Look for multi-threaded engagement and handling decision-makers. Penalize single point of contact only approach.",
            "technical_product_understanding": "Does the candidate have SaaS/product understanding, basic API awareness, and ability to map product to customer use cases? Look for explaining product workflows and understanding integrations. Penalize no technical curiosity.",
            "problem_solving_and_execution": "Does the candidate drive outcomes, resolve customer issues end-to-end, and coordinate with internal teams? Look for cross-functional collaboration and solving customer problems comprehensively.",
        },
        "weights": {
            "portfolio_size_and_complexity": 0.20,
            "account_management_and_planning": 0.20,
            "retention_and_adoption": 0.18,
            "expansion_ownership": 0.15,
            "stakeholder_management": 0.12,
            "technical_product_understanding": 0.08,
            "problem_solving_and_execution": 0.07,
        },
        "context": """Exotel Mid-Market CSM Evaluation Context:

ROLE NATURE: This is a balanced role between scale and depth. The Mid-Market CSM at Exotel owns a moderate portfolio (~20-100 accounts), drives adoption, retention, and expansion, engages with multiple stakeholders per account, requires structured account planning, and balances proactive engagement with scalable execution.

WHAT EXOTEL OPTIMIZES FOR: Ability to manage mid-sized portfolios (20-100 accounts), structured account management and prioritization, strong retention and adoption ownership, expansion mindset (upsell, cross-sell, renewals), multi-stakeholder engagement, problem-solving and execution, basic technical/product understanding (APIs, SaaS workflows).

NOT MANDATORY: Enterprise-level experience, telecom domain experience.

IMPORTANT CONSIDERATION ON ENTERPRISE EXPERIENCE: Enterprise-only experience should NOT be penalized if strong ownership of accounts is demonstrated, clear retention/adoption/expansion impact is visible, and candidate shows ability or intent to handle multiple accounts. Enterprise experience is not a dealbreaker for Mid-Market roles, but lack of ability to manage multiple accounts may reduce confidence.

EXPERIENCE EXPECTATIONS:
- CSM (2-6 years): Managing 20-100 accounts, ownership of adoption and retention, exposure to expansion.
- Senior CSM (6-10 years): Larger or more complex portfolios, strong KPI ownership, structured account management, better stakeholder influence.

CONFIDENCE BOOSTERS: Portfolio size (20-100 accounts), account planning/QBRs, adoption/churn reduction, expansion/upsell/renewals, stakeholder management, SaaS/API exposure, competitor company or similar industry domain.

CONFIDENCE REDUCERS: Only SMB volume (no structure), no metrics, generic descriptions.

HARD DISQUALIFIERS: No account ownership, pure support roles.

SOFT RED FLAGS: Only SMB volume experience, only enterprise (low-volume) experience, no metrics, no expansion involvement.

CLASSIFICATION:
- Tier 1 (Strong Fit): Balanced scale + depth, strong retention + expansion ownership.
- Tier 2 (Potential Fit): Good customer exposure but lacks structure or metrics.
- Tier 3 (Low Fit): Reactive, no ownership, no measurable impact.""",
    },

    # ── CX: Enterprise CSM ───────────────────────
    "CX — Enterprise CSM": {
        "description": "Enterprise Customer Success Manager owning high-value strategic accounts (5-20) with deep stakeholder influence, renewal/expansion ownership, and consultative engagement at Exotel.",
        "dimensions": {
            "account_value_and_complexity": "Has the candidate handled high-value, complex enterprise accounts (5-20)? Look for ownership of large or strategic customers, long-term account engagement, named enterprise accounts, high ARR ownership. Deprioritize candidates with only SMB high-volume accounts or no evidence of complexity/stakeholder depth.",
            "strategic_account_management": "Does the candidate demonstrate strategic account management — account plans, long-term engagement strategy, business alignment, QBRs/EBRs, defined success metrics, business outcome alignment, and strategic roadmap discussions? Penalize reactive engagement or no structured planning.",
            "renewals_and_retention": "Does the candidate own renewals, retention, and churn mitigation? Look for renewal ownership, multi-year retention, managing contract cycles, specific metrics like 'managed renewals worth $X' or 'maintained 95%+ retention'. Penalize no renewal ownership.",
            "expansion_ownership": "Does the candidate drive significant revenue growth through upsell/cross-sell? Look for large upsell/cross-sell deals and expansion strategy. Enterprise CSMs are expected to drive substantial revenue growth within accounts. Penalize no revenue influence.",
            "cxo_stakeholder_management": "Does the candidate engage CXO and senior stakeholders? Look for engagement with CTO, Product Heads, Business Leaders, multi-threaded relationships, and influence across functions. This is a key differentiator for enterprise CSMs. Penalize single-threaded relationships.",
            "consultative_problem_solving": "Does the candidate solve business problems, not just product issues? Look for understanding customer business goals, mapping product to outcomes, use-case driven engagement. Enterprise CSMs must operate as strategic advisors, closer to consultative sales + program management.",
            "technical_product_understanding": "Does the candidate understand APIs and integrations, discuss technical workflows, and work comfortably with product/engineering teams? Look for integration discussions and technical discovery. Penalize no technical exposure.",
        },
        "weights": {
            "account_value_and_complexity": 0.20,
            "strategic_account_management": 0.18,
            "renewals_and_retention": 0.18,
            "expansion_ownership": 0.15,
            "cxo_stakeholder_management": 0.15,
            "consultative_problem_solving": 0.08,
            "technical_product_understanding": 0.06,
        },
        "context": """Exotel Enterprise CSM Evaluation Context:

ROLE NATURE: This is a high-impact, strategic ownership role — fundamentally different from SMB/Mid-Market. The Enterprise CSM at Exotel owns a small portfolio of high-value accounts (typically 5-20), drives long-term retention and large renewals, influences expansion (upsell/cross-sell), engages CXOs, Product, and Business leaders, navigates complex stakeholder environments, and acts as a strategic advisor — not just a relationship manager. This role should feel closer to consultative sales + program management, not support or SMB CS.

WHAT EXOTEL OPTIMIZES FOR: Ownership of high-value accounts, strategic account management, strong retention and renewal ownership, expansion mindset (upsell/cross-sell), CXO and multi-stakeholder engagement, problem-solving in complex environments, strong communication and influence, solid product/technical understanding (APIs, integrations).

NOT MANDATORY: Telecom domain experience.

EXPERIENCE EXPECTATIONS:
- CSM (3-6 years): Enterprise account ownership, renewal and retention exposure, stakeholder management.
- Senior CSM (6-9 years): Larger or more strategic accounts, strong renewal + expansion ownership, CXO influence, strategic thinking.

CONFIDENCE BOOSTERS: Enterprise accounts (5-20), renewals/retention metrics, expansion (upsell, cross-sell), QBRs/account plans, CXO engagement, strategic discussions, SaaS/API exposure, competitor company or similar industry domain.

CONFIDENCE REDUCERS: Only SMB volume experience, no renewal ownership, no strategic signals, generic relationship management.

HARD DISQUALIFIERS: No enterprise account ownership, pure support or SMB-only roles.

SOFT RED FLAGS: No renewal ownership, no expansion involvement, weak stakeholder depth, no strategic thinking.

CLASSIFICATION:
- Tier 1 (Strong Fit): Owns enterprise accounts, drives renewals + expansion, strong stakeholder influence.
- Tier 2 (Potential Fit): Good customer exposure but lacks depth in renewals or strategy.
- Tier 3 (Low Fit): No enterprise ownership, no strategic signals.""",
    },

    # ── SUPPORT: L1 Product Support ──────────────
    "Support — L1 Product Support Engineer": {
        "description": "Entry-level ECC support engineer responsible for troubleshooting production issues across Linux, networking, and databases in Exotel's real-time communication platform.",
        "dimensions": {
            "linux_fundamentals": "Proficiency in Linux system fundamentals including command-line tools (grep, awk, ps, top), log analysis, file system navigation, and process-level understanding. Evaluate depth of hands-on Linux exposure versus superficial mentions.",
            "networking_fundamentals": "Understanding of networking basics including DNS, DHCP, OSI model, TCP/IP, and basic connectivity troubleshooting. Note: weaker networking can be offset by strong Linux and database skills.",
            "database_querying": "Ability to work with relational databases (PostgreSQL, MySQL, MariaDB, Oracle) including SQL queries with joins, filters, aggregations, and query-based debugging for issue investigation.",
            "debugging_approach": "Evidence of structured, step-by-step troubleshooting methodology including log-based debugging, issue isolation, and logical thinking. Look for concrete examples like 'checked logs and identified...' or 'resolved issue by...'.",
            "communication_and_customer_handling": "Clarity in communication, ability to explain technical issues simply, and evidence of client or stakeholder interaction. For freshers, strong communication can compensate for limited experience.",
            "ownership_and_learning": "Evidence of end-to-end issue handling, closure responsibility, independent work, curiosity, hands-on projects or internships, and a learning mindset.",
        },
        "weights": {
            "linux_fundamentals": 0.25,
            "networking_fundamentals": 0.12,
            "database_querying": 0.20,
            "debugging_approach": 0.20,
            "communication_and_customer_handling": 0.13,
            "ownership_and_learning": 0.10,
        },
        "context": """Exotel L1 Product Support Engineer — ECC (Enterprise Contact Center) Support.

This is NOT a ticket-routing role. L1 engineers at Exotel troubleshoot issues across Linux, networking, and databases on production systems impacting real-time communication. They own issues end-to-end within defined scope and operate in an SLA-driven environment.

Experience expectation:
- Freshers: Strong fundamentals, good communication, learning mindset are sufficient.
- 1-3 years: Real troubleshooting experience, exposure to production systems, basic customer handling expected.

Strong signals: grep, awk, logs, process management, SQL joins, DNS, TCP/IP, troubleshooting, RCA, hands-on projects, concrete debugging examples.
Weak signals: "Basic knowledge of Linux/SQL" without examples, generic resume content, only theoretical knowledge.

Hard red flags: No Linux exposure, no database knowledge.
Soft red flags: No debugging examples, generic resume, poor communication indicators.

Classification:
- Tier 1 (Strong Fit): Strong fundamentals + debugging evidence + communication clarity.
- Tier 2 (Potential Fit): Strong Linux/DB but gaps in networking or experience.
- Tier 3 (Low Fit): Weak fundamentals across the board.""",
    },

    # ── SUPPORT: L3 Product Support ──────────────
    "Support — L3 Product Support Lead": {
        "description": "Senior ECC support lead responsible for complex production RCA, customer escalation handling, cross-system debugging, and mentoring junior engineers at Exotel.",
        "dimensions": {
            "advanced_technical_depth": "Advanced expertise across Linux (load average analysis, system bottleneck identification, advanced awk/grep), databases (connection pool issues, replication lag debugging, query optimization, indexing), and networking (DNS, TCP/IP, latency debugging, network-related RCA). Evaluate for depth beyond basics.",
            "rca_ownership": "Evidence of end-to-end root cause analysis ownership including cross-system debugging, identifying systemic issues, and implementing preventive long-term solutions rather than surface-level fixes.",
            "escalation_and_incident_handling": "Experience handling high-severity incidents, managing customer escalations under pressure, and communicating effectively during critical situations.",
            "mentorship_and_team_contribution": "Evidence of mentoring junior engineers (L1/L2), knowledge sharing, creating playbooks or runbooks, and contributing to team capability building.",
            "structured_problem_solving": "Logical debugging approach to complex, multi-system problems. Ability to break down complex systems and methodically isolate root causes across layers.",
            "cross_functional_collaboration": "Driving issues end-to-end across engineering, product, and other teams. Taking accountability beyond defined scope and influencing resolution across organizational boundaries.",
        },
        "weights": {
            "advanced_technical_depth": 0.30,
            "rca_ownership": 0.25,
            "escalation_and_incident_handling": 0.15,
            "mentorship_and_team_contribution": 0.10,
            "structured_problem_solving": 0.10,
            "cross_functional_collaboration": 0.10,
        },
        "context": """Exotel L3 Product Support Lead — ECC (Enterprise Contact Center) Support.

This is a senior ownership role requiring deep technical expertise combined with leadership and customer management. The L3 lead handles the most complex production issues, performs end-to-end RCA, manages customer escalations, mentors L1/L2 engineers, and drives resolution across teams.

Experience expectation: 5+ years with advanced troubleshooting, RCA ownership, escalation handling, and mentorship experience.

Strong signals: load average analysis, awk (advanced), performance debugging, replication lag, indexing, slow query optimization, RCA, incident resolution, "owned", "resolved", mentoring, playbooks, runbooks.
Weak signals: Only ticket handling without depth, no evidence of ownership or systemic thinking, only repetitive support work.

Hard red flags: No RCA ownership evidence, no advanced technical depth (only basic-level knowledge).
Soft red flags: No mentoring or leadership evidence, only repetitive support without progressive complexity.

Classification:
- Tier 1 (Strong Fit): Deep expertise + RCA ownership + escalation handling + mentorship evidence.
- Tier 2 (Potential Fit): Strong technically but lacks leadership or full RCA depth.
- Tier 3 (Low Fit): Limited depth and ownership.""",
    },

    # ── SUPPORT: L1 Platform Support ─────────────
    "Support — L1 Platform Support Engineer": {
        "description": "Entry-level platform/tech support engineer responsible for first-level debugging of production backend issues involving APIs, logs, Python, and backend systems at Exotel.",
        "dimensions": {
            "backend_and_python_fundamentals": "Basic Python understanding including scripts and small projects, familiarity with backend systems and request flow. Evaluate for hands-on coding evidence versus purely theoretical knowledge.",
            "api_and_web_fundamentals": "Understanding of HTTP, REST APIs, JSON request/response handling, and basic web stack awareness (HTML, CSS, JS). Look for evidence of working with API-driven systems.",
            "linux_and_debugging": "Basic Linux command usage, log reading (grep, basic commands), understanding of errors, and evidence of structured step-by-step debugging and log-based troubleshooting.",
            "database_basics": "SQL fundamentals including joins and filters. Ability to query databases for investigation purposes.",
            "communication_and_learning": "Clarity in explaining issues, ability to communicate with customers and internal teams, interest in backend systems, exposure to real-world problems, and evidence of learning curiosity.",
        },
        "weights": {
            "backend_and_python_fundamentals": 0.30,
            "api_and_web_fundamentals": 0.20,
            "linux_and_debugging": 0.20,
            "database_basics": 0.15,
            "communication_and_learning": 0.15,
        },
        "context": """Exotel L1 Platform Support Engineer — AI/Platform Tech Support.

This is an entry-level backend + production support role, NOT a ticket-routing role. The engineer handles first-level debugging of production issues, works with APIs, logs, and backend systems, supports L2/L3 in issue resolution, and learns system architecture and workflows.

This role is backend-heavy and SRE-like, with emphasis on Python/Django and distributed systems exposure over time. Django depth and distributed systems experience are NOT mandatory at L1.

Experience expectation: Freshers with strong fundamentals, debugging curiosity, and learning ability are acceptable.

Strong signals: Python scripts/projects, API debugging, log analysis, SQL usage, hands-on projects, concrete debugging examples, "resolved", "debugged".
Weak signals: "Basic knowledge" without examples, only theoretical knowledge, no hands-on evidence.

Classification:
- Tier 1 (Strong Fit): Python + debugging evidence + solid fundamentals.
- Tier 2 (Potential Fit): Good basics but limited real-world exposure.
- Tier 3 (Low Fit): Weak fundamentals across the board.""",
    },

    # ── SUPPORT: L2 Platform Support ─────────────
    "Support — L2 Platform Support Engineer": {
        "description": "Mid-level platform support engineer responsible for independent production debugging, RCA, backend system troubleshooting, and cross-team collaboration at Exotel.",
        "dimensions": {
            "backend_debugging": "Strong Python and backend understanding with evidence of debugging Python/Django systems, understanding request flow, and tracing issues through backend layers.",
            "database_debugging": "SQL debugging ability including query debugging, performance awareness, and ability to trace data-related issues in production systems.",
            "linux_and_system_debugging": "Linux troubleshooting including log analysis, system issue diagnosis, and process-level debugging in production environments.",
            "rca_capability": "Evidence of root cause identification, end-to-end issue tracing, and ability to independently determine why issues occurred rather than just resolving symptoms.",
            "system_awareness": "Understanding of APIs, basic distributed systems concepts, and exposure to cloud infrastructure (AWS basics). Ability to see how components interconnect.",
            "collaboration_and_communication": "Evidence of working with engineering teams, reducing escalations through independent resolution, and clear communication of technical findings.",
        },
        "weights": {
            "backend_debugging": 0.25,
            "database_debugging": 0.18,
            "linux_and_system_debugging": 0.17,
            "rca_capability": 0.20,
            "system_awareness": 0.12,
            "collaboration_and_communication": 0.08,
        },
        "context": """Exotel L2 Platform Support Engineer — AI/Platform Tech Support.

This is an independent production debugger role. The L2 engineer handles complex production issues, performs RCA, works across backend systems, collaborates with engineering, and actively reduces escalations through independent resolution.

This role bridges L1 fundamentals and L3 ownership. Strong Python/Django skills and the ability to independently trace and resolve issues are critical differentiators from L1.

Experience expectation: 2-4 years with real backend debugging experience, RCA exposure, and system-level understanding.

Strong signals: Django, API debugging, log-based RCA, SQL debugging, performance awareness, process-level debugging, "root cause", "end-to-end tracing", cloud/AWS exposure.
Weak signals: Surface-level debugging only, no evidence of independent issue resolution, no RCA depth.

Classification:
- Tier 1 (Strong Fit): Backend debugging + RCA capability + system understanding.
- Tier 2 (Potential Fit): Strong backend skills but limited RCA depth.
- Tier 3 (Low Fit): Surface-level debugging without independence.""",
    },

    # ── SUPPORT: L3 Platform Support ─────────────
    "Support — L3 Platform Support Lead": {
        "description": "Senior platform support lead owning mission-critical production issues, leading RCA and systemic improvements, building automation, mentoring L1/L2, and driving platform reliability at Exotel.",
        "dimensions": {
            "advanced_backend_expertise": "Strong Python and Django expertise, clean code practices, ability to write and review code. Evidence of working with distributed systems, AWS, Docker, Kubernetes. Deep understanding of backend architecture and request flow.",
            "advanced_database_and_linux": "Advanced SQL debugging including query optimization and performance issue resolution. Deep Linux troubleshooting including advanced debugging and system performance analysis.",
            "rca_and_system_ownership": "End-to-end RCA ownership with system-level debugging and preventive fixes. Evidence of driving long-term improvements, not just incident resolution. Identifying bottlenecks and suggesting architectural improvements.",
            "automation_and_tooling": "Building internal tools, automation workflows, monitoring systems, scripts, dashboards, and alerting systems. CI/CD understanding, deployment management, and release workflow experience.",
            "escalation_and_incident_management": "Handling mission-critical production issues, incident command experience, and ability to manage high-pressure situations with clear communication.",
            "mentorship_and_cross_functional_leadership": "Mentoring L1/L2 engineers, reviewing code, setting best practices, collaborating with Engineering/Product/Delivery teams, and driving improvements across organizational boundaries.",
        },
        "weights": {
            "advanced_backend_expertise": 0.25,
            "advanced_database_and_linux": 0.18,
            "rca_and_system_ownership": 0.22,
            "automation_and_tooling": 0.12,
            "escalation_and_incident_management": 0.13,
            "mentorship_and_cross_functional_leadership": 0.10,
        },
        "context": """Exotel L3 Platform Support Lead — AI/Platform Tech Support.

This is the highest escalation + ownership role, directly aligned with the senior platform support JD. The L3 lead owns mission-critical production issues, leads RCA and systemic improvements, drives platform reliability and performance, works with Engineering/Product/Delivery, mentors L1/L2, writes and reviews code (Python/Django), and builds automation and internal tooling.

This role is backend-heavy and SRE-like, requiring deep Python/Django expertise combined with distributed systems knowledge, infrastructure skills, and leadership.

Experience expectation: 5+ years with strong backend development/debugging, RCA ownership, automation, mentorship, and incident management experience.

Strong signals: Python, Django, AWS, Docker, Kubernetes, RCA, performance tuning, latency optimization, CI/CD, monitoring, alerting, automation, scripting, code review, mentoring, architectural improvements, system design discussions.
Weak signals: Only support without coding ability, no ownership evidence, no automation or tooling contributions.

Hard red flags: No backend depth, no evidence of code-level work.
Soft red flags: Strong technically but no leadership, mentoring, or cross-functional collaboration evidence.

Classification:
- Tier 1 (Strong Fit): Deep backend + system expertise + RCA ownership + leadership.
- Tier 2 (Potential Fit): Strong technically but limited leadership or architecture depth.
- Tier 3 (Low Fit): No depth, no ownership.""",
    },

    # ── PROFESSIONAL SERVICES ────────────────────
    "Professional Services — Integration & Customisation Engineer (ECC)": {
        "description": "Consultative engineer blending backend/frontend development, system customization, legacy codebase work, and client-facing delivery for Exotel's contact center platform.",
        "dimensions": {
            "technical_capability_and_breadth": "Evaluate full-stack engineering capability across backend and frontend. Backend: PHP is primary/preferred, plus familiarity with at least one additional language (Python, Go, Java). Frontend: JavaScript (React preferred), HTML/CSS understanding. System & architecture: REST APIs, HTTP, microservices, 3-tier architecture, Linux-based applications. Look for working versatility across layers, not perfection in every stack. Reduce confidence if profile is extremely narrow or single-layer only. Strong signals: multi-language familiarity, full-stack exposure, SQL/NoSQL usage, data modeling, caching, cloud exposure (AWS/GCP/Azure), observability tools (Grafana/Kibana), TCP/IP networking basics.",
            "problem_solving_and_engineering_depth": "Assess strength in fundamentals: DSA, concurrency, multithreading, structured thinking. Look for evidence of debugging complex issues, performance improvements, root cause analysis, optimization work, and system-level challenges. Weak signal: only feature development without depth. Strong signals: mentions of debugging, RCA, performance tuning, concurrency handling, and measurable optimization outcomes.",
            "ownership_and_delivery": "Critical differentiator. Evaluate end-to-end ownership of modules, responsibility for delivery cycles, production quality ownership. Strong signals: 'Owned module end-to-end', 'Handled deployment and stabilization', 'Improved system reliability/performance', shipped and deployed language. Weak signals: only task-based execution, no ownership language, no mention of delivery accountability. This dimension separates consultative engineers from task executors.",
            "legacy_systems_and_customization": "ECC environments are rarely clean. Evaluate experience with legacy systems, forked or complex codebases, client-specific customizations. Strong signals: migration work, refactoring, building custom solutions for specific use cases, handling messy or evolving systems. Weak signals: only greenfield development, no exposure to inherited or forked code. Especially value candidates who have navigated ambiguity in poorly documented or non-standard systems.",
            "stakeholder_collaboration": "Evaluate consultative ability: interaction with Product, Engineering, Infosec, Legal, Sales, or Clients. Assess requirement gathering, translating business needs into technical solutions. Strong signals: 'Worked with Product/Sales/Clients', 'Translated requirements into solutions'. Very strong: cross-functional collaboration spanning Infosec, Legal, etc. Weak signal: no stakeholder interaction, purely siloed work. The role demands a consultative engineer, not just a coder.",
            "code_quality_and_engineering_discipline": "Evaluate adherence to engineering best practices: code reviews, testing practices (test planning, unit/integration tests), SDLC understanding, documentation. Strong signals: Jira/Confluence usage, code review participation, test planning, architecture diagrams, process documentation. Weak signals: no mention of quality, testing, or process discipline. Indicates maturity and readiness for enterprise-grade delivery.",
            "leadership_and_team_contribution": "Even at 2-4 years experience, some leadership is expected. Evaluate mentoring juniors, unblocking teammates, driving solutions, contributing beyond individual tasks. Strong signals: 'Guided team members', 'Unblocked issues', proactive problem resolution for the team. Weak signals: pure individual contributor with zero team impact or collaboration evidence.",
        },
        "weights": {
            "technical_capability_and_breadth": 0.25,
            "problem_solving_and_engineering_depth": 0.15,
            "ownership_and_delivery": 0.20,
            "legacy_systems_and_customization": 0.15,
            "stakeholder_collaboration": 0.10,
            "code_quality_and_engineering_discipline": 0.08,
            "leadership_and_team_contribution": 0.07,
        },
        "context": """Exotel Professional Services — Integration & Customisation Engineer (ECC) role.

This is NOT a pure backend developer or support role. It is a blend of:
- Backend + frontend engineering (PHP primary, React/JS frontend)
- System customization and integrations for enterprise clients
- Working with complex, legacy, and forked codebases in the ECC platform
- Stakeholder collaboration (Product, Developers, Clients, Infosec)
- End-to-end ownership of delivery and production quality

The candidate must operate as a Consultative Engineer, not just a coder.

WHAT EXOTEL OPTIMIZES FOR:
- Strong backend + frontend capability (working proficiency, not perfection)
- Ability to handle complex, non-clean systems (legacy, forked codebases)
- Ownership of modules and delivery cycles
- Structured problem-solving and debugging
- Stakeholder collaboration and requirement translation
- Code quality and engineering discipline
- Ability to work in high-pressure, enterprise environments

NOT MANDATORY: Perfect expertise in all technologies, prior ECC/telecom experience, GenAI exposure.

SIGNAL-BASED VALIDATION — INCREASE CONFIDENCE:
- Tech stack: PHP, Python/Go/Java, React, JavaScript, SQL, APIs
- Ownership signals: Owned, delivered, deployed, end-to-end responsibility
- Problem-solving signals: Debugging, RCA, optimization
- Complexity signals: Legacy, migration, refactoring, customization
- Collaboration signals: Product, Client, Infosec, cross-functional

REDUCE CONFIDENCE WHEN DETECTING:
- Generic phrases: "Worked on...", "Involved in..."
- No measurable impact
- No ownership language
- No real-world complexity evidence

HARD DISQUALIFIERS:
- No backend experience whatsoever
- No ability to work with APIs or systems

SOFT RED FLAGS:
- Extremely narrow skillset (single layer only)
- Only greenfield work, never touched legacy/inherited code
- No ownership of delivery
- No stakeholder interaction

TIER CLASSIFICATION:
- Tier 1 (Strong Fit): Balanced tech + ownership + problem-solving + stakeholder collaboration
- Tier 2 (Potential Fit): Technically capable but lacks ownership, complexity, or consultative signals
- Tier 3 (Low Fit): Narrow skillset, no ownership, no real-world complexity""",
    },
}


# ─────────────────────────────────────────────
# VERDICT THRESHOLDS & HELPERS
# ─────────────────────────────────────────────

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
VERDICT THRESHOLDS: Strong Yes (>=8.0), Yes (6.5-7.9), Maybe (5.0-6.4), No (<5.0)
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
VERDICT THRESHOLDS: Strong Yes (>=8.0), Yes (6.5-7.9), Maybe (5.0-6.4), No (<5.0)
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
