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

Located in `docs/AI-Assistant-Job-Search.md` (lines 44-68). Key scoring rules:

- **Start at 0, add/subtract points based on alignment**
- Direct technology experience: +10-20 points
- Exceeds YoE requirement: +5-10 points
- Domain expertise match: +10-15 points
- Missing required skills: -10-20 points
- Industry mismatch: -5-10 points
- **Minimum inclusion threshold: 75/100**
- Jobs older than 60 days: exclude

When adding jobs to `jobs/Similar-Job-Postings.md`, calculate fit score using Profile.md:1-435 for background reference.

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

## Common Development Tasks

### Adding a New Job Posting

```bash
# 1. Fetch and analyze job description
# 2. Read Profile.md for fit scoring
# 3. Add to jobs/Similar-Job-Postings.md with fit score ≥75
# 4. Maintain sort order (highest fit scores first)
# 5. Update "Last Updated" date
# 6. Optionally save full job description to jobs/descriptions/{company}.md
```

See `docs/AI-Assistant-Job-Search.md` for detailed instructions on fit analysis format.

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
# Current branch: claude/init-project-setup-ILHXq
git add .
git commit -m "Descriptive message"
git push -u origin claude/init-project-setup-ILHXq
```

GitHub Pages deployment runs on push (see `.github/workflows/static.yml`).

## File Organization

### Root Directory
- `Profile.md` - Professional background, skills, achievements (SINGLE SOURCE OF TRUTH)
- `CLAUDE.md` - This file - instructions for Claude Code
- `README.md` - Repository overview and navigation guide

### Documentation (`docs/`)
- `AI-Assistant-Job-Search.md` - Fit scoring algorithm and workflow instructions
- `Claude-User-Guide.md` - User guide for working with Claude Code

### Resumes (`resumes/`)
- `resume-designed.html` - Base resume template
- `resume-{company}.html` - Company-specific tailored resumes (anthropic, lightyear, pagerduty, plaid, postman, twilio, zoom)

### Cover Letters (`cover-letters/`)
- `cover-letter-{company}.md` - Company-specific cover letters (anthropic, lightyear, pagerduty, plaid, postman, twilio, zoom)

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

1. **Fetch job details** - Company, title, requirements, compensation, location, post date
2. **Read Profile.md** - Lines 1-435 for complete background
3. **Calculate fit score** - Use docs/AI-Assistant-Job-Search.md algorithm (lines 44-68)
4. **Only proceed if ≥75 score** - Otherwise inform user why not included
5. **Write fit analysis** - ✅ strengths with specific evidence + ⚠️ honest gaps
6. **Add to jobs/Similar-Job-Postings.md** - Maintain score-sorted order
7. **Update "Last Updated" date**
8. **Optionally save full description** - To jobs/descriptions/{company}.md

## Notes

- This is a job search repository, not a software project - no build/test/lint commands
- Focus is on document generation, fit analysis, and application tracking
- All application materials must be tailored, never generic
- GitHub Pages publishes all content - avoid committing sensitive information
- Job links expire - verify before applications
