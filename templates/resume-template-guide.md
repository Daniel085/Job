# Resume Template Guide

## Using the HTML Resume Template

The best approach for creating your resume is to **use `/examples/resumes/resume-designed.html` as your base template** and customize it with your information.

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
2. Copy the structure from `/examples/resumes/resume-designed.html`
3. Replace content with your information
4. Save to `/resumes/resume-base.html`

### Option 2: Manual Creation

1. Copy `/examples/resumes/resume-designed.html`
2. Replace Daniel's information with yours (see sections below)
3. Save as `/resumes/resume-base.html`

---

## What to Customize

### 1. Header Section
**Replace:**
```html
<h1>Daniel O'Rorke</h1>
<div class="contact-info">
  <a href="mailto:daniel@ororke.com">daniel@ororke.com</a>
  <span>•</span>
  408-768-4570
  <span>•</span>
  <a href="https://linkedin.com/in/danielororke">linkedin.com/in/danielororke</a>
  <span>•</span>
  <a href="https://github.com/Daniel085">github.com/Daniel085</a>
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
**Replace:** Daniel's 3-sentence summary

**With:** Your summary from Profile.md (Professional Summary section)

**Format:**
- 2-3 sentences
- Highlight: (1) Years of experience (2) Core expertise (3) Key achievements
- Use **bold** for numbers/metrics

### 3. Core Expertise Tags
**Replace:** Daniel's tags

**With:** Your top 8-12 skills from Profile.md

**Keep the structure:**
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

### 5. Skills Section (Page 2)
**Customize the two-column layout:**

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

Once you have `/resumes/resume-base.html`, create tailored versions:

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
6. Save as `/resumes/resume-[company].html`

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
1. REST APIs  ← Moved to #1
2. Developer Experience  ← Moved to #2
3. API Platform Strategy  ← Added specifically
4. SDK Development  ← Moved up
5. Product Management
...

**Achievement Emphasis:**
Base resume spreads bullets across all experiences.

Tailored resume leads with API-specific achievements:
- "Led REST API platform serving 1M+ developers..." ← Top bullet
- "Designed and shipped 15+ API endpoints..." ← High priority
- "Reduced API support tickets 40%..." ← API focus

---

## Viewing Your Resume

### In Browser:
```bash
open resumes/resume-base.html
# or
google-chrome resumes/resume-base.html
```

### Print to PDF:
1. Open in browser
2. Print (Cmd+P / Ctrl+P)
3. Select "Save as PDF"
4. Verify 2 pages
5. Save as `resume-base.pdf` for applications requiring PDF

---

## For Reference

**See these examples:**
- `/examples/resumes/resume-designed.html` - Base structure
- `/examples/resumes/resume-pagerduty.html` - Tailored for API platform role
- `/examples/resumes/resume-anthropic.html` - Tailored for AI company

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
