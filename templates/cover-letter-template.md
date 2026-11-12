# Cover letter template

The letter is short, specific, and honest about gaps. Four paragraphs and a one-line close, under 350 words. The complete example is `examples/applications/northwind-platform-pm/cover-letter-northwind-platform-pm.md`.

## File layout

Save as `applications/<company-role>/cover-letter-<company-role>.md`.

```markdown
# Cover Letter - [Company], [Role Title]

[Your Name]
[phone] | [email]
[linkedin.com/in/you](https://linkedin.com/in/you) | [github.com/you](https://github.com/you)
Work sample: [a public link to something you built, if you have one]

---

Dear [Company] Hiring Team,

[Paragraph 1]

[Paragraph 2]

[Paragraph 3]

[Paragraph 4]

I am available now and would welcome a conversation about [the specific place you would start].

[Your Name]

---

*Claims to confirm (reviewed by the candidate, deleted before sending):*

1. [Anything inferred, combined, or newly worded]
2. ...
```

The contact header uses single line breaks; `scripts/build-letter.sh` keeps them so the header does not wrap into one line.

## The four paragraphs

**Paragraph 1: the posting and the matching line of your record.** One or two sentences. Name what the posting is asking for, in its own words where that is natural, and state the one thing in your record that answers it. No warm-up, no "I am writing to express my interest."

> Your posting describes a platform team that owns the public API every Northwind product exposes and wants a PM who has taken a partner-only API to self-serve. I did that at Ledgerline over the last three years.

**Paragraph 2: the most relevant experience, with numbers and the right verb.** Three to five sentences. What the product was, what you owned, what happened. Say what was there before you arrived and what you built, so the reader cannot mistake the product's history for yours. Use the weakest verb the evidence supports: built, then helped guide, then documented.

> At Ledgerline I owned the developer-facing surface of a payments-reconciliation platform used by 2,400 finance teams: the public REST API, webhooks and events, SDKs in four languages, and the developer portal. The reconciliation engine was designed before I joined; what I built is how developers reach it. We moved from 60 partner integrations to 900 active API customers in fourteen months.

**Paragraph 3: a second experience, or how you work.** Two to four sentences. Either a second role that answers a second requirement, or a short account of your method with one concrete instance. Prototyping, discovery, a migration handled without a cliff: whichever the posting cares about.

**Paragraph 4: what you have not done.** One to three sentences, plain. If the posting asks for something your record lacks, say so here, with the nearest thing you have done and without apology. This paragraph is the one most readers remember, and the one most letters omit.

> What I have not done: owned pricing for a usage-based API beyond one launch, or managed a PM team. I have onboarded and mentored two PMs, which is not the same thing.

**The close.** One line: available now, and the specific place you would start. Not enthusiasm, not a restatement of the posting.

## Rules

- Every claim about your role traces to `Profile.md`. If it is not there, it goes in the claims list, not in the letter as fact.
- Never upgrade a verb while tailoring. "Led" in the profile does not become "built from scratch" here.
- Product facts stay product facts. What the platform does is context; what you did is the claim.
- Do not state a departure or its reason. The resume's dates carry it; approved wording lives in the profile for forms and interviews.
- Do not name a former employer's customers or partners unless you have confirmed they are public and you are comfortable naming them to this company. "Launch partners" and "enterprise customers" are usually enough.
- No "mentored" dressed as "managed," and no "managed" when the record says "mentored."
- Strip phrasing that reads as machine-written before sending: "the shape of," "it's not X, it's Y," "I should say plainly," rhetorical triplets, and a closing line that restates the posting back at the company.

## Length and tone

Three hundred to three hundred fifty words. Short declarative sentences. First person, active voice, no superlatives. The reader is a hiring manager or recruiter skimming thirty of these; the letter should give them the one thing they need to decide to call you, and no reason to doubt it.

## Before sending

- Answer every numbered claim. Corrections are applied everywhere the phrase appears, not only in this letter.
- Delete the claims block.
- Run `scripts/lint-claims.sh`.
- Build the PDF with `scripts/build-letter.sh <letter.md> <out.pdf>` and confirm one page.
- Record the submission in the tracker when it is in.
