# Northwind Payments, Staff Product Manager, Platform APIs: application checklist

*Fictional example. The checklist travels with every package so the form can be filled in one sitting and every claim has been looked at once more before it goes out.*

**Apply at:** https://jobs.example.com/northwind/staff-pm-platform-apis (company careers page; Greenhouse form)
**Salary on posting:** $195,000 - $245,000 base
**Location on posting:** Remote, US
**Posted:** January 6, 2026 (checked open January 12)
**Fit score:** 81/100
**Prepared:** January 12, 2026. **Submitted:** not yet

## Read this first

1. **Level.** The posting says Staff; the band's top is under the preferred $220K by only a little. Ask on the first call how the role is leveled and whether the band is the full range.
2. **The gaps are stated in the letter.** One pricing launch, no people management. Do not let an interviewer upgrade either one.
3. **Departure.** Not mentioned in the letter; the resume dates carry it. If the form or an interviewer asks, use the approved wording from Profile.md ("Most Recent Role") and then stop.
4. **Posting age.** Six days. Fine.

## Files to upload

| Field | File |
|-------|------|
| Resume | `applications/northwind-platform-pm/Jordan-Avery-Resume-Northwind.pdf` (2 pages, letter) |
| Cover letter | `applications/northwind-platform-pm/Jordan-Avery-Cover-Letter-Northwind.pdf` |

## Fields, pre-filled from Profile.md

| Field | Answer |
|-------|--------|
| Name | Jordan Avery |
| Email | jordan.avery@example.com |
| Phone | 555-010-0199 |
| Location | Portland, Oregon, United States |
| LinkedIn | https://linkedin.com/in/jordan-avery-example |
| GitHub / website | https://github.com/jordan-avery-example and https://developer.ledgerline.example |
| Most recent company / title | Ledgerline, Staff Product Manager, Developer Platform (March 2023 - December 2025) |
| Authorized to work in the US / need sponsorship | Yes / No |
| How did you hear | Company careers page (January 2026 discovery sweep) |
| Desired salary, if asked | $220K preferred; ask the level first |

## Claims to confirm

1. "Reviewed every API proposal across four teams": confirm the count.
2. The posting's "sunset legacy integration paths" read as a v1 deprecation: confirm.
3. 35% ticket drop attributed to the migration alone: confirm.

## AI-tells pass

Checked: no "the shape of," no "it's not X, it's Y" contrasts, no rhetorical triplets, no closing line that restates the posting back at it.

## Before submitting

- [ ] Confirm or correct the three claims; regenerate the PDFs if anything changes (`scripts/build-resume.sh`, `scripts/build-letter.sh`).
- [ ] Run `scripts/lint-claims.sh`.
- [ ] Delete the "Claims to confirm" block from the letter before building the PDF.
- [ ] Read the resume PDF end to end.
- [ ] Open the posting link first; if it is gone, stop.
