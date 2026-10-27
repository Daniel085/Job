# Seed Jobs for Automated Discovery

*Created: October 27, 2026*

These three roles are the seeds for the pattern-based search run on October 27, 2026. They are the roles in `Similar-Job-Postings.md` that scored at or near threshold on verified claims after the October 22 attribution corrections. Full fit analyses live in the tracker; this file records only what the search was built from.

## Seeds

### S1. Anthropic, Product Manager, Multi-Cloud Growth - Google (85/100)
- **Link:** https://job-boards.greenhouse.io/anthropic/jobs/5153924008
- **Status:** Submitted October 23, 2026
- **Location:** San Francisco, hybrid (25% in office)
- **Base band:** $305,000 - $460,000
- **Surface:** Enterprise API strategy for the Platform Org (APIs, self-serve developer experience, multi-cloud integrations, agentic infrastructure); roadmap across authentication, rate limiting, compliance, SDKs; shipping through a hyperscaler partner channel
- **Bar:** 10+ years developer-facing software, 5+ years PM, owned a revenue or channel number

### S2. Anthropic, Product Manager, Safe Access (78/100)
- **Link:** https://job-boards.greenhouse.io/anthropic/jobs/5428898008
- **Status:** Application started October 23, 2026; confirm submitted
- **Location:** San Francisco or New York, hybrid (25% in office)
- **Base band:** $305,000 - $385,000
- **Surface:** Centralized identity, verification, and access system; access APIs used by platforms, resellers, and internal services; 0-to-1 on the critical path of every model launch
- **Bar:** Owned a developer platform, identity, authorization, or access-management product end to end; 8+ years PM preferred

### S3. Mercury, Head of Product, Interfaces (76/100, closed October 23, 2026)
- **Link:** https://job-boards.greenhouse.io/mercury/jobs/6213000004
- **Status:** Closed before application; kept as a pattern seed
- **Location:** SF, NYC, Portland, or remote within the US or Canada
- **Base band:** $289,700 - $362,100
- **Surface:** Dashboard, Mobile, Command (AI surface), the public API, and the MCP server; agent interactions, permissions, and customer control over consequential actions
- **Bar:** 10+ years PM including 5+ leading PMs; hands-on AI product experience with evidence of evaluation

## Pattern extracted

| Dimension | Pattern | Search filter applied |
|-----------|---------|-----------------------|
| Titles | Product Manager (Principal-scope at Anthropic), Head of Product | Principal, Staff, Lead, Head of, Director, Group PM; Senior only if the band reaches $280K |
| Seniority | 8-10+ years PM; two of three ask for ownership of a platform end to end | Same |
| Surface | APIs and developer platform (3 of 3); identity, verification, and access (2 of 3); AI agents, MCP, or agentic infrastructure (3 of 3) | Required one of: API or developer platform, identity/access, agent platform, network APIs |
| Company | Revenue-generating, well capitalized (Anthropic; Mercury at roughly $650M annualized revenue, profitable) | Real revenue; no pre-seed or seed-stage companies |
| Base band | $290K - $460K, floor of bands $290K-$305K | Band top at or above $280K, or no band stated ($250K for telecom, which pays lower) |
| Location | 2 of 3 SF-hybrid; 1 of 3 remote US | Remote within the US required; hybrid only if remote is explicitly an option (Daniel is Boise-based and the SF relocation floor is roughly $455K base) |
| Posting age | All open within 60 days of evaluation | Posted or updated on or after August 28, 2026 |

## Search slices run

1. Identity, authentication, authorization, and access-management companies
2. Developer platform, API, and developer-tooling companies
3. AI model, agent-platform, and voice-AI companies
4. Communications, CPaaS, telecom-software, and network-API companies

Each slice checked company job boards directly (Greenhouse, Ashby, Lever, Workday APIs) rather than relying on aggregator snippets, because Indeed and LinkedIn block fetches from this environment. Results and scores are in `Similar-Job-Postings.md` under "Discovery Search, October 27, 2026."
