# How roles are found, scored, and tracked

This document is the reference for the evaluation half of the repository: where postings come from, how each one is scored against `Profile.md`, what the fit analysis has to contain, and how the tracker is kept. `CLAUDE.md` summarizes it; this is the long form.

## Inputs

- `Profile.md`. Read all of it before scoring anything. The score depends on the candidate's record, their stated gaps, their pay numbers, and their location rules, and all four live there.
- The posting. Fetched from the employer's own page where possible. Many careers pages are rendered by JavaScript and return an empty shell to a plain fetch; the applicant-tracking systems behind them usually expose a JSON endpoint (Greenhouse, Ashby, Lever, Workday, SmartRecruiters), and a headless browser works for the rest.
- `jobs/Seed-Jobs.md`, for the patterns a discovery run is filtering on.

## Output

`jobs/Similar-Job-Postings.md`, with a status block at the top, one full entry per role at or above the bar, and a table of below-threshold roles after each run.

## The scoring method

Start at zero and add or subtract. Use the posting's own requirements, not a generic idea of the role.

Add:

| For | Points |
|---|---|
| Direct experience with the technologies or surfaces the posting names | 10 to 20 |
| Exceeding the years of experience required | 5 to 10 |
| Domain match (the posting's industry or customer is one on the record) | 10 to 15 |
| Previous experience at a similar company (size, stage, business model) | 5 to 10 |
| Leadership experience the posting asks for, of the kind the record has | 10 to 15 |
| Matching seniority | 5 to 10 |
| Certifications, patents, or publications the posting values | up to 5 |

Subtract:

| For | Points |
|---|---|
| A required skill or domain that is not on the record | 10 to 20 |
| Fewer years than required | 10 to 15 |
| Industry mismatch | 5 to 10 |
| A location constraint the candidate has not accepted (on-site, hybrid in a city they are not in, residency) | 5 to 10 |
| A pay band between the acceptable and preferred numbers | small, about 3 to 5 |
| A title two or more levels under the record | 5 to 10 |

Then apply the exclusions, which are not point deductions:

- A band whose top is under the candidate's acceptable base is excluded, whatever the score.
- A posting older than sixty days is excluded unless it has been refreshed or the employer confirms it is open.
- A posting with no working application link is excluded.
- A posting that requires a legal status the candidate lacks (a right to work in a region, a clearance) is excluded.

The bar is 75. A role at or above it gets a full entry and a package. A role under it gets a row in the below-threshold table.

Two deliberate exceptions are written into `CLAUDE.md`. A role shared by a friend or family member is packaged at 65 or above if the candidate accepts its location, with the location presented as their decision rather than a reason to exclude. And the candidate may ask for a package below the bar for reasons of their own (a local office, a former employer); the tracker records the score honestly and notes that the package was built at their request.

### Reading the ranges

- 90 to 100: the posting could have been written from the record. Full package, plus research on the team.
- 80 to 89: strong match with one or two named gaps. Full package.
- 75 to 79: good match with real gaps. Package when the pipeline is thin or the role has something specific going for it.
- 60 to 74: the surface fits but a requirement does not. Log it with the reason; it may come back under a different rule (a revised pay band, a location decision).
- Under 60: log it in one line.

### Things that are not points

The posting's prose is not the requirement; the requirements list is. A posting that says "you will prototype" is asking for a prototyping PM and the record either shows that or it does not. A posting that says "deep architectural knowledge" under preferred qualifications is a small deduction when missing, not a large one.

The score describes fit, not desirability. A high band at a company the candidate dislikes is still a high score; the decision to apply is theirs and goes in the status block, not in the number.

### A worked example

The fictional candidate in `examples/Profile-example.md` against the fictional Northwind posting in `examples/jobs/Similar-Job-Postings.md`:

| Item | Change | Running total |
|---|---|---|
| Public API, webhooks, SDKs, portal: all named in the posting and all on the record | +20 | 20 |
| Eight years required, eleven on the record | +8 | 28 |
| "Has taken a partner-only API to self-serve": the Ledgerline move, with numbers | +15 | 43 |
| Payments domain, three years | +12 | 55 |
| "Writes API standards other teams build against": co-wrote them with Architecture (shared credit, so the middle of the range) | +10 | 65 |
| Deprecation experience: the Brightmail endpoint retirement | +10 | 75 |
| Staff title matches | +6 | 81 |
| Band top of $245K reaches the preferred $220K | 0 | 81 |
| Remote US | 0 | 81 |
| "Pricing input" under responsibilities; one usage-based launch on the record | 0 (not a requirement) | 81 |

Final: 81. Note what did not happen: the candidate's mentoring of two PMs did not count as leadership, because the posting did not ask for people management and the record does not contain it. If the posting had required "4+ years managing PMs," that would be a 15 to 20 point deduction and a line in the gaps.

## The fit analysis

Each full entry carries a short analysis with both strengths and gaps. The format is fixed so entries can be compared:

```
**Fit analysis:**
- **Strength, partner-only to self-serve:** Ledgerline, 60 partner integrations to 900 active API customers in fourteen months; 31% of 2025 new revenue through self-serve (Profile.md, Key Achievements)
- **Strength, API standards:** co-wrote the design standards with Architecture; reviewed every proposal across four teams
- **Gap, pricing:** "pricing input" is listed under responsibilities; one usage-based launch on the record
- **Gap, band:** top of $245K clears the preference, but the level question still needs asking
```

Rules for the analysis:

1. Every strength cites the record: a role, a number, a section of `Profile.md`. "Strong API background" is not evidence.
2. Every entry has at least one gap. A posting with no gap has not been read closely.
3. The verb in a strength is the one `Profile.md` uses. If the profile says "helped guide the structure of the API with Architecture," the strength does not say "designed the API."
4. Product facts stay product facts. What the candidate's former employer's platform does is context; what the candidate did is the claim.
5. Quote the posting where the match is specific. It makes the entry checkable and gives the cover letter its opening.

## The below-threshold table

After every run, the roles that fell short go in a table under the run's heading:

```
| Role | Comp / location / posted | Score | Why it falls short |
|------|--------------------------|-------|--------------------|
| [Director of PM, Developer Platform, Meridian Cloud](link) | $230K-$310K; remote US; Jan 3 | 62 | Leads a team of six PMs; "4+ years managing PMs" is required and the record has mentoring only |
```

One line per role, with the reason stated as the posting's requirement against the record. A role can move out of this table later: when a pay rule changes, when the candidate opens a location, or when the posting is reissued at a different level. Re-score it under the new rule and say so.

## Keeping the tracker

- The status block at the top lists what is submitted and awaiting a response, what is prepared and not yet submitted, what is waiting on the candidate, and when the next sweep is due. Update it on every change; it is what the candidate reads first.
- Full entries are sorted by score within their run's section. Runs are dated.
- When a posting closes, mark the heading closed with the date rather than deleting the entry. The analysis is still useful when the role is reposted.
- When a package is submitted, record the date in the status block and in the entry, and note anything to raise on the first call (the level, the pay tier, the location).
- Update the "Last Updated" line at the top of the file on every edit.

## Where postings come from

**Company boards through their APIs.** `scripts/sweep-boards.py` holds three slug lists, one each for Greenhouse, Ashby, and Lever. Each slug is the company's board identifier, which is visible in the URL of its careers page. The script calls the public JSON endpoint for every slug, keeps the postings whose titles look like product management, and writes them out with description text, location, date, URL, and any dollar figures found. Edit the lists for the companies you care about; a few hundred boards answer in under a minute.

**Aggregator boards.** Built In (by metro), Wellfound, and the boards that white-label a shared index (several newsletter job boards do) cover companies on Workday, iCIMS, SmartRecruiters, and Rippling, which the sweep script does not call. Use them through web search or their own search pages.

**Web search.** Five to ten queries built from the seed patterns: the common title plus the year, the title plus the primary technology, the company type plus "product manager" plus "remote," and so on.

**People.** Roles sent by friends and family get their own dated section in the tracker and the more generous packaging rule.

Whatever the source, read the employer's own posting before scoring. Aggregators lag, truncate, and sometimes carry a stale band.

## Questions to put to the candidate

When a score turns on something `Profile.md` does not settle, ask rather than guess, and ask about every open item at once:

- "The posting requires [X]. Have you done it, and where?"
- "This is hybrid in [city]. Is that on the table, and at what base?"
- "The posting asks for people management. Your profile says you mentored. Is that the whole story?"
- "The band tops at [N]. Is that acceptable for this role?"

Record the answers in `Profile.md` so the next evaluation does not ask again.

## Mistakes this method is designed to prevent

- Scoring from the posting's prose rather than its requirements.
- Letting a product's public description stand in for the candidate's role in it.
- Counting mentoring as management.
- Re-evaluating a posting the last sweep already rejected.
- Including a posting with a dead link or an expired window.
- Dropping a role for pay when the band reaches the candidate's preferred number.
- Excluding a role for location when the candidate has not been asked.
