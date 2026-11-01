# Product Manager, Identity & Access Management — Stripe

**Link:** https://stripe.com/jobs/search?gh_jid=8165137 (canonical: https://stripe.com/careers/listing/product-manager-identity-access-management/8165137; Greenhouse 8165137, department "Developer Platform - PM")
**Location:** Greenhouse location "US-Remote, US-Chicago." Structured data on the page: jobLocationType TELECOMMUTE, applicant location requirement United States, offices New York, Seattle, South San Francisco HQ. Stripe's page asks candidates to "apply for roles that match the location where you currently live or plan to live."
**Compensation:** "The annual US base salary range for this role is $178,600 - $268,000." Stripe uses a single "Product Manager" title; level is set in the interview process.
**Posted:** August 28, 2026 (first published); refreshed October 29, 2026. 65 days old on November 1, five days past the 60-day window.
**Fit Score:** 76/100
**Found by:** Discovery search re-run, November 1, 2026 (identity and access slice)

## About the team (quoted)

"IAM is the nerve center of Stripe. We control how millions of businesses grant access to their account, including employees, AI agents, apps, and API integrations, across the Dashboard, API, CLI, and MCP. We're also a platform team, building the unified, fine-grained permissions model that every product at Stripe builds on."

"AI agents are changing how businesses operate, and how they get authorized, governed, and secured is being defined right now—largely by us. We're tackling challenging and unsolved problems for real businesses, like how to model agents when they blur the line between acting on behalf of a human vs. standalone principals, or how to authorize entire agent workflows rather than step-by-step actions. We're collaborating directly with the frontier AI labs on the evolution of MCP, new identity protocols, and agent integrations. We build for solo founders and Fortune 500s alike."

## What you'll do

"You'll set the vision and drive the roadmap for how every principal, human, agent, or app, gets access to a Stripe account. You'll do it by talking directly to the founders, admins, and developers who use it."

- Design the experience of granting access, everywhere: signing up, inviting a teammate, creating an API key, authorizing an agent or a third-party app
- Design for agents as a new principal within Stripe: how they authenticate, what they're allowed to do, how businesses stay in control, "including approvals and human-in-the-loop checkpoints for actions involving real money"
- Drive least privilege, made easy: custom roles, smart permission defaults, permission recommendations based on real API usage
- "Push toward a world without secrets. Make secretless authentication (Workload Identity Federation) the default way developers integrate with Stripe"
- Partner across Dashboard, API Platform, Security, Payments, and Money Movement

## Minimum requirements

- 5+ years in PM, shipping platform or infrastructure products that other teams build on
- Background in security, identity, auth, or developer platforms, or serious curiosity about the space
- A habit of talking to users to find the real problem, not the reported one
- Technical fluency to go deep with engineers on authorization and authentication design
- A bias toward experimentation over big-bang launches
- Comfort setting direction in a space that's still being invented, across teams you don't manage

No preferred-qualifications list is published.

## Notes for tailoring

- This is the Safe Access story: the Anthropic Safe Access resume (`applications/anthropic-safe-access/`) is the starting point, with the attribution rules from October 22 kept intact. Daniel owns the developer-facing surface of Crux and publishes its OAuth 2.0 (private_key_jwt, key rotation) authentication guide; he did not design the access model or the authentication.
- Crux applies identity, entitlements, policy, and consent in the network before any AI is invoked (product fact). The posting's "agents as a new principal" and "human-in-the-loop checkpoints" are the same problem on the credential side. Describe Crux's behavior as a product fact; describe Daniel's role as owning and exposing the surface.
- Built an MCP server for the Crux API ("built" tier, confirmed October 28, 2026). Stripe names MCP as one of the four access surfaces.
- Enhanced Number Verification and the two credential-management patents are the identity evidence; Auth0 SDK work on GitHub is adjacent.
- Gaps to state plainly: never owned a first-party account or authentication system at scale; Workload Identity Federation and secretless auth are practitioner-level identity topics not on the record; fintech is new.
- Level and pay: flat title with a $178,600 - $268,000 band. Ask the recruiter which level the role is calibrated at before investing in tailoring; Profile.md's lateral rule applies if the offer reaches current base.
