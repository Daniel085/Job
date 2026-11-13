# Resume Template Guide

## Using the HTML Resume Template

The best approach for creating your resume is to **use `/examples/applications/northwind-platform-pm/resume-northwind-platform-pm.html` as your base template** and customize it with your information.

### Why HTML?

- **2-page print format:** CSS ensures exactly 2 pages when printed
- **ATS-friendly:** Semantic HTML structure parseable by Applicant Tracking Systems
- **Easy to edit:** Simple HTML tags, no complex formatting
- **Consistent styling:** All company-specific resumes use same base structure

---

## Quick Start

### Option 1: Let Claude Create It (Recommended)

Tell Claude:
```
"Create a base resume HTML file for me using my Profile.md"
```

Claude will:
1. Read your Profile.md
2. Copy the structure from `/examples/applications/northwind-platform-pm/resume-northwind-platform-pm.html`
3. Replace content with your information
4. Save to `/applications/generic/resume-designed.html` (your base resume; every tailored resume starts from it)

### Option 2: Manual Creation

1. Copy `/examples/applications/northwind-platform-pm/resume-northwind-platform-pm.html`
2. Replace the example candidate's information with yours (see sections below)
3. Save as `/applications/generic/resume-designed.html`

---

## What to Customize

### 1. Header Section
**Replace:**
```html
<h1>JORDAN AVERY</h1>
<div class="contact-info">
  555-010-0199 <span>|</span>
  <a href="mailto:jordan.avery@example.com">jordan.avery@example.com</a> <span>|</span>
  <a href="https://linkedin.com/in/jordan-avery-example">linkedin.com/in/jordan-avery-example</a> <span>|</span>
  <a href="https://github.com/jordan-avery-example">github.com/jordan-avery-example</a>
</div>
```

**With:**
```html
<h1>[Your Name]</h1>
<div class="contact-info">
  <a href="mailto:[your.email@example.com]">[your.email@example.com]</a>
  <span>•</span>
  [Your Phone]
  <span>•</span>
  <a href="[LinkedIn URL]">linkedin.com/in/[yourprofile]</a>
  <span>•</span>
  <a href="[GitHub URL]">github.com/[yourusername]</a> <!-- Remove if no GitHub -->
</div>
```

### 2. Professional Summary
**Replace:** the example candidate's summary

**With:** Your summary from Profile.md (Professional Summary section)

**Format:**
- 2-3 sentences
- Highlight: (1) Years of experience (2) Core expertise (3) Key achievements
- Use **bold** for numbers/metrics

### 3. Core Expertise Tags (optional)
The example resume has no tag row. Add one on a tailored resume only when every tag mirrors the posting's own vocabulary and maps to a bullet below it; a tag the record cannot support is a claim you will be asked about.

**If you use one, keep the structure:**
```html
<div class="expertise-tags">
  <span class="tag">[Your Skill 1]</span>
  <span class="tag">[Your Skill 2]</span>
  ...
</div>
```

### 4. Experience Section
**For each job, replace:**

```html
<div class="job">
  <div class="job-header">
    <div>
      <div class="job-title">[Job Title]</div>
      <div class="company">[Company Name]</div>
    </div>
    <div class="dates">[Start Date] – [End Date or Present]</div>
  </div>
  <ul class="achievements">
    <li>[Achievement with metric]</li>
    <li>[Achievement with metric]</li>
    <li>[Achievement with metric]</li>
  </ul>
</div>
```

**Tips:**
- Include 3-5 bullet points per role
- Start each bullet with action verb
- Include metrics whenever possible
- Most recent role gets most detail

### 5. Skills Section (optional)
The example resume has no Technical Skills grid. For product managers a skills grid tends to invite a solo coding test, and the experience bullets already show the tools in use. If your field expects one, use the two-column layout:

```html
<div class="two-col">
  <div class="col">
    <div class="skill-category">[Category 1 Title]</div>
    <div class="skill-list">[Skill], [Skill], [Skill]...</div>

    <div class="skill-category">[Category 2 Title]</div>
    <div class="skill-list">[Skill], [Skill], [Skill]...</div>
  </div>
  <div class="col">
    <div class="skill-category">[Category 3 Title]</div>
    <div class="skill-list">[Skill], [Skill], [Skill]...</div>

    <div class="skill-category">[Category 4 Title]</div>
    <div class="skill-list">[Skill], [Skill], [Skill]...</div>
  </div>
</div>
```

### 6. Education
**Replace:**
```html
<div class="education-item">
  <div class="degree-info">
    <span class="degree">[Degree]</span> — <span class="school">[University]</span>
  </div>
  <div>[Department/Major]</div>
</div>
```

---

## Important: CSS Preserved

**DO NOT modify the `<style>` section!** The CSS ensures:
- Exactly 2 pages when printed
- Proper page breaks between pages
- ATS-friendly structure
- Professional appearance

The only CSS you might adjust:
- `font-size` in `body` (currently 10.5px) - only if content doesn't fit on 2 pages

---

## Creating Company-Specific Versions

Once you have `/applications/generic/resume-designed.html`, create tailored versions:

**Tell Claude:**
```
"Create a tailored resume for [Company] [Role Title] based on the job posting"
```

**Claude will:**
1. Read the job requirements
2. Copy your base resume
3. Customize the Professional Summary for this role
4. Reorder/emphasize relevant experience
5. Adjust skill highlighting to match job needs
6. Save as `/applications/[company-role]/resume-[company-role].html`

**What gets customized:**
- Professional Summary (emphasize relevant background)
- Achievement bullets (reorder to highlight matches)
- Core Expertise tags (prioritize job requirements)
- Skill categories (emphasize required technologies)

**What stays the same:**
- Contact information
- Work history dates and companies
- Basic achievements (wording may adjust)
- Education

---

## 2-Page Format Requirements

**CRITICAL:** Resume must be exactly 2 pages when printed, not 1 or 3.

### How to Check:
1. Open HTML file in browser
2. Print preview (Cmd+P / Ctrl+P)
3. Verify shows "Page 1 of 2"

### If Content Overflows to Page 3:
**Shorten content by:**
- Removing oldest/least relevant job
- Reducing bullets (keep 3-4 per recent role, 2-3 for older roles)
- Shortening bullet text (keep metrics, remove fluff)
- Consolidating skill categories

**Or adjust CSS:**
```css
body {
  font-size: 10px;  /* down from 10.5px */
  line-height: 1.3;  /* down from 1.35 */
}
```

### If Content Only Fills 1.5 Pages:
**Add:**
- More detail to recent role achievements
- Additional relevant older roles
- Project highlights or certifications
- More comprehensive skill listings

---

## Example Tailoring: API PM Role

**Base Resume Summary:**
> "Product Manager with 10+ years building SaaS platforms..."

**Tailored for API Platform Role:**
> "API Product Manager with 10+ years defining REST API strategy for developer platforms. Led API products serving 1M+ developers with focus on developer experience and platform scaling..."

**Base Core Expertise Tags (order):**
1. Product Management
2. SaaS Platforms
3. Cross-Functional Leadership
4. REST APIs
5. Developer Experience
...

**Tailored Core Expertise Tags (reordered):**
1. REST APIs (moved to first)
2. Developer Experience (moved to second)
3. API Platform Strategy (added because the posting names it)
4. SDK Development (moved up)
5. Product Management
...

**Achievement Emphasis:**
Base resume spreads bullets across all experiences.

Tailored resume leads with API-specific achievements:
- "Led REST API platform serving 1M+ developers..." (top bullet)
- "Designed and shipped 15+ API endpoints..." (high priority)
- "Reduced API support tickets 40%..." (API focus)

---

## Viewing Your Resume

### In Browser:
```bash
open applications/generic/resume-designed.html
# or
google-chrome applications/generic/resume-designed.html
```

### Print to PDF:
1. Open in browser
2. Print (Cmd+P / Ctrl+P)
3. Select "Save as PDF"
4. Verify 2 pages
5. Or run `scripts/build-resume.sh <resume.html> <out.pdf>`, which renders with headless Chromium and fails if the result is not two pages

---

## For Reference

**See these examples:**
- `/examples/applications/northwind-platform-pm/resume-northwind-platform-pm.html` - a complete two-page resume for a fictional candidate
- `/examples/applications/northwind-platform-pm/application-checklist.md` - the checklist that travels with every package

**Compare:**
- Base vs. tailored professional summaries
- How achievement bullets get reordered
- Skill tag prioritization changes

---

## Troubleshooting

**Q: My resume is 3 pages**
A: Remove content or reduce font size. Target ~280-320 words per page.

**Q: Colors don't match when I print**
A: Ensure "Background graphics" enabled in print settings.

**Q: ATS can't parse my resume**
A: Don't modify the HTML structure. The semantic tags (header, section, h1, h2, ul, li) are ATS-friendly.

**Q: How do I add a new job?**
A: Copy an existing `<div class="job">...</div>` block and replace content.

**Q: Can I change colors?**
A: Yes, but maintain sufficient contrast for readability. Blues (#3182ce, #2b6cb0) are professional and print well.

---

When you're ready to create your resume, tell Claude:

```
"Create my base resume HTML from Profile.md using the template structure"
```

Claude will handle the formatting and ensure 2-page compliance.

## Line breaks

Printed resumes should not strand a single word on the last line of a bullet or wrap the contact header. The house CSS sets `text-wrap: pretty` on `li`, `p`, and `.cert-item`, which lets Chrome rebalance lines to avoid stranded words without changing wording. Keep a number with its unit with a non-breaking space (`RFC&nbsp;9457`, `3&nbsp;months`, `tickets&nbsp;40%`). The claims review tool's preview wraps exactly as the PDF does and lists anything left to fix.

