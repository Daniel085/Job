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

Review these in the claims review tool (`scripts/claims-review/`) before rendering PDFs; the tool rewrites the block below.

<!-- claims:start -->

*Maintained by the claims review tool (`scripts/claims-review/`); edit claims there, not here.*

1. **PENDING:** Reviewed every API proposal across four teams. "reviewed every API proposal across four teams" (cover-letter-northwind-platform-pm.md); "reviewed every API proposal across four engineering teams" (resume-northwind-platform-pm.html)
   Source: Profile.md says four teams; confirm the count held for the full three years.
2. **PENDING:** The posting's "sunset legacy integration paths" read as a v1 deprecation. "Your posting mentions a v1 deprecation ahead" (cover-letter-northwind-platform-pm.md)
   Source: An inference from the posting, not a fact on the record; confirm the reading.
3. **PENDING:** 35% ticket drop attributed to the migration. "delivery-failure tickets fell 35% afterward" (cover-letter-northwind-platform-pm.md); "delivery-failure support tickets fell 35% after the migration" (resume-northwind-platform-pm.html)
   Source: Confirm no other change landed in the same quarter.

<!-- claims:end -->

## AI-tells pass

Checked: no "the shape of," no "it's not X, it's Y" contrasts, no rhetorical triplets, no closing line that restates the posting back at it.

## Before submitting

- [ ] Approve or edit the three claims in the claims review tool, then press Render PDFs there.
- [ ] Run `scripts/lint-claims.sh`.
- [ ] Read the resume PDF end to end.
- [ ] Open the posting link first; if it is gone, stop.
