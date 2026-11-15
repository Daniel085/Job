---
name: workday-apply
description: Fill a Workday job application (myworkdayjobs.com) page by page in the built-in browser from applications/application-profile.json, stopping for the user's review before every Save and Continue. Use when the user says "drive the Workday application," "fill out Workday," or shares a myworkdayjobs.com apply link for a role with a package in applications/. Desktop app only. Never signs in, uploads files, answers voluntary disclosures, accepts consents, or submits.
---

# Workday application

Built from a real Workday application, November 2026. Workday tenants share the same front end, so field ids and traps carry over; question pages differ by company.

## Before starting

1. Read `applications/application-profile.json` and the package's `application-checklist.md`. If the package has pending claims, stop: render first. If `applications/application-profile.json` does not exist, build it from `templates/application-profile-template.json`, `Profile.md`, and the user's LinkedIn experience page (month dates come from LinkedIn), and have the user confirm it before any form.
2. Check the profile against the resume about to be uploaded (titles, dates, company names). Raise any mismatch before the form, not after.
3. Open the posting in its own tab with `preview_start` and keep the tab id. Decline non-essential cookies.
4. Click **Apply**, then **Apply Manually**. Never "Autofill with Resume": the parser scrambles fields and is slower to fix than typing.
5. Account creation or sign-in is the user's (passwords and the Terms checkbox). Ask, wait for "signed in."

## Hard rules

- **Stop before every Save and Continue.** List what was entered in a table and wait for the user's go. They may also click it themselves; check the step indicator before acting.
- **Never click by guessed DOM position.** A `querySelector('button')` near a section header hit **Delete** and removed a work entry. Find buttons with `find` (by label) and click by `ref`; for work entries use the "Add" / "Add Another" ref under Work Experience specifically.
- The user does: sign-in, street address, resume and letter upload (the pane has no file-upload tool), voluntary disclosures (ethnicity, gender, veteran, disability), consent checkboxes, the final Submit.
- Desired salary: leave blank when optional.
- Never type into a tab that may hold the user's unsaved input without checking the field first.

## Typing into Workday fields

React inputs need real keystrokes. The proven pattern: focus with `javascript_tool`, then `computer` `type`.

Install helpers once per page load:

```js
window.__last = () => { const t=[...document.querySelectorAll('[id^=workExperience-][id$="--jobTitle"]')].pop(); window.__wp=t.id.replace('--jobTitle',''); return window.__wp; };
window.__f = k => { const e=document.getElementById(window.__wp+'--'+k); e.focus(); return k; };
window.__v = () => ['jobTitle','companyName','location','startDate-dateSectionMonth-input','startDate-dateSectionYear-input','endDate-dateSectionMonth-input','endDate-dateSectionYear-input'].map(k=>document.getElementById(window.__wp+'--'+k).value).join(' | ') + ' | desc lines: ' + document.getElementById(window.__wp+'--roleDescription').value.split('\n').length;
```

Per work entry (one `browser_batch`, at most 25 actions): click the Work Experience Add ref, wait 1s, `__last()`, then for each field `__f('<field>')` + `type`. Field suffixes: `jobTitle`, `companyName`, `location`, `startDate-dateSectionMonth-input`, `startDate-dateSectionYear-input`, `endDate-dateSectionMonth-input`, `endDate-dateSectionYear-input`, `roleDescription`. End the batch with `__v()` and compare against the profile.

### Traps

- **Dates:** type month and year into their separate inputs ("04", then "2025"). Typing "042025" into the month box garbles both. A year with no month becomes 2012; every entry needs a month (the profile has them).
- **Clearing a textarea:** `cmd+a` does not select the textarea's text; the retype doubles it. Clear with `e.focus(); e.select()` in `javascript_tool`, then press Backspace, then check `value.length === 0`.
- **Illegal characters** in descriptions: `< > [ ] " { } \`. Strip them before typing (the profile is already clean). The error shows only after Save and Continue.
- **Dropdowns** (`button` with "Select One"): click by ref, wait 1s, then click the option with `[...document.querySelectorAll('[role=option]')].find(o=>o.textContent.trim()==='Yes').click()`. Some open only on a coordinate click; take a screenshot if the option list is empty.
- **Conditional questions:** answering one can insert another (one tenant added a sponsorship question after "authorized: Yes"). Re-read the page after each answer instead of reusing refs.
- **Multiselect prompts** ("How did you hear", Field of Study): click, then drill into categories (Career Websites > Corporate Website). Search lists can lack the value (a degree's exact field may be missing); leave optional ones blank and say so.
- **Entry order** is the order added. Add work history newest first and do not delete and re-add, or the order breaks.

## Page by page

1. **My Information:** how-heard, former employee, name, state, phone type and number from the profile. Address is the user's.
2. **My Experience:** work history (all entries in the profile, newest first), education, websites. Skills and Languages optional; leave blank unless asked. The user uploads the resume (and letter if the field takes two files).
3. **Application Questions:** standard answers from the profile; anything company-specific or unusual goes to the user with a recommendation.
4. **Voluntary Disclosures:** the user's.
5. **Review:** read every section back against the profile and the package; report differences; the user submits.

## After submission

Record it the same day: the package checklist (`**Submitted:**`) and the tracker status block in `jobs/Similar-Job-Postings.md` (count and dated line), then commit.
