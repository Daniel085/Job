# A job search you run with Claude Code

I built this repository to run my own search for product roles, and then cleaned it up so it is portable. It is not an app. It is a folder structure, a set of rules that Claude Code reads before it works, a few scripts, and a worked example. Everything in `examples/` describes a fictional candidate; there is no real person's data on this branch.

The short version of how it works:

1. You give Claude your resume and LinkedIn text. It drafts a profile document and asks you questions until the profile is right. That file, `Profile.md`, becomes the only source Claude is allowed to draw on when it writes about you.
2. You give it two or three postings you like. It extracts what they have in common, sweeps company job boards for similar roles, scores each one against your profile, and keeps a tracker of everything it looked at, including the ones it rejected and why.
3. For each role you decide to pursue, it builds a package: a two-page resume tailored to the posting, a short cover letter, and a checklist with the form fields filled in. Every package ends with a list of claims for you to confirm before anything is sent.
4. As you create application materials, Claude asks more about you where it relates to those roles as a good recruiter would. That goes into profile.md and helps refine the job search suggestions.

The most common failure in AI-drafted application material is attribution: the model reads a phrase or public docs and writes as if you built the product. The rules in `CLAUDE.md` are mostly about preventing that, and the "claims to confirm" step exists because the rules alone are not enough.

## What you need

- Claude Code, in the terminal, the desktop app, or the web.
- Your current resume as a PDF or HTML file, and the text of your LinkedIn profile.
- Two or three job postings that represent what you want.
- For rendering PDFs: pandoc, a Chromium or Chrome binary, and poppler-utils for `pdfinfo`. The scripts tell you what is missing.

## Getting started

Fork or clone the repository, then make a branch for your own search and keep `main` clean. That way you can pull improvements to the template later without merging your personal files into it.

```
git checkout -b search/your-name
```

Put your inputs in `setup/inputs/`. The folder is git-ignored, so your resume and LinkedIn text stay on your machine:

```
setup/inputs/resume.pdf          (or resume.html)
setup/inputs/linkedin-profile.txt
setup/inputs/additional-info.txt (optional)
```

Then open Claude Code in the repository and say:

> Help me set up this job search repository. I've placed my resume and LinkedIn profile in setup/inputs/.

Claude drafts `Profile.md`, asks about compensation, location, priorities, seniority, and whether you have formally managed people, and shows you the draft for corrections. When you approve it, give it your seed postings and it runs the first discovery pass. The whole setup takes most people under an hour. `setup/GETTING-STARTED.md` walks through every step with the exact prompts.

## How the pieces fit together

```
Profile.md                       the single source of truth about you
  |
  v
jobs/Similar-Job-Postings.md     every role evaluated, scored, and sorted
  |
  v
applications/<company-role>/     one folder per role you pursue
    resume-<company-role>.html       two pages, built from your base resume
    cover-letter-<company-role>.md   four short paragraphs
    application-checklist.md         form fields, decisions, claims to confirm
    <Name>-Resume-<Role>.pdf         rendered copies
    <Name>-Cover-Letter-<Role>.pdf
```

Nothing goes into a resume or letter that cannot be traced back to `Profile.md`. If Claude needs a fact that is not there, it asks you, shows you the exact line it wants to add, and adds it only when you say yes. The profile gets more complete as the search goes on, and every later package benefits.

## The repository layout

```
README.md                  this file
CLAUDE.md                  the rules Claude Code follows in this repository
Profile.md                 your profile (created during setup; not on main)

setup/
  GETTING-STARTED.md       step-by-step setup with the prompts to use
  inputs/                  where your resume and LinkedIn text go (git-ignored)

templates/
  Profile-template.md      the sections your profile needs, with guidance
  resume-template-guide.md how the two-page HTML resume works and what to change
  cover-letter-template.md the letter structure and what to leave out
  seed-jobs-template.md    the seed-jobs file and the pattern analysis

examples/
  Profile-example.md       a complete profile for a fictional candidate
  applications/northwind-platform-pm/
                           one complete package: resume, letter, checklist
  jobs/Similar-Job-Postings.md
                           a small tracker showing the format

scripts/
  sweep-boards.py          pulls PM postings from Greenhouse, Ashby, and Lever boards
  lint-claims.sh           greps your materials for phrases you have already corrected
  build-resume.sh          renders a resume to PDF and fails if it is not two pages
  build-letter.sh          renders a cover letter to a one-page PDF

docs/
  AI-Assistant-Job-Search.md   the scoring method in detail
  Claude-User-Guide.md         how to talk to Claude in this repository
  LinkedIn-Workflow.md         pulling the LinkedIn tracker and searches
  Network-Lead-Research.md     finding referral paths in your network

.claude/skills/
  linkedin-search/             the LinkedIn pull, as a skill (desktop app)
  network-leads/               the network map, as a skill (desktop app)

network/                   lead maps per company (private branch only)
outreach/                  the outreach log (private branch only)

applications/              your packages (created as you go)
jobs/                      your tracker, seed jobs, and saved descriptions
```

## Scoring

Every posting gets a score from 0 to 100, built up from zero. Direct experience with the technologies the posting names adds the most. Exceeding the years required, matching the domain, having worked at a similar company, and relevant leadership each add a little. Missing a required skill, falling short on experience, an industry mismatch, and a location constraint each subtract. Seventy-five is the bar for a full entry and a package. Everything below the bar still gets a row in a table with the score and the reason, so the same posting is never re-evaluated by accident on the next sweep. That table turned out to be the biggest time saver over a long search.

Two rules bend the bar on purpose. Compensation is judged against two numbers you set, an acceptable base and a preferred base: a band that reaches the preferred number costs nothing, a band between the two takes a small deduction, and a band under the acceptable number is excluded. And a role sent to you by a friend or family member is packaged at 65 or above if you accept its location, because a personal referral is worth more than a board find.

`docs/AI-Assistant-Job-Search.md` has the full method with a worked example.

## Finding roles

The first pass uses your seed postings. Claude extracts the common titles, technologies, company types, pay bands, seniority, and work arrangements, shows you the pattern, and asks before it searches. The search itself has two parts. `scripts/sweep-boards.py` calls the public JSON endpoints of Greenhouse, Ashby, and Lever for every company slug you list in it, and writes out every product-management posting with its description, location, date, and any dollar figures it finds. For companies on other applicant-tracking systems, Claude uses web search and aggregator boards. Postings older than sixty days, under your pay floor, or at the wrong level are dropped before scoring.

Each run is logged in `jobs/Seed-Jobs.md` with its date, filters, sources, and results, and the next run is scheduled two to three weeks out. Re-running is a one-line request.

## Building a package

When you decide to pursue a role, say so:

> Build the Northwind Staff PM package.

Claude reads the posting and your profile, then writes three files. The resume starts from your base resume in `applications/generic/` and changes the summary and the most recent role's description to answer the posting, reordering bullets so the matching evidence comes first. It keeps the two-page layout; the build script refuses anything else. The letter is four short paragraphs: what the posting asks for and the matching line of your record, a second experience, how you work, and what you have not done. It closes on availability rather than enthusiasm. The checklist holds the posting facts, the form fields pre-filled from your profile, the decisions you should make before submitting, and the claims to confirm.

Then you answer the claims. A typical reply looks like:

> 1 and 2 yes. 3: it was take-share from competing platforms, not a legacy migration. 4 cut.

Claude applies the corrections everywhere the phrase appears, records any new wording in your profile, adds a pattern to the linter so the old phrasing cannot come back, and only then builds the PDFs. When you have submitted, say so and the tracker is updated.

## Keeping claims honest

Three things work together here.

The attribution rules in `CLAUDE.md` say that a claim about your role must trace to `Profile.md`, that the verb must be the weakest one the evidence supports (built, then helped guide, then documented), that a verb is never upgraded while tailoring, and that public product facts stay product facts. Management claims are exact: mentored is not managed, and when a posting asks for people management the letter says plainly whether you have done it.

The "claims to confirm" list at the end of every new material catches what the rules miss. Anything inferred, combined, or newly worded is listed with a number, and nothing is sent until you have answered each one.

`scripts/lint-claims.sh` is the memory. Every time you correct a phrase, a pattern goes in, and the script runs before anything is committed or sent. It ships with a handful of generic patterns; the useful ones will be yours.

There is also a short pass for phrasing that reads as machine-written. The rules name the habits to strip: "the shape of," contrasts of the form "it's not X, it's Y," rhetorical triplets, and closing lines that restate the posting back at the company.

## LinkedIn and your network

Two skills run in the Claude desktop app, where Claude has a browser pane you sign in to. `/linkedin-search` pulls your LinkedIn jobs tracker and the standing searches, finds each role on the employer's own board, scores it, and records it. `/network-leads <company>` maps who in your network can refer or introduce you at a target company, ranks the paths, and drafts a message for you to approve. Neither sends anything on its own, and both read pages one at a time, the way a person would; LinkedIn does not allow automated scraping, and a restricted account would cost you more than any shortcut saves. The methods are written out in `docs/LinkedIn-Workflow.md` and `docs/Network-Lead-Research.md`. The lead files and the outreach log name real people, so they belong on your private branch, never on a published template.

## Scripts

| Command | What it does |
|---|---|
| `python3 -I scripts/sweep-boards.py out.json` | Sweeps the boards listed in the script and writes every PM-titled posting to a JSON file. Edit the slug lists for your target companies. |
| `scripts/lint-claims.sh [files]` | Greps resumes and cover letters for banned phrases. Defaults to everything under `applications/`. Exits 1 on a hit. |
| `scripts/build-resume.sh in.html out.pdf` | Renders a resume with headless Chromium and fails unless the PDF is exactly two pages. |
| `python3 -I scripts/linkedin-reconcile.py ids.txt` | Says which LinkedIn job ids from a list are already in the tracker, so a pull skips them. |
| `scripts/build-letter.sh in.md out.pdf` | Renders a cover letter to a one-page PDF with pandoc and Chromium. Set `CHROME` if the binary is not on your PATH. |

## Things I learned running it

Keep the below-threshold table. It feels like clutter and it is the reason the second and third sweeps take a fraction of the time of the first.

State the gaps in the letter. A gap you name is a conversation; a gap the interviewer finds is a mark against you.

Answer the claims list seriously, every time. The errors it catches are small in wording and large in consequence, and they tend to come from your own old resumes rather than from the model.

Record submissions and recruiter answers in the tracker as they happen. Three weeks in, you will not remember which version of which letter went where.

When a role ends, change the dates and the tense everywhere, but do not put the reason in letters. Keep approved wording for forms and interviews in your profile and in every checklist.

## Privacy

Your profile has your contact details and your pay expectations. Your tracker names the companies you are talking to. Keep your search on a private fork, or on a branch you never publish, and keep `main` as the template. `setup/inputs/` is git-ignored. If you ever turn on GitHub Pages, point it at `main` only.

## Contributing

Improvements to the scripts, the templates, or the rules in `CLAUDE.md` are welcome as pull requests against `main`. Personal materials never belong on `main`; the fictional example is there so the structure can be shown without anyone's real record.
