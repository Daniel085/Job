---
name: ats-apply
description: Fill the common fields of a Greenhouse, Ashby, or Lever job application in the built-in browser from applications/application-profile.json and the package's form-answers.md, then stop for the user's review. Use when the user says "fill the application," "fill out Greenhouse / Ashby / Lever," or shares a job-boards.greenhouse.io, jobs.ashbyhq.com, or jobs.lever.co apply link for a role with a package in applications/. Desktop app only. Workday has its own skill (workday-apply). Never uploads files, answers voluntary disclosures, accepts consents, or submits.
---

# Greenhouse, Ashby, and Lever applications

Written November 2026 from live Greenhouse, Ashby, and Lever application forms. The field reading was checked on those forms; the fill helper had not yet been run on a real application. Treat the first real use as its test: watch every field it reports as filled, and correct this file with what you learn. Design and the decision to fill in the built-in browser instead of a Chrome extension: `docs/Form-Fill-Design.md`.

All three systems put the whole application on one page, so there is one review stop, before the user submits.

## Before starting

1. Read `applications/application-profile.json` and the package's `application-checklist.md`. If the package has pending claims, stop: the PDFs are not rendered yet.
2. Read the posting and the form for an AI-use rule (some employers ask applicants to acknowledge an AI-use policy; some ask that AI not be used on the form at all). If one forbids assisted filling, stop and tell the user. If one only asks for acknowledgment, the user reads it and ticks the box.
3. **Greenhouse:** run `python3 -I scripts/form-questions.py <posting-url> applications/<package>` (sandbox off). That writes `form-answers.md` with every question, its field name, and an owner. **Ashby and Lever:** open the form, run `__ats.fields()` (below), and write the same table into `form-answers.md` by hand.
4. Free-text answers (owner DRAFT) are drafted from Profile.md, added to the package's `claims.json`, and approved in the claims review before the form is filled. Never type unapproved free text.
5. Open the application in its own tab with `preview_start` and keep the tab id. Decline non-essential cookies.

## Hard rules

- **Stop before submit.** After filling, show the `__ats.report()` table and wait. The user clicks Submit. Never click Submit, Apply, or Send, and never solve a CAPTCHA (Ashby has an invisible reCAPTCHA).
- **The user does:** resume and letter upload (the pane has no file-upload tool); voluntary disclosures (gender, race, veteran, disability, sexual orientation, pronouns); consent, privacy, attestation, and acknowledgment boxes; export-control and residency questions until the profile has an approved answer; anything company-specific with no approved answer.
- **Never overwrite** a field that already has a value. The helper refuses; report it instead. The user may have typed there.
- **Find controls by label or name, never by DOM position.** A Workday run once lost a work entry to a guessed `querySelector('button')`.
- **Location and current company:** fill them only from approved values in `application-profile.json`; otherwise leave them for the user.
- Desired salary: leave blank when optional. If required, ask the user.

## The helper

Install once per page load with `javascript_tool`:

```js
window.__ats = (() => {
  const SKIP = /gender|race|ethnic|veteran|disab|sexual orientation|pronoun|self-identif|signature|attest|acknowledg|consent|i agree|i confirm|i certify|privacy|terms|recaptcha|citizen or resident|export/i;
  const vis = e => e.offsetParent !== null || e.type === 'radio' || e.type === 'checkbox';
  const txt = n => (n ? n.textContent : '').replace(/\s+/g, ' ').replace(/[*✱]/g, '').trim();
  const labelOf = e => {
    if (e.id) { const l = document.querySelector(`label[for="${CSS.escape(e.id)}"]`); if (l && txt(l)) return txt(l); }
    if (e.getAttribute('aria-labelledby')) return txt(document.getElementById(e.getAttribute('aria-labelledby')));
    if (e.getAttribute('aria-label')) return e.getAttribute('aria-label').trim();
    const box = e.closest('li.application-question, .application-question, [class*=fieldEntry], fieldset, .field-wrapper, .select__container');
    if (box) for (const sel of ['.application-label', 'legend', 'label', '.text']) { const l = box.querySelector(sel); if (l && txt(l)) return txt(l); }
    return e.placeholder || '';
  };
  const all = () => [...document.querySelectorAll('input:not([type=hidden]):not([type=file]):not([type=submit]), textarea, select')]
    .filter(e => vis(e) && !/recaptcha/.test(e.name || e.id) && (e.name || e.id || e.getAttribute('role') === 'combobox'));
  const fields = () => all().map(e => ({ label: labelOf(e).slice(0, 90), name: e.name || e.id, type: e.getAttribute('role') === 'combobox' ? 'combobox' : e.type || e.tagName.toLowerCase(), required: e.required || e.getAttribute('aria-required') === 'true', protected: SKIP.test(labelOf(e)), value: e.type === 'radio' || e.type === 'checkbox' ? (e.checked ? 'checked' : '') : e.value }));
  const find = key => all().find(e => (e.name || e.id) === key) || all().find(e => e.type !== 'radio' && e.type !== 'checkbox' && new RegExp(key, 'i').test(labelOf(e)));
  const setNative = (e, v) => {
    const proto = e.tagName === 'TEXTAREA' ? HTMLTextAreaElement.prototype : e.tagName === 'SELECT' ? HTMLSelectElement.prototype : HTMLInputElement.prototype;
    Object.getOwnPropertyDescriptor(proto, 'value').set.call(e, v);
    ['input', 'change', 'blur'].forEach(t => e.dispatchEvent(new Event(t, { bubbles: true })));
    return e.value === v;
  };
  const fill = (key, v) => {
    const e = find(key); if (!e) return `NOT FOUND: ${key}`;
    const l = labelOf(e);
    if (SKIP.test(l)) return `SKIPPED (protected): ${l}`;
    if (e.getAttribute('role') === 'combobox') return `COMBOBOX: ${l} (use the combobox steps)`;
    if (e.value && e.value !== v) return `HAS VALUE, not changed: ${l} = ${e.value}`;
    if (e.tagName === 'SELECT') { const o = [...e.options].find(o => o.text.trim() === v); if (!o) return `NO OPTION "${v}": ${l}`; v = o.value; }
    return setNative(e, v) ? `OK: ${l}` : `REVERTED: ${l} (type it with keystrokes)`;
  };
  const radio = (questionRe, answerRe) => {
    const r = all().filter(e => e.type === 'radio' || e.type === 'checkbox').find(e => {
      const box = e.closest('fieldset, li, [class*=fieldEntry], .application-question');
      return new RegExp(questionRe, 'i').test(txt(box)) && new RegExp(answerRe, 'i').test(labelOf(e) || txt(e.parentElement));
    });
    if (!r) return `NOT FOUND: ${questionRe} / ${answerRe}`;
    if (SKIP.test(txt(r.closest('fieldset, li, [class*=fieldEntry], .application-question')))) return `SKIPPED (protected): ${questionRe}`;
    if (!r.checked) r.click();
    return r.checked ? `OK: ${questionRe} = ${answerRe}` : `DID NOT STICK: ${questionRe}`;
  };
  const option = text => { const o = [...document.querySelectorAll('[role=option]')].find(o => o.textContent.trim() === text); if (!o) return `NO OPTION: ${text}`; o.click(); return `OK: ${text}`; };
  const report = () => fields().filter(f => !f.protected).map(f => `${f.required ? '*' : ' '} ${f.label} | ${f.type} | ${f.value || '(empty)'}`).join('\n');
  return { fields, fill, radio, option, report };
})();
```

- `__ats.fields()`: every visible field with label, name, type, required, and whether it is protected. Run it first; it is read-only.
- `__ats.fill(nameOrLabelRegex, value)`: sets a text, email, tel, url, textarea, or native select field. Exact field name wins over label. It refuses protected fields, comboboxes, and fields that already hold a value.
- `__ats.radio(questionRegex, answerRegex)`: clicks one radio or checkbox inside a question.
- `__ats.option(text)`: clicks an option in an open combobox list.
- `__ats.report()`: the non-protected fields and their values, for the review stop.

If a fill returns `REVERTED`, the form is React-controlled and ignored the value. Fall back to the Workday pattern: focus the field with `javascript_tool`, then `computer` `type`.

## Comboboxes (Greenhouse and Ashby dropdowns)

Greenhouse's Country, Location, and yes/no questions, and Ashby's location and "how did you hear" fields, are type-ahead comboboxes, not native selects. For each one:
1. Click it by `ref` (from `find` with the question label).
2. `computer` `type` the start of the answer ("Yes", "United").
3. Wait 1 second, then `__ats.option('Yes')`, using the exact option text from `form-answers.md`.
4. Re-read the field. Greenhouse can add a follow-up question after an answer.

## Per system

**Greenhouse** (`job-boards.greenhouse.io`). Field names match the board API, so `form-answers.md` gives exact keys:
- Fixed fields: `first_name`, `last_name`, `preferred_name`, `email`, `phone`.
- Questions: `question_<id>`. Checkbox groups such as "How did you hear" are `question_<id>[]`.
- Combobox fields: `country` and `candidate-location`.
- Demographic questions are numeric ids near the end of the form. Protected; never touched.
- The phone field sits next to a country combobox; set Country first.

**Ashby** (`jobs.ashbyhq.com/.../application`):
- System fields: `_systemfield_name` (preferred first and last name in one field), `_systemfield_email`, `_systemfield_resume` (upload, the user's).
- Every other field has a random id, so match it by label: Legal First Name, Legal Last Name, Phone Number, LinkedIn Profile, GitHub Profile, Other Website.
- Work-authorization questions are radio groups; use `__ats.radio`.
- Interview-recording consent ("consent to be recorded" / "Opt out") is the user's.

**Lever** (`jobs.lever.co/.../apply`):
- Plain HTML with stable names: `name` (full name), `email`, `phone`, `location`, `org` (current company), `urls[LinkedIn]`, `urls[GitHub]`, `urls[Portfolio]`, `urls[Other]`.
- Custom questions are `cards[<uuid>][field<n>]`.
- EEO questions are native selects (`eeo[gender]`, `eeo[race]`, `eeo[veteran]`). Protected; never touched.

## Standard fill, from the profile

| Field | Value source | Greenhouse | Ashby | Lever |
|-------|--------------|-----------|-------|-------|
| First / last name | `contact.first_name`, `contact.last_name` | `first_name`, `last_name`; `preferred_name` = first name | Legal First Name, Legal Last Name; `_systemfield_name` = first and last | `name` = first and last |
| Email | `contact.email` | `email` | `_systemfield_email` | `email` |
| Phone | `contact.phone` | `phone` (Country combobox first) | Phone Number | `phone` |
| LinkedIn | `websites` (linkedin.com) | the LinkedIn question | LinkedIn Profile | `urls[LinkedIn]` |
| GitHub | `websites` (github.com) | if asked | GitHub Profile | `urls[GitHub]` |
| Portfolio | `websites` (your portfolio link) | if asked | Other Website | `urls[Portfolio]` |
| Work authorization, sponsorship | `standard_answers` | combobox, Yes / No | radio | per question |
| How did you hear | `standard_answers.how_did_you_hear`, or the referral if there is one | the "Careers Website" style option | combobox | per question |

Then the approved DRAFT answers from `form-answers.md`, one `fill` each, and the review stop.

## After submission

Record it the same day: the package checklist (`**Submitted:**`) and the tracker status block in `jobs/Similar-Job-Postings.md` (count and dated line), then commit.

Add anything the form taught you (a field that reverted, a combobox that would not open) to this file.
