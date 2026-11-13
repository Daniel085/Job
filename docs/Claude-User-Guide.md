# Working with Claude Code in this repository

This guide is for the person running the search. It covers what Claude does and does not do here, the phrases that start each piece of work, and how to answer when it comes back with questions. The rules Claude itself follows are in `CLAUDE.md`; the scoring method is in `AI-Assistant-Job-Search.md`.

## What Claude does here

- Drafts and maintains `Profile.md` from your inputs and your answers.
- Fetches postings, scores them, and keeps the tracker.
- Sweeps job boards and logs each run.
- Builds application packages: resume, cover letter, checklist, PDFs.
- Lists the claims in each package for you to confirm, and applies your corrections everywhere a phrase appears.
- Keeps the phrase linter current with your corrections.
- Commits and pushes on your branch.

## What it does not do

- Log in to anything. It cannot open LinkedIn as you, submit a form, or read a posting behind a sign-in. If a careers page refuses an automated fetch, it will tell you and you can paste the text.
- Submit applications. You submit; you tell it when a package is in.
- Invent facts about you. If something it needs is not in `Profile.md`, it asks, and it adds nothing you have not confirmed.
- Soften a gap. If a posting requires something you have not done, the letter says so.

## First-time setup

Put your resume and LinkedIn text in `setup/inputs/` and say:

> Help me set up this job search repository. I've placed my resume and LinkedIn profile in setup/inputs/.

Claude drafts `Profile.md` and asks about seven things: your acceptable and preferred base salary, your location rules, your top three must-haves, whether to read your GitHub, your strongest domains, the level you are targeting, and whether you have formally managed people. Answer plainly. The management question matters more than it looks: the materials will say "mentored" or "managed" according to your answer, and an interviewer will ask.

Review the draft. The sections most worth your attention are "Key Achievements" (every number will be reused), "Areas for Development" (honest gaps make the scores useful), and "Most Recent Role" (this is where approved wording for a departure lives, for forms and interviews only).

Then give it two or three postings:

> Here are three jobs I'd want. [three URLs]

It extracts the pattern, shows it to you, and asks before it searches. `setup/GETTING-STARTED.md` has each step in more detail.

## The phrases that start work

You do not need exact wording; these are the requests the workflow is built around.

| You say | What happens |
|---|---|
| "Add this job: [URL]" | Fetches, scores, writes the fit analysis, adds a full entry or a below-threshold row, updates the tracker date. |
| "Run the job search again" or "Let's re-run the sweep" | Sweeps the boards and the other sources under the current filters, scores the new postings, logs the run in `jobs/Seed-Jobs.md`, and reports what reached the bar. |
| "What should we apply to next?" | Reads the status block and the open entries and recommends, with reasons. |
| "Build the [Company] [Role] package" | Writes the resume, letter, checklist, and `claims.json`, runs the linter, and lists the claims to confirm. No PDFs until every claim is decided. |
| "Open the claims review" | Starts the review page (http://127.0.0.1:8765) where you approve or edit each claim in context and render the PDFs. |
| "1, 2 yes; 3: [correction]; 4 cut" | Applies each answer, fixes the phrase everywhere it appears, records new wording in `Profile.md` and the linter, builds the PDFs. |
| "[Company] is in" or "[Company] submitted" | Records the submission date in the tracker and the checklist and moves the role to the awaiting-response list. |
| "Update Profile.md: [fact]" | Shows the exact lines it would add or change, then applies them when you say yes. |
| "My wife sent these: [URLs]" (or any referral) | Evaluates them in their own dated section under the more generous rule for referrals, and puts location decisions to you. |
| "Check if the jobs in the tracker are still open" | Fetches each link and marks closed roles. |
| "Compare these three roles" | A short table of requirements, bands, locations, and your fit on each. |

## Answering the claims list

Every new package lists its claims in `claims.json`; the review page shows each one highlighted in the resume and letter, and Claude also lists them in chat like this:

> Claims to confirm:
> 1. "Reviewed every API proposal across four teams": the profile says four teams; confirm the count held for the full three years.
> 2. The posting's "sunset legacy integration paths" read as a v1 deprecation: confirm.
> 3. The 35% ticket drop is attributed to the migration alone: confirm no other change landed that quarter.

Answer by number. "Yes" confirms. A correction replaces the claim ("3: the drop was 35% but two changes landed; say 'after the migration and a retry fix'"). "Cut" removes it. Partial answers are fine ("1 and 2 yes, I'll come back on 3"); nothing is built until every item is answered.

Two habits make this work. First, read the claim against your memory, not against the draft; the draft is what is being checked. Second, when a claim is wrong, say what is true. Claude will find the weakest verb that fits and will fix the phrase in every file, not only the one in front of you.

## When Claude asks you something mid-task

It will stop and ask when a posting requires something your profile does not cover, when a location or pay question decides the score, or when two readings of a posting lead to different letters. It asks about every open item at once rather than one at a time. A short answer is enough; "no, never done that" is as useful as a paragraph, and it will not add the skill.

If you say "sort of" or "a little," it will not add the item to your profile as a strength. It may offer "exposure to [X]" on the resume for that one application.

## Keeping the profile current

The profile improves in three ways: your answers to mid-task questions, your corrections to claims, and direct updates ("Update Profile.md: I also owned the SDK release process at Ledgerline, 2024 to 2025"). Each change is shown before it is applied and noted in the commit message. Corrections to wording also go into the "Approved Wording and Corrections" section at the end of the profile and into `scripts/lint-claims.sh`, so the old phrasing cannot return.

If your situation changes, say so once and the rules follow: a new pay floor re-scores the tracker, a role ending switches tense and dates in every new material, a location you open brings roles out of the below-threshold table.

## Reading the tracker

Open `jobs/Similar-Job-Postings.md` and read the status block first. It lists what is submitted and waiting, what is prepared and not yet sent, what is waiting on you, and when the next sweep is due. Below it, each run has its own dated section with full entries sorted by score and a table of the roles that fell short. Entries for closed roles stay, marked closed with the date.

## Working on a branch

Keep your search in your own private copy (made with **Use this template** on GitHub) and leave the template repository alone. Claude commits as it goes and pushes when a piece of work is complete. If it cannot push (a credential problem is the usual cause), it will say so rather than report success; the commits are safe locally until the problem is fixed.

Improvements that belong in the template (a script fix, a better rule) can be cherry-picked to `main` in a separate commit. Personal files never are.

## Safety

Share postings, descriptions, and your own resume freely. Do not paste passwords, tokens, or identity numbers; Claude does not need them for anything here. Your profile and tracker contain your contact details, your pay expectations, and the companies you are talking to, so keep the branch they live on private.
