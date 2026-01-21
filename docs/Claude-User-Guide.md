# Claude Code Reference Guide

*Created: January 7, 2026*

This document provides guidance on working with Claude Code for job search and repository management tasks.

---

## First-Time Setup

If you're setting up this repository for the first time (new user, not Daniel):

### Prerequisites
1. Your resume (PDF or HTML format)
2. Your LinkedIn profile text (copy/paste entire profile)
3. 2-3 example job postings you're interested in

### Setup Process

**Step 1:** Place files in `/setup/inputs/`:
- `resume.pdf` or `resume.html`
- `linkedin-profile.txt`
- `additional-info.txt` (optional)

**Step 2:** Tell Claude:
```
"Help me set up this job search repository. I've placed my resume and
LinkedIn profile in /setup/inputs/"
```

**Step 3:** Follow Claude's prompts:
- Answer clarifying questions (compensation, location, priorities, etc.)
- Review generated Profile.md
- Request any needed edits

**Step 4:** Provide 2-3 seed jobs:
```
"Here are 3 jobs I'm interested in:
1. [URL]
2. [URL]
3. [URL]"
```

**Step 5:** Confirm automated search:
- Claude analyzes patterns
- Shows you common characteristics
- Asks permission to search for similar jobs

**Result:** After 35-50 minutes, you'll have:
- Complete Profile.md (single source of truth)
- 10-20 curated job opportunities with fit scores
- Ready to create tailored application materials

For complete step-by-step instructions, see [`/setup/GETTING-STARTED.md`](/setup/GETTING-STARTED.md).

---

## Repository Contents

### Core Documents

1. **Profile.md** - Daniel O'Rorke's professional profile and background ⭐
   - Comprehensive overview of experience, skills, and achievements
   - GitHub portfolio analysis and AI/ML capabilities
   - Job search priorities and compensation expectations
   - Used as reference for calculating job fit scores

2. **resume-designed.html** - Current resume (HTML format)
   - Updated with AI/ML Technologies section
   - Professional formatting optimized for readability

### Job Descriptions Saved

1. **job-description.md** - Principal Product Manager - API & Developer Platforms
   - Generic role focused on API strategy, developer programs, and cross-functional leadership
   - Requirements: 8-10+ years experience, hands-on API/gateway experience

2. **Wavelo.md** - Senior Technical Product Manager at Wavelo (Tucows)
   - Compensation: $134,100 - $149,000 USD / $120,690 - $134,100 CAD
   - Focus: External integration framework, TM Forum Open API, GSMA CAMARA
   - Requirements: 5+ years technical PM experience

3. **Similar-Job-Postings.md** - Curated list of verified active job postings
   - 7 verified active positions (as of Jan 7, 2026)
   - Includes fit scores (0-100) based on Profile.md
   - Detailed fit analysis for each position
   - Salary ranges: $150,000 - $400,000 USD
   - All links verified working

---

## What Claude Code Can Do

### Job Search Tasks

✅ **Can Do:**
- Search for job postings across multiple platforms
- Extract job details (title, compensation, requirements)
- Verify links are active and working
- Create organized markdown files with job information
- Compare job requirements across multiple positions
- Track and organize job applications
- Commit and push files to git repositories

❌ **Cannot Do:**
- Login to any service with your credentials (LinkedIn, Indeed, etc.)
- Fill out job applications on your behalf
- Access authenticated/private content
- Submit forms or applications
- Maintain browser sessions

### Best Practices for Job Searches

1. **Provide Specific URLs** - If you find a job posting, share the direct URL
2. **Use Public Job Boards** - Sites like Greenhouse, Lever, company career pages work best
3. **Request Verification** - Ask Claude to verify links are still active
4. **Organize by File** - Keep job descriptions in separate markdown files
5. **Track in Git** - Use git commits to track when jobs were added/updated

---

## Using the Profile Document

**Profile.md** is the master reference for evaluating job fit. It contains:

### What's in Profile.md
- **Professional Summary** - 10+ years experience overview
- **Core Expertise** - API strategy, developer experience, telecom/CPaaS
- **Key Achievements** - Metrics: 10x growth, $3M revenue, 40% support reduction
- **GitHub Portfolio** - AI/ML projects, technical depth
- **Strengths & Differentiators** - CAMARA, WebRTC, Twilio alumni
- **Areas for Development** - Monetization, PLG, generative AI at scale
- **Compensation Expectations** - $226K-$400K range
- **Job Search Priorities** - Must-haves and nice-to-haves

### How Claude Uses Profile.md
When you share a job posting, Claude will:
1. Extract job requirements and details
2. Reference Profile.md for your background
3. Compare requirements to your experience
4. Calculate fit score (0-100)
5. Provide detailed fit analysis with ✅ strengths and ⚠️ gaps

### Keeping Profile.md Updated
Update Profile.md when:
- You complete new projects (GitHub work)
- You earn new certifications or awards
- You learn new technologies
- Your compensation expectations change
- You remember forgotten achievements with metrics

**Manual updates:**
```
"Update Profile.md: add [new information]"
```

**Dynamic updates during job search:**
Claude may ask clarifying questions while creating application materials. When you provide new information, Claude will offer to update Profile.md so future applications automatically include it.

Example:
```
Claude: "This role requires GraphQL experience. Have you worked with GraphQL?"
You: "Yes - used it extensively at Company X for 2 years"
Claude: "I'll add GraphQL to your Technical Skills. Future resumes will include this."
```

---

## Automated Job Discovery

### How It Works

Instead of adding jobs one-by-one, you can provide 2-3 "seed jobs" (examples of what you want), and Claude will automatically find similar opportunities.

**Step 1: Provide Seed Jobs**
```
"Here are 3 jobs I'm interested in:
1. https://company1.com/job/api-pm
2. https://company2.com/job/developer-platform
3. https://company3.com/job/staff-pm"
```

**Step 2: Claude Analyzes Patterns**
Claude extracts common characteristics across your seed jobs:
- Role titles and seniority levels
- Required technologies (REST APIs, GraphQL, SDKs, etc.)
- Company types (size, stage, industry)
- Compensation ranges
- Work arrangements (remote, hybrid, on-site)

**Step 3: Confirm Search**
Claude presents the patterns and asks:
```
"I've identified these patterns in your seed jobs:
- Titles: Principal PM, Staff PM
- Tech: REST APIs (100%), GraphQL (67%)
- Companies: B2B SaaS, 500-5000 employees
- Comp: $200K-$350K

Should I search for similar jobs? (Yes/No)"
```

**Step 4: Automated Search**
If you confirm, Claude:
- Generates 5-10 targeted search queries
- Uses WebSearch to find jobs posted in last 60 days
- Fetches each job description
- Calculates fit scores using your Profile.md
- Only includes jobs scoring ≥75
- Saves all to `/jobs/Similar-Job-Postings.md`

**Step 5: Results**
```
"Found 14 jobs matching your criteria:
- 4 excellent matches (90-100 fit)
- 7 strong matches (80-89 fit)
- 3 good matches (75-79 fit)

Top 3:
1. Company X - Principal PM API (95/100) - $225K-$375K
2. Company Y - Staff PM DevTools (92/100) - $200K-$320K
3. Company Z - Senior Staff PM (88/100) - $240K-$400K"
```

### Benefits
- **Time savings:** Find 10-20 curated opportunities in 10-15 minutes
- **Quality filtering:** Only jobs scoring ≥75 are included
- **Consistent evaluation:** All jobs evaluated using same algorithm
- **Pattern-based:** Finds jobs similar to what you've indicated you want

### When to Use
- Initial repository setup (after Profile.md is created)
- When pivoting to different role types
- Periodically to refresh your job list (monthly)
- When seed jobs produced good results previously

---

## Dynamic Profile Updates

### What It Does

While creating tailored application materials, Claude may discover gaps between job requirements and your Profile.md. Instead of just noting the gap, Claude asks clarifying questions and updates your Profile so future applications benefit.

### How It Works

**Scenario:** Creating resume for fintech API role

**Trigger:**
```
Job requires: "Payment API experience and PCI-DSS compliance"
Profile.md: No payment APIs or compliance mentioned
```

**Claude asks:**
```
"I'm tailoring your resume for Company X's API Platform role.
They require payment API and compliance experience.

Questions:
1. Have you worked with payment APIs (Stripe, Plaid, etc.)? (Yes/No/Details)
2. Any PCI-DSS, SOC2, or compliance experience? (Yes/No/Details)
3. Relevant fintech experience to highlight? (Yes/No/Details)"
```

**You respond:**
```
"Yes - integrated Stripe at Company Y. Led SOC2 compliance for our API platform."
```

**Claude updates Profile.md:**
```
"I'll update your Profile.md:
- Technical Skills: Add 'Payment APIs (Stripe)'
- Domain Expertise: Add 'Financial APIs'
- Key Achievements: Add 'Led SOC2 compliance for API platform'

Your updated Profile will be used for this resume and all future applications."
```

### Benefits
- **Continuous improvement:** Profile gets richer over time
- **No repetition:** Answer once, benefit forever
- **Consistent messaging:** All future materials include new information
- **Better fit scores:** More complete Profile leads to more accurate scoring

### When It Happens
- Creating tailored resumes → job requirement not in Profile.md
- Writing cover letters → need specific metric/example
- User explicitly requests: "Update Profile.md: [info]"

### Important
- Claude always asks permission before updating
- You'll see exact changes before they're applied
- You can reject or modify suggested updates
- Only factual information you confirm gets added
- You discover new preferences in job search

---

## Common Tasks & Commands

### Search for Similar Jobs

```
"Find jobs similar to [job title] with [specific requirements]"
"Search for API Product Manager roles posted in the last 90 days"
```

### Evaluate Job Fit

```
"Here's a job link: [URL] - please evaluate fit"
"Add this job to Similar-Job-Postings.md with fit analysis"
"Compare my profile to this job description"
```

### Verify Job Postings

```
"Verify all links in Similar-Job-Postings.md still work"
"Check if [URL] is still an active posting"
```

### Organize Job Information

```
"Create a markdown file with [job details]"
"Extract compensation and requirements from [URL]"
```

### Update Profile

```
"I completed [project/achievement] - please update Profile.md"
"Add [skill/technology] to my profile"
"Review my GitHub for updates"
```

### Git Operations

```
"Commit these changes with message: [your message]"
"Push to branch [branch-name]"
```

---

## Job Search Resources

### Recommended Job Boards

**API/Developer Platform Roles:**
- [Greenhouse Job Boards](https://boards.greenhouse.io/) - Many tech companies
- [Lever Job Boards](https://jobs.lever.co/) - Startups and tech companies
- [LinkedIn Jobs](https://www.linkedin.com/jobs/) - 9,000+ API PM roles
- [Wellfound](https://wellfound.com/) - Startup-focused
- [Built In](https://builtin.com/) - Tech hubs (SF, NYC, etc.)

**Company Career Pages:**
- Anthropic, Stripe, Twilio, Postman, Kong, Plaid
- PagerDuty, Salesforce, AWS, Google Cloud, Microsoft Azure

### Search Keywords

For roles similar to your saved job descriptions:
- "API Product Manager"
- "Principal Product Manager API"
- "Developer Platform Product Manager"
- "Technical Product Manager API"
- "Product Manager Developer Experience"
- "Senior Product Manager API Platform"

### Filters to Use

- **Date Posted:** Last 30 days or Last 90 days
- **Experience Level:** Senior, Staff, Principal, Director
- **Location:** Remote, or specific cities
- **Salary Range:** $150K - $400K (based on your target roles)

---

## Salary Benchmarks (2026)

Based on verified postings in Similar-Job-Postings.md:

| Level | Salary Range (USD) | Companies |
|-------|-------------------|-----------|
| Senior PM | $160K - $230K | Postman |
| Staff PM | $152K - $224K | Twilio |
| Principal PM | $180K - $304K | PagerDuty |
| Senior Staff PM | $226K - $400K | Plaid |
| PM (AI Focus) | $305K - $385K | Anthropic |

**Note:** Ranges vary by location (SF/NYC highest, other cities 10-30% lower)

---

## Key Requirements Across Roles

### Common Must-Haves
- 5-10+ years product management experience
- Strong API platform/developer tools background
- RESTful API design expertise
- Cross-functional leadership skills
- Developer-first mindset

### Preferred Skills
- Technical background (CS degree or engineering experience)
- Experience with API gateways, microservices
- Developer community building
- Telecom/communications industry (for specialized roles)
- TM Forum Open API, GSMA CAMARA (for telecom)

---

## Security Best Practices

### ✅ Safe to Share with Claude
- Public job posting URLs
- Company career page links
- Your resume/CV content
- Job descriptions
- Requirements for job searches

### ❌ Never Share with Claude (or anyone)
- Usernames and passwords
- Authentication tokens
- Social Security Number or similar IDs
- Private/confidential company information
- API keys or credentials

---

## Tips for Working with Claude Code

1. **Be Specific** - "Find API PM jobs posted in last 30 days with $200K+ salary"
2. **Verify Links** - Ask Claude to verify links before applying
3. **Save Everything** - Keep job descriptions in markdown for easy reference
4. **Use Git** - Track changes so you can see when jobs were added
5. **Ask for Comparisons** - "Compare requirements between these 3 roles"
6. **Request Summaries** - "Summarize the key differences in these job postings"

---

## Current Branch

**Branch Name:** `claude/add-job-description-rtifT`

All job-related files are tracked in this branch. Use this branch for future job search updates.

---

## Workflow for Evaluating New Jobs

### Step 1: Share the Job
```
"Here's a job posting: [URL]"
```

### Step 2: Claude Will Automatically:
1. Fetch job details (title, company, compensation, requirements)
2. Reference **Profile.md** for your background
3. Calculate fit score (0-100)
4. Provide detailed analysis comparing requirements to your experience
5. Add to Similar-Job-Postings.md with verified link

### Step 3: Review Fit Analysis
- **95-100:** Excellent match - prioritize application
- **85-94:** Strong fit - good opportunity
- **75-84:** Moderate fit - consider gaps
- **<75:** Weaker match - may require skill development

### Step 4: Apply or Pass
Based on fit score, compensation, and your priorities

---

## Next Steps

### To Continue Job Search:
1. Review **Similar-Job-Postings.md** for active opportunities sorted by fit score
2. Ask Claude to search for new postings in specific areas
3. Request verification of links before applying
4. Add new interesting roles to the repository

### To Apply:
1. Review each job description and fit analysis carefully
2. Verify the link is still active
3. Tailor your application based on fit analysis (highlight ✅ strengths, address ⚠️ gaps)
4. Visit the company career page directly
5. Apply through their official application system
6. Track applications in a separate file (e.g., Applications-Tracker.md)

### To Update Your Profile:
```
"I completed [new project/achievement] - update Profile.md"
"Review my GitHub for recent updates"
```

---

## Important Files Reference

| File | Purpose | When to Use |
|------|---------|-------------|
| **Profile.md** | Your master professional profile | Reference for all job evaluations |
| **resume-designed.html** | Current resume | For applications |
| **Similar-Job-Postings.md** | Active job opportunities with fit scores | Daily job search review |
| **Claude.md** | This guide | When you need help using Claude for job search |

---

## Questions or Issues?

If you need help with:
- Finding more similar jobs → "Search for [specific criteria]"
- Evaluating a job → "Here's a job link: [URL]"
- Verifying a link → "Check if this URL still works: [URL]"
- Extracting info → "Get compensation details from [URL]"
- Organizing data → "Create a table comparing these 5 roles"
- Updating profile → "Add [new skill/achievement] to Profile.md"
- Git operations → "Commit and push these changes"

---

*This document will be updated as new job search strategies and resources are discovered.*
