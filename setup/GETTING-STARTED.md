# Getting Started - New User Setup

Welcome to your personalized job search repository! This guide will help you set up the system in about 45 minutes.

## What You'll Need

Before starting, gather these materials:

- ✅ **Your current resume** (PDF or HTML format)
- ✅ **Your LinkedIn profile text** (copy/paste your entire profile into a .txt file)
- ✅ **2-3 example job postings** you're interested in (URLs)
- ✅ **Claude Code** installed and configured

---

## Setup Overview

The setup process has 4 main steps:

1. **Prepare Input Files** (5 minutes) - Place your resume and LinkedIn text in the right folder
2. **Generate Your Profile.md** (15-20 minutes) - Claude creates your professional profile
3. **Analyze Seed Jobs** (5-10 minutes) - Claude learns what types of jobs you want
4. **Discover Similar Jobs** (10-15 minutes) - Claude finds 10-20 curated opportunities

**Total time:** 35-50 minutes

---

## Step 1: Prepare Your Input Files (5 minutes)

### 1.1 Create Your Input Files

**Resume File:**
- Save as `resume.pdf` or `resume.html`
- Should include: work history, skills, education, achievements
- Don't worry about perfect formatting - Claude will extract the information

**LinkedIn Profile:**
1. Go to your LinkedIn profile
2. Copy your entire profile text including:
   - Summary/About section
   - All work experience descriptions
   - Skills section
   - Education
   - Certifications
   - Projects or publications (if any)
3. Paste into a file named `linkedin-profile.txt`

**Additional Info (Optional):**
- Create `additional-info.txt` if you have context not on resume/LinkedIn:
  - Specific achievements with metrics
  - Technologies you know but aren't listed
  - Compensation expectations
  - Job search priorities

### 1.2 Place Files in `/setup/inputs/`

Your directory should look like:
```
/setup/inputs/
  ├── resume.pdf  (or resume.html)
  ├── linkedin-profile.txt
  └── additional-info.txt  (optional)
```

---

## Step 2: Generate Your Profile.md (15-20 minutes)

### 2.1 Invoke Claude Code

Tell Claude:
```
"Help me set up this job search repository. I've placed my resume and
LinkedIn profile in /setup/inputs/"
```

### 2.2 What Claude Will Do

Claude will:
1. Read your resume and LinkedIn files
2. Extract key information (contact, experience, skills, achievements)
3. Ask you 5-7 clarifying questions
4. Generate your `/Profile.md` file
5. Present it for your review

### 2.3 Answer Clarifying Questions

Claude will ask questions like:

**Compensation Expectations**
```
What's your target salary range for your next role?
Example: "$180K-$280K total compensation for Principal PM level"
```

Be realistic based on:
- Your years of experience
- Your target seniority level
- Your location (remote roles often have location-based bands)
- Market rates for 2026

**Location Preferences**
```
Are you open to remote, hybrid, or specific cities?
```

Options:
- "Remote only"
- "Hybrid - San Francisco Bay Area"
- "Remote or hybrid in NYC, Seattle, Austin"

**Job Search Priorities**
```
What are your top 3 must-haves in your next role?
```

Examples:
- "API platform or developer tools focus"
- "IC role (not people management)"
- "B2B SaaS company"
- "Minimum $200K base salary"

**GitHub Portfolio** (if applicable)
```
Should I analyze your GitHub repositories for your profile?
```

Say "Yes" if you have:
- Projects demonstrating technical depth
- Code samples relevant to PM work
- Open source contributions

Say "No" if your GitHub is:
- Empty or minimal activity
- Only private repos
- Not relevant to your PM work

**Domain Expertise**
```
Which industries do you have the strongest background in?
```

Examples:
- "Fintech / financial services"
- "Healthcare / health tech"
- "Developer tools / API platforms"
- "E-commerce / marketplace"

**Target Career Level**
```
What seniority level are you targeting?
```

Options:
- Senior Product Manager (5-8 years experience)
- Staff PM (8-12 years)
- Senior Staff PM (10-15 years)
- Principal PM (12+ years)

### 2.4 Review Your Profile.md

Claude will create `/Profile.md` and show you a summary:

```markdown
I've created your Profile.md with:
- 15 sections covering your professional background
- 18 extracted skills and technologies
- 5 quantified achievements
- 8 years of work history

Please review /Profile.md and let me know:
1. Are there any achievements or metrics I missed?
2. Should I add or emphasize any specific technologies?
3. Do the "Areas for Development" seem accurate?
4. Any corrections to job titles, dates, or companies?
```

**Read through Profile.md carefully.** This becomes your single source of truth - everything else derives from it.

### 2.5 Request Edits

If something is missing or incorrect, tell Claude specifically:

```
"Add this achievement: Reduced API latency by 40% through caching optimization"

"Update my current role end date to 'Present' instead of a specific date"

"Add GraphQL to my technical skills under APIs & Integration"

"Change compensation range to $200K-$350K"
```

Claude will update Profile.md and show you the changes.

---

## Step 3: Provide Seed Jobs (5-10 minutes)

### 3.1 Find 2-3 Example Jobs

Find job postings that represent what you're looking for. These can be:
- Jobs you're genuinely interested in applying to
- Roles similar to what you want
- Positions you'd be excited about

**Where to find jobs:**
- Company career pages
- LinkedIn Jobs
- Indeed, Glassdoor
- Specialized job boards (e.g., Wellfound for startups, Levels.fyi)

**Copy the full URLs**, for example:
- `https://company1.com/careers/principal-pm-api-platform`
- `https://boards.greenhouse.io/company2/jobs/123456`
- `https://linkedin.com/jobs/view/123456789`

### 3.2 Share Jobs with Claude

Tell Claude:
```
"Here are 3 jobs I'm interested in:
1. https://company1.com/job/api-pm
2. https://company2.com/job/developer-platform
3. https://company3.com/job/staff-pm"
```

### 3.3 Claude Analyzes Patterns

Claude will:
1. Fetch each job description
2. Calculate fit scores (using your Profile.md)
3. Identify common patterns across the 3 jobs
4. Save to `/jobs/Seed-Jobs.md`

Example output:
```markdown
Analyzing your 3 seed jobs, I've identified these patterns:

**Common Role Characteristics:**
- Titles: "Principal PM", "Staff PM", "Senior PM API"
- Focus: API platforms, Developer Experience, Enterprise SaaS
- Required experience: 8-10+ years
- Technical depth: REST APIs, SDKs, developer tools

**Common Technologies:**
- REST APIs (100% of jobs)
- GraphQL (67%)
- Developer portals/documentation (100%)
- SDK development (67%)

**Company Profiles:**
- B2B SaaS with API products
- 500-5000 employees
- Series C-D or public companies

**Compensation Ranges:**
- Base: $180K-$280K
- Total comp: $250K-$450K

Should I search for similar jobs matching these patterns? (Yes/No)
```

### 3.4 Confirm Pattern Search

Review the patterns. If they look right, say **"Yes"** to trigger automated job discovery.

If patterns seem off, you can:
- Provide different seed jobs
- Clarify what you're looking for: "Focus more on API platform roles, less on generic PM"

---

## Step 4: Automated Job Discovery (10-15 minutes)

### 4.1 Claude Searches for Similar Jobs

When you confirm, Claude will:
1. Generate 5-10 targeted search queries based on patterns
2. Use WebSearch to find jobs posted in last 60 days
3. Fetch each job description
4. Calculate fit scores using your Profile.md
5. Only include jobs scoring ≥75
6. Write detailed fit analysis for each (✅ strengths + ⚠️ gaps)
7. Populate `/jobs/Similar-Job-Postings.md` sorted by fit score

This process takes 10-15 minutes depending on how many jobs are found.

### 4.2 Review Job Results

Claude will report findings:

```markdown
Found 14 jobs matching your criteria:

**Fit Score Breakdown:**
- 90-100 (Excellent matches): 4 jobs
- 80-89 (Strong matches): 7 jobs
- 75-79 (Good matches): 3 jobs

**Top 5 Matches:**
1. Company X - Principal PM API Platform (95/100) - $225K-$375K
   ✅ Perfect API platform match, telecom experience valued
   ⚠️ Prefer GraphQL experience (you have REST only)

2. Company Y - Staff PM Developer Tools (92/100) - $200K-$320K
   ✅ Developer experience focus aligns perfectly
   ✅ Remote-first matches your preference
   ⚠️ Compensation slightly below your target range

3. Company Z - Senior Staff PM Platform (90/100) - $240K-$400K
   ✅ Exceeds compensation expectations
   ✅ Enterprise SaaS experience required - you have 8+ years
   ⚠️ Requires some blockchain knowledge (gap for you)

All jobs saved to /jobs/Similar-Job-Postings.md

Ready to create tailored resumes for top matches? (Yes/No)
```

### 4.3 Next Steps

At this point, you have:
- ✅ Complete Profile.md (single source of truth)
- ✅ Seed jobs analyzed in `/jobs/Seed-Jobs.md`
- ✅ 10-20 curated job opportunities in `/jobs/Similar-Job-Postings.md` with fit scores

You're now ready to create tailored application materials!

---

## Creating Application Materials

### For Any Job in Your List

Tell Claude:
```
"Create a tailored resume and cover letter for [Company] [Role Title]"
```

Example:
```
"Create a tailored resume and cover letter for Company X Principal PM API Platform"
```

Claude will:
1. Read the job requirements from `/jobs/descriptions/CompanyX.md`
2. Identify key requirements and must-haves
3. Customize your resume highlighting relevant Profile.md experience
4. Write a cover letter with specific examples matching job needs
5. Ensure 2-page resume format (exact fit when printed)
6. Save to `/resumes/resume-companyx.html` and `/cover-letters/cover-letter-companyx.md`

**If Claude finds gaps:**

While creating materials, Claude might ask:
```
"This role requires payment API experience. Have you worked with Stripe,
Plaid, or financial APIs? (Yes/No/Details)"
```

When you provide information, Claude will:
- Update your Profile.md with the new details
- Use the updated profile for this resume and all future ones

### Adding More Jobs Manually

As you find new jobs:
```
"Add this job to my tracking: [URL]"
```

Claude will:
- Fetch the job description
- Calculate fit score
- Add to `/jobs/Similar-Job-Postings.md` if score ≥75
- Tell you the fit score and analysis

---

## Troubleshooting

### "Claude can't parse my resume PDF"

**Solution:** Convert to HTML or provide plain text in `additional-info.txt`:
```
# additional-info.txt
WORK EXPERIENCE:

Senior Product Manager, Company Name (2022-Present)
- Led API platform serving 1M+ developers
- Increased adoption 200% through improved documentation
...
```

### "My compensation expectations changed"

**Solution:** Either:
1. Edit `/Profile.md` directly (search for "Compensation Expectations" section)
2. Tell Claude: `"Update my compensation range to $X-$Y in Profile.md"`

### "Automated search found too few jobs"

**Possible causes:**
- Seed jobs too niche
- Fit threshold too strict
- Search timing (try different time of week/month)

**Solutions:**
- Provide broader seed jobs
- Temporarily lower threshold: `"Search with minimum fit score of 70 instead of 75"`
- Try more generic role titles

### "Job fit scores seem inaccurate"

**Check:**
1. Is your Profile.md complete? Missing skills lower scores.
2. Are "Areas for Development" honest? These subtract points appropriately.
3. Do "Notes for Job Fit Evaluation" match your actual priorities?

**Fix:** Update Profile.md with missing information, then tell Claude:
```
"Recalculate fit scores for all jobs in Similar-Job-Postings.md"
```

### "I want to target different types of roles now"

**Solution:** Provide new seed jobs:
```
"I want to pivot focus. Here are 3 new seed jobs:
1. [URL for different role type]
2. [URL]
3. [URL]

Please analyze patterns and search for similar jobs."
```

---

## Tips for Success

### 1. Keep Profile.md Current

Your Profile.md is living document. When you:
- Complete a new project → Add achievement with metrics
- Learn a new technology → Add to Technical Skills
- Get a promotion → Update Current Role and Experience Timeline
- Remember a forgotten achievement → Add to Key Achievements

Tell Claude: `"Update Profile.md: [what changed]"`

### 2. Quality Over Quantity for Jobs

A 95/100 fit job deserves 10x more attention than a 76/100 job.

**Focus your effort:**
- 90-100 scores: Tailored resume + cover letter + research company
- 80-89 scores: Tailored resume + short cover letter
- 75-79 scores: Monitor, but only apply if others don't work out

### 3. Understand Your Fit Analyses

The ✅ strengths and ⚠️ gaps help you:
- **Tailor your resume** - Emphasize strengths, address gaps
- **Prepare for interviews** - Anticipate questions about gaps
- **Prioritize applications** - Jobs with minor gaps > jobs with major gaps

### 4. Verify Links Before Applying

Job links expire fast (30-60 days typical).

Before spending time on application:
```
"Verify this job link still works: [URL]"
```

If closed, Claude can check company career site for similar roles.

### 5. Track Your Applications

Create `/jobs/Applications-Tracker.md` to monitor:
- Which jobs you applied to
- When you applied
- Status (submitted, phone screen, onsite, offer, rejected)

Tell Claude:
```
"Create an applications tracker and add [Company] [Role] as applied on [date]"
```

---

## What's Next?

### Immediate Actions (Today)
1. ✅ Place resume and LinkedIn in `/setup/inputs/`
2. ✅ Generate Profile.md with Claude
3. ✅ Provide 2-3 seed jobs
4. ✅ Review discovered job opportunities

### This Week
- Create tailored resumes for your top 3-5 matches
- Write cover letters for highest fit jobs
- Research companies for those roles
- Submit applications

### Ongoing
- Add new jobs as you find them
- Update Profile.md when you complete achievements
- Refine your "must-haves" based on what you're learning
- Track application responses

---

## Need Help?

**Documentation:**
- `/docs/Claude-User-Guide.md` - How to interact with Claude
- `/docs/AI-Assistant-Job-Search.md` - How fit scoring works
- `/CLAUDE.md` - Complete workflow documentation
- `/examples/Profile-example.md` - See a complete working profile

**Common Commands:**
```bash
# Generate Profile from inputs
"Help me set up this job search repository"

# Add a job
"Add this job: [URL]"

# Create materials
"Create resume and cover letter for [Company] [Role]"

# Update profile
"Update Profile.md: add [new information]"

# Recalculate fits
"Recalculate fit scores for all jobs"

# Find more jobs
"Search for more [role type] jobs"
```

---

## You're Ready!

Once you complete Step 4, you'll have:
- ✅ Professional Profile.md (single source of truth)
- ✅ 10-20 curated job opportunities with fit scores
- ✅ Clear understanding of your strengths and gaps
- ✅ System ready to generate tailored application materials

**Start your setup now by placing your files in `/setup/inputs/` and telling Claude:**

```
"Help me set up this job search repository. I've placed my resume and
LinkedIn profile in /setup/inputs/"
```

Good luck with your job search! 🚀
