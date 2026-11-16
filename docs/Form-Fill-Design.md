# Application Form Filling

*November 2026.* How this template fills job application forms, and why it does not rely on third-party autofill extensions.

## The approach

Fill forms in the Claude desktop app's built-in browser, from one stored profile, with every free-text answer reviewed before it is typed. Three pieces:

**1. Pre-flight: read the form before opening it (`scripts/form-questions.py`).** Greenhouse's public board API returns every application question with its field name, type, options, and whether it is required (`?questions=true`). The script writes `applications/{package}/form-answers.md`, one row per question, each with an owner:

- `PROFILE`: answered from `applications/application-profile.json` (contact details, links, work authorization, sponsorship, how-heard). Check it against the resume being uploaded.
- `DRAFT`: free text. Draft it from Profile.md and add it to the package's `claims.json`, so it goes through the claims review like the resume and letter.
- `USER`: uploads, consents, export-control and residency questions, anything company-specific. Voluntary disclosures are always yours and are not listed.

```bash
python3 -I scripts/form-questions.py https://job-boards.greenhouse.io/<company>/jobs/<id> applications/<package>
```

Ashby, Lever, and Workday have no public questions endpoint. For those, the form is read in the browser on the first pass and the same table is written by hand.

**2. Apply skills.**
- `.claude/skills/ats-apply` covers Greenhouse, Ashby, and Lever with one in-page helper (`__ats`). The helper lists fields, fills by field name or label, refuses protected and already-filled fields, and prints a review table.
- `.claude/skills/workday-apply` stays separate because Workday spans several pages.

Both skills fill from `form-answers.md` only after every DRAFT row is approved, and share these rules:
- Stop for review before the form advances or is submitted.
- Find buttons by label, never by DOM position.
- The user does sign-in, uploads, voluntary disclosures, consents, and the final Submit.
- Before filling, check the posting and form for an AI-use policy, and stop if it forbids assisted filling. Some employers ask applicants not to use AI on the form; others ask them to acknowledge a policy.

**3. Later, a review UI.** The claims review tool (`scripts/claims-review/`) is the natural place to approve `form-answers.md` rows next to the resume and letter claims. Not built.

## Third-party autofill extensions

Two were assessed in November 2026, from their own pages and privacy policies.

**JobAiro (jobairo.com) and its ApplyAssist extension.**
- **The board:** aggregates postings from company hiring systems (Greenhouse, Lever, Ashby, and others), removes duplicates and filled roles, and links to the employer's original post. It is free to browse. It has no usable search API, so treat it as a browser source for companies outside `scripts/sweep-boards.py`'s slug lists.
- **ApplyAssist (free Chrome extension), behavior that matches this template's rules:**
  - The profile lives in `chrome.storage.local`, with no account, backend, or telemetry.
  - Race, gender, veteran, disability, attestation, and signature fields are always skipped.
  - It never submits, does not store or upload resume files, and writes no AI answers.
  - It supports Greenhouse, Lever, Ashby, Gem, and BambooHR, but not Workday.
- **Caveats:** it runs in Chrome, not the built-in browser; its source is not public; the team is small. A reasonable fallback if you apply from Chrome. Keep its saved answers to text you have already approved.

**Jobaro (jobaro.io).** Not recommended:
- Its AI writes free-text answers from your CV, outside the claims review.
- The CV and profile are stored on its servers, and the privacy policy names no LLM provider and no retention period for profile data.
- Its pages do not say which systems it supports or whether it stops before submitting.

Generic extensions that write AI answers have the same problem: answers about your experience should trace to Profile.md and pass review. The useful idea, answering from one stored profile, is what `application-profile.json` already does.

## Profile fields forms often ask for

Greenhouse forms often ask for these. Add approved values to `application-profile.json` if you want them filled:
- City and state ("Location (City)").
- An export-control residency question (citizen or resident of embargoed countries).
- "How did you hear" wording that matches Greenhouse's list ("Careers Website").
