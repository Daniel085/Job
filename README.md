# A job search you run with Claude Code

This repository runs a senior product-management job search end to end with Claude Code: finding roles, scoring them, tailoring a resume and cover letter for each one, checking every claim before anything leaves the building, filling application forms, and keeping track of who you have talked to. It is not an app. It is a folder structure, a set of rules Claude reads before it works (`CLAUDE.md`), a handful of small scripts, and a set of skills for the jobs that need a browser.

It was built for one real search and used daily through it. The design choices below come from what went wrong along the way, and the most important one is this: **nothing about you goes into an application unless it traces to one document you have approved.** The most common failure in AI-written application material is attribution, where the model reads a product's public documentation and writes as if you built the product. Most of the machinery here exists to stop that.

This repository is the public template. Your search lives in your own **private** copy, made with **Use this template** on GitHub; your profile, tracker, packages, and outreach never come back here. Everything in `examples/` describes a fictional candidate.

---

## Contents

- [What it does](#what-it-does)
- [Start here](#start-here)
- [How it works](#how-it-works)
- [What you need](#what-you-need)
- [Getting started](#getting-started)
- [A week of running it](#a-week-of-running-it)
- [The pieces in detail](#the-pieces-in-detail)
- [The rules that keep claims honest](#the-rules-that-keep-claims-honest)
- [Command reference](#command-reference)
- [Repository layout](#repository-layout)
- [Privacy and safety](#privacy-and-safety)
- [Troubleshooting](#troubleshooting)
- [What running it taught us](#what-running-it-taught-us)
- [Contributing](#contributing)

---

## What it does

**Knows who you are, accurately**
- Builds `Profile.md` from your resume and LinkedIn text, then interviews you until it is right. Every later fit score, resume, letter, and message draws only on this file.
- Records exact approved wording, the verbs you are entitled to, and the things you have explicitly not done, so tailoring cannot drift.
- Interviews you like a good headhunter (the `resume-interview` skill) to turn past roles into measured evidence: what changed, how you knew, what was yours.

**Finds roles**
- Sweeps company job boards directly through the public Greenhouse, Ashby, and Lever APIs (about 570 board names in the default list, of which roughly 190 currently answer).
- Pulls a weekly feed of postings from Workday, iCIMS, and about 30 other systems through MobiusEngine Jobs Data, run in a Docker sandbox.
- Searches the a16z speedrun list, LinkedIn's saved jobs and standing searches, and aggregator boards like JobAiro.
- Takes roles shared by friends and family on a more generous bar.

**Decides what is worth your time**
- Scores every posting from 0 to 100 against your profile, with written strengths and gaps.
- Keeps every role it evaluated, including the rejected ones and why, so nothing is scored twice.

**Builds the application**
- Writes a two-page resume and a one-page cover letter tailored to each posting, plus a checklist with the form fields filled in and the decisions you need to make.
- Lists every inferred or newly worded claim, and refuses to render PDFs until you have approved or edited each one in a local review page that shows the claim highlighted in the document.
- Lints every document for phrases you have corrected before.

**Helps you apply**
- Reads a Greenhouse form's questions before you open it and drafts the answers.
- Fills the common fields of Greenhouse, Ashby, Lever, and Workday applications in the Claude desktop app's browser, stops before every page advances, and never touches disclosures, uploads, consents, or Submit.

**Works your network**
- Maps who you know at a target company and the best path to the hiring manager.
- Drafts short outreach messages for your approval, sends only the exact text you approve, and logs every message and reply.
- Reviews your email and LinkedIn messages for anything that needs an answer.

---

## Start here

| If you want to | Read |
|---|---|
| Understand the system in ten minutes | This README, sections 1 to 4 |
| Set up your own search | [`setup/GETTING-STARTED.md`](setup/GETTING-STARTED.md) |
| Know what to say to Claude | [`docs/Claude-User-Guide.md`](docs/Claude-User-Guide.md) |
| Understand scoring and where postings come from | [`docs/AI-Assistant-Job-Search.md`](docs/AI-Assistant-Job-Search.md) |
| Use LinkedIn without getting your account restricted | [`docs/LinkedIn-Workflow.md`](docs/LinkedIn-Workflow.md) |
| Find referral paths | [`docs/Network-Lead-Research.md`](docs/Network-Lead-Research.md) |
| Understand form filling and the autofill tools we rejected | [`docs/Form-Fill-Design.md`](docs/Form-Fill-Design.md) |
| See the rules Claude follows | [`CLAUDE.md`](CLAUDE.md) |
| See a complete package for a fictional candidate | [`examples/`](examples/) |

---

## How it works

```
                          +---------------------------+
                          |        Profile.md         |   the only source of facts about you
                          |  approved wording, verbs, |   (grows as interviews and claim
                          |  ruled-out claims         |    reviews confirm new evidence)
                          +-------------+-------------+
                                        |
    sources                             v
  +----------------+        +-----------------------+        +-------------------------+
  | board sweep    |        |   score 0-100         |        | jobs/Similar-Job-       |
  | MobiusEngine   +------->|   strengths and gaps  +------->|   Postings.md (tracker) |
  | LinkedIn, aggr.|        |   75 = the bar        |        |                         |
  | friends, family|        +-----------------------+        +------------+------------+
  +----------------+                                                      |
                                                       you choose a role  |
                                                                          v
  +-------------------------+     +-------------------------+     +------------------------+
  | applications/<role>/    |     | claims review page      |     | PDFs (2-page resume,   |
  |  resume, letter,        +---->| approve / edit / reject +---->|  1-page letter),       |
  |  checklist, claims.json |     | each claim in context   |     |  page counts checked   |
  +-------------------------+     +-------------------------+     +-----------+------------+
                                                                              |
           +-------------------------------+--------------------------------+
           v                               v                                v
  +------------------+          +---------------------+          +---------------------+
  | form pre-flight  |          | form filling skills |          | network leads and   |
  | (questions and   |          | (stop before every  |          | outreach drafts     |
  |  draft answers)  |          |  page; you submit)  |          | (you approve text)  |
  +------------------+          +---------------------+          +----------+----------+
                                                                            |
                                                                            v
                                                              +-----------------------+
                                                              | outreach/log.md       |
                                                              | inbox and LinkedIn    |
                                                              | follow-up reviews     |
                                                              +-----------------------+
```

The loop closes back to the top. When a package's claims are approved, the new wording goes into `Profile.md` (with your OK), so the next package starts from a better record. When an interview uncovers a number, it becomes a confirmed claim card and then a profile line. When a claim is corrected, a pattern goes into the linter so the old phrasing cannot come back.

Three principles run through everything:

1. **One source of truth.** A claim about your role must trace to `Profile.md`. If it is not there, it is drafted, marked, and listed for you to confirm.
2. **You approve anything that leaves.** Claude drafts messages, fills forms, and builds documents. You approve the final text of every message, decide every claim, and press every Submit.
3. **Read from the source.** Aggregators find roles; scores and pay come from the employer's own posting.

---

## What you need

### Included in this repository

| Piece | What it gives you |
|---|---|
| `CLAUDE.md` | The rules: scoring, attribution, writing style, outreach, privacy |
| `templates/` and `examples/` | Profile, resume, letter, and seed-job templates, and one complete fictional package |
| `scripts/` | Board sweep, MobiusEngine pull, PDF rendering, claims linter, form pre-flight, LinkedIn reconciliation, the claims review page |
| `.claude/skills/` | Five skills for browser and interview work (listed below) |
| `docs/` | Method and workflow guides |

### What you supply

| Requirement | Needed for | Notes |
|---|---|---|
| **Claude Code** | Everything | The **desktop app** is recommended: its built-in browser runs the LinkedIn, network, and form-filling skills, and you sign in there once. The terminal and web versions handle everything else. |
| **Python 3** | All scripts | The macOS system Python (3.9) is enough. No packages to install; scripts fall back to the standard library. |
| **Google Chrome or Chromium** | PDFs and the review page's Render button | Set `CHROME=/path/to/chrome` if it is not in the usual place. No pandoc, no poppler. |
| **Your resume and LinkedIn text** | Building `Profile.md` | PDF or HTML resume; the LinkedIn text copied from your profile page. |
| **Two or three seed postings** | The first discovery pass | Roles that represent what you want. |
| A LinkedIn account | LinkedIn skills, outreach | Signed in once in the desktop app's browser. |
| Docker (optional) | MobiusEngine feed | Runs the Treg CLI in a sandbox. Colima works on macOS. |
| A MobiusEngine Jobs key (optional) | MobiusEngine feed | Free credit covers about ten weekly pulls; you add funds only if you choose. |
| Gmail connector (optional) | Inbox reviews | Connected in Claude; read-only use unless you approve a send. |

---

## Getting started

### Path 1: See it work in two minutes

Run the claims review page against the fictional example package:

```bash
python3 -I scripts/claims-review/server.py 8765 examples/applications
```

Open http://127.0.0.1:8765. You will see the example resume and letter with each claim highlighted. Approve, edit, or reject them with A, E, and R, and press Render to produce both PDFs. Nothing in `examples/` is real.

### Path 2: Set up your own search (about an hour)

1. On GitHub, choose **Use this template** on this repository, and make the new repository **private**.
2. Clone it and put your inputs in `setup/inputs/` (the folder is git-ignored):
   ```
   setup/inputs/resume.pdf            or resume.html
   setup/inputs/linkedin-profile.txt
   setup/inputs/additional-info.txt   optional
   ```
3. Open the folder in Claude Code and say:
   > Help me set up this job search repository. I've placed my resume and LinkedIn profile in setup/inputs/.
4. Claude drafts `Profile.md`, asks about pay, location, priorities, seniority, and whether you have formally managed people, and shows you the draft. Correct it until it is right.
5. Give it your seed postings. It shows you the pattern it found and asks before searching.
6. Pick a role and say "Build the [Company] [Role] package."

[`setup/GETTING-STARTED.md`](setup/GETTING-STARTED.md) has every step with the exact prompts and timings.

### Path 3: The full desktop setup

After Path 2, in the Claude desktop app:

1. **Sign in to LinkedIn** in the app's browser pane once. The skills reuse the session and never sign in for you.
2. **Connect Gmail** if you want inbox reviews.
3. **Create `applications/application-profile.json`** from `templates/application-profile-template.json`: contact details, work history with LinkedIn's month dates, and standard answers. Every form-filling skill reads it.
4. **Optional: the MobiusEngine feed.** Build the sandbox, sign in to Treg, and connect your key inside it:
   ```bash
   docker build -t treg-sandbox:0.30.0 scripts/treg-sandbox
   ```
   ```bash
   docker run --rm -it --name treg-sandbox -v treg-sandbox-home:/home/treg treg-sandbox:0.30.0 bash
   ```
   Inside the container, run `treg login`, then `treg connections connect --provider mobiusengine-jobs` and paste the key when asked. The key never touches the repository.

---

## A week of running it

| When | Say or run | What happens |
|---|---|---|
| Monday | "Run this week's round" | Board sweep, MobiusEngine pull, speedrun, LinkedIn searches; every new posting scored and recorded |
| Monday | "Review email and LinkedIn for follow-ups" | A list of what needs an answer, with drafts; nothing sent until you approve the text |
| As needed | "Build the [Company] [Role] package" | Resume, letter, checklist, claims list |
| As needed | Open the claims review page | Approve, edit, or reject each claim; render PDFs |
| As needed | "Who do I know at [Company]?" | A ranked lead map and drafted outreach |
| As needed | "Fill the application" | Form pre-flight, then the form filled up to Submit |
| After each submission | "Submitted [Company]" | Checklist, tracker status, and pipeline updated, then committed |
| Monthly | "Interview me about [role]" | New evidence for the profile, one question at a time |

---

## The pieces in detail

### Profile.md

The single source of truth. Beyond the usual sections (roles, achievements, skills, education, pay, location), it holds three things that make tailoring safe:

- **Approved wording**, quoted, with the date you approved it. Tailoring reuses it instead of paraphrasing.
- **Verb tiers** for each piece of work: built or designed (yours alone), helped guide (shared), documented or presented (exposed).
- **Ruled-out claims**: things you have explicitly not done, so a later draft cannot quietly add them.

Claude changes `Profile.md` only after showing you the exact edit and getting a yes.

### Discovery sources

| Source | How it is read | Covers | Script or skill |
|---|---|---|---|
| Company boards | Public JSON APIs | Greenhouse, Ashby, Lever; the companies listed in the script (about 190 boards answer) | `scripts/sweep-boards.py` |
| MobiusEngine Jobs Data | Paid API through Treg, in Docker | Workday, iCIMS, SmartRecruiters, Recruitee, and about 30 more | `scripts/mobius-search.py` |
| a16z speedrun | Its public job list | Portfolio startups | read through a fetch tool |
| LinkedIn | Your saved jobs and standing searches, read in the browser | Anything posted there | `linkedin-search` skill |
| JobAiro | Browser search only (its terms forbid scraping) | About 540,000 ATS postings | by hand; new companies go into the sweep list |
| Friends and family | You paste the link | Anything | scored on a more open bar |

Every source finds roles; the score and pay always come from the employer's own posting. When an aggregator surfaces a company the sweep does not know, its board slug goes into `sweep-boards.py`, and from then on that company is read directly.

### Scoring and the tracker

Each posting is scored from zero up: direct technology experience, years beyond the requirement, domain match, similar companies, and relevant leadership add points; missing required skills, too few years, an industry mismatch, and location constraints subtract. **75 is the bar** for a full entry and a package. Pay is judged against two numbers you set (acceptable and preferred base). Roles shared by friends or family are packaged at 65 or above if you accept the location.

`jobs/Similar-Job-Postings.md` keeps:
- a dated status block at the top: what is submitted, prepared, waiting on you;
- a full entry for every role at the bar, with requirements and a fit analysis in "Strength, category" and "Gap, category" form;
- a below-threshold table for every role that fell short, with the score and the reason.

### Application packages

One folder per role in `applications/<company-role>/`:

| File | What it is |
|---|---|
| `resume-<role>.html` | Two pages, built from `applications/generic/resume-designed.html`, summary and bullets reordered and reworded for the posting |
| `cover-letter-<role>.md` | One page: the posting's need and your matching record, a second experience, how you work, what you have not done, and a plain closing |
| `application-checklist.md` | Posting facts, form fields pre-filled, decisions to make, the approved reason-for-leaving wording, and the claims list |
| `claims.json` | Every inferred, combined, or newly worded claim, with the exact text and file of every place it appears |
| `form-answers.md` | Optional: the form's questions and drafted answers |
| `<Name>-Resume-<Role>.pdf`, `<Name>-Cover-Letter-<Role>.pdf` | Rendered only after every claim is decided |

Closed roles' folders are deleted, not archived; they stay in git history and regenerate from the profile in minutes.

### The claims review page

`scripts/claims-review/` is a local web page (Python standard library, port 8765, localhost only) that shows each package's claims next to the resume and letter, with the claim highlighted where it appears.

| Key | Action |
|---|---|
| J / K | Next / previous claim |
| A | Approve |
| E | Edit (the edit is written into the source file, so what you approve is what renders) |
| R | Reject (render stays blocked until the text is removed) |
| U | Back to pending |
| Cmd+Enter | Save an edit |

Render produces both PDFs with Chrome and checks the page counts. It is refused while any claim is pending.

### Rendering and linting

- `scripts/build-resume.sh in.html out.pdf` fails unless the resume is exactly two pages.
- `scripts/build-letter.sh in.md out.pdf` fails unless the letter is one page.
- Both call `scripts/render.py`, the same renderer as the review page. On macOS it stages files in a temp folder so Chrome can read them.
- `scripts/lint-claims.sh [files]` greps for every phrase that has been corrected once and exits 1 on a hit. Add a pattern every time you correct a phrase.

### Skills

Skills are instruction sets Claude loads when a task calls for them. The browser skills run in the Claude desktop app.

| Skill | Say | What it does | Never does |
|---|---|---|---|
| `linkedin-search` | "Check LinkedIn" | Pulls saved jobs and standing searches, finds each on the employer's board, scores, records | Scrape in bulk |
| `network-leads` | "Who do I know at X?" | Maps referral and intro paths, ranks them, drafts outreach in `network/leads-<company>.md` | Send anything |
| `resume-interview` | "Interview me about X" | One question at a time, turns a role or a posting's gaps into claim cards | Suggest a number or a stronger verb |
| `ats-apply` | "Fill the application" | Fills Greenhouse, Ashby, and Lever forms from your profile and approved answers | Upload, answer disclosures, consent, or submit |
| `workday-apply` | "Fill out Workday" | Fills Workday page by page, stopping before each Save and Continue | Sign in, upload, answer disclosures, or submit |

### Form filling

1. **Pre-flight.** `python3 -I scripts/form-questions.py <greenhouse-url> applications/<pkg>` reads the form through Greenhouse's public API and writes `form-answers.md`. Each question gets an owner: `PROFILE` (answered from your profile), `DRAFT` (free text that goes through claims review), or the candidate (uploads, consents, export-control questions, anything company-specific).
2. **Fill.** The `ats-apply` or `workday-apply` skill fills from approved answers only, refuses protected fields, and stops for your review.
3. **Submit.** You read the page and press Submit yourself.

Before filling, the skill checks the posting for an AI-use policy and stops if the employer forbids assisted filling. `docs/Form-Fill-Design.md` explains why third-party autofill extensions were assessed and not adopted.

### Network and outreach

- `network/leads-<company>.md`: ranked paths to a hiring manager, with facts kept apart from inferences.
- `outreach/log.md`: every message sent, with date, person, channel, summary, status, and next step. Append only.

The outreach rules in `CLAUDE.md` are strict: show the full draft, send only the exact approved text, keep claims exact ("we overlapped at Acme," not "we worked together"), one concrete hook and one ask, and never navigate a browser tab that holds an unsent draft.

### Interviews

`interviews/<role>-<date>.md` holds a resume interview's transcript, claim cards, and open threads. Each card records what happened, your role with its verb tier, the result (exact, approximate, or not measured), who could confirm it, and how it may be said in public. Confirmed cards go into `Profile.md` with your OK.

---

## The rules that keep claims honest

From `CLAUDE.md`, in short:

1. A claim about your role must trace to `Profile.md`. Otherwise it is drafted, marked, and listed for you to confirm.
2. Use the weakest verb the evidence supports. When unsure, go one tier down.
3. Never upgrade a verb while tailoring.
4. Public product facts stay product facts. "The platform applies consent in the network" is fine; "I designed consent in the network" is not, unless the profile says so.
5. Every new material ends with a numbered claims list, mirrored in `claims.json`, and no PDF is rendered until each claim is decided.
6. Run the linter before sending or committing.
7. Inherited text is not verified text. When a line is challenged, fix it everywhere it appears.

There is also a pass for phrasing that reads as machine-written: "the shape of," contrasts of the form "it's not X, it's Y," rhetorical triplets, and closing lines that restate the posting back at the company.

---

## Command reference

Run scripts from the repository root. Scripts that use Chrome, Docker, or the network need the Claude Code Bash sandbox turned off.

| Command | What it does |
|---|---|
| `python3 -I scripts/sweep-boards.py out.json` | Sweeps the Greenhouse, Ashby, and Lever boards listed in the script |
| `python3 -I scripts/mobius-search.py out.json` | Weekly MobiusEngine pull: senior remote PM titles, US, last 7 days (`--days`, `--max-jobs`, `--count-only`) |
| `python3 -I scripts/linkedin-reconcile.py ids.txt` | Which LinkedIn job ids are already in the tracker |
| `python3 -I scripts/form-questions.py <url> applications/<pkg>` | Greenhouse form pre-flight |
| `python3 -I scripts/claims-review/server.py [port] [dir]` | The claims review page (default port 8765, `applications/`) |
| `scripts/build-resume.sh in.html out.pdf` | Render a resume; fails unless two pages |
| `scripts/build-letter.sh in.md out.pdf` | Render a letter; fails unless one page |
| `scripts/lint-claims.sh [files]` | Check for corrected phrases; exits 1 on a hit |

---

## Repository layout

```
README.md                    this file
CLAUDE.md                    the rules Claude follows here
Profile.md                   the single source of truth about you (created during setup)

setup/                       first-run guide and the git-ignored inputs folder
templates/                   profile, resume, letter, seed-jobs, and application-profile templates
examples/                    a complete package for a fictional candidate

jobs/
  Similar-Job-Postings.md    the tracker: status block, full entries, below-threshold tables
  Seed-Jobs.md               seed postings, patterns, and the log of discovery runs (created as you go)
  descriptions/              saved posting text

applications/
  application-profile.json   form-filling data, built from the template during setup
  generic/                   the base resume every tailored resume starts from
  <company-role>/            one package per role

network/                     lead maps per company (private: names real people)
outreach/log.md              every message sent (private)
interviews/                  resume-interview notes (private)

scripts/
  sweep-boards.py            board sweep (Greenhouse, Ashby, Lever)
  mobius-search.py           MobiusEngine weekly pull
  treg-sandbox/              Dockerfile for the Treg CLI sandbox
  linkedin-reconcile.py      LinkedIn ids against the tracker
  form-questions.py          Greenhouse form pre-flight
  claims-review/             the claims review page
  render.py                  the PDF renderer behind the build scripts and the review page
  build-resume.sh            two-page resume render
  build-letter.sh            one-page letter render
  lint-claims.sh             corrected-phrase linter

.claude/
  launch.json                attaches the desktop browser pane to the review page
  skills/                    linkedin-search, network-leads, resume-interview, ats-apply, workday-apply

docs/                        method and workflow guides
```

---

## Privacy and safety

**Private by design.** Your copy holds contact details, pay expectations, the companies you are talking to, and the names of real people. Keep it private. `network/`, `outreach/`, and `interviews/` name real people; `setup/inputs/` is git-ignored. MobiusEngine data is licensed for personal use only and stays out of any public repository.

**What Claude will not do here:**
- send a message, accept an invitation, apply, post, or spend an InMail credit without your approval of the final text;
- enter passwords, API keys, or payment details anywhere (you sign in and paste keys yourself);
- answer voluntary disclosures, tick consent boxes, upload files, or press Submit on an application;
- solve a CAPTCHA;
- add anything to `Profile.md` you have not confirmed;
- script a site whose terms forbid it (JobAiro is searched by hand for this reason).

**Third-party tools are contained.** The Treg CLI, which the MobiusEngine feed requires, runs inside a Docker container with no access to your files, telemetry off, and without the skill and MCP server its installer would otherwise add to every coding agent on the machine.

---

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| PDF render fails or Chrome cannot read the file | Run with the Bash sandbox off. On macOS, `render.py` stages files in a temp folder because privacy settings keep Chrome out of `~/Documents`. |
| `ModuleNotFoundError: requests` | Not a problem; current scripts fall back to the standard library. Pull the latest scripts. |
| Render button refused in the review page | A claim is still pending, or a rejected claim's text is still in a document. |
| Resume renders at three pages | Tighten the longest bullets; the build script refuses anything but two. |
| `treg: ... rejected that token (HTTP 503)` | MobiusEngine's API is down, not a bad key. Its error gives the expected recovery time; reconnect afterwards. |
| `treg: command not found` | You are on your Mac, not in the sandbox. Run Treg commands in the container's shell. |
| LinkedIn pages come back empty | Sign in once in the desktop app's browser pane; the skills reuse that session. |
| A Greenhouse form field reverts after filling | The form ignores programmatic input; the skill falls back to typing it. Note the field in the skill file. |
| The same posting keeps being re-scored | It is missing from the below-threshold table. Add the row. |

---

## What running it taught us

- **Keep the below-threshold table.** It looks like clutter, and it is why the second and later sweeps take a fraction of the time of the first.
- **Most of the ceiling on a resume is missing evidence, not phrasing.** A bullet without a result usually has none because nobody wrote the number down. Interview for it rather than polishing words.
- **Answer the claims list seriously, every time.** The errors it catches are small in wording and large in consequence, and most come from your own old resumes, not the model.
- **Name your gaps in the letter.** A gap you name is a conversation; a gap the interviewer finds is a mark against you.
- **Aggregators find roles; employers' pages settle them.** Pay and "remote" fields from aggregators were wrong often enough to matter.
- **A referral changes the odds more than any rewrite.** Map the network for every role worth applying to, and ask early.
- **Record submissions and replies the day they happen.** Three weeks in, you will not remember which letter went where.
- **When a role ends, change the dates and the tense everywhere, and keep the reason out of letters.** Approved reason-for-leaving wording lives in the profile and in every checklist, for forms and interviews only.

---

## Contributing

Improvements to the scripts, skills, templates, or rules are welcome as pull requests. Personal materials never belong here; the fictional example exists so the structure can be shown without anyone's real record.
