# Examples Directory

Everything in this directory describes **Jordan Avery, a fictional candidate**. The companies, products, metrics, links, and people are invented so the examples can show structure and tone without publishing anyone's real record. Do not copy the content; copy the shape.

## What's Here

### Profile-example.md
A complete Profile.md for the fictional candidate:
- All sections from `/templates/Profile-template.md`, filled in
- Quantified achievements with the number and the source
- An honest "Areas for Development" section
- A "Most Recent Role" block with approved reason-for-leaving wording (used on forms and in interviews, never in a letter)
- An "Approved Wording and Corrections" log: phrases that were corrected once and must not come back

### applications/northwind-platform-pm/
One complete application package, the unit this repository works in:
- `resume-northwind-platform-pm.html`: a two-page print-optimized resume. The CSS is the base template; copy this file to `applications/generic/resume-designed.html` and replace the content with yours. No Technical Skills grid and no tag row; the experience bullets carry the evidence.
- `cover-letter-northwind-platform-pm.md`: four short paragraphs (what the posting asks for and the matching record, a second experience, how the candidate works, what they have not done), a one-line close on availability, and a "Claims to confirm" block the candidate reviews and then deletes.
- `application-checklist.md`: the posting facts, the form fields pre-filled, the decisions to make before submitting, and the claims to confirm.

### jobs/Similar-Job-Postings.md
An example tracker: a status block at the top, one entry per role at or above the 75 bar with a strengths-and-gaps fit analysis, and a table of below-threshold roles with the reason, so a posting is never re-evaluated by accident.

## How to Use These Examples

1. **Setting up your Profile.md?** Read `Profile-example.md` next to `/templates/Profile-template.md`.
2. **Creating your base resume?** Copy the example resume to `/applications/generic/resume-designed.html`, replace every line of content, keep the `<style>` block, and run `scripts/build-resume.sh` to confirm two pages.
3. **Writing a cover letter?** Match the example's length and its ending. Keep the "Claims to confirm" habit.
4. **Building your tracker?** Keep the status block current and keep the below-threshold table; it saves the most time over a long search.

## What Makes These Good Examples

- Every claim about the candidate's role traces to Profile.md, and the verb is the weakest one the evidence supports ("owned the developer-facing surface," not "designed the platform").
- Gaps are stated in the letter in plain words, before an interviewer finds them.
- The letter does not restate the posting back at the company, and it closes on availability rather than enthusiasm.
- The checklist makes the form a ten-minute task.

When you are ready to create your own materials, return to `/setup/GETTING-STARTED.md`.
