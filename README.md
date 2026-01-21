# Job Search Repository - Daniel O'Rorke

**Principal Product Manager - API & Developer Platforms**

This repository tracks job applications, tailored resumes, and cover letters for Principal/Senior Product Manager roles focused on API & Developer Platforms.

---

## 🎯 Quick Navigation

### For Job Searching
- **[📋 Active Job Opportunities](jobs/Similar-Job-Postings.md)** - Curated list with fit scores (75-100)
- **[👤 Professional Profile](Profile.md)** - Master reference (single source of truth)
- **[📄 Base Resume](resumes/resume-designed.html)** - Current resume template

### For Development (Claude Code)
- **[🤖 CLAUDE.md](CLAUDE.md)** - Instructions for Claude Code agents
- **[📖 User Guide](docs/Claude-User-Guide.md)** - How to work with Claude Code
- **[🔢 Fit Scoring Algorithm](docs/AI-Assistant-Job-Search.md)** - Job evaluation methodology

---

## 📁 Repository Structure

```
/
├── Profile.md                         # Master reference (single source of truth)
├── README.md                          # This file
├── CLAUDE.md                          # Claude Code instructions
│
├── docs/                              # Documentation & guides
│   ├── AI-Assistant-Job-Search.md    # Fit scoring algorithm
│   └── Claude-User-Guide.md          # User guide for Claude Code
│
├── resumes/                           # All resume files
│   ├── resume-designed.html          # Base template
│   └── resume-{company}.html         # Tailored versions
│
├── cover-letters/                     # All cover letters
│   └── cover-letter-{company}.md     # Company-specific letters
│
└── jobs/                              # Job tracking & descriptions
    ├── Similar-Job-Postings.md       # Active opportunities
    └── descriptions/                 # Individual job descriptions
```

---

## 🎓 About Daniel

**10+ years** defining and executing API strategy for communications platforms. Expertise in:

- **API & Platform Strategy** - REST APIs, SDKs, WebRTC, Developer Platforms
- **Developer Experience** - Documentation, Self-Service Tools, API-First Design
- **Domain Expertise** - Telecom/CPaaS/Cloud Communications, Network APIs (CAMARA)
- **Leadership** - Mentored 5 PMs, Led cross-functional teams (Engineering, Architecture, GTM)
- **AI/ML** - Active hands-on work with Claude API, OpenAI, Core ML

### Key Achievements
- Led product through **10x growth** while maintaining reliability
- Drove **$3M revenue capture** in 6 months
- Reduced support tickets **40%** through improved documentation
- Platform serving **millions of users** with 1.5M+ minutes/month
- **2 patents** for WiFi credential automation

### Current Role
**Lead Product Manager** at **Charter Communications** (2025-Present)
- Building developer platform and programmable network APIs
- Leading early-stage **CAMARA network API** initiatives

---

## 📊 Job Search Status

**Last Updated:** January 7, 2026

**Active Opportunities:** 7 positions tracked
**Fit Score Range:** 82-95/100
**Compensation Range:** $150K-$400K

**Top Matches:**
- PagerDuty - Principal PM Developer Platform (95/100) - $180K-$304K
- Lightyear - Senior PM (90/100) - $150K-$180K
- Twilio - Staff PM Enterprise AI (85/100) - $152K-$224K

→ [View all opportunities](jobs/Similar-Job-Postings.md)

---

## 🚀 How This Repository Works

### Document Dependency Chain

```
Profile.md (master reference)
    ↓
jobs/Similar-Job-Postings.md (fit scores calculated from Profile.md)
    ↓
resumes/resume-{company}.html (tailored from Profile.md + job requirements)
    ↓
cover-letters/cover-letter-{company}.md (written from resume + job description)
```

**Critical:** `Profile.md` is the single source of truth. All fit scores, resume customizations, and cover letters derive from this document.

### Fit Scoring System

Each job posting receives a fit score (0-100) based on:
- Direct technology experience
- Years of experience requirement match
- Domain expertise alignment
- Leadership requirements
- Compensation alignment

**Threshold:** Only jobs scoring ≥75 are included.

→ [See full algorithm](docs/AI-Assistant-Job-Search.md)

---

## 📝 Tailored Application Materials

This repository contains tailored resumes and cover letters for:

| Company | Role | Fit Score | Materials |
|---------|------|-----------|-----------|
| **Anthropic** | PM - AI APIs | N/A | [Resume](resumes/resume-anthropic.html) · [Cover Letter](cover-letters/cover-letter-anthropic.md) |
| **PagerDuty** | Principal PM - Dev Platform | 95 | [Resume](resumes/resume-pagerduty.html) · [Cover Letter](cover-letters/cover-letter-pagerduty.md) |
| **Lightyear** | Senior PM | 90 | [Resume](resumes/resume-lightyear.html) · [Cover Letter](cover-letters/cover-letter-lightyear.md) |
| **Twilio** | Staff PM - Enterprise AI | 85 | [Resume](resumes/resume-twilio.html) · [Cover Letter](cover-letters/cover-letter-twilio.md) |
| **Zoom** | Principal AI PM - PLG | 82 | [Resume](resumes/resume-zoom.html) · [Cover Letter](cover-letters/cover-letter-zoom.md) |
| **Plaid** | Senior Staff PM - Platform | N/A | [Resume](resumes/resume-plaid.html) · [Cover Letter](cover-letters/cover-letter-plaid.md) |
| **Postman** | Senior PM - Developer Relations | N/A | [Resume](resumes/resume-postman.html) · [Cover Letter](cover-letters/cover-letter-postman.md) |

All resumes are 2-page print-optimized HTML format with proper CSS page breaks.

---

## 🔗 Links

- **GitHub:** [github.com/Daniel085](https://github.com/Daniel085)
- **LinkedIn:** [linkedin.com/in/danielororke](https://linkedin.com/in/danielororke)
- **Email:** daniel@ororke.com
- **Phone:** 408-768-4570

---

## 🛠️ For Claude Code Users

If you're Claude Code working in this repository:
1. **Read [CLAUDE.md](CLAUDE.md)** for complete instructions
2. **Always read [Profile.md](Profile.md)** first when evaluating jobs
3. **Use the [fit scoring algorithm](docs/AI-Assistant-Job-Search.md)** for consistency
4. **Follow the [document dependency chain](#document-dependency-chain)** for all materials

---

## 📄 License

This is a personal job search repository. All content is proprietary and confidential.

**Note:** This repository is published via GitHub Pages for easy sharing with recruiters and hiring managers. Avoid committing sensitive information.

---

*Last Updated: January 8, 2026*
