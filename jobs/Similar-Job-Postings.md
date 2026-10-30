# Similar API & Developer Platform Product Manager Roles

*Last Updated: October 30, 2026*

This document contains active job postings for API Product Manager and Developer Platform Product Manager roles with similar requirements to the positions saved in this repository. Each position includes a fit score (0-100) based on alignment with Daniel O'Rorke's resume.

---

## Discovery Search, October 27, 2026

Pattern-based search built from three seeds (Anthropic Multi-Cloud Growth, Anthropic Safe Access, Mercury Interfaces; see `Seed-Jobs.md`). Filter: remote US, Principal/Staff/Head-of level, base band top at or above $280K ($250K for telecom), posted or updated since August 28, 2026, on an API, developer-platform, identity/access, agent-platform, or network-API surface. Four slices, roughly 130 company boards read directly through their Greenhouse, Ashby, Lever, and Workday APIs. Indeed and LinkedIn were not used (they block fetches).

**Result: 4 roles at or above 75, all remote US.** Below the five-job minimum CLAUDE.md sets for a healthy run; see the note after the table on what would widen it.

### D1. **Senior Director, Product Management, Developer & AI** 🔥 **FIT SCORE: 82/100**
**Application status:** Submitted by Daniel, October 28, 2026 (package in `applications/1password-developer-ai/`).
**Company:** 1Password
**Location:** Remote (United States | Canada); remote-first company, travel for offsites and customer or industry events
**Compensation:** $267,000 - $401,000 USD base + equity, benefits, incentive programs where applicable
**Posted:** October 6, 2026 ("existing vacancy")
**Link:** [Apply Here](https://jobs.ashbyhq.com/1password/618d6f38-988d-4e1f-af12-f5fdeebf05ed)
**Full Description:** [jobs/descriptions/1Password-Senior-Director-Developer-AI.md](descriptions/1Password-Senior-Director-Developer-AI.md)

**Key Requirements:**
- Lead product strategy for Developer Experience (DevX), Security for AI, and AI for Security; define identity, delegation, secrets delivery, and access control for developers and AI agents
- 10+ years PM including 5+ years leading senior PMs or product portfolios
- Owned platform, developer-facing, or infrastructure products; shipped developer tools or security products at scale
- Familiarity with LLMs, orchestration frameworks, agentic workflows; understanding of identity, secrets management, access control
- Product input into standards participation and developer advocacy; recruit and lead senior PMs

**Fit Analysis:**
✅ **Developer platform ownership is the core of the role** - 11 years on API products; built developer.alianza.com and the AI documentation system behind it; built an MCP server for the Crux API; helped guide the structure of the Crux API with Architecture
✅ **Agent access is the same problem from the other side** - Daniel owns the developer-facing surface of Crux, the control plane through which AI experiences get governed access to live calls on operator networks (identity, consent, and policy applied in-network before any AI is invoked). 1Password's "identity, delegation, secrets delivery, and access control for AI agents" is the credential-side counterpart
✅ **AI fluency with production evidence** - Operates an AI-built documentation system in production; daily Claude Code user; published on hallucination risk (Dec 2025) and AI for product discovery (May 2026)
✅ **Standards and developer engagement** - CAMARA network API work at Charter and Ericsson; presented API strategy at Ericsson Innovation Days
✅ **Exceeds the experience bar** - 13 years PM vs. 10+
⚠️ **People leadership is the real gap** - The posting asks for 5+ years "leading senior PMs or product portfolios." The record is mentoring and onboarding a team of 5 PMs (not managing them) plus portfolio ownership (video clients across 8 platforms; the full Crux developer surface). Lead with the portfolio half of that "or" and say the mentoring part plainly
⚠️ **Security depth is product-level, not practitioner-level** - Enhanced Number Verification, two credential-management patents, and documenting the Crux access model cover "solid understanding"; no secrets-management or security-engineering background
⚠️ **Company signals** - Glassdoor 3.2; recent reviews report product-leadership turnover and a reporting-line change (Product under the CISO). Ask the recruiter directly

---

### D2. **Principal Product Manager, Platform** 🔥 **FIT SCORE: 80/100**
**Application status:** Submitted by Daniel, October 28, 2026 (package in `applications/github-platform/`).
**Company:** GitHub (Microsoft)
**Location:** Remote, United States
**Compensation:** $160,200 - $425,000 USD base (one range "across the United States") + annual bonus and stock eligibility
**Posted:** September 8, 2026 (ongoing until filled)
**Link:** [Apply Here](https://www.github.careers/careers-home/jobs/5764) | Staff-level sibling: [jobs/5763](https://www.github.careers/careers-home/jobs/5763) ($140,400 - $372,300)
**Full Description:** [jobs/descriptions/GitHub-Principal-PM-Platform.md](descriptions/GitHub-Principal-PM-Platform.md)

**Key Requirements:**
- Build the platforms, APIs, and enterprise capabilities that power GitHub's developer and AI experiences; enable partners, integrators, and developers to extend GitHub
- Experience building enterprise-grade platform capabilities (governance, security, platform guarantees) for AI-powered and/or developer-facing products
- Deep understanding of developer ecosystems, APIs, SDKs, and partner integration models; platform adoption and ecosystem growth
- Significant experience on AI-powered products; preferred background in applied AI/ML
- 10+ years; pooled posting across Copilot, Core Productivity, and Platform & Enterprise teams

**Fit Analysis:**
✅ **Platform, APIs, and ecosystem are the stated job** - Ran Aerohive's API platform and developer ecosystem; Vonage Video API served first-party apps, direct API customers, and third-party developers at scale; now owns the public APIs, webhooks, and portal for a platform where AI experience providers integrate once and reach 1,000+ operators
✅ **Governance and platform guarantees, at the product level** - With Architecture, sets the API standards engineering teams build against and reviews API proposals across teams; publishes the operational runbooks and known-issues documentation most API docs omit; Crux 1.0.0 shipped webhooks with at-least-once delivery and zero-downtime key rotation (API facts Daniel exposes and documents, not designs)
✅ **Developer ecosystem and SDK depth** - SDKs across iOS, Android, Web, Windows, Mac, Linux at Vonage; 40% support-ticket reduction from the VoiceBase v3 API, SDKs, and console
✅ **Exceeds the experience bar, remote, band top of $425K** - 13 years PM vs. 10+
⚠️ **"Significant experience on AI-powered products" is the thin spot** - The evidence is the AI-built documentation system in production and VoiceBase's AI speech-to-text API; no consumer-scale generative AI product shipped (Profile.md, Areas for Development). The preferred applied-AI/ML background is not met
⚠️ **Pooled requisition** - Candidates are considered across three teams; only Platform & Enterprise is the fit. Posted seven weeks ago; the wide band means level and pay are decided in interviews. Ask which team is hiring before investing in tailoring

---

### D3. **Staff Product Manager, AI Builder Experience (Partner Platform)** ⭐ **FIT SCORE: 78/100**
**Application status:** Package prepared October 29, 2026 (`applications/mongodb-partner-platform/`); six claims to confirm in the checklist before submitting.
**Company:** MongoDB
**Location:** United States; Greenhouse working model "2-Flexible" (sibling postings: office or remote within the US). Confirm remote eligibility
**Compensation:** $151,000 - $297,000 USD base + equity, ESPP, benefits
**Posted:** September 4, 2026; updated October 27, 2026
**Link:** [Apply Here](https://www.mongodb.com/careers/job/?gh_jid=8129885)
**Full Description:** [jobs/descriptions/MongoDB-Staff-PM-AI-Builder-Experience.md](descriptions/MongoDB-Staff-PM-AI-Builder-Experience.md)

**Key Requirements:**
- Own the Partner Platform: the Partner API, self-serve onboarding, enterprise and admin controls, partner-managed account creation and billing, partner discovery, integration quality bar
- Make APIs and tools "understandable to people, usable by agents, observable, secure, and resilient under automation"
- 8+ years owning complex technical products, platforms, APIs, developer tools, ecosystems, or partner integrations
- Technical fluency on APIs, authentication and authorization, platform boundaries, integrations, security trade-offs; MCP and agent experience strongly preferred
- A clear point of view on building for human developers versus AI agents; hands-on AI tool use

**Fit Analysis:**
✅ **Partner API and partner onboarding is Daniel's current job** - Built developer.alianza.com with 10-minute quickstarts to a live INVITE for AI experience providers integrating with Crux; helped guide the Crux API structure with Architecture; owns public APIs, events, and webhooks
✅ **Built for humans and agents** - Built an MCP server for the Crux API; reference docs generated from the API's technical definition with explicit gap reporting; published on where to trust AI systems. The "point of view on humans versus agents" requirement maps to his 2025-2026 writing
✅ **Authn/z and governance fluency** - Publishes the Crux OAuth 2.0 (private_key_jwt, key rotation) authentication guide; API standards and design review with Architecture; two credential-management patents. Nice-to-haves on OAuth, delegated access, and API governance are partly covered
✅ **Partner ecosystems at scale** - Ericsson's Global Network API Platform across hundreds of MNOs; Enhanced Number Verification with operators and handset manufacturers
✅ **Exceeds the experience bar** - 13 years PM vs. 8+
⚠️ **Staff title and band** - One level below the current Principal title; the band's top ($297K) reaches the floor but a remote Idaho offer will land lower. Acceptable only if base reaches current (Profile.md lateral rule)
⚠️ **Remote not stated in the posting body** - "2-Flexible" and "United States" only; confirm before applying
⚠️ **Data infrastructure is a new domain** - No database or data-platform background; the nice-to-have MongoDB familiarity is not met

---

### D4. **Director of Product, AI Growth** ⭐ **FIT SCORE: 78/100**
**Company:** 1Password
**Location:** Remote (United States | Canada); travel 10-20% to design customers, partners, events
**Compensation:** $238,000 - $357,000 USD base + equity, benefits, incentive programs where applicable
**Posted:** October 22, 2026 (same day 1Password for Agents launched; "existing vacancy")
**Level:** Director-level individual contributor, no direct reports
**Link:** [Apply Here](https://jobs.ashbyhq.com/1password/8151254c-b7d1-4653-87b1-7afeba176898)
**Full Description:** [jobs/descriptions/1Password-Director-AI-Growth.md](descriptions/1Password-Director-AI-Growth.md)

**Key Requirements:**
- Own the growth thesis for 1Password's AI business; run the design-customer program as the single person accountable for each agentic-access deployment, with a forward-deployed engineering team
- Decide where 1Password sits in the customer's AI stack; build the partnerships and integrations that complete an end-to-end outcome; work with BD on commercial terms
- 8+ years PM including carrying a revenue or adoption target; took a new product area from hypothesis to customers in production
- Technical depth on how AI agents are built, deployed, and given access to systems; AI-first daily work
- Preferred: familiarity with agentic access products

**Fit Analysis:**
✅ **Hypothesis to production is the strongest story on the record** - Video Express: validated with a prototype, beta in under 3 months, GA in under 9, 10% of 2019 platform minutes within a year; developer.alianza.com launched September 9, 2026
✅ **Technology partnerships and integrations** - Enhanced Number Verification with mobile operators and handset manufacturers; Ericsson's Global Network API Platform; CAMARA at Charter; Crux launched with AI experience providers through operators
✅ **Agent access depth** - Owns the developer surface of the control plane that gives AI experiences governed access to phone calls; built an MCP server; daily Claude Code user, which meets "works AI-first" literally
✅ **Revenue and adoption evidence** - $3M revenue capture through developer migration in 6 months; platform grown to 1.5M+ minutes/month; 40% support-ticket reduction
⚠️ **The design-customer "general contractor" motion is field-heavier than the record** - Daniel has built demos and sales enablement (VoiceBase, Vonage) and worked with GTM, but has not been the person accountable for enterprise deployments with forward-deployed engineers
⚠️ **Commercial terms with BD** - SendGrid M&A proposals are the nearest evidence; no documented partner revenue-term negotiation (Profile.md lists monetization as an area for development)
⚠️ **Growth role, not platform ownership** - Title is Director IC, band tops $44K below D1; the platform roadmap belongs to other PMs

---

### Evaluated and Below Threshold (Discovery Search, October 27, 2026)

Sorted by score. Every link was opened; bands are base salary as posted.

| Role | Comp / location / posted | Score | Why it falls short |
|------|--------------------------|-------|--------------------|
| [Product Manager, Enterprise Identity, OpenAI](https://jobs.ashbyhq.com/openai/83f6d415-9462-4afc-a539-ca8d996e011a) | $347K-$490K; San Francisco, relocation assistance; Sept 21 | 70 | SSO, SCIM, federation, and admin controls across ChatGPT and the API for IT buyers; 10+ years on large-scale enterprise products. Daniel's identity evidence is network-side verification and the Crux access surface, not enterprise IT identity. The only SF role in this run whose band top clears the ~$455K relocation floor; worth a conversation if relocation is on the table |
| [Product Manager, Ecosystem, Stripe](https://stripe.com/jobs/listing/product-manager-ecosystem/8234705) | $214K-$322K; remote US; Oct 6 | 68 | Owns the Stripe Apps Marketplace: merchant funnel, discovery and ranking, app quality standards, partner incentives and revenue share. Two-sided platform evidence from Aerohive and Crux fits; marketplace growth mechanics and monetization design do not |
| [Staff PM, Agent Connectivity / Core Primitives / Nexus, Temporal](https://jobs.ashbyhq.com/temporal/7592248c-719a-485c-a1a9-9285f99ed56b) | $160K-$262.5K; remote US; Oct 16 | 68 | Best surface in the developer-tools slice (SDKs, agent tool calling, cross-service APIs) at a band that tops $18K under the floor. Revisit if the floor drops to $250K |
| [Senior Group PM (Apono), 1Password](https://jobs.ashbyhq.com/1password/0759fd1f-945b-40a6-95e1-e498bcab2044) | $202K-$293K, commission-eligible; remote US "with a focus on the East Coast"; Oct 9 | 68 | Leads the Apono PM team (just-in-time access for humans, machines, agents). People-manager role; IAM/PAM depth asked; East Coast focus from Mountain time; band below D1-D4 |
| [Staff PM, Telephony, LiveKit](https://jobs.ashbyhq.com/livekit/d0dbf189-af6d-400e-ac1f-4da798be85bb) | $225K-$265K; remote or SF; Aug 13 | 65 | SIP trunking and phone numbers for voice agents, squarely adjacent to Crux. Fails band and the 60-day window |
| [Staff PM, Identity, Twilio](https://job-boards.greenhouse.io/twilio/jobs/8319160) | $155K-$229K (top tier); remote US excluding CA, CT, NJ, NY, PA, WA; Oct 26 | 65 | Authentication, authorization, agentic and non-human identity for developers; Twilio alumni. Staff level and a band that tops roughly $50K under the floor |
| [Sr. Principal PM, Developer Platform, Twilio](https://job-boards.greenhouse.io/twilio/jobs/8108776) | $233K-$305K by tier (Idaho not listed); remote US excluding Bay Area and Seattle; Aug 7 | 62 | Internal platform-as-a-product (golden paths, DORA metrics) requiring 12+ years on "cloud native commerce systems for usage-based and metered products." Stated application deadline (Oct 5) has passed; posting still open |
| [Product Manager, Auth, Supabase](https://jobs.ashbyhq.com/supabase) | no band; remote global; Oct 7 | 62 | OAuth for MCP clients and agent auth are the strong signals. Flat PM title and no band; level unknown |
| [Technical PM, Developer Experience & PLG, Telnyx](https://job-boards.greenhouse.io/telnyx54/jobs/8042159003) | no band; remote US; Oct 22 | 60 | Head-of scope (reports to the COO, leads a 6-person DevRel and PLG engineering team) but requires "a strong software engineering background... comfortable building and debugging real applications." Conflicts with the no-solo-coding constraint |
| [Staff PM, AI & Data Foundations, Plaid](https://jobs.ashbyhq.com/plaid/f1e8a2ca-d4cc-4b00-9548-c73bce9cf069) | $208K-$340K; SF or NYC; Sept 29 | 60 | Internal platform ("platforms that Plaid teams choose to use"), not the public API; no remote sentence |
| [Staff PM, Trust Hub / KYC, Twilio](https://job-boards.greenhouse.io/twilio/jobs/8131091) | $188K-$277K; remote US excluding CA, CT, NJ, NY, PA, WA; Aug 26 | 60 | Onboarding and compliance gateway to Twilio's APIs; regulated-telecom experience wanted. Band and date both marginal |
| [Staff PM, AI Applications, Deepgram](https://jobs.ashbyhq.com/deepgram/9762d2a1-3d07-4e65-a0bb-6ed8162ca7d5) | $200K-$250K outside SF/NYC/Seattle; remote US; Oct 9 | 60 | Voice AI applications; band tops at the telecom floor |
| [Director of PM, Agentic Software Delivery, GitLab](https://job-boards.greenhouse.io/gitlab/jobs/8806017002) | $203K-$346K; remote US; Sept 14 | 58 | Requires managing senior and principal PMs with hiring and performance authority, CI/CD, artifact, and observability depth, and pricing and packaging ownership. Three gaps |
| [Principal PM, Security, 1Password](https://jobs.ashbyhq.com/1password/ff516ff4-2726-4c18-ae6e-681640d9c81d) | $238K-$357K + 15% bonus; remote US/CA; Oct 5 | 58 | Owns agentic credential access and MCP trust models (fits) but requires demonstrable cryptography, zero-knowledge architecture, WebAuthn/FIDO, and threat-modeling depth (does not) |
| [Senior PM, Agent Marketplace, Snowflake](https://jobs.ashbyhq.com/snowflake/3c565761-4ce8-40f4-a346-1997b117afbc) | $200K-$287.5K; Menlo Park (Ashby remote flag, no remote sentence); Oct 13 | 55 | Agent and MCP marketplace with "commercial architecture mastery": metered consumption, outcome pricing, committed-spend drawdowns, revenue share. Pricing is the stated gap |
| [Staff PM, Agentic Test Intelligence, GitLab](https://job-boards.greenhouse.io/gitlab/jobs/8871820002) | $168K-$286K; remote US/CA; Oct 13 | 55 | Test automation and code-coverage domain |
| [PM, Enterprise Agent Platform, Decagon](https://jobs.ashbyhq.com/decagon/e27fcbdf-891c-4b2f-9c47-d2bdc26eb2d4) | $232K-$290K; in-office; Aug 8 | 55 | Integrations, SDK, external APIs for an agent platform; "we're an in-office company" |
| [Principal PM, AI-Native Merchant Experiences, Adyen](https://careers.adyen.com) | $330K-$462K; SF office-first, 3 days a week | 50 | Merchant-facing payments product; office-first in SF |
| [Senior PM, Agent Identity Management, Pindrop](https://job-boards.greenhouse.io/pindropsecurity/jobs/8301450) | $150K-$190K; remote US; Oct 20 | 50 | Right surface, Senior level, band far below floor |
| [PM, Agent Development, Financial Services, Sierra](https://jobs.ashbyhq.com/sierra/bc98b50a-d6ea-42b8-b1c6-f55099d1bb1c) | $180K-$390K; SF or NYC on-site; Aug 30 | 45 | "Primarily an in-person company"; financial-services agent builds |
| [Product Manager, Storage, Vercel](https://job-boards.greenhouse.io/vercel/jobs/6228301004) | $208K-$312K (SF); remote US beyond commuting distance; Oct 20 | 40 | Requires shipped storage or database products |

**Companies read with no qualifying opening (so the check is not repeated):** Okta/Auth0 (all PM roles hybrid in office cities or Toronto), WorkOS, Stytch (now on Twilio's board), Descope, Ping Identity, Veza (board unreachable, worth a manual look), ConductorOne (SF hybrid), Oso, Permit.io, Cerbos, Aembit, Astrix (Cisco), Teleport, SGNL (CrowdStrike), Silverfort (Tel Aviv), Persona, Prove, Telesign, Aduna (PM in Łódź only), Vonage (PM roles Wrocław only; a BSS Senior Director role is billing, not APIs), Bandwidth, Dialpad, RingCentral, Zoom, 8x8, Nokia, Ericsson, Verizon, AT&T, Comcast, Charter, T-Mobile, Lumen, Intrado, Sinch, Infobip, Plivo, Boku, Hiya (Senior PM Voice AI, Seattle, $188K-$218K, July), OpenAI (every PM role SF-based), Google DeepMind and Vertex AI (on-site), Cohere (June posting), Mistral, Together AI (four days in SF), Fireworks (hybrid San Mateo), Baseten (April/June postings), Modal, Replicate (via Cloudflare), LangChain (NYC on-site), Composio, Arcade, Browserbase, Retell, Vapi ($240K-$270K, Aug 13), Cartesia, Bland, PolyAI, Cresta, Observe.ai, Hume, Speechmatics, Gladia, LiveKit (above), Daily (not hiring), Agora, Smallest, Rime, Stripe office-only roles (Sandboxes, Developer Experience Bridge, Agentic Commerce), Postman ($240K-$275K, stale), Kong (SF), Cloudflare (hybrid Austin/London), PagerDuty (hybrid), Datadog (NYC hybrid), Confluent, HashiCorp, Netlify, Speakeasy, Stainless, Mintlify, ReadMe, Apollo, Zuplo, Sendbird, Stream, Ably, PubNub, LaunchDarkly (Staff PM Data Products, Aug 13, Boise zone tops $251K; VP Product needs 20+ PM org), Workato (Palo Alto), Zapier, Slack, Shopify, Square, Atlassian, Checkout.com, Lithic, Unit, Modern Treasury, Databricks (SF/Seattle), Snowflake (above).

### Shared by Daniel via LinkedIn (Evaluated October 28, 2026)

All four read through LinkedIn's guest endpoint and, where one exists, the company's own board. None reaches 75.

| Role | Comp / location / posted | Score | Why it falls short |
|------|--------------------------|-------|--------------------|
| [Principal PM, Platform & APIs, Avaya](https://www.linkedin.com/jobs/view/4483557841/) | "up to $234,100 in total compensation, inclusive of base salary and bonus"; United States (remote not stated); 7-10 years; posted ~Oct 26 | 64 | The surface is the best of the four and reads like the Alianza job: APIs, events, authentication and authorization, integrations, developer tooling, "evolve an established enterprise product toward a more open and extensible platform," CCaaS/CPaaS valued. Two things sink it. Total comp tops roughly $234K including bonus, so base lands well under the Principal floor and under a lateral move. And Avaya is in a multi-year contraction: Chapter 11 in 2023, layoff rounds from November 2024 through at least October 2025 (reported 30% at the India hub), and support dropped for CCaaS customers under 200 seats in June 2025. Not found on careers.avaya.com under the posted job code; the LinkedIn apply button points at avaya.com. |
| [Senior PM, Integrations and Orchestration, Agiloft](https://jobs.lever.co/agiloft/0ccb411f-b7ab-4fec-a26a-2b55da3bfb2a) | No band; remote US; 5-8 years; Lever posting created Oct 26 | 62 | Owns the external API surface (versioning, developer experience, authentication patterns), MCP and AI orchestration, webhooks and event-driven patterns, developer enablement. Strong overlap with Crux work. But it is a Senior title scoped at 5-8 years (two levels under the record), requires iPaaS or middleware experience (Workato, MuleSoft, Boomi) the record lacks, sits in contract-lifecycle-management software, and shows no band; Agiloft's other Senior PM listings this year showed $120K-$160K. About 375 employees, private-equity owned. |
| [Principal PM, Findem](https://jobs.lever.co/findem/df08f2ad-7c9e-4749-abd8-ea4ed9a21e18) | $190K-$220K; US remote; 7+ years; Lever posting created Sept 2 | 48 | HR and recruiting software; wants agentic and conversational AI workflow automation, B2B PLG, and prior HR-tech experience. No API or platform component. Band below the Principal floor. Venture-backed startup. |
| [Principal PM, Buyer Products, G2](https://www.linkedin.com/jobs/view/4482774649/) | No band; United States; 10+ years; posted ~Oct 23 | 45 | "A consumer-grade product role inside a B2B marketplace": growth, personalization, search and discovery, experimentation, and an owned P&L or growth number. Requires Principal-level ownership of a major consumer-facing product, which the record does not have (Yahoo Mail Monetization is the nearest, 2013-2015). No API surface; MCP appears only as a nice-to-have. |

### Shared by Daniel, October 29, 2026 (Intuit, ServiceNow, Indeed links)

| Role | Comp / location / posted | Score | Status and why it scores under 75 |
|------|--------------------------|-------|-----------------------------------|
| Principal PM, Member Experience, Teladoc Health (Indeed, one of four links shared Oct 29; read from Daniel's PDF) | $200K-$230K base + bonus; remote US; 12+ years; no sponsorship | 42 | Owns the consumer member experience across the care journey: onboarding, activation, engagement, retention, habit formation, A/B testing, design critique. Requires "12+ years ... in consumer-facing products at meaningful scale" and direct ownership of a consumer product from ambiguous problem to adoption; the record is enterprise and developer platforms, with Yahoo Mail Monetization (2013-2015) the only consumer line. No API or platform component ("without requiring deep platform or architectural expertise"), SQL and product-analytics tooling asked, healthcare domain, band tops $230K. Indeed employer rating 3.2. |
| [Senior Staff Inbound PM, Conversational AI, ServiceNow](https://careers.servicenow.com/jobs/744000149871496/senior-staff-inbound-product-manager-conversational-ai/) | No band shown; San Diego, "Flexible or Remote" (persona assigned by role and distance from an office); 12+ years; posted Sept 16 | 64 | Feature PM for the conversational experience itself: disambiguation, slot filling, fallback and error handling, multimodal, feedback intelligence, across AI orchestrators. Fits on 13 years, hands-on AI fluency, VoiceBase speech-to-text and the Crux virtual-agent hand-off as adjacency, and enterprise pilots and escalations. Falls short on the core: no API or platform component, no evaluation-dataset or comparative model-evaluation work on the record, no Virtual Agent or AI Agent product ownership, Figma is a stated non-proficiency, and no band. Full description: [jobs/descriptions/ServiceNow-Senior-Staff-Inbound-PM-Conversational-AI.md](descriptions/ServiceNow-Senior-Staff-Inbound-PM-Conversational-AI.md). |
| [Principal PM, Agent Development Platform, Intuit](https://jobs.intuit.com/job/-/-/27595/99493492384) | $243K-$328.5K (Mountain View) or $230K-$311K (San Diego); hybrid, three days onsite, no remote; posted Aug 20 | 64 | **Package prepared October 29 at Daniel's request** (`applications/intuit-agent-platform/`). Internal agent SDLC platform (Agent Starter Kit, sandbox, developer tooling) for thousands of Intuit builders. Fits on developer-platform ownership, agents in production (docs system, MCP server, daily Claude Code), standards across teams with Architecture, and the Vonage PM process that became company-wide. Falls short on location (no remote; Mountain View band top is under the relocation floor), agentic-framework depth at scale (LangGraph, SDK-level harness work not on the record), internal rather than external platform, tax and accounting domain, and age (70 days). Oct 29: Daniel's contact reports the role is finalizing candidates; still listed on the site. Eight similar Intuit PM roles scanned and scored 48-66, best [Senior Staff PM, AI Driven API Management Platform](https://jobs.intuit.com/job/-/-/27595/102516305200) (66; MCP and API governance surface, Mountain View hybrid, $205.5K-$278K). **Package for 24739 prepared October 30 at Daniel's request** (`applications/intuit-api-management/`); description: [jobs/descriptions/Intuit-Senior-Staff-PM-API-Management-Platform.md](descriptions/Intuit-Senior-Staff-PM-API-Management-Platform.md). Full description and the similar-roles table: [jobs/descriptions/Intuit-Principal-PM-Agent-Development-Platform.md](descriptions/Intuit-Principal-PM-Agent-Development-Platform.md). |

**What would widen the pipeline.** The telecom and voice-AI slices have the right surfaces but pay $225K-$275K at Staff and Principal; dropping the floor to $250K admits Temporal, LiveKit, and Twilio Identity. Accepting SF with a band above the relocation floor admits only OpenAI Enterprise Identity. Otherwise the fix is time: the boards refresh weekly, and this run can be repeated against the same seed pattern.

---

## Anthropic — Current Openings (Evaluated October 13, 2026)

Full sweep of anthropic.com/jobs on October 13, 2026. All Anthropic roles are hybrid (minimum 25% in-office; no fully remote option stated) and offer visa sponsorship. Greenhouse does not show posting dates; all links below were verified open on the evaluation date. The previously tracked **Product Manager, API** (job 4936029008) and the Claude Code, Developer Services, Cloud Inference, API Growth, and Developer Education Lead roles are **closed**.

### A1. **Product Manager, Multi-Cloud Growth - Google** 🔥 **FIT SCORE: 85/100**
**Application status:** Submitted by Daniel, October 23, 2026 (package in `applications/anthropic-multi-cloud-growth/`).
**Company:** Anthropic (Platform Org)
**Location:** San Francisco, CA (hybrid)
**Compensation:** $305,000 - $460,000 USD base + equity and benefits
**Posted:** Not shown (open as of October 13, 2026)
**Link:** [Apply Here](https://job-boards.greenhouse.io/anthropic/jobs/5153924008)
**Full Description:** [jobs/descriptions/Anthropic-Multi-Cloud-Growth-Google.md](descriptions/Anthropic-Multi-Cloud-Growth-Google.md)

**Key Requirements:**
- Platform Org owns APIs, self-serve developer experience, multi-cloud integrations, agentic infrastructure
- Define enterprise API strategy; roadmap spanning authentication, rate limiting, compliance, SDKs
- Have built or shipped products with a hyperscaler as a partner (AWS/GCP/Azure)
- Have owned a revenue number, margin target, or channel P&L
- Preferred: 10+ years in high-scale developer-facing software, 5+ years PM, founder/GM experience

**Fit Analysis:**
✅ **Enterprise API strategy is the core of the role** - 11 years on API products at Alianza, Charter, Vonage/Ericsson, Twilio (SendGrid), and VoiceBase; currently set API standards and review API proposals across engineering teams at Alianza; owned auth, rate limiting, and SDK roadmaps across iOS/Android/Web/desktop
✅ **Exceeds experience bar** - 10+ years developer-facing software and 10+ years PM vs. 10+/5+ preferred
✅ **Partner-channel platform experience** - Led Enhanced Number Verification, distributed through Ericsson to mobile network operators, overcoming the existing product's limits with operators and handset manufacturers; closest analog to shipping through a hyperscaler channel
✅ **Scale and reliability** - Led Vonage Video API through 10x growth while maintaining platform reliability; 1.5M+ minutes/month platform
✅ **Hands-on with Anthropic's product** - GitHub portfolio shows active Claude API integration work (GrocerySelector, AlianzaDocs)
⚠️ **No direct hyperscaler partnership** - Minimum qualification asks for products shipped with AWS/GCP/Azure as partner; MNO and carrier partnerships are the nearest substitute and must be framed explicitly
⚠️ **Owned P&L is partial** - $3M revenue capture and Yahoo Mail Monetization show revenue impact, but no explicit channel P&L ownership
⚠️ **San Francisco only, hybrid** - Requires 25%+ in-office; relocation or regular travel from Boise

---

### A2. **Product Manager, Safe Access** ⭐ **FIT SCORE: 78/100** (revised October 22, 2026, from 85)
**Application status:** Submitted by Daniel, October 29, 2026 (package in `applications/anthropic-safe-access/`; "Why Anthropic?" written by Daniel).
**Revision note:** Earlier scoring credited Daniel with designing the Crux access model and authentication. He documents and exposes the access model; the platform and its auth design predate his hire. The identity evidence is now Enhanced Number Verification, the credential-management patents, and the developer-facing access journey he built. Still a credible fit, seven points lower.
**Company:** Anthropic
**Location:** San Francisco, CA | New York City, NY (hybrid)
**Compensation:** $305,000 - $385,000 USD base + equity and benefits
**Posted:** Not shown (open as of October 13, 2026)
**Link:** [Apply Here](https://job-boards.greenhouse.io/anthropic/jobs/5428898008)
**Full Description:** [jobs/descriptions/Anthropic-Safe-Access.md](descriptions/Anthropic-Safe-Access.md)

**Key Requirements:**
- Own strategy and roadmap for Anthropic's centralized identity, verification, and access system (0-to-1 product on the critical path of every model launch)
- Support API design and UX of access APIs used by platforms, resellers, and internal services
- Have owned a developer platform, identity, authorization, or access-management product end to end
- Preferred: 8+ years PM; multi-tenant platforms serving first-party apps, direct API customers, and third parties; zero-to-one

**Fit Analysis:**
✅ **Identity verification API experience** - Led Enhanced Number Verification at Vonage/Ericsson, extending a commercial CAMARA identity API past its limits with operators and handset manufacturers; owns the developer-facing access journey for Crux (the platform itself predates his hire; auth design was not his)
✅ **Credential and access patents** - 2 patents for WiFi credential automation and seamless device onboarding (Aerohive); demonstrates deep access-management product thinking
✅ **Multi-tenant developer platform** - Vonage Video API served first-party apps, direct API customers, and third-party developers at scale
✅ **Zero-to-one track record** - Enhanced Number Verification (united a multi-company team, per Vonage Sr. Director recommendation); Video Express beta in under 3 months, GA in under 9; developer.alianza.com designed and launched; early-stage CAMARA initiatives at Charter
✅ **Cross-org execution** - Coordinated Engineering, Architecture, DevRel, Legal/compliance, and GTM across telecom partners
⚠️ **No first-party account/auth system ownership at scale** - Auth0 SDK work on GitHub and credential patents are adjacent, but never owned a company-wide login/account system
⚠️ **Hybrid in SF or NYC** - Requires 25%+ in-office; relocation or regular travel from Boise

---

### A3. **Product Manager, New Markets and Monetization** ⚠️ **FIT SCORE: 66/100** (revised October 20, 2026, from 82)
**Revision note:** Daniel confirmed on October 20 that he has not worked on pricing, program terms, revenue share, or partner billing at any employer, and that the Charter billing work does not cover metering or settlement. The minimum qualification "have negotiated pricing or program terms" and the billing pillar are therefore unmet. Only the Verticals pillar (telecom as a target API market) remains a fit. Not pursuing unless a verticals-only opening appears.
**Company:** Anthropic (Claude Platform)
**Location:** San Francisco, CA (hybrid)
**Compensation:** $305,000 - $385,000 USD base + equity and benefits
**Posted:** Not shown (open as of October 13, 2026)
**Link:** [Apply Here](https://job-boards.greenhouse.io/anthropic/jobs/5386182008)
**Full Description:** [jobs/descriptions/Anthropic-New-Markets-Monetization.md](descriptions/Anthropic-New-Markets-Monetization.md)

**Key Requirements:**
- Founding PM owning one of: partner/platform billing (metering, attribution for reseller usage), spend observability and controls, one account across API and subscriptions, or a vertical (platform strategy for a specific industry)
- Have owned a developer platform, API, billing, or self-serve growth product end to end
- Technically fluent (read API docs, design billing/identity/attribution with engineers); pull your own data with SQL
- Preferred: 8+ years PM; metering or cloud-marketplace channels; regulated industries; zero-to-one

**Fit Analysis:**
✅ **Developer platform/API owned end to end** - Alianza developer platform (developer.alianza.com), Vonage Video API, SendGrid Email API, VoiceBase Speech API, Charter network APIs
✅ **Telecom as a target vertical** - The role's "Verticals" pillar is about finding the next API markets; deep telecom/CPaaS domain expertise plus CAMARA leadership is a ready-made vertical thesis
✅ **Partner-channel usage and billing** - Early-stage telecom billing system work at Charter; Number Verification distributed through MNO partners; Crux usage flows from AI experience providers through operators who monetize it by revenue share, referral, or white label (usage flowing through partners is the role's core billing problem)
✅ **Technical fluency and SQL** - SQL, Python, TypeScript in skill set; active GitHub; product analytics background
✅ **Regulated industry and zero-to-one** - Telecom is regulated; multiple 0-to-1 launches
⚠️ **Monetization is a stated development area** - Profile.md flags limited explicit SaaS monetization strategy; Yahoo Mail Monetization and $3M revenue capture need to carry the story
⚠️ **No cloud-marketplace or usage-metering product shipped** - Preferred qualification, not minimum
⚠️ **San Francisco only, hybrid**

---

### A4. **Developer Relations** ⭐ **FIT SCORE: 78/100**
**Company:** Anthropic (Claude Code / Claude Tag)
**Location:** San Francisco, CA | New York City, NY (hybrid)
**Compensation:** $290,000 - $435,000 USD base + equity and benefits
**Posted:** Not shown (open as of October 13, 2026)
**Link:** [Apply Here](https://job-boards.greenhouse.io/anthropic/jobs/5383596008)
**Full Description:** [jobs/descriptions/Anthropic-Developer-Relations.md](descriptions/Anthropic-Developer-Relations.md)

**Key Requirements:**
- Shape how developers discover, onboard, and succeed with Claude Code and Claude Tag; measure developer success; feed roadmap
- 5+ years in developer relations, developer experience, or technical product/engineering roles
- Write production-quality code demos; explain AI/ML and API concepts to varied audiences
- Nice to have: LLM experience, conference speaking, technical writing or video content

**Fit Analysis:**
✅ **Developer experience track record** - Reduced support tickets 40% through documentation and self-service tooling; built developer portals and consoles at VoiceBase, SendGrid, Vonage
✅ **Production-quality code and demos** - 28-repo GitHub portfolio including Claude API integrations, iOS WebRTC/CallKit, Auth0 and Twilio SDK work; built product demos and sales enablement at VoiceBase
✅ **Technical API communication** - Presented API strategy at Ericsson Innovation Days to European MNOs; created developer documentation across four API platforms
✅ **Active Claude Code user** - Daily use of Claude Code in this and other repositories; credible first-hand perspective on the product
⚠️ **Role is DevRel, not product management** - A lateral move out of the PM track; conference speaking and public content portfolio are thin
⚠️ **Hybrid in SF or NYC**

---

### Evaluated and Below Threshold (October 13, 2026)

| Role | Comp | Score | Why it falls short |
|------|------|-------|--------------------|
| [Technical Program Manager, API Platform](https://job-boards.greenhouse.io/anthropic/jobs/5256303008) | $290K-$435K | 70 | Requires 7+ years TPM experience; scaling programs for API stack is a strong thematic match (10x growth) but it is a TPM, not PM, track |
| [Product Manager, Claude](https://job-boards.greenhouse.io/anthropic/jobs/5448167008) | $385K-$460K | 70 | Consumer product taste and experimentation for millions of consumer users; API/B2B background is an industry mismatch |
| [Product Manager, Research (Code)](https://job-boards.greenhouse.io/anthropic/jobs/5324349008) | $305K-$385K | 68 | Wants AI/ML technical depth, Python/SQL, founder-style launches of new model-driven products; hands-on LLM work helps but no shipped AI product at scale |
| [Product Manager, Enterprise Privacy](https://job-boards.greenhouse.io/anthropic/jobs/5434369008) | $305K-$385K | 65 | Preferred 8+ years with deep privacy/security/compliance product exposure (audit logging, key management, SOC 2, FedRAMP); not in Profile.md |
| [Product Manager, Public Sector](https://job-boards.greenhouse.io/anthropic/jobs/5393452008) | $305K-$385K | 65 | Only remote-friendly role; no government or FedRAMP experience; product judgment weighted over domain, so a stretch application is possible |
| [Product Manager, Billing](https://job-boards.greenhouse.io/anthropic/jobs/5434361008) | $385K-$460K | 60 | Minimum requires 7+ years including self-serve purchase/subscription/billing with owned conversion metrics; Charter billing work is early-stage |
| [Product Manager, Multi-Cloud Trust & Safety](https://job-boards.greenhouse.io/anthropic/jobs/5409934008) | $305K-$385K | 55 | Trust & safety, fraud, and abuse domain; no overlap in Profile.md |

Also open but not evaluated (no API/platform component): Product Manager roles in Safeguards (Rare Harms, Cyber, Generalist, Account Integrity & Abuse), Cybersecurity, Claude Science, Human Data Platform, Research; Manager, Product Program Management; Product Marketing Manager, Platform.

---

## Clera Recruiter Referrals (Evaluated October 18, 2026)

Source: email thread with Alexander Farr (Clera, alexander.farr@clera-connect.org), September 4-16, 2026. The original pitch, a Senior Agent PM role at Gradient Labs, was ruled out (on-site, forward-deployed scope, no published range). On September 9 he added "6 principal and head-of PM roles" to a Clera dashboard: https://www.getclera.com/match/9h642lnr8byu. His September 16 follow-up ("Any of those roles catching your eye?") is still unanswered. The dashboard now shows three roles and Clera's October 18 weekly email added five more. All eight were read in full. Clera handles applications by intro request rather than a form.

### C1. **Product Manager** ⚠️ **FIT SCORE: 65/100** (revised October 18, 2026, from 80)
**Company:** Opal Security (Series B, Greylock and Battery Ventures, $59M raised; AI-native identity and access management; new CEO Howard Ting Dec 2025, new CPO Sameer Mehta from Veza Jun 2026)
**Location:** Clera says San Francisco or Remote (US). **Opal's own posting says hybrid San Francisco, 3 days a week required, hiring manager strongly prefers 5 days initially.** The role is "the CPO's number two." Opal's careers page lists every non-sales role in San Francisco.
**Compensation:** $180,000 - $250,000 USD + equity (ceiling is at current pay; SF relocation floor in Profile.md is ~$455K)
**Revision note:** Score lowered 15 points for the in-office requirement from Boise and for the "successor to the CPO" pitch resting on a CPO who arrived four months ago. Company diligence is in [jobs/descriptions/Opal-Security-Product-Manager.md](descriptions/Opal-Security-Product-Manager.md).
**Posted:** July 14, 2026 on Clera (96 days old; still served as an active match on October 18, verify with Alexander before applying)
**Link:** [Clera listing](https://www.getclera.com/jobs/opal-security/product-manager--uzoqzedf8ew1)
**Full Description:** [jobs/descriptions/Opal-Security-Product-Manager.md](descriptions/Opal-Security-Product-Manager.md)

**Key Requirements:**
- Own one of two swim lanes: agentic security strategy (how enterprises govern AI agents' access) or building AI-powered agents for customer outcomes
- Half the time with enterprise customers and GTM, half on requirements, KPIs, and 2-week to 6-month roadmaps
- 5+ years building and scaling technical B2B products, including 0-to-1 launches and turnarounds
- Nice to have: identity security, IAM, or adjacent infrastructure and security
- Explicit path to succeed the CPO

**Fit Analysis:**
✅ **Identity and access is the product** - Owns the developer-facing access journey for Crux (eligibility, connection gate, assignment scope, auth guide); Enhanced Number Verification; two credential-management patents; the Safe Access resume already tells this story
✅ **Agentic access governance maps to current work** - Daily Claude Code use, an LLM-built documentation system in production, MCP server for the Crux API, and published writing on where AI systems should and should not be trusted
✅ **0-to-1 and turnaround record** - Video Express prototype to GA in under 9 months; Number Verification; developer.alianza.com; SendGrid platform transition
✅ **Enterprise customer time** - Half the role is customer-facing, which matches the ODI/JTBD discovery practice and partner-integrator interviews at Alianza
✅ **Remote and succession path** - Remote US is explicit, and "potential successor to the CPO" offsets the title
⚠️ **Title and compensation are a step down** - "Product Manager" at $180K-$250K tops out at current pay; the CPO succession path is the only reason to engage, so lead with that in the intro
⚠️ **Posting age** - 96 days exceeds the 60-day inclusion rule; included because the recruiter channel is warm and Clera still matches it

---

### C2. **Technical Product Manager, Atlas** ⚠️ **FIT SCORE: 72/100** (conditional on remote)
**Company:** Basis (Series B, Accel and Avid Ventures, $100M raised; AI agents for accounting)
**Location:** New York, NY. Clera lists Remote (US); a mirror listing says 5 days a week in Flatiron. Unresolved.
**Compensation:** $175,000 - $275,000 USD + equity
**Posted:** August 5, 2026 on Clera (74 days old)
**Link:** [Clera listing](https://www.getclera.com/jobs/basis/technical-product-manager-atlas--p1hf1koxn0yb)

**Why it is close:** Atlas is an internal team shipping agent teammates, context architecture, MCPs for internal tools, and evaluation suites. That is the AlianzaDocs and MCP-server work at larger scale, and the "unlimited token budget" culture fits. **Why it falls short:** it is an internal-tooling TPM role rather than an external platform, accounting is an industry mismatch, and if the role is five days in Flatiron it fails the relocation bar. Ask Alexander which it is before spending time.

---

### Evaluated and Below Threshold (Clera, October 18, 2026)

| Role | Comp | Score | Why it falls short |
|------|------|-------|--------------------|
| [Chief Product Officer, TitanX](https://www.getclera.com/jobs/titanx/chief-product-officer--ueot72ohgcef) | $260K-$320K + 0.5-0.75% equity, remote US (ET preferred) | 65 | Phone Intent platform is telephony-adjacent and the pay fits, but it requires deep sales-tech/revenue-intelligence domain, $10M-$100M ARR scaling, and building a product org from scratch; no CPO/VP history. Stretch only. |
| [Product Manager, Traba](https://www.getclera.com/jobs/traba/product-manager--yk0o9en7ssay) | $150K-$250K + equity, remote | 55 | AI Agents track is 0-to-1 and interesting, but it is a labor-marketplace company, a PM-level title reporting to a VP, and the band floor is $150K |
| [Senior Technical PM, Loancrate](https://www.getclera.com/jobs/loancrate/senior-technical-product-manager--9as6el0ovw54) | $170K-$250K + equity, remote US | 55 | Mortgage loan-origination system, IC role, monthly customer-site travel, no API/platform component; posted April 2026 |
| [Founding Principal, Solvea](https://www.getclera.com/jobs/solvea/founding-principal--i8p59y7yqh19) | $200K-$250K + equity | 30 | Despite the title it is a deployment-strategist role requiring Bain/McKinsey/BCG due-diligence experience and PE associate background |
| Transformation Strategist, Duvo AI | £150K-£250K | n/a | UK-based |
| Head of Growth, Cello | not listed | n/a | Growth role, not product |

---

## Inbound Recruiter Pitches, August-October 2026 (Evaluated October 18, 2026)

Source: Gmail. Four agencies pitched roles in the last two months: Sidebar Talent (Mercury), BreakLine (Code Metal), American IT Systems (FullEnrich), and Twill (Chromatic, declined August 10 on compensation). The roles pitched were checked against the companies' own job boards; where the pitched role had closed, the nearest open role was evaluated instead.

### R1. **Head of Product, Interfaces** ❌ **CLOSED October 23, 2026** (was FIT SCORE: 76/100)
**Status:** Removed from Mercury's Greenhouse feed between October 18 and October 23, 2026; the posting URL returns 404. Materials were finished but not submitted, and were deleted in the October 28 cleanup (recoverable from git history before commit "Consolidate application materials"). Head of Product, Business Lending closed in the same window. Remaining Mercury options: Senior Product Manager, Users (R2 below, still open as of October 23) and the Open Call for Founders / Founding Teams.
**Company:** Mercury (Series D, $5.2B valuation May 2026 led by TCV; ~$650M annualized revenue; profitable 3+ years; 300K+ customers; national bank charter application pending)
**Location:** San Francisco, New York, Portland, or Remote within US or Canada
**Compensation:** $289,700 - $362,100 USD base + equity (US, any location)
**Posted:** Marked "New" on October 18, 2026
**Link:** [Apply Here](https://job-boards.greenhouse.io/mercury/jobs/6213000004)
**Full Description:** [jobs/descriptions/Mercury-Head-of-Product-Interfaces.md](descriptions/Mercury-Head-of-Product-Interfaces.md)
**How it surfaced:** Lexy Franklin (Sidebar Talent) pitched the Staff PM, API & Agentic Banking role on August 25-31 at $239K-$298.8K. That role, and a Senior-level repost of it, are now closed. Interfaces is the open role that owns the same surface.

**Key Requirements:**
- Set product direction across Dashboard, Mobile, Command (Mercury's AI surface), the API, and MCP; own shared foundations for navigation, tasks, notifications, and agent interactions
- Lead and develop the PM team; reports to the VP of Product
- 10+ years of product management including 5+ years leading PMs
- Hands-on AI product experience, including how it was evaluated, where it failed, and what changed
- Design for customer control over consequential actions, permissions, and visibility

**Fit Analysis:**
✅ **API and MCP are in scope** - Shipped the Crux API 1.0.0 and built an MCP server for it; Mercury's own API has an MCP server in beta and a 20-plus-resource reference, so this is a platform to grow, not start
✅ **Hands-on AI with evaluation** - Operates an LLM-built documentation system in production that reports its own gaps; published on where AI systems fail and how to evaluate them; AI-agent discovery experiments
✅ **Agent interactions and consequential actions** - Crux applies identity, consent, and policy before an AI acts on a phone call; the posting's "customer control over consequential actions" is the same problem in banking
✅ **13 years PM, multi-surface SDK ownership** - Client SDKs across 8 platforms at Vonage; Video Express shipped across web and native
✅ **Remote at Principal-plus compensation** - $290K-$362K base, remote US, clears every bar in Profile.md
⚠️ **5+ years leading PMs is a formal gap** - Profile.md records mentoring and onboarding a team of 5 PMs and building team process at Vonage, not line management; this must be addressed honestly in the cover letter
⚠️ **Dashboard and Mobile are consumer-grade surfaces** - Most of the record is developer-facing; the strongest consumer-adjacent work is Video Express and Yahoo Mail
⚠️ **Fintech is new** - No banking or payments domain experience beyond Charter's early billing work

---

### R2. **Senior Product Manager, Users** ⚠️ **FIT SCORE: 70/100**
**Company:** Mercury
**Location:** Remote within US or Canada
**Compensation:** $200,700 - $250,900 USD base + equity
**Link:** [Apply Here](https://job-boards.greenhouse.io/mercury/jobs/6148371004)

**Why it is close:** The Users team owns roles, permissions, invitations, and the authorization layer every other Mercury team builds on, with an explicit "what gets harder when the actor isn't a person" question about agents. That is the Safe Access story. **Why it falls short:** Senior title, band tops out at current pay, and 7+ years asked where 13 are offered. Worth mentioning in a Mercury conversation as the adjacent team, not as the application.

**Also at Mercury:** an [Open Call for Founders / Founding Teams in Product Management](https://job-boards.greenhouse.io/mercury/jobs/6107075004) covering Command, CLI, and MCP, with no fixed level. A plausible side door if Interfaces turns on the people-management requirement.

---

### Evaluated and Below Threshold (Inbound, October 18, 2026)

| Role | Comp | Score | Why it falls short |
|------|------|-------|--------------------|
| [Senior PM, Code Translation & Developer Tooling, Code Metal](https://jobs.ashbyhq.com/code-metal/6d0b5b63-9fd0-4656-8b27-5b018913bf33) | $180K-$220K + equity, remote | 60 | Strong company ($125M Series B Feb 2026 led by Salesforce Ventures, ~$1.25B valuation, USAF/L3Harris/RTX/Toshiba customers, ex-Tableau CEO as President) and a real developer-tools PM role, but Senior level with a ceiling below current pay, compilers/embedded/defense domain, US citizenship for some assignments. Posted Sept 28, 2026. |
| PM, Waterfall-as-a-Service, FullEnrich (via American IT Systems) | $155K-$193K base, hybrid SF 3-4 days | 45 | Fails location and compensation outright. Recruiter claims $16M ARR; public record shows a $2M seed in Feb 2025 and seven-figure ARR. |
| Chromatic (via Twill) | not retained | n/a | Declined August 10, 2026 on compensation bands. |

### Targeted Company Checks (October 19-22, 2026)

Companies Daniel asked about by name. Boards read in full via their Ashby APIs.

| Company | Board on date checked | Nearest roles | Score | Verdict |
|---------|----------------------|---------------|-------|---------|
| Clerk (Oct 19) | 2 open: Brand Designer, GRC Engineer | Product Manager, Billing closed 6+ months ago | n/a | No product openings. Friend referral note drafted; general "join our team" link exists. |
| ElevenLabs (Oct 22) | 160 open; no PM for ElevenAgents or ElevenAPI | [Enterprise PM, ElevenCreative](https://jobs.ashbyhq.com/elevenlabs/934dbe9d-1c1f-4939-944a-6671469009db) (remote, Oct 7): owns enterprise revenue, pricing, packaging, admin/governance for creative tooling | 60 | Pricing and packaging ownership is a stated lever (Daniel has none); creative/marketing industry mismatch; the governance layer (permissions, spend controls) is the only overlap. No comp listed; ElevenLabs has no titles. |
| | | [PM, ElevenCreative Self-Serve](https://jobs.ashbyhq.com/elevenlabs/7389c057-3e25-4e7a-8a03-5e80f40a15a0) (remote, Oct 15) | 50 | Consumer and prosumer PLG: onboarding, activation, upgrade moments. |
| | | [Developer Advocate](https://jobs.ashbyhq.com/elevenlabs/969bbf7d-037c-4965-812e-442105ce58c1) (remote global, Oct 15): docs, example projects, conferences | 55 | Requires "a strong full-stack engineering skillset." Fails the no-solo-coding constraint. |
| | | [Product & Technical Communications](https://jobs.ashbyhq.com/elevenlabs/db7abc8d-67b1-4d64-a623-59be88d65fba) (US remote, Oct 13) | 55 | Comms role: launch narratives, security and safety incident comms, journalist relationships. Writing fits; media relationships and incident comms do not. |
| | | [Product Marketing, ElevenAPI](https://jobs.ashbyhq.com/elevenlabs/e062d169-7294-4125-bc7b-e3a821dcd620) (remote, Oct 12) | 60 | PMM, not PM. Closest to the API surface; GTM-materials record is the only direct evidence. |

| Micron (Oct 24) | 3,123 open worldwide; roughly 15 product-management roles, all semiconductor product-line management | [Principal Technical Product Manager, Data Center SSD](https://micron.wd1.myworkdayjobs.com/External/job/Folsom-CA/Principal-Technical-Product-Manager_JR114459) (Folsom/San Jose, Oct 20, $171K-$337K) | 40 | Requires SSD, NAND, ASIC, firmware depth and standards-body work (PCIe-SIG, OCP, JEDEC); on-site California. |
| | | [Staff DRAM Product Line Manager](https://micron.wd1.myworkdayjobs.com/External/job/Boise-ID---Main-Site/Staff-DRAM-Product-Line-Manager_JR112173) (Boise, Oct 19, $129K-$251K) | 35 | P&L, pricing, and supply strategy for embedded DRAM; "extensive semiconductor experience" required. |
| | | [Director, CMBU Product Management](https://micron.wd1.myworkdayjobs.com/External/job/San-Jose-CA/Director--CMBU-Product-Management_JR108248-1) (San Jose or Boise, Aug 19, $170K-$353K) | 40 | Leads a DRAM product-management team; 10+ years semiconductor required. |
| | | [Principal Product Marketing Manager, Cloud Memory](https://micron.wd1.myworkdayjobs.com/External/job/Boise-ID---Main-Site/Principal-Product-Marketing-Manager---Cloud-Memory_JR109594) (Boise, Aug 25, $141K-$319K) | 40 | PMM; requires HBM/DDR/LPDDR understanding. Asks for AI-agent fluency, the only overlap. |
| | | [Sr/Staff Product Owner, Smart Manufacturing & AI](https://micron.wd1.myworkdayjobs.com/External/job/Boise-ID---Main-Site/Senior-Product-Owner_JR98988-1) (Boise, Apr 29) | 30 | Requires 5+ years in process integration or process equipment engineering. |

Micron note: no software, API, or developer-platform product roles exist at Micron. Every PM role is hardware product-line management with semiconductor domain as a minimum qualification. Boise headquarters does not change the fit.

ElevenLabs note: the roles that would fit (PM for ElevenAgents telephony and integrations, PM for ElevenAPI) are not posted. ElevenAgents deploys voice agents over SIP, which is the Crux side of the same call. Also note that ElevenLabs is a plausible Crux experience provider; check for any partner relationship before approaching.

### Shared by Christina via Messages (Evaluated October 20, 2026)

| Role | Comp | Score | Why it falls short |
|------|------|-------|--------------------|
| Lead Product Manager, Hims & Hers (Indeed jk=a8b0afd75c28a862) | $200K-$235K, remote US | 55 | 0-to-1 "relationship-first" consumer health experience built on AI-native workflows; requires 3+ years owning consumer mobile products at scale, which the record does not have; consumer healthcare is an industry mismatch; band tops out below current pay; Indeed employer rating 2.6 |
| Sr. Product Manager, Provider Experience, Rula (Indeed jk=d5236b0dc4f43f18) | $180K-$221K, remote US | 45 | Expired on Indeed as of October 19; SMB SaaS tooling for therapists (AI note-writing, scheduling); Senior level, band below current pay, no API or platform component |

---

## Posted Within Last 90 Days (October 2025 - January 2026)

### 1. **Senior Product Manager** 🔥 **FIT SCORE: 90/100**
**Company:** Lightyear
**Location:** Remote (Fully Remote)
**Compensation:** $150,000 - $180,000 USD + competitive equity
**Posted:** November 19, 2025
**Link:** [Apply Here](https://lightyear.applytojob.com/apply/2ppez0KTrd/Senior-Product-Manager)

**Key Requirements:**
- 4+ years in enterprise/consumer software as PM or engineer
- Deep customer problem-space understanding
- Software development deployment familiarity
- **Bonus:** Telecom industry knowledge

**Fit Analysis:**
✅ **Exceptional telecom match** - Your Charter (ISP/network APIs) and Vonage/Ericsson (CPaaS) experience directly align with their telecom management software
✅ **Exceeds experience requirement** - 10+ years vs. 4+ required
✅ **Enterprise API expertise** - Perfect match for their platform serving Honeywell, Alo Yoga, Louis Vuitton
⚠️ **Compensation consideration** - Salary range ($150K-$180K) may be below market value for your Principal-level experience
✅ **Developer portal expertise** - Extensive experience creating developer portal content and self-service tools aligns with product needs

---

### 2. **Principal Product Manager - Developer Platform** 🔥 **FIT SCORE: 95/100**
**Company:** PagerDuty
**Location:** Remote (USA) - Preference for San Francisco, Atlanta, or Toronto
**Compensation:** $180,000 - $304,000 USD (base salary) + equity, bonus, and benefits
**Posted:** November 7, 2025
**Link:** [Apply Here](https://job-boards.greenhouse.io/pagerduty/jobs/5703257004)

**Key Requirements:**
- 5+ years in SaaS, enterprise software, or developer tools product management
- Deep knowledge of integration architecture, patterns, and platforms
- Hands-on experience designing RESTful APIs
- Strong customer communication and cross-functional leadership

**Fit Analysis:**
✅ **Perfect API platform experience** - Your REST API, SDK, and WebRTC platform work at Vonage/Ericsson directly matches
✅ **Strong leadership track record** - Mentored and onboarded team of 5 PMs, led cross-functional collaboration
✅ **Developer-first mindset** - Reduced support tickets 40% through improved documentation and self-service tooling at VoiceBase
✅ **Integration expertise** - Your work on video SDK integration across iOS, Android, Web, Windows, Mac, Linux demonstrates deep integration knowledge
✅ **Compensation alignment** - Upper range ($304K) appropriate for your Principal-level experience

---

### 3. **Staff Product Manager - Enterprise AI** **FIT SCORE: 85/100**
**Company:** Twilio
**Location:** Remote - US (excluding SF Bay Area)
**Compensation:**
- Colorado, Hawaii, Illinois, MD, MA, MN, VT, DC: $152,500 - $190,600
- NY, NJ, WA State, CA (outside Bay): $161,500 - $201,800
- San Francisco Bay Area: $179,400 - $224,200
**Posted:** October 2, 2025
**Application Deadline:** January 15, 2026
**Link:** [Apply Here](https://job-boards.greenhouse.io/twilio/jobs/7296104)

**Fit Analysis:**
✅ **Twilio alumni** - Previous experience at Twilio (SendGrid Labs) 2017-2020 provides cultural fit and company knowledge
✅ **Platform experience** - Led video platform serving millions aligns with enterprise AI platform scale
✅ **Developer experience** - Strong track record building developer-facing products
✅ **AI/ML experience** - GitHub shows active work with Claude/OpenAI APIs (GrocerySelector automation), Core ML (Hearth), and LLM prompt engineering experiments; VoiceBase Speech-to-Text platform experience
✅ **Communications platform expertise** - Deep CPaaS and cloud communications background

---

### 4. **Principal AI Product Manager - PLG** **FIT SCORE: 82/100**
**Company:** Zoom
**Location:** Seattle, WA (Hybrid)
**Compensation:** $171,800 - $375,900 USD + bonus and equity
**Application Deadline:** January 13, 2026
**Link:** [Apply Here](https://careers.zoom.us/jobs/principal-ai-product-manager-plg-seattle-washington-united-states)

**Key Requirements:**
- 8+ years product management experience
- Deep expertise in enterprise software, AI technologies, and SaaS monetization
- Proven track record with generative AI applications and PLG scaling
- Product analytics and A/B testing experience with developer-focused products
- Understanding of AI/ML pricing models

**Fit Analysis:**
✅ **Exceeds experience requirement** - 10+ years vs. 8+ required at Principal level
✅ **Developer API alignment** - Job focuses on developer APIs and PLG, matching your API platform expertise
✅ **Developer relations experience** - Your cross-functional work with Developer Relations teams at Vonage aligns with this role
✅ **Enterprise software background** - Strong track record with enterprise SaaS platforms
✅ **Cross-functional leadership** - Experience coordinating across engineering, marketing, and GTM teams
✅ **AI/LLM experience** - GitHub demonstrates active work with Claude API, OpenAI APIs (GrocerySelector), Core ML (Hearth), prompt engineering, and VoiceBase Speech-to-Text platform
✅ **Communications platform fit** - Zoom's video platform aligns perfectly with your WebRTC and video SDK expertise
⚠️ **Generative AI products** - While you have LLM integration experience, less evidence of shipping generative AI products at scale
⚠️ **Monetization/pricing strategy** - Limited explicit SaaS monetization or pricing model experience shown on resume
⚠️ **PLG specialization** - While you've built developer-focused products, explicit PLG experience not highlighted on resume

---

## Recently Posted & Still Active

### 5. **Product Manager, API** ❌ **CLOSED** (was FIT SCORE: 95/100)
**Company:** Anthropic
**Location:** San Francisco, CA | New York City, NY
**Compensation:** $305,000 - $385,000 USD + equity and benefits
**Posted:** September 29, 2025
**Status:** ❌ Closed as of October 13, 2026 (link redirects to job board). See "Anthropic — Current Openings" above for replacements.
**Link:** [Apply Here](https://job-boards.greenhouse.io/anthropic/jobs/4936029008)

**Key Highlights:**
- Drive development and adoption of API platform across enterprise organizations
- Own end-to-end enterprise API experience
- Build scalable, secure, and compliant solutions
- 5+ years of product management experience with significant API background
- Visa sponsorship available

**Fit Analysis:**
✅ **Enterprise API expertise** - Led API products used by millions across Vonage/Ericsson platform
✅ **Scalability proven** - Led product through 10x growth while maintaining platform reliability
✅ **Developer adoption success** - Drove $3M revenue capture through developer migration strategies
✅ **End-to-end ownership** - Owned video SDK product strategy across multiple platforms
✅ **Premium compensation** - $305K-$385K range appropriate for your experience level
✅ **AI/LLM expertise** - GitHub shows active Claude API experimentation and integration work; built automation using Claude/OpenAI APIs (GrocerySelector); VoiceBase Speech-to-Text platform experience; hands-on with Anthropic's own API

---

### 6. **Senior Product Manager, API Collaboration** 🔥 **FIT SCORE: 95/100**
**Company:** Postman
**Location:** San Francisco, CA (hybrid - west coast options available)
**Compensation:** $160,000 - $230,000 USD + competitive equity package
**Posted:** September 18, 2025
**Link:** [Apply Here](https://job-boards.greenhouse.io/postman/jobs/7331454003)

**Key Highlights:**
- World's leading API platform used by 40M+ developers
- Own strategy, roadmap, and evolution of APIs
- Strong technical background with API design/integration experience

**Fit Analysis:**
✅ **Perfect API documentation match** - Extensive experience developing REST API documentation, SDKs, and interactive demos
✅ **Developer tools expertise** - Proficient with Postman and API documentation platforms (listed on resume)
✅ **API evolution leadership** - Advocated for API evolution to improve developer experience at Vonage
✅ **Developer community focus** - Created developer portal content and self-service analytics
✅ **Scale experience** - Worked with platforms serving 40M+ users (matches Postman's developer base)

---

### 7. **Senior Staff Product Manager - API & Developer Experience** 🔥 **FIT SCORE: 98/100**
**Company:** Plaid
**Location:** San Francisco | New York
**Compensation:** $226,800 - $400,000 USD (Zone 1) + equity
**Posted:** June 3, 2025
**Link:** [Apply Here](https://plaid.com/careers/openings/product/san-francisco/senior-staff-product-manager-api-developer-experience/)

**Key Highlights:**
- Shape the developer experience for Plaid's API platform
- 8+ years of product management experience
- Deep empathy for developers and understanding of their challenges
- Familiarity with modern API design practices

**Fit Analysis:**
✅ **Nearly perfect match** - 10+ years experience exceeds 8+ requirement at Senior Staff level
✅ **Developer empathy demonstrated** - Reduced support tickets 40% through improved documentation and self-service tooling
✅ **API design mastery** - Hands-on experience with REST APIs, WebRTC, modern API design across multiple companies
✅ **Developer experience focus** - Advocated for API evolution specifically to improve developer experience and ease of integration
✅ **Premium compensation alignment** - $226K-$400K range matches your Principal/Senior Staff level
✅ **Financial services relevance** - Your work on enterprise platforms for major clients translates well to fintech

---

## Recently Closed (For Reference)

### **Staff Product Manager, Integrations and APIs**
**Company:** Checkr
**Location:** San Francisco, CA | Denver, CO (Hybrid)
**Compensation:**
- San Francisco: $207,000 - $244,000 USD
- Denver: $176,000 - $207,000 USD
**Posted:** October 30, 2025
**Closed:** December 24, 2025
**Status:** ❌ No longer accepting applications

---

## Additional Resources

### Job Search Platforms
- [LinkedIn - API Product Manager Jobs](https://www.linkedin.com/jobs/api-product-manager-jobs) (9,000+ listings)
- [Indeed - API Product Manager](https://www.indeed.com/q-api-product-manager-jobs.html) (720+ listings)
- [Wellfound - Product Manager Jobs](https://wellfound.com/role/product-manager)

### Companies Actively Hiring for API/Platform PM Roles
- Anthropic (multiple API platform roles)
- Twilio (Developer Experience, Platform)
- PagerDuty (Developer Platform)
- Postman (API Collaboration)
- Plaid (API & Developer Experience)
- Stripe
- Kong
- Calendly

---

## Notes

**Verification Status:** All links verified as of January 7, 2026
**Salary Market Range:** $150,000 - $400,000 USD depending on level, location, and company
**Common Requirements:**
- 5-10+ years product management experience
- Deep API platform and developer tools expertise
- Strong technical fluency with RESTful APIs, microservices
- Cross-functional leadership and stakeholder management
- Developer-first mindset and empathy for developer experience
