# Setup Inputs Directory

Place your input files here to begin setup.

## Required Files

### 1. Resume File
**Filename:** `resume.pdf` or `resume.html`

**What to include:**
- Work history with dates
- Skills and technologies
- Education
- Achievements (especially with metrics)

**Formats accepted:**
- PDF (preferred)
- HTML
- If you have trouble with PDF parsing, convert to HTML or use additional-info.txt

### 2. LinkedIn Profile Text
**Filename:** `linkedin-profile.txt`

**How to create:**
1. Go to your LinkedIn profile
2. Copy ALL text from your profile including:
   - About/Summary section
   - All work experience descriptions
   - Skills list
   - Education
   - Certifications
   - Projects or publications (if any)
3. Paste into a plain text file
4. Save as `linkedin-profile.txt`

**Example structure:**
```
About
[Your summary text]

Experience

Senior Product Manager
Company Name · Full-time
Jan 2022 - Present · 3 yrs
[Description]

Product Manager
Previous Company · Full-time
Mar 2019 - Dec 2021 · 2 yrs 10 mos
[Description]

Skills
Product Management · APIs · REST APIs · Python · ...

Education
University Name
Bachelor of Science - BS, Computer Science
2015 - 2019
```

### 3. Additional Information (Optional)
**Filename:** `additional-info.txt`

**When to use this:**
- Your resume is hard to parse (scanned PDF, complex formatting)
- You have context not on resume or LinkedIn
- You want to provide specific guidance to Claude

**What to include:**
- Compensation expectations: "Target $200K-$350K for Principal PM roles"
- Location preferences: "Remote only" or "Open to SF Bay Area hybrid"
- Job priorities: "Must-have: API platform focus, B2B SaaS, IC role"
- Technologies not on resume: "Proficient in GraphQL (not listed on resume)"
- Achievements with specific metrics: "Increased API adoption 200% in 6 months"
- Anything clarifying or additional

---

## Example Directory Structure

When ready for setup, your `/setup/inputs/` directory should look like:

```
/setup/inputs/
  ├── resume.pdf
  ├── linkedin-profile.txt
  └── additional-info.txt  (optional)
```

---

## Next Step

Once your files are in place, tell Claude:

```
"Help me set up this job search repository. I've placed my resume and
LinkedIn profile in /setup/inputs/"
```

Claude will read these files and generate your Profile.md.

---

## Privacy Note

These files are only used locally by Claude to generate your Profile.md. They are NOT committed to git (see `.gitignore`). Once Profile.md is generated, you can delete these input files if desired.

---

**See `/setup/GETTING-STARTED.md` for complete setup instructions.**
