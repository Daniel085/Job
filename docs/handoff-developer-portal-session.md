# Handoff: context for the developer.alianza.com portal session

*Prepared October 18, 2026 by the job-search session (Daniel085/Job, branch `claude/epic-carson-r8qipx`). Paste or attach this file in the session where the portal was built.*

## Why this file exists

Daniel is running a job search from the `Daniel085/Job` repository. The portal at developer.alianza.com is now his strongest public work sample, and it is cited in application materials for Anthropic's **Product Manager, Safe Access** role (identity, verification, and access system). The portal session should (1) confirm the claims below are accurate, (2) know which review findings came out of an outside read, and (3) supply metrics if any exist.

## Where Daniel stands (as of October 18, 2026)

- Principal Product Manager, APIs & Developer Platforms at Alianza, full-time, remote, since January 2026. Owns the developer-facing surface of Crux: public APIs, events and webhooks, developer.alianza.com.
- Crux, per Alianza's September 9, 2026 press release: the orchestration and intelligence control plane for "Cognitive Communications." It sits in the call path of operators' telephone networks and is the connector through which AI experiences interact with live phone conversations and voice data on existing numbers. It coordinates network infrastructure, AI, applications, identity, consent, and policy around each call. Launch experience providers: SoundHound, Revmo, MiaRec, Dubber. Controlled availability from September 9, 2026; commercial availability planned 1H 2027. Earlier drafts in the job-search session described Crux as "a cloud communications platform carriers resell," which was wrong and has been corrected everywhere.
- Previously Lead PM at Charter (Apr 2025 to Jan 2026, CAMARA network APIs), Expert PM at Vonage/Ericsson (2020 to 2025, Video API and CAMARA Number Verification), Senior PM at Twilio SendGrid Labs and VoiceBase, PM at Aerohive and Yahoo.
- Location: Boise metropolitan area. Open to remote and on-site.
- Target roles: Principal / Senior Staff API and developer-platform PM, $226K to $400K.
- Active Anthropic targets, scored against `Profile.md`: Multi-Cloud Growth - Google (85), Safe Access (85), New Markets and Monetization (82), Developer Relations (78). Resume and cover letter for Safe Access are in `resumes/resume-anthropic-safe-access.html` and `cover-letters/cover-letter-anthropic-safe-access.md`.

## Claims about the portal now in application materials

These were read off the public site on October 18, 2026. Please confirm or correct each one. Anything marked *inferred* was not stated on the site.

| Claim | Source page | Status |
|-------|-----------|--------|
| Crux API 1.0.0 public release, September 2026 | /docs/resources/changelog | Stated |
| OAuth 2.0 with client-credentials and authorization-code + PKCE grants | /docs/authentication/overview | Stated |
| Five scopes split by read and manage (assignability:check, connections:read/manage, assignments:read/manage) | /docs/authentication/overview | Stated. The conventions page also lists `users:manage`, so the count may be six. |
| private_key_jwt recommended; up to two active public keys for zero-downtime rotation | /docs/authentication/overview | Stated |
| Eligibility check before access; Connection with ACTIVE/INACTIVE gate; Assignment scoped to ACCOUNT, USER, or PHONE_NUMBER | /docs/concepts/overview, /docs/reference/data-model | Stated |
| A phone number cannot be on two AGENT experiences | /docs/reference/errors | Stated |
| APIs used by third-party Experience Providers, reseller service providers, and Alianza's own provisioning | /docs landing, webhooks event names | Confirmed by Daniel, October 18, 2026 |
| Daniel built developer.alianza.com; helped guide the structure of the Crux API; sets API standards and reviews proposals jointly with Architecture. The Crux platform and its access model were designed before he joined; he documents the access model, he did not design it. | Daniel, October 22, 2026 | Corrected. Earlier materials credited him with designing the OAuth access model; that was wrong and has been removed. |
| AI-built documentation system generates reference docs from the API definition and states gaps plainly | LinkedIn summary; endpoint pages carry "gaps" notes | Daniel's own statement, consistent with the site |
| Launch coordinated across engineering, operations, and go-to-market; Experience Providers integrated in sandbox during early access | /docs/webhooks/delivery-and-troubleshooting mentions "Experience Provider early access" | Confirmed by Daniel, October 18, 2026 |
| Runbooks: recovering from desynchronization, seed-then-stream user counts | /docs/webhooks/* | Stated |

## Outside review of the portal (what a first-time reader saw)

Read on October 18, 2026 across 16 pages. Written up for Daniel in the job-search session.

**Strengths worth keeping exactly as they are**
- The three-resource model (Experience, Connection, Assignment) and five-step lifecycle, with the two journeys differing only at steps 3 and 5.
- "What you need from Alianza" as a pre-flight checklist.
- Quickstarts that end with a real SIPREC or SIP INVITE in about ten minutes.
- The operational runbooks (desync recovery, user counting with sets rather than counters, `updatedAt` comparison, deletion reconciliation).
- Candor: webhooks not yet authenticated, desync procedure not fully supported yet, no endpoint for Experience metadata, known issues with real failure modes.
- Design rationale on endpoint pages (why `telephoneNumber` is a query parameter; look up the existing connection on 409 and on ambiguous 5xx).
- Conventions: cursor paging with no total count, trace IDs on errors, RFC 9457, rate-limit guidance about retry storms, deprecation paths for `tn` and `CONNECTED`.

**Findings to consider**
1. The root `https://developer.alianza.com/` renders a bare "Alianza API" shell with a logo and no links. The real front door is `/docs`. Redirect the root.
2. Quickstart step 3 ("complete the Authorization Code + PKCE flow end to end") shows no request. It is the one step that can take an hour in a ten-minute quickstart. A sandbox shortcut or copy-paste block would help.
3. Drift between hand-written and generated pages:
   - `/docs/authentication/overview` lists the `:read` scopes; `/docs/reference/conventions` omits them and adds `users:manage`.
   - `/docs/reference/conventions` caps `pageSize` at 100 as of 1.0.0; `/docs/webhooks/tracking-user-counts` says to use the maximum page size of 200 for list-users. May be two different APIs, but the reader cannot tell.
4. Webhook retry schedule is unstated (count, spacing, exhaustion behavior). Developers size dead-letter handling from that.
5. No diagrams. The lifecycle and two journeys would land faster as one picture on `/docs/concepts/overview`.
6. Minor: the create-connection page does not say what happens if both `telephoneNumber` and `tn` are supplied, nor the removal date for `tn`.

## Metrics the job search would use if they exist

Any of these would go into `Profile.md` and the Safe Access materials:
- Number of endpoints or APIs documented; number of Experience Providers integrated or in early access.
- Time-to-first-call or quickstart completion data.
- Support deflection or ticket volume before and after the portal.
- Engineering hours saved by the generated documentation, or doc coverage percentage.
- Any uptime, error-rate, or latency figure Daniel is allowed to cite.

## How to hand information back

Reply in the job-search session with corrections or numbers, or edit `Profile.md` directly under "Developer Platform (Alianza, current)" in Key Achievements. `Profile.md` is the single source of truth for every resume, cover letter, and fit score in that repository.
