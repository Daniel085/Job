# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Job search repository for Daniel O'Rorke - tracking applications for Principal/Senior Product Manager roles focused on API & Developer Platforms. Contains professional profile, resumes, job descriptions, and automated fit scoring system.

## Core Architecture

### Document Dependency Chain

```
Profile.md (master reference)
    ↓
jobs/Similar-Job-Postings.md (fit scores calculated from Profile.md)
    ↓
resumes/resume-{company}.html (tailored from Profile.md + job requirements)
    ↓
cover-letters/cover-letter-{company}.md (written from resume + job description)
```

**Critical:** `Profile.md` is the single source of truth. All fit scores, resume customizations, and cover letters derive from this document. Always read `Profile.md` first when evaluating new jobs or creating application materials.

### Fit Scoring Algorithm

Located in `docs/AI-Assistant-Job-Search.md` (lines 44-68). **Critical:** Start at 0 and add/subtract points.

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

When adding jobs to `jobs/Similar-Job-Postings.md`, always read complete `Profile.md` for scoring context.

### Resume Generation Pattern

All resume HTML files follow 2-page print-optimized format with CSS page breaks (see commit 17466ca). When creating new tailored resumes:

1. Read `resumes/resume-designed.html` as base template
2. Read target job requirements from `jobs/descriptions/` or job posting URL
3. Read `Profile.md` for relevant experience matching job requirements
4. Customize "Professional Summary" and project descriptions to highlight relevant experience
5. Ensure CSS includes `page-break-after: always` between pages
6. Verify 2-page format (not 3+ pages)
7. Save as `resumes/resume-{company}.html`

**Key Differentiators to Emphasize (from Profile.md:263-292):**
- CAMARA network API experience (rare for API PMs)
- WebRTC platform expertise
- Telecom/CPaaS domain knowledge
- GitHub portfolio demonstrating hands-on technical work
- 10x growth scaling experience

### Cover Letter Pattern

Tailored cover letters live in `cover-letters/cover-letter-{company}.md`. Standard structure:

1. Opening hook connecting candidate background to company mission
2. 2-3 specific experiences matching job requirements (with metrics)
3. Why this company/role specifically
4. Closing with clear next step

Target length: 60% of original draft (see commit e59f0ba for example compression).

## Quick Start

When beginning any task in this repository:

1. **Read Profile.md first** - It's the single source of truth for all job evaluations and application materials
2. **Check current context** - Use `git status` and `git branch` to understand current state
3. **Review recent changes** - Use `git log --oneline -5` to see recent work
4. **Understand the task** - Job evaluation? Resume creation? Cover letter? Follow the appropriate workflow below

## Setup for New User

**Trigger:** If `/Profile.md` doesn't exist (only templates and examples present) → New user setup mode

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

1. **Compensation Expectations**: What's your target salary range for your next role?
   (e.g., $200K-$350K total compensation for Principal level)

2. **Location Preferences**: Are you open to remote, hybrid, or specific cities?

3. **Job Search Priorities**: What are your top 3 must-haves in your next role?
   (e.g., "API platform focus", "Remote flexibility", "B2B SaaS")

4. **GitHub Portfolio**: Should I analyze your GitHub repos for technical credentials? (Yes/No/URL if different from resume)

5. **Domain Expertise**: Which industries are your strongest? Rank top 3.
   (e.g., fintech, healthcare, developer tools, e-commerce)

6. **Target Career Level**: What seniority are you targeting?
   (Senior PM, Staff PM, Principal PM, Senior Staff PM)
```

**Step 4: Generate Profile.md**
- Use `/templates/Profile-template.md` as structure guide
- Map parsed data + user responses to appropriate sections
- Reference `/examples/Profile-example.md` for formatting patterns
- Ensure all 15 required sections are populated
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
```

**Step 6: Iterate Based on Feedback**
- Make requested edits to Profile.md
- Show changes before applying
- Repeat until user approves

**Step 7: Next Steps**
Once Profile.md is approved:
```markdown
Your Profile.md is ready! This is now your single source of truth.

Next steps:
1. Provide 2-3 seed job URLs (jobs you're interested in or represent what you want)
2. I'll analyze patterns and search for similar opportunities
3. Then we can create tailored resumes and cover letters

Ready to add seed jobs? Share 2-3 job posting URLs.
```

## Common Development Tasks

### Adding a Single Job Posting

When user provides a single job URL:

1. Use WebFetch to retrieve job description
2. Read `Profile.md` for fit scoring context
3. Calculate fit score using algorithm in `docs/AI-Assistant-Job-Search.md:44-68`
4. Only add if score ≥75 (otherwise inform user why it didn't qualify)
5. Write fit analysis with ✅ strengths (specific Profile.md evidence + metrics) and ⚠️ gaps
6. Add to `jobs/Similar-Job-Postings.md` maintaining score-sorted order (highest first)
7. Update "Last Updated" date at top of file
8. Optionally save full description to `jobs/descriptions/{company}.md`

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
  - Size: employee count ranges
  - Stage: Series C-D, public, growth stage
  - Industry: B2B SaaS, API-first, developer tools
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
- [Tech 3] (67%)

**Company Profiles:**
- Size: [employee range]
- Industry: [industries]
- Stage: [funding/growth stage]

**Compensation:**
- Base: $[X]K - $[Y]K
- Total: $[X]K - $[Y]K

**Work Arrangement:**
- Remote: [X] of [total]
- Hybrid: [X] of [total]

Should I search for similar jobs matching these patterns? (Yes/No)
```

**Step 4: Generate Search Queries** (if user confirms)
Create 5-10 targeted WebSearch queries:
- "[Most common title] 2026"
- "[Common title] [primary technology] [domain] 2026"
- "[Company type] Product Manager jobs remote 2026"
- "[Technology] PM [compensation range] 2026"

Apply mental filters:
- Posted within 60 days only
- Compensation ±20% of pattern range
- Matching seniority level (don't search for "Senior PM" if patterns show "Principal PM")
- Active application links

**Step 5: Execute Search and Fetch Jobs**
- Run WebSearch queries
- Collect job posting URLs from results
- Use WebFetch to retrieve each job description
- Remove duplicates (same URL or very similar company/title)
- Verify links are accessible

**Step 6: Score and Filter**
For each discovered job:
- Read Profile.md for scoring context
- Calculate fit score using algorithm
- Only include if score ≥75
- Write detailed fit analysis (✅ strengths with specific Profile.md evidence, ⚠️ honest gaps)

**Step 7: Populate Jobs File**
- Add all qualifying jobs to `/jobs/Similar-Job-Postings.md`
- Sort by fit score (highest first)
- Save full job descriptions to `/jobs/descriptions/{company}.md`
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
   ✅ [Key strength]
   ⚠️ [Notable gap]

2. [Company] - [Role] ([score]/100) - $[comp range]
   ...

All jobs saved to /jobs/Similar-Job-Postings.md

Ready to create tailored resumes for top matches? (Yes/No)
```

**Edge Cases:**
- If <5 jobs found: Suggest broadening seed jobs or lowering threshold temporarily
- If >30 jobs found: Consider if patterns were too broad, offer to narrow
- If fit scores all <80: May indicate seed jobs don't align well with Profile.md - review gaps

### Creating Tailored Application Materials

```bash
# 1. Read Profile.md and target job description
# 2. Create resumes/resume-{company}.html from resumes/resume-designed.html
# 3. Create cover-letters/cover-letter-{company}.md
# 4. Verify 2-page resume format
# 5. Commit with message: "Add tailored resume and cover letter for {Company} {Role}"
```

### Viewing Resumes Locally

```bash
# Open HTML resume in browser
firefox resumes/resume-designed.html
# or
google-chrome resumes/resume-anthropic.html
```

### Verifying Job Links

Before applications, verify links in `jobs/Similar-Job-Postings.md` are still active:

```bash
# Use WebFetch to check each URL still returns valid job posting
# Update or remove closed positions
```

### Git Workflow

Standard branch naming: `claude/{task-description}-{id}`

```bash
# Example workflow
git add .
git commit -m "Descriptive message"
git push -u origin <current-branch-name>
```

**Important:** Check `.github/workflows/static.yml` for current deployment configuration. The workflow may be configured to deploy from a specific branch.

### Dynamic Profile Updates

**Purpose:** Keep Profile.md current by adding new information discovered during job search process.

**Trigger Points:**
1. Creating tailored resume → job requirement not clearly addressed in Profile.md
2. Writing cover letter → need specific metric/example not documented
3. Calculating fit score → unclear skill proficiency level
4. User explicitly requests: "Update Profile.md: [new information]"

**Workflow:**

**Step 1: Detect Gap**
While working on application material, if you encounter:
- Job requires skill/technology not in Profile.md Technical Skills
- Need achievement metric for cover letter not in Key Achievements
- Domain experience mentioned but not detailed in Domain Expertise
- Technology proficiency unclear (have used it, but how extensively?)

**Step 2: Ask Targeted Clarifying Question**
Template:
```markdown
I'm [task] for [Company]'s [Role]. They require [specific requirement].

I don't see this clearly addressed in your Profile.md.

Questions:
1. [Direct question about the requirement] (Yes/No/Details)
2. [Follow-up if relevant]
3. Should I add this to your Profile.md for future applications? (Yes/No)
```

Example:
```markdown
I'm tailoring your resume for Stripe's API Platform role. They require payment API
experience and PCI-DSS compliance knowledge.

I don't see payment APIs or compliance mentioned in your Profile.md.

Questions:
1. Have you worked with payment APIs (Stripe, Plaid, financial APIs)? (Yes/No/Details)
2. Any PCI-DSS, SOC2, or API compliance experience? (Yes/No/Details)
3. Relevant fintech domain experience to highlight? (Yes/No/Details)
```

**Step 3: Update Profile.md if User Provides Info**
Based on response, determine appropriate section:
- **New technology** → Technical Skills section (appropriate category)
- **New achievement with metric** → Key Achievements & Metrics
- **Domain experience** → Domain Expertise in Core Areas
- **Skill clarification** → Update existing entry with proficiency note

Show exact change before applying:
```markdown
I'll update Profile.md:

Section: Technical Skills > APIs & Integration
Adding: "Payment APIs (Stripe, Plaid)"

Section: Core Areas of Expertise > Domain Expertise
Adding: "Financial APIs" under domain list

Section: Key Achievements & Metrics
Adding: "Led SOC2 compliance for API platform"

Proceed with these updates? (Yes/No)
```

**Step 4: Apply Updates**
- Edit Profile.md with approved changes
- Note in commit message: "Update Profile.md: added payment API and compliance experience"
- Inform user: "Profile.md updated. This information will be available for all future applications."

**Step 5: Continue Original Task**
- Use updated Profile.md information for current resume/cover letter/fit analysis
- Benefit: All future applications automatically include this information

**Important Guidelines:**
- **Always ask permission** before updating Profile.md
- **Show exact changes** being made
- **Allow user to reject** or modify
- **Don't make assumptions** - if user says "No" or "I don't have that experience", don't add it
- **Keep updates factual** - only add what user confirms they actually have
- **Log all changes** in commit messages for transparency

**Edge Cases:**

*User provides vague response:*
```
User: "Yeah, I've done some work with that"
Claude: "Can you provide specifics? For example:
- Which company/project?
- How long did you use it?
- Any metrics or outcomes?
This helps me add accurate, compelling details to your Profile."
```

*User says "sort of" or "a little":*
Don't add to Profile as a strength. Instead:
```
Claude: "I won't add this as a core skill since your experience is limited.
However, I can mention it in your resume as 'exposure to [technology]' if relevant.
Should I do that for this application?"
```

*Multiple gaps discovered:*
Ask about all at once rather than one-by-one:
```
Claude: "I noticed a few gaps between this job and your Profile:
1. [Gap 1]
2. [Gap 2]
3. [Gap 3]

Let me know which of these you have experience with, and I'll update your Profile accordingly."
```

## File Organization

### Root Directory
- `Profile.md` - Professional background, skills, achievements (SINGLE SOURCE OF TRUTH)
- `CLAUDE.md` - This file - instructions for Claude Code
- `README.md` - Repository overview and navigation guide

### Documentation (`docs/`)
- `AI-Assistant-Job-Search.md` - Fit scoring algorithm and workflow instructions
- `Claude-User-Guide.md` - User guide for working with Claude Code

### Resumes (`resumes/`)
- `resume-designed.html` - Base resume template and the generic (untailored) resume. Rebuilt October 27, 2026 from the approved Safe Access layout: current roles, corrected attribution, no Technical Skills section, canonical expertise tags, and the `section.experience` print fix. Start every new tailored resume from this file. The 2025 version is in `archive/2025/resumes/resume-designed-2025.html`.
- `resume-{company}.html` - Active tailored resumes (anthropic-safe-access, anthropic-multi-cloud-growth, anthropic-devrel, mercury, 1password-developer-ai)

### Cover Letters (`cover-letters/`)
- `cover-letter-{company}.md` - Active cover letters (anthropic-safe-access, anthropic-multi-cloud-growth, anthropic-devrel, mercury, 1password-developer-ai)

### Archive (`archive/2025/`)
- Resumes and cover letters from the 2025 search (anthropic API PM, lightyear, pagerduty, plaid, postman, twilio, zoom). All those roles are closed. These files predate the October 2026 attribution corrections and must not be reused as-is.

### Job Tracking (`jobs/`)
- `Similar-Job-Postings.md` - Active opportunities with fit scores (sorted by score)
- `descriptions/` - Individual job description files
  - `generic-api-pm.md` - Generic API PM role reference
  - `{Company}.md` - Company-specific job descriptions (Gordon-Brothers-AI-Specialist.md, Wavelo.md)

## Key Constraints

### Resume Requirements
- **Must be exactly 2 pages** when printed (not 1, not 3)
- CSS page breaks required between pages
- HTML format preferred over PDF for easy editing
- Optimize for ATS parsing (proper semantic HTML structure)

### Terminology Standards (from commit 62fb5da)
- Use "mentored" not "managed" when referring to PM team (mentored 5 PMs, not managed)
- Accurate representation of IC vs management roles
- "Led cross-functional teams" is acceptable for project leadership
- "Enhanced Number Verification," never "Number Verification from PoC to commercial." NV was already commercial; Daniel led the enhancement with operators and handset manufacturers.
- Alianza, three separate things: Daniel **built** developer.alianza.com; he **helped guide the structure of** the Crux API **with Architecture**; the Crux **platform** was designed before he joined. API standards and design review are "with Architecture," never solo.
- Daniel did not design Crux authentication. He **documents** the access model; say "wrote the authentication guide," not "designed the access model."
- No Technical Skills section on resumes. Daniel builds with AI assistance; a skills grid invites a solo coding test.
- No "Areas of Expertise" tag row on the generic resume (`resume-designed.html`). On a tailored resume the row is allowed only when every tag mirrors the posting's own vocabulary and maps to a bullet below it; never invent a tag the record cannot support.
- No Alianza customer or partner names in any external material (resumes, cover letters, recruiter messages, notes to contacts), even when the names appear in Alianza's own press. Say "AI experience providers" or "launch partners." Names may stay in internal reference files (`jobs/descriptions/Alianza-Crux-Reference.md`, Profile.md) where they are sourced to the press release.
- The portal's resource model and lifecycle are the API's design, not Daniel's. Docs were generated by AI agents and human-reviewed: say "built the portal" or "published," never "wrote the docs."

### Attribution Rules (added October 22, 2026, after a correction round)

The inaccuracies that round fixed all came from one mistake: attributing what a **product** does to what **Daniel** did. Public sources (docs, press releases, product pages) describe the product. Only `Profile.md` describes Daniel's role in it. Follow these rules on every resume, cover letter, fit analysis, and recruiter message:

1. **A claim about Daniel's role must trace to Profile.md.** If it is not there, it does not go in a deliverable as fact. Draft it, mark it, and list it under "Claims to confirm" in the reply.
2. **Use the weakest verb the evidence supports.** Built / designed (sole, confirmed) > helped guide / co-designed / with Architecture (shared) > documented / wrote the guide for / owns the surface of (exposed). When unsure, go one tier down.
3. **Never upgrade a verb while tailoring.** "Spearheaded" in Profile.md does not become "from PoC to commercial" in a cover letter. Reuse the Profile.md phrasing or quote it.
4. **Public product facts stay product facts.** "Crux applies consent in the network" is fine. "Daniel designed consent in the network" is not, unless Profile.md says so.
5. **Every new material ends with a numbered "Claims to confirm" list** of anything inferred, combined, or newly worded, and Profile.md is updated only after Daniel confirms.
6. **Run `scripts/lint-claims.sh` before sending or committing** application materials. It greps for the phrases that have already been corrected once. Add a phrase to it every time a new correction lands.
7. **Inherited text is not verified text.** Lines that came from an old resume or an earlier session carry the same risk as new inferences. When a line is challenged, fix it everywhere it appears (resumes, letters, tracker, handoff, drafts), not only in the file the user pointed at.

### Compensation Expectations
Target range from Profile.md:318-331: **$226K-$400K** for Principal/Senior Staff level.

Flag jobs below $200K base as potentially under-leveled.

## GitHub Portfolio Integration

Daniel's GitHub (github.com/Daniel085) validates resume claims and demonstrates:
- Active LLM integration work (Claude API, OpenAI)
- WebRTC implementations across platforms
- On-device ML (Core ML)
- Recent 2025-2026 activity surge (8 repos updated Nov 2025-Jan 2026)

When writing about technical background, reference specific repos from Profile.md:127-226.

## Fit Analysis Standards

Use this exact format in `jobs/Similar-Job-Postings.md`:

```markdown
**Fit Analysis:**
✅ **[Strength Category]** - [Specific evidence from Profile.md with metrics]
✅ **[Strength Category]** - [Specific evidence from Profile.md with metrics]
⚠️ **[Gap/Consideration]** - [Honest assessment]
✅ **[Strength Category]** - [Specific evidence from Profile.md with metrics]
```

Always include both strengths (✅) and gaps (⚠️). Honest gap assessment is required.

## Important Context from Profile.md

### Core Expertise (Profile.md:33-62)
API strategy, developer experience, telecom/CPaaS, WebRTC, CAMARA network APIs

### Key Achievements (Profile.md:72-93)
- 10x growth scaling
- $3M revenue capture in 6 months
- 40% support ticket reduction
- 1.5M+ minutes/month platform
- 2 patents

### Competitive Differentiators (Profile.md:263-292)
- Twilio alumni
- CAMARA network API leadership (Charter + Vonage/Ericsson)
- Deep telecom/CPaaS expertise (rare for API PMs)
- Active hands-on technical engagement (GitHub portfolio)

### Areas for Development (Profile.md:295-315)
- SaaS monetization strategy (limited explicit experience)
- Product-Led Growth methodology (implicit experience, needs reframing)
- Generative AI at enterprise scale (hands-on but not shipped)
- Figma/Sketch proficiency (uses alternative prototyping methods)

## Workflow: Evaluating New Job Posting

When the user provides a job posting URL or description:

1. **Fetch job details** - Company, title, requirements, compensation, location, post date
2. **Read Profile.md** - Complete file for background context
3. **Calculate fit score** - Use docs/AI-Assistant-Job-Search.md algorithm (lines 44-68)
   - Start at 0, add/subtract points based on alignment
   - **Only proceed if score ≥75** - Otherwise inform user why not included
4. **Write fit analysis** - Use ✅ for strengths (with specific evidence from Profile.md + metrics) and ⚠️ for honest gaps
5. **Add to jobs/Similar-Job-Postings.md** - Insert in score-sorted order (highest first)
6. **Update "Last Updated" date** at top of file
7. **Optionally save full description** - To jobs/descriptions/{company}.md if user requests it

## Notes

- This is a job search repository, not a software project - no build/test/lint commands
- Focus is on document generation, fit analysis, and application tracking
- All application materials must be tailored, never generic
- GitHub Pages publishes all content - avoid committing sensitive information
- Job links expire - verify before applications
