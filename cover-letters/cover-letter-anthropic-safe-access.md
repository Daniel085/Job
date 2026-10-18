# Cover Letter - Anthropic Product Manager, Safe Access

Daniel O'Rorke
408-768-4570 | daniel@ororke.com
[linkedin.com/in/danielororke](https://linkedin.com/in/danielororke) | [developer.alianza.com](https://developer.alianza.com/docs)

---

Dear Anthropic Hiring Team,

The Safe Access role describes a product I have spent the last year building at a smaller scale: a centralized access system that every other product depends on, used by first-party systems, direct API customers, and third parties, and shipped from zero while the rest of the company waited on it.

At Alianza I own the developer-facing surface of Crux, the control plane through which AI experiences get access to live phone calls and voice data on more than a thousand operators' telephone networks. Crux sits in the call path. It decides which AI may reach which phone number, applies identity and policy before any AI is invoked, plays and logs consent in the network, then hands the call to a virtual agent or streams the media to a post-call intelligence partner. It is an access system by construction, and the stakes are the same as yours: get it wrong and a third party hears a conversation it should not. I designed the developer-facing access model from scratch and shipped it as the Crux API 1.0.0 in September 2026. The primitives are small on purpose. An eligibility check runs before any access is granted. A per-account Connection carries an explicit ACTIVE/INACTIVE switch that gates all traffic. An Assignment scopes access to an account, a user, or a single phone number, and the platform enforces that a number cannot be claimed by two agents. Authorization is OAuth 2.0 with five least-privilege scopes split by read and manage, client-credentials for service calls, PKCE for user-context calls, and private_key_jwt with two active keys so a partner can rotate credentials with zero downtime. The same APIs serve third-party AI experience providers such as SoundHound and Revmo, the operators whose networks carry the calls, and Alianza's own provisioning systems. I also set the API standards every engineering team builds against and review their proposals, which is the part of this job description about building new programs on shared primitives rather than forking them.

Identity and verification are not new ground for me. At Vonage and Ericsson I led CAMARA Number Verification, a cellular identity API, end to end from proof of concept to commercial product, uniting a team that spanned Vonage, Ericsson, and mobile network operators. Before that I owned Vonage's multi-tenant video platform through 650% telehealth growth in the first six weeks of the pandemic and shipped Video Express, a 0-to-1 SDK, from prototype to GA in under nine months. At Aerohive I co-invented two patents on credential management and device onboarding.

Why this role: scaling access to Claude safely sits on the critical path of every launch, and I have been the person on that path. I am a daily Claude Code user, I operate an LLM-built documentation system in production, and I have written publicly about where these systems should and should not be trusted. I would bring that same judgment to deciding how access is granted, verified, and revoked.

I would welcome a conversation about what the first six months of this product need.

Daniel O'Rorke
