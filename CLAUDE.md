# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

A job-search repository: one candidate's professional profile, a tracker of evaluated roles with fit scores, and one application package (tailored resume, cover letter, checklist) per role. The workflow is built for Claude Code to run. This branch is the clean template; a user's own search lives on their own branch or fork.

## Core Architecture

### Document Dependency Chain

```
Profile.md                                          the single source of truth
  feeds  jobs/Similar-Job-Postings.md                 fit scores calculated from Profile.md
  feeds  applications/{company-role}/resume-{company-role}.html
                                                      tailored from Profile.md and the posting
  feeds  applications/{company-role}/cover-letter-{company-role}.md
                                                      written from the resume and the posting
  feeds  applications/{company-role}/application-checklist.md
                                                      form fields, decisions, claims to confirm
```

**Critical:** `Profile.md` is the single source of truth. All fit scores, resume customizations, and cover letters derive from this document. Always read `Profile.md` first when evaluating new jobs or creating application materials.

### Fit Scoring Algorithm

Located in `docs/AI-Assistant-Job-Search.md` under "The scoring method." **Critical:** Start at 0 and add/subtract points.

**High fit indicators (add points):**
- Direct technology experience: +10-20 points
- Exceeds YoE requirement: +5-10 points
- Domain expertise match: +10-15 points
- Previous experience at similar companies: +5-10 points
- Relevant leadership experience: +10-15 points

**Gaps or concerns (subtract points):**
- Missing required skills: -10-20 points
- Below experience requirement: -10-15 points
- Industry mismatch: -5-10 points
- Geographic constraints (non-remote): -5-10 points

**Inclusion criteria:**
- **Minimum threshold: 75/100**
- Must be posted within 60 days
- Must have active application link

Roles that fall short still get a row in a "below threshold" table with the score and the reason, so the next sweep does not re-evaluate them.

When adding jobs to `jobs/Similar-Job-Postings.md`, always read the complete `Profile.md` for scoring context.

### Resume Generation Pattern

All resume HTML files follow a 2-page print-optimized format with CSS page breaks. When creating new tailored resumes:

1. Read `applications/generic/resume-designed.html` as the base template (the user builds it once from `examples/applications/northwind-platform-pm/resume-northwind-platform-pm.html`)
2. Read target job requirements from `jobs/descriptions/` or the job posting URL
3. Read `Profile.md` for relevant experience matching job requirements
4. Customize the "Professional Summary" and the most recent role's description to the posting; reorder bullets so the matching evidence comes first
5. Keep the `<style>` block; it carries the page-break rules
6. Render with `scripts/build-resume.sh <html> <pdf>`, which fails if the result is not exactly 2 pages
7. Save as `applications/{company-role}/resume-{company-role}.html`, next to the cover letter, PDFs, and `application-checklist.md` for that role

**Key differentiators to emphasize** come from Profile.md's "Strengths & Unique Differentiators" section. Read them there rather than carrying a copy here; the copy goes stale.

### Cover Letter Pattern

Tailored cover letters live in `applications/{company-role}/cover-letter-{company-role}.md`. Structure (see the example package):

1. One or two sentences naming what the posting asks for and the matching line of the record
2. The most relevant experience, with numbers and with the candidate's role stated at the weakest verb the evidence supports
3. A second experience, or how the candidate works
4. What the candidate has not done, in plain words
5. One-line close on availability: "I am available now and would welcome a conversation about [where to start]."

Target length: 60% of a first draft. Build the PDF with `scripts/build-letter.sh <letter.md> <out.pdf>`.

Every new package lists its claims (anything inferred, combined, or newly worded) in `applications/{company-role}/claims.json`, with the exact text and file for every place a claim appears, and the checklist's "Claims to confirm" heading carries `<!-- claims:start -->` / `<!-- claims:end -->` markers. The user approves, edits, or rejects each claim in the claims review tool (below); the PDFs are rendered only once nothing is pending. See `examples/applications/northwind-platform-pm/claims.json`.

### Claims Review Tool

`scripts/claims-review/` is a small local web app (Python standard library, no installs) for reviewing claims in context before rendering:

```bash
python3 -I scripts/claims-review/server.py                           # your packages, http://127.0.0.1:8765
python3 -I scripts/claims-review/server.py 8765 examples/applications # try it on the example
```

- The left side lists each claim with its source; the right side shows the resume and letter laid out at the printed page width, with every claim highlighted in place.
- Keys: J/K move, A approve, E edit, R reject, U back to pending, Cmd/Ctrl+Enter save an edit. Edits are written into the source files, so what is approved is what renders.
- A line-break check lists stranded words and wrapped headers in the preview; the preview wraps exactly as the PDF will.
- Render PDFs stays locked while any claim is pending, or rejected while its text is still in the documents. It renders with headless Chrome or Chromium (set `CHROME` to choose one) and checks for 2 resume pages and 1 letter page. PDF names come from `role` and `pdf_prefix` in `claims.json`.
- The checklist's claims block is rewritten after every decision, with dates.
- `.claude/launch.json` has a `claims-review` entry that opens the running server in the Claude desktop app's browser pane. On macOS, start the server from a terminal: the desktop app's own launcher may not be allowed to read ~/Documents.

### Application Checklist

Every package carries `application-checklist.md`: posting facts (link, band, location, posted date, fit score), a "Read this first" list of decisions and risks, the files to upload, the form fields pre-filled from Profile.md, the claims to confirm, an AI-tells pass, and a "Before submitting" checklist. See `examples/applications/northwind-platform-pm/application-checklist.md`.

## Quick Start

When beginning any task in this repository:

1. **Read Profile.md first** - It's the single source of truth for all job evaluations and application materials
2. **Check current context** - Use `git status` and `git branch` to understand current state
3. **Review recent changes** - Use `git log --oneline -5` to see recent work
4. **Understand the task** - Job evaluation? Resume creation? Cover letter? Follow the appropriate workflow below

## Setup for New User

**Trigger:** If `/Profile.md` doesn't exist (only templates and examples present), enter new-user setup mode

### Workflow: Initialize Repository for New User

When user says "Help me set up this job search repository" or similar:

**Step 1: Verify Input Files**
- Check `/setup/inputs/` for:
  - `resume.pdf` or `resume.html` (required)
  - `linkedin-profile.txt` (required)
  - `additional-info.txt` (optional)
- If files missing, direct user to `/setup/GETTING-STARTED.md` for instructions

**Step 2: Parse Resume and LinkedIn**
- Read resume file (PDF or HTML)
- Extract:
  - Contact information (email, phone, LinkedIn, GitHub)
  - Work history (company, title, dates, achievements with metrics)
  - Technical skills and tools
  - Education and certifications
  - Any quantified achievements
- Read `linkedin-profile.txt`
- Extract:
  - Professional summary/about section
  - Experience descriptions
  - Skills list
  - Projects or publications
- Read `additional-info.txt` if present for supplemental context

**Step 3: Ask Clarifying Questions**
Use this template:
```markdown
I've drafted your Profile.md from your resume and LinkedIn. Let me clarify a few things:

1. **Compensation Expectations**: What base salary is acceptable, and what would you prefer?
   (e.g., "$180K acceptable, $220K preferred")

2. **Location Preferences**: Are you open to remote, hybrid, or specific cities? Any relocation you would consider, and on what terms?

3. **Job Search Priorities**: What are your top 3 must-haves in your next role?
   (e.g., "API platform focus", "Remote flexibility", "B2B SaaS")

4. **GitHub Portfolio**: Should I analyze your GitHub repos for technical credentials? (Yes/No/URL if different from resume)

5. **Domain Expertise**: Which industries are your strongest? Rank top 3.

6. **Target Career Level**: What seniority are you targeting?
   (Senior PM, Staff PM, Principal PM, Director)

7. **Management**: Have you formally managed people? If you mentored or led without the title, say so; the materials will state it accurately.
```

**Step 4: Generate Profile.md**
- Use `/templates/Profile-template.md` as structure guide
- Map parsed data + user responses to appropriate sections
- Reference `/examples/Profile-example.md` for formatting patterns (it describes a fictional candidate)
- Ensure all required sections are populated, including "Most Recent Role," "Areas for Development," and an empty "Approved Wording and Corrections" log
- Include inline comments where user should add more detail
- Save to `/Profile.md`

**Step 5: Present for Review**
```markdown
I've created your Profile.md with:
- [X] sections covering your professional background
- [X] extracted skills and technologies
- [X] quantified achievements from your resume
- [X] years of work history

Please review /Profile.md and let me know:
1. Are there any achievements or metrics I missed?
2. Should I add or emphasize any specific technologies?
3. Do the "Areas for Development" seem accurate?
4. Any corrections to job titles, dates, or companies?
5. For each achievement, is the verb right? "Built" means you alone; "helped guide" or "with Architecture" means shared; "documented" or "owned the surface of" means you exposed someone else's design.
```

**Step 6: Iterate Based on Feedback**
- Make requested edits to Profile.md
- Show changes before applying
- Repeat until user approves

**Step 7: Next Steps**
Once Profile.md is approved:
```markdown
Your Profile.md is ready. This is now your single source of truth.

Next steps:
1. Provide 2-3 seed job URLs (jobs you're interested in or represent what you want)
2. I'll analyze patterns and search for similar opportunities
3. Then we can create tailored resumes and cover letters

Ready to add seed jobs? Share 2-3 job posting URLs.
```

## Common Development Tasks

### Adding a Single Job Posting

When user provides a single job URL:

1. Use WebFetch to retrieve the job description (careers pages rendered by JavaScript may need a headless browser; many boards expose a JSON API, see `scripts/sweep-boards.py`)
2. Read `Profile.md` for fit scoring context
3. Calculate fit score using the method in `docs/AI-Assistant-Job-Search.md`
4. If the score is 75 or above, add a full entry; otherwise add a row to the below-threshold table with the reason
5. Write the fit analysis: strengths with specific Profile.md evidence and metrics, and gaps
6. Add to `jobs/Similar-Job-Postings.md` maintaining score-sorted order (highest first)
7. Update "Last Updated" date at top of file
8. Save the full description to `jobs/descriptions/{Company}-{Role}.md` when a package is likely

See `docs/AI-Assistant-Job-Search.md` for detailed scoring methodology and fit analysis format.

### Automated Job Discovery from Seed Jobs

When user provides 2-3 seed job URLs (or says "find similar jobs"):

**Step 1: Collect and Analyze Seed Jobs**
- WebFetch each job description
- Calculate fit score for each using Profile.md
- Save to `/jobs/Seed-Jobs.md` with fit analyses
- If any seed job scores <75, flag to user (may indicate unrealistic targets)

**Step 2: Extract Patterns**
Analyze across all seed jobs to identify:
- **Common role titles** (e.g., "Principal PM", "Staff PM API", "Senior PM Platform")
- **Required technologies** (e.g., REST APIs 100%, GraphQL 67%, SDKs 67%)
- **Company characteristics** (size, stage, industry)
- **Compensation patterns** (base salary range, total comp range)
- **Experience levels** (years required, seniority)
- **Work arrangements** (remote %, hybrid %, on-site %)

**Step 3: Present Patterns to User**
```markdown
Analyzing your [X] seed jobs, I've identified these patterns:

**Common Role Characteristics:**
- Titles: [most frequent titles]
- Seniority: [level range]
- Focus: [common themes]

**Technologies (% of jobs mentioning):**
- [Tech 1] (100%)
- [Tech 2] (67%)

**Company Profiles:**
- Size: [employee range]
- Industry: [industries]
- Stage: [funding/growth stage]

**Compensation:**
- Base: $[X]K - $[Y]K

**Work Arrangement:**
- Remote: [X] of [total]
- Hybrid: [X] of [total]

Should I search for similar jobs matching these patterns? (Yes/No)
```

**Step 4: Run the Sources** (if user confirms)
- `python3 -I scripts/sweep-boards.py out.json` sweeps the Greenhouse, Ashby, and Lever boards listed in the script (edit the slug lists for your target companies) and writes every posting whose title matches the target roles, with description, location, date, and any dollar figures found. Choose the filter from the seed jobs: `--preset pm` (default) for product roles, `--preset gtm` for sales, revenue, growth, and partnerships leadership, or `--titles REGEX` for anything else
- Add 5-10 WebSearch queries for companies on other applicant-tracking systems (Workday, iCIMS, SmartRecruiters, Rippling); aggregator boards (Built In, Lenny's Jobs, Wellfound) cover many of these
- Filters: posted within 60 days; band top at or above the user's preferred base (see Compensation rule below); matching seniority; active link

**Step 5: Fetch and De-duplicate**
- Use WebFetch (or the sweep's captured description) for each posting
- Remove duplicates (same URL, or same company and title)
- Verify links are accessible

**Step 6: Score and Filter**
For each discovered job:
- Read Profile.md for scoring context
- Calculate fit score using algorithm
- Include a full entry if the score is 75 or above; a below-threshold row otherwise
- Write a detailed fit analysis: strengths with specific Profile.md evidence, honest gaps

**Step 7: Populate Jobs File**
- Add qualifying jobs to `/jobs/Similar-Job-Postings.md`, sorted by fit score
- Save full job descriptions to `/jobs/descriptions/`
- Log the run (date, filters, sources, results) in `/jobs/Seed-Jobs.md` under "Re-runs," and note when the next run is due (every two to three weeks)
- Update "Last Updated" date

**Step 8: Report Results**
```markdown
Found [X] jobs matching your criteria:

**Fit Score Breakdown:**
- 90-100 (Excellent matches): [X] jobs
- 80-89 (Strong matches): [X] jobs
- 75-79 (Good matches): [X] jobs

**Top 5 Matches:**
1. [Company] - [Role] ([score]/100) - $[comp range]
   Strength: [key strength]
   Gap: [notable gap]

All jobs saved to /jobs/Similar-Job-Postings.md

Ready to create tailored resumes for top matches? (Yes/No)
```

**Edge Cases:**
- If <5 jobs found: Suggest broadening seed jobs or lowering threshold temporarily
- If >30 jobs found: Consider if patterns were too broad, offer to narrow
- If fit scores all <80: May indicate seed jobs don't align well with Profile.md - review gaps

### Creating Tailored Application Materials

```bash
# 1. Read Profile.md and the target job description
# 2. Create applications/{company-role}/resume-{company-role}.html from applications/generic/resume-designed.html
# 3. Create applications/{company-role}/cover-letter-{company-role}.md
# 4. Create applications/{company-role}/application-checklist.md and claims.json (every claim, with exact text and file)
# 5. scripts/lint-claims.sh
# 6. The user reviews the claims in the claims review tool and presses Render PDFs there
#    (or, without the tool, after confirming the claims:
#     scripts/build-resume.sh applications/{company-role}/resume-{company-role}.html applications/{company-role}/{Name}-Resume-{Role}.pdf
#     scripts/build-letter.sh applications/{company-role}/cover-letter-{company-role}.md applications/{company-role}/{Name}-Cover-Letter-{Role}.pdf)
# 7. Commit: "Add tailored resume and cover letter for {Company} {Role}"
```

PDF filenames carry the role so two packages never share a name. Closed roles' folders are deleted, not archived; the materials regenerate from Profile.md in minutes and stay in git history.

### Verifying Job Links

Before applications, verify links in `jobs/Similar-Job-Postings.md` are still active: fetch each URL and update or remove closed positions.

### Git Workflow

Keep the search in the user's own private copy (made with **Use this template**; GitHub does not allow private forks of a public repository) or on a branch that is never pushed here, and leave this template clean. Branch naming: `claude/{task-description}-{id}`.

```bash
git add .
git commit -m "Descriptive message"
git push -u origin <current-branch-name>
```

Generic improvements (scripts, templates, workflow text in this file) are cherry-picked back to the template branch; personal files (Profile.md, jobs/, applications/) never are.

### Dynamic Profile Updates

**Purpose:** Keep Profile.md current by adding new information discovered during the job search.

**Trigger Points:**
1. Creating a tailored resume, and a job requirement is not clearly addressed in Profile.md
2. Writing a cover letter, and a specific metric or example is not documented
3. Calculating a fit score, and a skill's proficiency level is unclear
4. User explicitly requests: "Update Profile.md: [new information]"
5. The user corrects a phrase: add the correction to Profile.md's "Approved Wording and Corrections" log and a pattern to `scripts/lint-claims.sh`

**Workflow:**

**Step 1: Detect Gap**
While working on application material, if you encounter:
- Job requires skill/technology not in Profile.md
- Need an achievement metric for a cover letter not in Key Achievements
- Domain experience mentioned but not detailed
- Technology proficiency unclear

**Step 2: Ask Targeted Clarifying Question**
```markdown
I'm [task] for [Company]'s [Role]. They require [specific requirement].

I don't see this clearly addressed in your Profile.md.

Questions:
1. [Direct question about the requirement] (Yes/No/Details)
2. [Follow-up if relevant]
3. Should I add this to your Profile.md for future applications? (Yes/No)
```

Ask about all gaps at once rather than one by one.

**Step 3: Update Profile.md if User Provides Info**
Show the exact change before applying:
```markdown
I'll update Profile.md:

Section: Technical Skills > APIs & Integration
Adding: "Payment APIs (Stripe, Plaid)"

Proceed with these updates? (Yes/No)
```

**Step 4: Apply Updates**
- Edit Profile.md with approved changes
- Commit message: "Update Profile.md: added payment API experience"

**Important Guidelines:**
- **Always ask permission** before updating Profile.md
- **Show exact changes** being made
- **Don't make assumptions** - if the user says "No" or "I don't have that experience", don't add it
- **"Sort of" or "a little" is not a strength.** Offer "exposure to [technology]" on the resume instead, and do not add it to Profile.md as a skill
- **Keep updates factual** - only add what the user confirms they actually have

## File Organization

### Root Directory
- `Profile.md` - Professional background, skills, achievements (SINGLE SOURCE OF TRUTH; absent on the template branch)
- `CLAUDE.md` - This file - instructions for Claude Code
- `README.md` - Repository overview and navigation guide

### Documentation (`docs/`)
- `AI-Assistant-Job-Search.md` - Fit scoring algorithm and workflow instructions
- `Claude-User-Guide.md` - User guide for working with Claude Code
- `LinkedIn-Workflow.md` - Pulling the LinkedIn tracker and searches, and recording them
- `Network-Lead-Research.md` - Finding and ranking referral paths in the user's network

### Scripts (`scripts/`)
- `sweep-boards.py` - Sweeps Greenhouse, Ashby, and Lever boards for postings with matching titles: `--preset pm` (default), `--preset gtm` (sales, revenue, growth, commercial, customer success, partnerships leadership), or `--titles REGEX`; edit the slug lists. Standard library only.
- `lint-claims.sh` - Greps application materials for phrases that have already been corrected once (add your own patterns)
- `build-resume.sh` - Renders a resume HTML to PDF with headless Chrome and fails if it is not two pages
- `build-letter.sh` - Renders a cover letter Markdown file to a one-page PDF (headless Chrome; no pandoc)
- `render.py` - The renderer behind both build scripts and the review page: stages files in a temp dir, prints with Chrome (through LaunchServices on macOS), checks page counts
- `claims-review/` - Local web app for approving or editing claims in context, checking line breaks, and rendering both PDFs (see Claims Review Tool)

### Application packages (`applications/`)
- `generic/resume-designed.html` - The user's base resume; every tailored resume starts from it
- `{company-role}/` - One folder per role: `resume-{company-role}.html`, `cover-letter-{company-role}.md`, the rendered PDFs, and `application-checklist.md`

### Skills (`.claude/skills/`)
- `linkedin-search` - Pull the user's LinkedIn jobs tracker and run the standing searches in the Claude desktop app's built-in browser, score each new posting, record it. Desktop app only; from a cloud session it says so and stops.
- `network-leads <company>` - Map referral and intro paths at a target company from the user's LinkedIn network, write `network/leads-<company>.md`, draft outreach for approval. Desktop app only; never sends.
- `scripts/linkedin-reconcile.py ids.txt` - Which LinkedIn job ids are already in the tracker.

### Network and outreach (`network/`, `outreach/`)
- `network/leads-{company}.md` - Ranked referral and intro paths for one target company (method in `docs/Network-Lead-Research.md`).
- `outreach/log.md` - Every message sent about the search: date, person, channel, summary, status, next step. Append only.
- Both name real people. They stay on the user's private branch or fork, never on a published template branch.

### Job Tracking (`jobs/`)
- `Similar-Job-Postings.md` - Active opportunities with fit scores (sorted by score), a status block, and below-threshold tables
- `Seed-Jobs.md` - Seed jobs, extracted patterns, and the log of sweep re-runs
- `descriptions/` - Saved job descriptions (`generic-api-pm.md` is a reference example)

### Templates and Examples
- `templates/` - Blank Profile, cover letter, resume guide, and seed-jobs templates
- `examples/` - A complete fictional example: profile, one application package, one tracker

## Key Constraints

### Resume Requirements
- **Must be exactly 2 pages** when printed (not 1, not 3); `scripts/build-resume.sh` enforces it
- CSS page breaks required between pages
- HTML format preferred over PDF for easy editing
- Optimize for ATS parsing (proper semantic HTML structure)
- No Technical Skills grid by default: for product managers it invites a solo coding test, and the experience bullets already show the tools in use. Add one only if the user's field expects it
- No "Areas of Expertise" tag row on the base resume. On a tailored resume the row is allowed only when every tag mirrors the posting's own vocabulary and maps to a bullet below it

### Attribution Rules

The most common error in AI-drafted materials is attributing what a **product** does to what the **candidate** did. Public sources (docs, press releases, product pages) describe the product. Only `Profile.md` describes the candidate's role in it. Follow these rules on every resume, cover letter, fit analysis, and recruiter message:

1. **A claim about the candidate's role must trace to Profile.md.** If it is not there, it does not go in a deliverable as fact. Draft it, mark it, and list it under "Claims to confirm."
2. **Use the weakest verb the evidence supports.** Built / designed (sole, confirmed) > helped guide / co-designed / with Architecture (shared) > documented / wrote the guide for / owns the surface of (exposed). When unsure, go one tier down.
3. **Never upgrade a verb while tailoring.** "Led" in Profile.md does not become "built from scratch" in a cover letter. Reuse the Profile.md phrasing or quote it.
4. **Public product facts stay product facts.** "The platform applies consent before an agent acts" is fine. "The candidate designed consent enforcement" is not, unless Profile.md says so.
5. **Every new material has its claims listed for review** in `claims.json` (and the checklist), and Profile.md is updated only after the user confirms. Do not render final PDFs while claims are pending.
6. **Run `scripts/lint-claims.sh` before sending or committing** application materials. Add a pattern every time a correction lands.
7. **Inherited text is not verified text.** Lines from an old resume carry the same risk as new inferences. When a line is challenged, fix it everywhere it appears.
8. **Management claims are exact.** "Mentored" or "onboarded" is not "managed." When a posting asks for people management and the record has none, the letter says so.
9. **Never name a company's customers or partners in external material** unless the user confirms they are public and approves. Say "launch partners" or "enterprise customers."

### Compensation Rule
Profile.md records two numbers: an acceptable base and a preferred base. A band whose top reaches the preferred number is not marked down for pay; a top between acceptable and preferred takes a small deduction; a top under the acceptable number is excluded. Bands in the tracker are base salary as stated in the posting, equity separate.

### Roles shared by family or friends
Score them on the same scale, but be more open to applying than to a board find: package anything at 65 or above if the user accepts its location, and present location (relocation, residency, hybrid) as a decision for the user rather than a reason to exclude. Record who shared the role and the date in the tracker section heading.

### Outreach rules
- Never send, accept, apply, post, or spend an InMail credit without the user's explicit approval of the final text. Show the full draft first. When the user edits it, send their wording exactly; raise typos rather than fixing them silently.
- Claims in messages are exact: "we overlapped at [Company]," not "we worked together," unless the user confirms more. Wording about the user's own record comes from Profile.md.
- Short messages with one concrete hook (their post, a shared employer, a real overlap) and one ask. Separate facts from inferences in lead write-ups.
- LinkedIn is read one page at a time in a browser the user is signed in to, as a person would; no bulk scraping. A LinkedIn find is scored like a sweep find (75 bar), not like a referral.

### When the current role ends
Switch the most recent role to the past tense with its end date in every new material. New letters do not state the departure or the reason; the resume's dates carry it. Record approved reason-for-leaving wording in Profile.md under "Most Recent Role" for forms and interviews, and put it in every checklist. Already-submitted packages stay as submitted until a recruiter responds.

### Writing style
Plain prose in every file on this branch: no emoji, no decorative symbols, no exclamation marks in documentation. Headings are sentences or short noun phrases. Lists are for parallel items; paragraphs are for reasoning.

### AI-tells pass
Before anything is sent, strip phrasing that reads as machine-written: "the shape of," "it's not X, it's Y" contrasts, "I should say plainly," "rather than guessing," rhetorical triplets, and closing lines that restate the posting back at the company. Plain statements instead.

## Fit Analysis Standards

Use this exact format in `jobs/Similar-Job-Postings.md`:

```markdown
**Fit analysis:**
- **Strength, [category]:** [specific evidence from Profile.md with metrics]
- **Strength, [category]:** [specific evidence from Profile.md with metrics]
- **Gap, [category]:** [honest assessment]
- **Strength, [category]:** [specific evidence from Profile.md with metrics]
```

Always include both strengths and gaps. Honest gap assessment is required. No emoji or symbol markers; the words carry it.

## Workflow: Evaluating New Job Posting

When the user provides a job posting URL or description:

1. **Fetch job details** - Company, title, requirements, compensation, location, post date
2. **Read Profile.md** - Complete file for background context
3. **Calculate fit score** - Use the method in docs/AI-Assistant-Job-Search.md
4. **Write fit analysis** - strengths with specific Profile.md evidence and metrics, honest gaps
5. **Add to jobs/Similar-Job-Postings.md** - Full entry at 75 or above, below-threshold row otherwise, in score-sorted order
6. **Update "Last Updated" date** at top of file
7. **Save the full description** to jobs/descriptions/ when a package is likely

## Notes

- This is a job search repository, not a software project; the only checks are `scripts/lint-claims.sh` and the two-page rule in `scripts/build-resume.sh`
- Focus is on document generation, fit analysis, and application tracking
- All application materials must be tailored, never generic
- Treat the repository as public unless you know otherwise: no contact details or compensation in anything on the template branch
- Job links expire - verify before applications
