# A job search you run with Claude Code

I built this repository to run my own search for product roles, and then cleaned it up so it is portable. It is not an app. It is a folder structure, a set of rules that Claude Code reads before it works, a few scripts, and a worked example. Everything in `examples/` describes a fictional candidate; there is no real person's data on this branch.

The short version of how it works:

1. You give Claude your resume and LinkedIn text. It drafts a profile document and asks you questions until the profile is right. That file, `Profile.md`, becomes the only source Claude is allowed to draw on when it writes about you.
2. You give it two or three postings you like. It extracts what they have in common, sweeps company job boards for similar roles, scores each one against your profile, and keeps a tracker of everything it looked at, including the ones it rejected and why.
3. For each role you decide to pursue, it builds a package: a two-page resume tailored to the posting, a short cover letter, and a checklist with the form fields filled in. Every claim in a package (anything inferred, combined, or newly worded) is listed for you to approve or correct, on a small local review page that shows each one highlighted in the resume and letter, before any PDF is made.
4. As you create application materials, Claude asks more about you where it relates to those roles as a good recruiter would. That goes into profile.md and helps refine the job search suggestions.

The most common failure in AI-drafted application material is attribution: the model reads a phrase or public docs and writes as if you built the product. The rules in `CLAUDE.md` are mostly about preventing that, and the "claims to confirm" step exists because the rules alone are not enough.

## What you need

- Claude Code, in the terminal, the desktop app, or the web.
- Your current resume as a PDF or HTML file, and the text of your LinkedIn profile.
- Two or three job postings that represent what you want.
- For rendering PDFs: Google Chrome (or Chromium) and Python 3, which macOS and most Linux systems already have. Nothing else to install.
- The Claude desktop app is the easiest place to run it: its browser pane is where the LinkedIn skills and the claims review page open. The terminal works too.

## Getting started

On GitHub, click **Use this template**, choose **Create a new repository**, and set it to **Private**. Your search lives in that private copy; this repository stays a clean template. (GitHub does not allow a private fork of a public repository, which is why the template button is the way in.) Then open your copy in Claude Code: in the desktop app, choose the folder after cloning it, or ask Claude to clone it for you. If you have never used git, `setup/GETTING-STARTED.md` has a path that needs no git commands at all.

To pick up later improvements to the template, ask Claude to compare your copy with `Daniel085/Job` and bring over the changes you want.

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
    claims.json                      every claim, with the exact text and where it appears
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
  sweep-boards.py          pulls postings matching your target titles from Greenhouse, Ashby, and Lever
  lint-claims.sh           greps your materials for phrases you have already corrected
  build-resume.sh          renders a resume to PDF and fails if it is not two pages
  build-letter.sh          renders a cover letter to a one-page PDF
  render.py                the shared renderer behind both build scripts and the review page
  claims-review/           the local page for approving or editing claims in context

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

The first pass uses your seed postings. Claude extracts the common titles, technologies, company types, pay bands, seniority, and work arrangements, shows you the pattern, and asks before it searches. The search itself has two parts. `scripts/sweep-boards.py` calls the public JSON endpoints of Greenhouse, Ashby, and Lever for every company slug you list in it, and writes out every posting whose title matches your target roles, with its description, location, date, and any dollar figures it finds. The default filter is product management; `--preset gtm` targets sales, revenue, growth, commercial, customer success, and partnerships leadership, and `--titles` takes your own pattern for any other field. For companies on other applicant-tracking systems, Claude uses web search and aggregator boards. Postings older than sixty days, under your pay floor, or at the wrong level are dropped before scoring.

Each run is logged in `jobs/Seed-Jobs.md` with its date, filters, sources, and results, and the next run is scheduled two to three weeks out. Re-running is a one-line request.

## Building a package

When you decide to pursue a role, say so:

> Build the Northwind Staff PM package.

Claude reads the posting and your profile, then writes three files. The resume starts from your base resume in `applications/generic/` and changes the summary and the most recent role's description to answer the posting, reordering bullets so the matching evidence comes first. It keeps the two-page layout; the build script refuses anything else. The letter is four short paragraphs: what the posting asks for and the matching line of your record, a second experience, how you work, and what you have not done. It closes on availability rather than enthusiasm. The checklist holds the posting facts, the form fields pre-filled from your profile, the decisions you should make before submitting, and the claims to confirm.

Then you review the claims. Claude lists every one in the package's `claims.json`, with the exact wording and the file it sits in, and you open the review page:

```
python3 -I scripts/claims-review/server.py        # then open http://127.0.0.1:8765
```

The page shows the resume and letter exactly as they will print, with each claim highlighted in place. Approve with A, edit with E (the edit is written into the resume or letter itself), reject with R. A line-break check flags stranded words and wrapped headers. Render PDFs stays locked until nothing is pending; when you press it, both PDFs are built and their page counts checked. You can also answer in chat ("1 and 2 yes. 3: it was take-share from competing platforms, not a legacy migration. 4 cut") and Claude applies it the same way. Either way, corrections go into your profile and the linter so the old phrasing cannot come back. When you have submitted, say so and the tracker is updated.

## Keeping claims honest

Three things work together here.

The attribution rules in `CLAUDE.md` say that a claim about your role must trace to `Profile.md`, that the verb must be the weakest one the evidence supports (built, then helped guide, then documented), that a verb is never upgraded while tailoring, and that public product facts stay product facts. Management claims are exact: mentored is not managed, and when a posting asks for people management the letter says plainly whether you have done it.

The claims list catches what the rules miss. Anything inferred, combined, or newly worded goes into the package's `claims.json`, and the review page shows each one in context. Nothing is rendered or sent until every claim is approved, edited, or rejected.

`scripts/lint-claims.sh` is the memory. Every time you correct a phrase, a pattern goes in, and the script runs before anything is committed or sent. It ships with a handful of generic patterns; the useful ones will be yours.

There is also a short pass for phrasing that reads as machine-written. The rules name the habits to strip: "the shape of," contrasts of the form "it's not X, it's Y," rhetorical triplets, and closing lines that restate the posting back at the company.

## LinkedIn and your network

Two skills run in the Claude desktop app, where Claude has a browser pane you sign in to. `/linkedin-search` pulls your LinkedIn jobs tracker and the standing searches, finds each role on the employer's own board, scores it, and records it. `/network-leads <company>` maps who in your network can refer or introduce you at a target company, ranks the paths, and drafts a message for you to approve. Neither sends anything on its own, and both read pages one at a time, the way a person would; LinkedIn does not allow automated scraping, and a restricted account would cost you more than any shortcut saves. The methods are written out in `docs/LinkedIn-Workflow.md` and `docs/Network-Lead-Research.md`. The lead files and the outreach log name real people, so they belong on your private branch, never on a published template.

## Scripts

| Command | What it does |
|---|---|
| `python3 -I scripts/sweep-boards.py out.json [--preset gtm] [--titles REGEX]` | Sweeps the boards listed in the script and writes every posting with a matching title to a JSON file. Product management by default; `--preset gtm` for sales and growth leadership. Edit the slug lists for your target companies. No installs needed. |
| `scripts/lint-claims.sh [files]` | Greps resumes and cover letters for banned phrases. Defaults to everything under `applications/`. Exits 1 on a hit. |
| `scripts/build-resume.sh in.html out.pdf` | Renders a resume with headless Chrome and fails unless the PDF is exactly two pages. |
| `python3 -I scripts/linkedin-reconcile.py ids.txt` | Says which LinkedIn job ids from a list are already in the tracker, so a pull skips them. |
| `scripts/build-letter.sh in.md out.pdf` | Renders a cover letter to a one-page PDF with headless Chrome. Set `CHROME` to use a specific binary. |
| `python3 -I scripts/claims-review/server.py` | The claims review page at http://127.0.0.1:8765: approve or edit claims in context, check line breaks, render both PDFs. Add `8765 examples/applications` to try it on the example. |

## Things I learned running it

Keep the below-threshold table. It feels like clutter and it is the reason the second and third sweeps take a fraction of the time of the first.

State the gaps in the letter. A gap you name is a conversation; a gap the interviewer finds is a mark against you.

Answer the claims list seriously, every time. The errors it catches are small in wording and large in consequence, and they tend to come from your own old resumes rather than from the model.

Record submissions and recruiter answers in the tracker as they happen. Three weeks in, you will not remember which version of which letter went where.

When a role ends, change the dates and the tense everywhere, but do not put the reason in letters. Keep approved wording for forms and interviews in your profile and in every checklist.

## Privacy

Your profile has your contact details and your pay expectations. Your tracker names the companies you are talking to. Keep your search in a private repository made with **Use this template** (GitHub does not allow private forks of a public repository), or on a branch you never push, and keep this repository as the template. `setup/inputs/` is git-ignored. If you ever turn on GitHub Pages, point it at `main` only.

## Contributing

Improvements to the scripts, the templates, or the rules in `CLAUDE.md` are welcome as pull requests against `main`. Personal materials never belong on `main`; the fictional example is there so the structure can be shown without anyone's real record.
