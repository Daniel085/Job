# Claude Code Reference Guide

*Created: January 7, 2026*

This document provides guidance on working with Claude Code for job search and repository management tasks.

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
