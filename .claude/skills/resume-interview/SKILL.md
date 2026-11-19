---
name: resume-interview
description: Interview the candidate the way a good headhunter would, one question at a time, to turn a past role into confirmed evidence (what changed, how it was measured, what was theirs) and fold it into Profile.md. Use when the user says "interview me about X," "let's do the resume interview," "dig into my time at X," or before tailoring when a posting's requirements have no evidence in Profile.md. Two modes: deep (one role, end to end) and targeted (the gaps one posting exposes). Never invents a number, a verb, or a scope; nothing reaches Profile.md without the candidate's confirmation.
---

# Resume interview

Built November 2026. The ceiling on the resumes is missing evidence, not phrasing: many bullets have no result because Profile.md has none. This skill gets the evidence from the one person who has it, in a way that keeps the attribution rules in CLAUDE.md intact.

## Before the first question

1. Read Profile.md in full, and the CLAUDE.md attribution rules and terminology standards.
2. Pick the mode.
   - **Deep:** one role, end to end. Do this when a role's bullets lack results or a correction is pending (pending claims in a package often point here).
   - **Targeted:** one posting. List its requirements, mark each as backed, thin, or absent in Profile.md, and interview only on thin and absent ones. Five to eight questions.
3. Open the notes file `interviews/{role-or-company}-{YYYY-MM-DD}.md` (private, like `network/`). If one exists for the role, resume from its "Open threads" list instead of starting over.
4. Write down, before asking anything, what Profile.md already says about the role and what it explicitly rules out ("Not on the record" lines). Never re-ask a settled point unless the posting needs more detail on it.

## How to ask

- **One question per message.** Short. No preamble, no compliments, no restating the answer back at length.
- **Broad, then narrow.** Open with the role itself ("Walk me through what you owned at X and who you reported to"), then drill down on each thing named.
- **The drill-down ladder,** one rung per question, for each accomplishment:
  1. What was the situation or problem, and why did it matter then?
  2. What did you do, yourself? What did the team, the product, or someone else do?
  3. What changed because of it?
  4. How did you know? What number, date, or before-and-after would your manager cite?
  5. Who could confirm it? Is it public, internal, or confidential?
- **Numbers.** Ask for the number, then accept a range or an order of magnitude and label it ("roughly 20, the candidate's estimate"). Never offer a number for them to agree to, and never round up. "Not measured" is a valid answer; record it.
- **Verbs.** Ask what they did in plain words ("did you write it, review it, or own the decision?") and record the tier: built or designed (sole), helped guide or co-led (shared), documented or presented (exposed). Never suggest a stronger verb.
- **Scope.** Separate product facts from the candidate's role every time ("Is that something the product did, or something you decided?").
- **Confidential and unreleased work.** Ask what can be said in public, and record the approved public phrasing (for example, "designed the call control API (not yet public)").
- **Follow the energy.** If an answer opens something better than the planned next question, follow it and add the planned question to Open threads.
- **Stop points.** About every eight questions, or when a topic closes, show the claim cards gathered so far and ask whether to continue, pause, or confirm.

## Claim cards

Each piece of evidence becomes a card in the notes file:

```markdown
### C3. Push and SMS channel launch
- **What:** one sentence, in the candidate's words where possible
- **Role:** built / helped guide / documented (quote the answer that set the tier)
- **Result:** exact / approximate (their estimate) / not measured, with the figure
- **Evidence:** who could confirm; public, internal, or confidential; links
- **Public wording:** how it may be said externally, if it differs
- **Status:** draft / confirmed / rejected
```

"Not on the record" answers get a card too, with status `confirmed` and the line to add to Profile.md's ruled-out notes. They prevent the same overreach later.

## Folding into Profile.md

- Show the exact Profile.md edits (section, old line, new line) and wait for a yes, per the Dynamic Profile Updates workflow in CLAUDE.md.
- Write confirmed cards into the role's section with the date and "(candidate, {date})" as the source, the way existing approved wording is recorded.
- If the interview changes a claim in a live package (pending claims in `applications/*/claims.json`), say which claims it settles or changes. Do not edit the package's claims yourself; the candidate decides them in the claims review tool.
- Commit with a message that names the role and the Profile.md sections changed.

## Notes file layout

```markdown
# Interview: {role}, {date}
Mode: deep | targeted ({posting})
## Already on the record
## Ruled out (from Profile.md)
## Transcript (questions and answers, verbatim or close)
## Claim cards
## Open threads
```

The notes name real people and confidential details. They stay in this private repository and are never copied to the public template.
