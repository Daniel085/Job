# Seed Jobs - Initial Examples

<!-- These are 2-3 job postings you've identified as representing what you're looking for. Claude will analyze these to understand your preferences and search for similar opportunities. -->

*Last Updated: [Date]*

---

## Purpose

Seed jobs help Claude understand what types of roles you're interested in by analyzing:
- Common role titles and seniority levels
- Required technologies and skills
- Company characteristics (size, stage, industry)
- Compensation ranges
- Work arrangements (remote, hybrid, on-site)

**Provide 2-3 jobs that:**
- You're genuinely interested in OR
- Represent the type of role you want OR
- You've had success getting callbacks for

---

## Seed Job 1: [Company Name] - [Role Title]

**URL:** [Full job posting URL]
**Posted:** [Date found/posted]
**Status:** [Bookmarked / Applied / Callback / Pass]

**Why this job:**
<!-- 1-2 sentences on what appeals to you about this specific role -->
[What excites you about this role?]

**Key Requirements:**
- [Requirement 1 from job posting]
- [Requirement 2]
- [Requirement 3]

**Compensation:** [Range if listed]
**Location:** [Location/Remote status]

**Fit Score:** [Will be calculated by Claude]

**Fit Analysis:**
<!-- Claude will add this -->

---

## Seed Job 2: [Company Name] - [Role Title]

**URL:** [Full job posting URL]
**Posted:** [Date found/posted]
**Status:** [Bookmarked / Applied / Callback / Pass]

**Why this job:**
[What appeals to you about this role?]

**Key Requirements:**
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

**Compensation:** [Range if listed]
**Location:** [Location/Remote status]

**Fit Score:** [Will be calculated]

**Fit Analysis:**
<!-- Claude will add this -->

---

## Seed Job 3: [Company Name] - [Role Title]

**URL:** [Full job posting URL]
**Posted:** [Date found/posted]
**Status:** [Bookmarked / Applied / Callback / Pass]

**Why this job:**
[What appeals to you]

**Key Requirements:**
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

**Compensation:** [Range if listed]
**Location:** [Location/Remote status]

**Fit Score:** [Will be calculated]

**Fit Analysis:**
<!-- Claude will add this -->

---

## Pattern Analysis

<!-- After analyzing your seed jobs, Claude will extract common patterns here -->

### Common Role Characteristics
- **Titles:** [e.g., "Principal PM", "Staff PM API", "Senior PM Platform"]
- **Seniority:** [e.g., "Principal/Staff level (10+ years)"]
- **Focus Areas:** [e.g., "API platforms, Developer Experience, Enterprise SaaS"]

### Common Technologies & Skills
- **Required (100% of jobs):** [Technologies appearing in all jobs]
- **Frequently Mentioned (67%+):** [Technologies in 2+ jobs]
- **Nice-to-Have:** [Technologies in only 1 job]

### Company Profiles
- **Size:** [e.g., "500-5000 employees, Series C-D or public"]
- **Industry:** [e.g., "B2B SaaS, API-first companies, developer tools"]
- **Stage:** [e.g., "Growth stage, post-PMF"]

### Compensation Patterns
- **Base Salary Range:** $[X]K - $[Y]K
- **Total Comp Range:** $[X]K - $[Y]K
- **Equity:** [Standard/Significant/Minimal]

### Work Arrangements
- **Remote:** [X out of 3 jobs]
- **Hybrid:** [X out of 3 jobs]
- **On-site:** [X out of 3 jobs]

---

## Search Strategy

Based on these patterns, Claude will search for jobs matching:

**Search Queries:**
<!-- Claude will generate these -->
- "[Common title] [technology] 2026"
- "[Domain] Product Manager [location] 2026"
- etc.

**Filters:**
- Posted within 60 days
- Compensation within ±20% of pattern range
- Matching seniority level
- Active application links

**Target Outcome:**
- Find 10-20 jobs with fit scores ≥75
- At least 3-5 jobs with scores 90+
- Diverse companies (not all same type)

---

## How to Use This File

### Initial Setup
1. Fill out Seed Jobs 1-3 with your example jobs
2. Tell Claude: "Analyze my seed jobs and extract patterns"
3. Review pattern analysis
4. Confirm search: "Yes, search for similar jobs using these patterns"

### Updating Your Seed Jobs
If your priorities change:
```
"I want to pivot focus. Replace Seed Job 2 with: [new URL]"
"Re-analyze patterns with updated seed jobs"
```

### Refining Search
If results aren't what you expected:
```
"Focus more on [aspect] and less on [aspect]"
"Expand search to include [role type] roles"
"Narrow search to only [specific characteristic]"
```

---

## Tips for Choosing Good Seed Jobs

**DO choose jobs that:**
- ✅ Genuinely interest you
- ✅ Match your target seniority level
- ✅ Represent your ideal role characteristics
- ✅ Have clear, detailed job descriptions
- ✅ Are recently posted (within 60 days)

**DON'T choose jobs that:**
- ❌ Are aspirational but unrealistic stretch roles
- ❌ Have vague or minimal job descriptions
- ❌ Are very different from each other (creates confusing patterns)
- ❌ Are significantly above/below your compensation expectations
- ❌ Include deal-breakers (e.g., relocation if you won't relocate)

**Ideal scenario:**
Your 3 seed jobs are similar enough that patterns emerge, but diverse enough to cast a reasonably wide net.

---

## Example Seed Job Entry

```markdown
## Seed Job 1: Stripe - Principal Product Manager, Developer Platform

**URL:** https://stripe.com/jobs/listing/principal-pm-developer-platform/12345
**Posted:** January 15, 2026
**Status:** Bookmarked

**Why this job:**
Stripe's developer-first culture and API excellence align perfectly with my background. Excited about their focus on platform scalability and global developer experience.

**Key Requirements:**
- 10+ years product management experience with developer-facing products
- Deep understanding of REST APIs, webhooks, and API design
- Experience scaling platforms to millions of developers
- Track record of driving developer adoption through great DX

**Compensation:** $250K-$400K (base + equity)
**Location:** Remote (US) or San Francisco

**Fit Score:** 95/100

**Fit Analysis:**
✅ **API Platform Expertise** - 10+ years REST API product experience at VoiceBase and Vonage
✅ **Developer Experience Focus** - Reduced support 40% through documentation and self-service tools
✅ **Scale** - Led platform through 10x growth to 1.5M+ minutes/month
✅ **Compensation Alignment** - Range matches expectations ($226K-$400K target)
⚠️ **Webhooks Depth** - Have implemented but not primary focus area
```

---

For a real example of pattern analysis in action, see `/examples/jobs/Similar-Job-Postings.md` which was generated from seed job analysis.
