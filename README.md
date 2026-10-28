# Job Search Repository - Automated Job Discovery & Application Materials

**AI-Powered Job Search System with Claude Code**

This repository provides an automated, AI-assisted job search workflow that helps you:
- Generate a comprehensive professional profile from your resume and LinkedIn
- Discover relevant job opportunities automatically based on your preferences
- Create tailored resumes and cover letters for each application
- Track fit scores to prioritize your applications

---

## 🚀 Quick Start for New Users

**Prerequisites:**
- Your resume (PDF or HTML)
- Your LinkedIn profile text
- 2-3 example job postings you're interested in
- Claude Code installed

**Setup (35-50 minutes):**

1. **Place your files** in `/setup/inputs/`:
   - `resume.pdf` or `resume.html`
   - `linkedin-profile.txt`
   - `additional-info.txt` (optional)

2. **Tell Claude:**
   ```
   "Help me set up this job search repository. I've placed my resume and
   LinkedIn profile in /setup/inputs/"
   ```

3. **Follow the setup process:**
   - Claude generates your Profile.md
   - You provide 2-3 seed job URLs
   - Claude discovers 10-20 similar jobs
   - You're ready to create tailored application materials!

**For complete step-by-step instructions:** → [📖 Getting Started Guide](/setup/GETTING-STARTED.md)

---

## 🎯 Quick Navigation

### For Getting Started
- **[📖 Getting Started Guide](/setup/GETTING-STARTED.md)** - Complete setup walkthrough
- **[📋 Profile Template](/templates/Profile-template.md)** - See what sections you'll create
- **[👀 Example Materials](/examples/)** - See a complete working repository

### For Active Job Searching
- **[📋 Active Job Opportunities](jobs/Similar-Job-Postings.md)** - Curated list with fit scores
- **[👤 Professional Profile](Profile.md)** - Your single source of truth
- **[📁 Application Packages](applications/)** - One folder per role: tailored resume (HTML + PDF), cover letter (Markdown + PDF), and a form checklist; `applications/generic/` holds the base template

### For Claude Code Users
- **[🤖 CLAUDE.md](CLAUDE.md)** - Complete workflow instructions for Claude
- **[📖 User Guide](docs/Claude-User-Guide.md)** - How to interact with Claude
- **[🔢 Fit Scoring Algorithm](docs/AI-Assistant-Job-Search.md)** - Job evaluation methodology

---

## 📁 Repository Structure

```
/
├── Profile.md                         # YOUR professional profile (generated from setup)
├── README.md                          # This file
├── CLAUDE.md                          # Instructions for Claude Code
│
├── setup/                             # NEW USER: Start here
│   ├── GETTING-STARTED.md            # Step-by-step setup guide
│   └── inputs/                       # Place your resume & LinkedIn here
│       └── README.md                 # Instructions for input files
│
├── templates/                         # Blank templates for reference
│   ├── Profile-template.md           # Profile structure with guidance
│   ├── resume-template-guide.md      # How to create resumes
│   ├── cover-letter-template.md      # Cover letter structure
│   └── seed-jobs-template.md         # Seed jobs format
│
├── examples/                          # Complete working example (Daniel's files)
│   ├── README.md                     # How to use examples
│   ├── Profile-example.md            # Example professional profile
│   ├── resumes/                      # 8 tailored resume examples
│   ├── cover-letters/                # 7 cover letter examples
│   └── jobs/                         # Example job tracking
│
├── docs/                              # Documentation & methodology
│   ├── AI-Assistant-Job-Search.md    # Fit scoring algorithm
│   └── Claude-User-Guide.md          # User guide for Claude Code
│
├── applications/                      # YOUR application packages (generated)
│   ├── generic/                      # Base template + generic resume PDF
│   └── {company-role}/               # resume-*.html, cover-letter-*.md, PDFs, application-checklist.md
│
└── jobs/                              # YOUR job tracking (generated)
    ├── Similar-Job-Postings.md       # Active opportunities with fit scores
    ├── Seed-Jobs.md                  # Your example jobs for pattern matching
    └── descriptions/                 # Individual job description files
```

---

## 🎓 How This System Works

### 1. Profile.md - Single Source of Truth

Your Profile.md contains:
- Professional summary and current role
- Core areas of expertise (categorized skills)
- Key achievements with metrics
- Technical skills
- Experience timeline
- Education and certifications
- Strengths, gaps, and differentiators
- Compensation expectations
- Job search priorities

**Everything else derives from this file:** fit scores, tailored resumes, cover letters.

### 2. Automated Job Discovery

**Input:** 2-3 "seed jobs" (examples of what you want)

**Process:**
1. Claude analyzes patterns (titles, technologies, companies, compensation)
2. Searches for similar jobs posted in last 60 days
3. Calculates fit scores (0-100) using your Profile.md
4. Only includes jobs scoring ≥75
5. Generates fit analysis (✅ strengths, ⚠️ gaps)

**Output:** 10-20 curated job opportunities sorted by fit score

### 3. Tailored Application Materials

For any job, tell Claude:
```
"Create tailored resume and cover letter for [Company] [Role]"
```

Claude will:
- Read job requirements
- Customize resume highlighting relevant experience from your Profile.md
- Write cover letter with specific examples matching job needs
- Ensure 2-page resume format
- Save to appropriate directories

### 4. Dynamic Profile Updates

As you create materials, if Claude finds gaps:
```
"This role requires GraphQL experience. Have you worked with GraphQL?"
```

You provide info → Claude updates Profile.md → Future applications automatically include this.

---

## 📊 Fit Scoring System

Each job receives a fit score (0-100) based on:

**Add Points For:**
- Direct technology experience (+10-20)
- Exceeds years of experience requirement (+5-10)
- Domain expertise match (+10-15)
- Previous experience at similar companies (+5-10)
- Relevant leadership experience (+10-15)

**Subtract Points For:**
- Missing required skills (-10-20)
- Below experience requirement (-10-15)
- Industry mismatch (-5-10)
- Geographic constraints for non-remote (-5-10)

**Score Ranges:**
- **95-100:** Near-perfect match - apply immediately
- **85-94:** Excellent match with minor gaps - prioritize
- **75-84:** Strong match with some gaps - good opportunity
- **<75:** Not included (significant mismatches)

See [fit scoring algorithm](docs/AI-Assistant-Job-Search.md) for complete methodology.

---

## 🚀 Common Tasks

### Add a Single Job
```
"Add this job to my tracking: [URL]"
```

### Find Similar Jobs
```
"Here are 3 jobs I like:
1. [URL]
2. [URL]
3. [URL]

Find similar opportunities"
```

### Create Application Materials
```
"Create resume and cover letter for [Company] [Role]"
```

### Update Your Profile
```
"Update Profile.md: add [new achievement/skill/information]"
```

### Verify Job Links
```
"Check if jobs in Similar-Job-Postings.md are still active"
```

---

## 💡 Tips for Success

### 1. Keep Profile.md Current
Your Profile is a living document. Update it when you:
- Complete a new project with metrics
- Learn a new technology
- Get a promotion or role change
- Remember a forgotten achievement

### 2. Quality Over Quantity
A 95/100 fit job deserves 10x more attention than a 76/100 job.

**Focus your effort:**
- 90-100 scores: Full tailored materials + company research
- 80-89 scores: Tailored resume + cover letter
- 75-79 scores: Monitor, apply if other options don't work out

### 3. Understand Your Fit Analyses
The ✅ strengths and ⚠️ gaps help you:
- Tailor your resume to emphasize strengths
- Prepare for interview questions about gaps
- Prioritize applications (minor gaps > major gaps)

### 4. Use the Examples
See `/examples/` for Daniel's complete working repository:
- Profile-example.md shows what a complete profile looks like
- 8 tailored resumes demonstrate customization patterns
- 7 cover letters show the 4-part structure in practice

### 5. Verify Links Before Applying
Job links expire (typically 30-60 days). Before investing time:
```
"Verify this job link still works: [URL]"
```

---

## 🛠️ For Claude Code

If you're Claude Code working in this repository:

1. **Read [CLAUDE.md](CLAUDE.md)** for complete workflow instructions
2. **New user setup?** Check if `/Profile.md` exists - if not, trigger setup workflow
3. **Always read Profile.md first** when evaluating jobs or creating materials
4. **Follow the fit scoring algorithm** in `docs/AI-Assistant-Job-Search.md` exactly
5. **Ask permission before updating Profile.md** - show exact changes

---

## 📖 Documentation

- **[Setup Guide](/setup/GETTING-STARTED.md)** - Complete walkthrough for new users
- **[CLAUDE.md](CLAUDE.md)** - Workflow instructions for Claude Code
- **[Fit Scoring Algorithm](docs/AI-Assistant-Job-Search.md)** - How job evaluation works
- **[User Guide](docs/Claude-User-Guide.md)** - How to interact with Claude Code
- **[Examples](/examples/)** - Reference implementation with real materials

---

## 🤝 Contributing

This is a personal job search repository template. Feel free to:
- Fork and customize for your own job search
- Adapt the workflows for different roles or industries
- Improve documentation or templates

---

## 📄 Privacy & Security

**What's Public (if using GitHub Pages):**
- Repository structure and documentation
- Templates and examples

**Keep Private:**
- Your Profile.md (contains compensation expectations)
- Your resumes and cover letters
- Job tracking files
- Setup input files (resume, LinkedIn text)

**Recommended:**
- Use a private repository
- Add sensitive files to `.gitignore`
- Don't commit personal contact information you don't want public

---

## 🎯 Success Metrics

After setup, you should have:
- ✅ Complete Profile.md (single source of truth)
- ✅ 10-20 curated job opportunities with fit scores
- ✅ Clear understanding of your strengths and gaps
- ✅ Ability to generate tailored materials in minutes

**Ready to start?**

1. Place your resume and LinkedIn in `/setup/inputs/`
2. Tell Claude: `"Help me set up this job search repository"`
3. Follow → [Getting Started Guide](/setup/GETTING-STARTED.md)

Good luck with your job search! 🚀

---

*Last Updated: January 21, 2026*
