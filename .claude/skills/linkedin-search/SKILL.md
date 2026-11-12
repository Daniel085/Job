---
name: linkedin-search
description: Pull the candidate's LinkedIn job tracker and run the standing LinkedIn searches in the built-in browser, then score every new posting against Profile.md and record it in jobs/Similar-Job-Postings.md. Use when the user says "check LinkedIn," "pull my saved jobs," "run the LinkedIn search," or shares a linkedin.com/jobs link. Requires a browser the user is signed in to (the Claude desktop app's built-in browser); from a cloud session without one, say so and stop.
---

# LinkedIn job search

Follow `docs/LinkedIn-Workflow.md`. This skill is the operational checklist for it.

## Preconditions

1. Browser tools are present (`mcp__Claude_Browser__*` or `mcp__remote-devices__Claude_Browser__*`). If not, tell the user this needs the Claude desktop app and stop. Do not try to fetch LinkedIn pages from the shell.
2. Read `Profile.md` in full and the status block of `jobs/Similar-Job-Postings.md` before scoring anything.
3. Open a fresh tab for this work (`preview_start` with the first URL) and keep its tab id. Never navigate a tab that may hold an unsaved draft.

## Pull the tracker

1. `linkedin.com/jobs-tracker/`. Read Saved (ten per page; click Next until it ends), then In Progress with each sub-type (Draft, Clicked apply) selected through the on-page controls, then Applied.
2. For each row capture: title, company, location text, posted or reposted age, and the job id from the `/jobs/view/<id>/` link.
3. Reconcile "Clicked apply" and "Applied" against the repository. Mark matches with the recorded submission date. List the ones the repository does not know about as questions for the user; do not guess.

## Run the standing searches

Use `linkedin.com/jobs/search/?keywords=...` with location and remote filters set explicitly each time. Standing queries come from the pattern in `jobs/Seed-Jobs.md`; typical ones: the common titles plus the primary domain terms, and the target companies by the company filter (a company name in keywords does not filter by company). Read the first three pages of each.

## Evaluate each new posting

1. Open `/jobs/view/<id>/` and read the full description, the pay range, and the remote-versus-on-site wording. The text wins over LinkedIn's workplace tag.
2. Find the same role on the employer's own board (Greenhouse, Ashby, Lever, Workday, SmartRecruiters). Use its band, date, and location rules. If the board has no such role, note that LinkedIn may be carrying a pulled posting.
3. Score with the method in `docs/AI-Assistant-Job-Search.md`, the 75 bar (a LinkedIn find is not a referral), and the compensation rule in `CLAUDE.md`.
4. Write the fit analysis in the repository format with "Strength, category:" and "Gap, category:" lines. Mark inferences as inferences.

## Record

- Add a dated section to `jobs/Similar-Job-Postings.md`: full entries at 75 or above, a below-threshold table for the rest, one line each for roles already tracked. Include the LinkedIn job id in every link so the next pull de-duplicates.
- Save descriptions worth keeping to `jobs/descriptions/`.
- Update the status block and the "Last Updated" line. Commit with a message naming the date and the count of new roles.

## Never

- Apply, save, archive, or move anything in LinkedIn's tracker without being asked.
- Send a message or connection request from this skill; that is `network-leads`, and only with the user's approval of the final text.
- Bulk-scroll or scrape lists beyond what the evaluation needs. One posting at a time, read as a person would.
