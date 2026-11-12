# Seed jobs

*Last updated: [date]*

Two or three postings that represent what you want. Claude scores each one against `Profile.md`, extracts the pattern across them, and uses the pattern to filter every later sweep. This file also keeps the log of sweep runs, so the next run starts from the last one's filters and date.

## Choosing seeds

Good seeds are postings you would apply to today, at the level you are targeting, with detailed descriptions, posted within the last sixty days, and similar enough to each other that a pattern emerges. Poor seeds are stretch roles, vague postings, three unrelated roles, or anything with a condition you would not accept (a relocation, a band under your floor). If a seed scores under 75 against your profile, that is a signal about the seed, and the search built on it will produce more of the same.

## Seed 1: [Company], [Role Title]

**URL:** [posting URL]
**Posted:** [date]
**Compensation:** [band, or "not shown"]
**Location:** [remote, hybrid in a city, on-site]
**Why this one:** [one or two sentences in your own words]

**Key requirements:**
- [from the posting]
- [from the posting]
- [from the posting]

**Fit score:** [Claude fills this in]

**Fit analysis:**
[Claude fills this in, in the tracker's format: strengths and gaps, each citing the profile]

## Seed 2: [Company], [Role Title]

**URL:**
**Posted:**
**Compensation:**
**Location:**
**Why this one:**

**Key requirements:**
-
-
-

**Fit score:**

**Fit analysis:**

## Seed 3: [Company], [Role Title]

**URL:**
**Posted:**
**Compensation:**
**Location:**
**Why this one:**

**Key requirements:**
-
-
-

**Fit score:**

**Fit analysis:**

## Pattern extracted

[Claude fills this in after reading the seeds.]

- **Titles and level:** [the common titles; the level range]
- **Focus:** [the themes the postings share]
- **Technologies and surfaces:** [what most of them name, with the share of seeds that name it]
- **Company profile:** [size, stage, business model, industry]
- **Compensation:** [base range across the seeds; note which showed a band]
- **Work arrangement:** [remote, hybrid, on-site, with counts]
- **Filters for the sweep:** posted within sixty days; band top at or above the preferred base in `Profile.md` (or no band shown); level matching the seeds; working application link

## Sources

- `scripts/sweep-boards.py`, with the Greenhouse, Ashby, and Lever slug lists edited toward the companies in the pattern
- Aggregator boards for companies on other applicant-tracking systems
- Web search queries built from the pattern: [list the five to ten queries used]

## Re-runs

| Date | Filters | Sources | Result |
|---|---|---|---|
| [date] | [what changed since last time, if anything] | [boards answered, aggregators, searches] | [how many survived the filters; how many were already tracked; how many reached 75, named; the closest misses] |

Next re-run: [date, two to three weeks out].

## Changing direction

To pivot, replace the seeds and say so: "Replace seed 2 with [URL] and re-extract the pattern." The old pattern and run log stay above, dated, so a later reader can see when the target moved.

## Example entry

A filled-in seed for the fictional candidate in `examples/Profile-example.md`:

```markdown
## Seed 1: Northwind Payments, Staff Product Manager, Platform APIs

**URL:** https://jobs.example.com/northwind/staff-pm-platform-apis
**Posted:** January 6, 2026
**Compensation:** $195,000 - $245,000 base + equity
**Location:** Remote, US
**Why this one:** A public API that every product at the company exposes, with a stated need for someone who has taken a partner API to self-serve. That is the Ledgerline work.

**Key requirements:**
- 8+ years in product management, 5+ on public APIs
- Has taken a partner-only API to self-serve
- Writes API standards other teams build against
- Experience sunsetting legacy integration paths

**Fit score:** 81/100

**Fit analysis:**
- **Strength, partner-only to self-serve:** Ledgerline, 60 partner integrations to 900 active API customers in fourteen months; 31% of 2025 new revenue through self-serve
- **Strength, API standards:** co-wrote the design standards with Architecture; reviewed every proposal across four teams
- **Strength, deprecation:** Brightmail polling endpoint retired over nine months for 1,100 customers
- **Gap, pricing:** "pricing input" is listed under responsibilities; one usage-based launch on the record
- **Gap, level:** band top clears the preference, but ask how the role is leveled
```
