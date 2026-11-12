# LinkedIn job search workflow

LinkedIn is a second discovery source next to the board sweep, and the place where the candidate's saved and in-progress applications live. This workflow pulls both into the repository's tracker so one file holds the truth. It is run in a browser the candidate is signed in to (the Claude desktop app's built-in browser, or Claude in Chrome with the candidate's permission); nothing here works from a plain fetch.

## What to pull

**The job tracker** at `linkedin.com/jobs-tracker/`. Tabs: Saved, In Progress (with Draft and Clicked apply sub-types), Applied, Interview, Archived.

- Saved is paginated ten per page; click Next until the list ends.
- Switching sub-types sets `?stage=draft`, `?stage=clicked_apply`, or `?stage=applied` in the URL, but loading those URLs directly returns an empty list. Use the on-page controls.
- "Clicked apply" is a hint, not a record. Reconcile each one against the repository: was the application completed, and on which date?

**New searches** at `linkedin.com/jobs/search/?keywords=...`.

- Results default to a San Francisco Bay Area location and to AI-matched results, which mix in loosely related roles. Set the location and remote filters explicitly every time.
- A company name in the keywords does not filter by company. Use the company filter.
- Posting ages shown as "reposted" restart the clock for the sixty-day rule only if the employer's own page shows the repost.

**Each job page** at `linkedin.com/jobs/view/<id>/` for the full description, the pay range, and the remote-versus-on-site wording. The posting text wins over LinkedIn's workplace tag; "Hybrid" tags on remote postings are common.

## Scoring

Score every posting against `Profile.md` with the method in `AI-Assistant-Job-Search.md`, exactly as a sweep find. A LinkedIn find is not a referral; the 75 bar applies. Mark inferences as inferences in the fit analysis.

Before scoring, open the employer's own board (Greenhouse, Ashby, Lever, Workday, SmartRecruiters) for the same role. The board has the real band, the real date, the location rules, and often sibling roles LinkedIn does not surface. If the board shows no such role, say so in the entry; LinkedIn sometimes carries postings an employer has pulled.

## Recording

- Every evaluated posting goes in `jobs/Similar-Job-Postings.md` under a dated section, with the LinkedIn job id in the link so the next pull de-duplicates against it.
- Saved roles that were already evaluated get a one-line "already tracked, score N" rather than a second entry.
- Roles in "Clicked apply" that the repository shows as submitted are marked with the submission date. Ones the repository does not know about are a question for the candidate, not a guess.
- LinkedIn's own tracker is the candidate's; do not archive or move items there without being asked.

## Cadence

Pull the tracker and run the standing searches with each discovery sweep (every two to three weeks), and whenever the candidate says they have saved new roles.
