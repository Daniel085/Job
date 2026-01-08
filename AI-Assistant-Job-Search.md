# AI Assistant Instructions: Building a Similar Jobs File

## Purpose
This document provides instructions for an AI assistant to take a resume and job descriptions, then create a curated list of similar job postings with fit analysis.

## Input Files Required
1. **Resume file** (HTML or Markdown format) - Contains the candidate's professional background
2. **Job description files** - One or more job postings to use as reference
3. **Profile.md** (optional but recommended) - Comprehensive background information about the candidate

## Output File
Create a file named `Similar-Job-Postings.md` with job postings that match the candidate's background.

## Process Overview

### Step 1: Understand the Candidate's Background
Read all provided files to understand:
- Years of experience and seniority level
- Technical skills and domain expertise
- Industry background (e.g., telecom, CPaaS, SaaS, fintech)
- Key achievements and metrics
- Current role and responsibilities
- Career trajectory and focus areas

### Step 2: Identify Key Search Criteria
Based on the resume and reference job descriptions, identify:
- **Job titles** to search for (e.g., "Principal Product Manager API", "Staff PM Developer Platform")
- **Required skills** (e.g., REST APIs, developer tools, platform scaling)
- **Industry focus** (e.g., developer tools, communications, fintech)
- **Company types** (e.g., enterprise SaaS, API-first companies, platform companies)

### Step 3: Search for Similar Positions
Search for job postings using web search with queries like:
- "[Job Title] [Year]" (e.g., "Principal Product Manager API 2026")
- "[Company] [Job Title]" for target companies
- "[Skill] Product Manager jobs [Year]"

**Filtering Criteria:**
- **Posted date:** Within last 60 days only
- **Status:** Currently accepting applications (not closed)
- **Relevance:** Strong alignment with candidate's background

### Step 4: Calculate Fit Score (0-100)
For each job posting, assign a fit score based on:

**High fit indicators (add points):**
- Direct experience with required technologies (+10-20 points)
- Exceeds years of experience requirement (+5-10 points)
- Proven track record in required domain (+10-15 points)
- Previous experience at similar companies (+5-10 points)
- Relevant leadership experience if required (+10-15 points)
- Matching seniority level (+5-10 points)
- Relevant certifications or patents (+5 points)

**Gaps or concerns (subtract points):**
- Missing required technical skills (-10-20 points)
- Below experience requirement (-10-15 points)
- Different industry background (-5-10 points)
- Geographic constraints if role isn't remote (-5-10 points)
- Compensation significantly below market value (-5 points)

**Score ranges:**
- **95-100:** Near-perfect match
- **85-94:** Excellent match with minor gaps
- **75-84:** Strong match with some gaps
- **60-74:** Moderate match, significant gaps
- **Below 60:** Poor match, do not include

**ONLY include jobs with fit score ≥75%**

### Step 5: Create Fit Analysis
For each job, provide:

**Strengths (use ✅):**
- List specific experiences, skills, or achievements that align with job requirements
- Include metrics and concrete examples from the resume
- Highlight competitive advantages

**Gaps or Considerations (use ⚠️):**
- Note any missing requirements or potential concerns
- Include compensation considerations if relevant
- Mention areas where candidate may need to demonstrate capability

### Step 6: Format the Output File

Use this structure:

```markdown
# Similar [Job Category] Roles

*Last Updated: [Date]*

This document contains active job postings for [job category] roles with similar requirements to [reference positions]. Each position includes a fit score (0-100) based on alignment with [Candidate Name]'s resume.

---

## Posted Within Last 60 Days

### 1. **[Job Title]** 🔥 **FIT SCORE: [XX]/100**
**Company:** [Company Name]
**Location:** [Location]
**Compensation:** [Salary Range]
**Posted:** [Date Posted]
**Link:** [Application URL]

**Key Requirements:**
- [Requirement 1]
- [Requirement 2]
- [Bonus requirement if applicable]

**Fit Analysis:**
✅ **[Strength category]** - [Specific evidence from resume]
✅ **[Strength category]** - [Specific evidence from resume]
⚠️ **[Gap or consideration]** - [Explanation]
✅ **[Strength category]** - [Specific evidence from resume]

---

[Repeat for each position]

---

## Additional Resources

### Job Search Platforms
- [Relevant job boards]
- [Industry-specific platforms]

### Companies Actively Hiring
- [List of companies in target space]

---

## Notes

**Verification Status:** All links verified as of [Date]
**Salary Market Range:** [Typical range for this role category]
**Common Requirements:**
- [Common requirement 1]
- [Common requirement 2]
- [Common requirement 3]
```

## Best Practices

### 1. Verify Links Work
- Test each application URL before including it
- Note if link requires authentication (e.g., LinkedIn)
- If link is broken or inaccessible, do not include the posting

### 2. Be Honest in Fit Analysis
- Don't overstate qualifications
- Include genuine gaps or concerns
- Balance strengths and areas for growth

### 3. Use Specific Evidence
- Reference specific roles, companies, and achievements from resume
- Include metrics when available (e.g., "10+ years vs. 5+ required")
- Cite concrete examples rather than generic statements

### 4. Prioritize Quality Over Quantity
- Better to have 5 high-quality matches (85-100 fit) than 20 mediocre ones
- Only include jobs genuinely worth applying to
- Don't force-fit positions that aren't aligned

### 5. Keep Information Current
- Note the last update date
- Mark closed positions clearly
- Verify posting dates are within 60-day window

### 6. Consider Compensation Appropriately
- Flag if compensation is significantly below candidate's level
- Note if equity/benefits may compensate for lower base
- Consider geographic cost of living differences

### 7. Use Clear Language
- Avoid superlatives and hype
- Use precise technical terminology
- Write fit analysis that could inform application strategy

## Example Fit Score Calculation

**Example Job:** Principal Product Manager - Developer Platform
**Candidate:** 10 years PM experience, 5 years in API platforms, managed team of 5 PMs

**Scoring:**
- Required: 5+ years PM experience → Candidate has 10+ years (+10 points) = 10
- Required: Deep API platform knowledge → 5 years direct experience (+20 points) = 30
- Required: Team leadership → Managed 5 PMs (+15 points) = 45
- Required: Enterprise SaaS → Multiple enterprise roles (+15 points) = 60
- Preferred: Developer tools expertise → Built developer consoles (+10 points) = 70
- Preferred: Cross-functional leadership → Led across Eng/GTM (+10 points) = 80
- Strong compensation match → Upper range appropriate (+5 points) = 85
- Location: Remote → Perfect match (+5 points) = 90

**Final Score: 90/100** - Include with "Excellent match" rating

## Common Pitfalls to Avoid

1. **Don't include jobs older than 60 days** - They're likely filled or stale
2. **Don't include jobs below 75% fit** - Not worth the candidate's time
3. **Don't guess at requirements** - Only include if you can verify from job posting
4. **Don't exaggerate fit** - Be honest about gaps
5. **Don't include broken links** - Test every URL
6. **Don't use generic fit analysis** - Make it specific to the candidate and role
7. **Don't skip the verification date** - Users need to know how current the information is

## Updating the File

When adding new positions:
1. Update the "Last Updated" date at the top
2. Verify all existing links still work
3. Move closed positions to a "Recently Closed" section
4. Maintain fit score ordering (highest scores first)
5. Ensure all new positions meet the 60-day and 75% fit criteria

## Questions to Ask Candidate (If Needed)

If you need clarification to assess fit:
- "Do you have experience with [specific technology mentioned in JD]?"
- "Have you worked with [company type/industry]?"
- "What's your target compensation range?"
- "Are you open to [location type, e.g., hybrid vs remote]?"
- "Do you have experience in [specific domain area]?"

Store answers in Profile.md for future reference.
