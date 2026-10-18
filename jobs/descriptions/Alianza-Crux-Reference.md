# Alianza Crux — Reference for Application Materials

*Compiled October 18, 2026 from Alianza's press release, product pages, and trade press. Use this, not memory, when describing Daniel's current product.*

## One-sentence definition

Crux is Alianza's orchestration and intelligence control plane that sits in the call path of operators' telephone networks and is the connector through which AI experiences interact with live phone conversations and voice data on existing phone numbers, with identity, consent, and policy applied in the network before any AI is invoked.

## What it does on each call (Light Reading, September 2026)

1. Tags a phone line as AI-ready.
2. On each call, checks whether the line has an "experience" attached.
3. Plays a consent and privacy announcement in the network and logs that the caller stayed on.
4. Hands the call to an AI agent (AI-handled), lets an agent assist a human in real time (AI-assisted), or copies the media to an intelligence partner (post-call).
5. The experience attaches to the existing number, so businesses do not forward or port numbers.

## Core capabilities (press release)

- **Multi-experience orchestration:** several intelligences can join one live conversation, across applications and models, within regulatory, privacy, security, and sovereignty requirements.
- **Network-native context:** identity, call state, entitlements, history, and policy applied before intelligence is invoked.
- **Trust, consent, and sovereignty controls:** operators govern how communications data is processed, where it may travel, and which intelligences may participate.
- **Conversation-speed performance:** low-latency participation in real-time conversation.
- **Open developer access:** connectors and APIs (developer.alianza.com) so operators and experience providers can build, integrate, and distribute experiences.

## Components (product page)

- **Orchestrator:** cloud-hosted call routing, media aggregation, policy engine; subscriber onboarding and auditable authorization.
- **Gateway:** directs signaling and media between operator infrastructure and the Orchestrator; returns calls with caller ID preserved.
- **Connector:** works with infrastructure control planes and user databases to determine which directory numbers may subscribe to AI experiences.
- **Citadel:** fully air-gapped, on-premises deployment; sits between IMS core, media resources, and AI services; adds or removes AI services mid-call via REST or SIP INFO; uses iFC policies for entitlement.

## The parties

- **Operators (CSPs):** keep control of connectivity, call handling, governance, and the customer relationship; monetize experiences by revenue share, referral, or white label (Fierce, Light Reading).
- **Experience providers (AI developers):** integrate once and reach every operator on the platform. Launch partners quoted: SoundHound (AI-handled), Revmo AI (AI phone agents, outcome-priced), MiaRec and Dubber (post-conversation intelligence).
- **Businesses:** activate an AI experience on the phone number they already have.

## Positioning and dates

- Framing: Connected Communications (connect calls) to Cloud Communications (deliver services) to Cognitive Communications (understand and act on conversations). Closes the "Telecom Intelligence Gap."
- Controlled availability: September 9, 2026. Commercial availability: planned first half of 2027.
- Alianza: 1,000+ service providers in 80+ countries. CEO Brian Beutler; Chief Product and Technology Officer Dag Peak.
- Study cited: HyperFRAME Research with Alianza found nearly 44% of operators losing subscribers to AI-enabled rivals.

## How this maps to the developer portal

developer.alianza.com documents the experience-provider side: Experience (your integration), Experience Connection (per-account link with ACTIVE/INACTIVE gate), Experience Assignment (scope to account, user, or phone number), eligibility check, OAuth 2.0 scopes, SIPREC for post-call, SIP for virtual agent, webhooks for provisioning events.

## Sources

- https://www.alianza.com/whats-new/alianza-crux-powering-cognitive-communications/
- https://www.alianza.com/products/alianza-crux
- https://www.alianza.com/products/crux-citadel/
- https://www.lightreading.com/telecoms-software/alianza-s-crux-protects-the-phone-number-as-telcos-brace-for-an-experience-provider-wave
- https://www.fierce-network.com/wireless/alianza-launches-crux-platform-help-telcos-monetize-ai-voice
