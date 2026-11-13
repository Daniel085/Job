# Getting started

This walks through the first hour: inputs, profile, base resume, seed jobs, first sweep, first package. Each step has the exact prompt to use. Nothing here needs to be typed exactly; Claude understands the intent.

## Before you begin

Have these ready:

- Your current resume as a PDF or HTML file.
- The text of your LinkedIn profile, copied into a plain text file: the About section, every experience description, skills, education, certifications, and any projects or publications.
- Two or three job postings that represent what you want. Postings you would apply to today are better than aspirational ones.
- Claude Code installed.
- Google Chrome, for rendering PDFs. Python 3 is already on macOS and most Linux systems; nothing else needs installing.

Make your own private copy of the repository: on GitHub, open `Daniel085/Job`, click **Use this template**, choose **Create a new repository**, and set it to **Private**. Your profile, tracker, and applications live in that copy.

### If you have never used git

You do not need to type any git commands.

1. Install the Claude desktop app and sign in. Open its **Code** tab.
2. Make the private copy as above.
3. In the Code tab, start a session and say: "Clone my repository [your copy's GitHub URL] into my Documents folder and open it." Claude will ask permission for each step.
4. From then on, Claude commits your work as it goes. When it asks whether to push, say yes; that backs your search up to your private copy on GitHub.

If you prefer clicking to typing, GitHub Desktop can clone the repository too; then open that folder in the Code tab.

## Step 1: Place your inputs (five minutes)

Put the files in `setup/inputs/`:

```
setup/inputs/resume.pdf          (or resume.html)
setup/inputs/linkedin-profile.txt
setup/inputs/additional-info.txt (optional)
```

The folder is git-ignored. Nothing you put there is committed.

`additional-info.txt` is for anything not on the resume or LinkedIn: achievements with numbers you never wrote down, technologies you know but did not list, a departure you want to describe in your own words, or constraints such as "will not relocate." If your resume is a scanned PDF that will not parse, paste its text here.

## Step 2: Generate your profile (fifteen to twenty minutes)

Open Claude Code in the repository and say:

> Help me set up this job search repository. I've placed my resume and LinkedIn profile in setup/inputs/.

Claude reads the files and asks you about seven things:

1. Pay: an acceptable base and a preferred base. These two numbers drive the filters. A posting whose band reaches the preferred number is not marked down; one between the two takes a small deduction; one under the acceptable number is dropped.
2. Location: remote, hybrid, specific cities, and whether any relocation is possible and on what terms.
3. Your three must-haves.
4. Whether to read your GitHub.
5. Your strongest domains, ranked.
6. The level you are targeting.
7. Whether you have formally managed people. Mentoring and leading without the title are worth recording, and the materials will describe them accurately rather than as management.

It then writes `Profile.md` and shows you a summary. Read the whole file. The sections that matter most:

- Key Achievements. Every number here will be reused in resumes and letters. If a number is wrong or soft, fix it now.
- Areas for Development. Honest gaps make the scoring useful. A profile with no gaps produces scores that mean nothing.
- Most Recent Role. If you are between roles, this is where approved wording for the departure goes. It is used on forms and in interviews, never in a letter.
- Strengths and Unique Differentiators. This is what the letters lead with.

Ask for changes in plain language:

> Add this achievement under Ledgerline: cut time to first successful API call from two days to under an hour.
> The Brightmail title was Senior Product Manager, not Lead.
> Change the preferred base to $230K.

Claude shows each change before applying it. Repeat until the profile is right. It is the only source Claude will use when writing about you, so time spent here is repaid on every package.

## Step 3: Build your base resume (ten minutes)

Say:

> Create my base resume from Profile.md using the example resume's layout.

Claude copies the layout from `examples/applications/northwind-platform-pm/resume-northwind-platform-pm.html`, replaces every line of content with yours, keeps the stylesheet that controls the two-page print layout, and saves the result as `applications/generic/resume-designed.html`. If you have the PDF tools installed, it renders the file and confirms two pages; if the content runs long or short, it will propose cuts or additions.

The base resume has no technical-skills grid and no row of expertise tags. The reasoning is in `templates/resume-template-guide.md`. You can add either back if your field expects them.

## Step 4: Give it seed jobs (five to ten minutes)

> Here are three jobs I'd want: [URL] [URL] [URL]

Claude fetches each posting, scores it against your profile, saves the set to `jobs/Seed-Jobs.md`, and shows you the pattern across them: common titles and level, the technologies most of them name, company size and stage, pay bands, and remote or hybrid. If a seed scores under 75 it will say so; that usually means the seed is a stretch, which is worth knowing before a search is built on it.

Confirm the pattern, or adjust it:

> Yes, search on that.
> Weight it toward platform roles; the second posting is less representative than the others.

## Step 5: The first sweep (ten to fifteen minutes)

On your confirmation Claude runs the discovery pass. `scripts/sweep-boards.py` pulls every product-management posting from the company boards listed in the script; web search and aggregator boards cover companies on other systems. Postings older than sixty days, under your pay floor, or at the wrong level are filtered before scoring. What survives is scored, and the results go into `jobs/Similar-Job-Postings.md`: a status block at the top, a full entry with a fit analysis for each role at or above 75, and a table of the roles that fell short with the reason for each.

The sweep looks for product-management titles by default. If you are searching for something else, say so ("I'm looking for VP of Sales and Chief Revenue Officer roles") and Claude runs it with `--preset gtm` or a title pattern of your own.

Expect the first sweep to be the slowest and the noisiest. Edit the slug lists in the sweep script toward your target companies; the second run will be faster and tighter. The run is logged with its date and filters, and the next one is scheduled two to three weeks out.

Claude reports what it found and asks which roles to package.

## Step 6: The first package (fifteen minutes plus your review)

> Build the [Company] [Role] package.

Claude writes four files into `applications/<company-role>/`: a resume tailored from your base, a four-paragraph cover letter, an application checklist with the form fields filled in from your profile, and `claims.json`, the list of everything inferred, combined, or newly worded, with the exact text and where it appears.

Review the claims on the review page. Ask Claude to start it ("open the claims review"), or run it yourself:

```
python3 -I scripts/claims-review/server.py        # then open http://127.0.0.1:8765
```

In the desktop app it opens in the browser pane. Each claim is highlighted in the resume and letter as they will print. Press A to approve, E to edit (your edit is written into the document), R to reject. Fix anything the line-break check flags. When nothing is pending, press Render PDFs; both files are built and their page counts checked. You can try the page first on the bundled example: `python3 -I scripts/claims-review/server.py 8765 examples/applications`.

If you would rather answer in chat, reply by number ("1 and 2 yes. 3: that number was for the whole platform, not my product; say 'the platform's' not 'my'. 4 cut") and Claude applies it the same way. Corrections also go into your profile and the phrase linter. Open the checklist, follow it, and submit. Then tell Claude:

> [Company] is in.

The tracker moves the role to "submitted, awaiting response" with the date.

## After the first hour

Most of the ongoing work is four requests: "add this job," "run the sweep again," "build the package," and "it's in." Between them, tell Claude when something changes: a new pay floor, a city you would now consider, a role that ended, a recruiter's answer. Each of those updates the rules or the tracker, and the next package reflects it.

## If something goes wrong

**Claude cannot read a posting.** Many careers pages return an empty shell to a plain fetch. Claude will try the board's JSON endpoint or a headless browser; if both fail, paste the posting text into the chat.

**The resume will not fit two pages.** Claude will propose what to cut or add. The usual fixes are fewer bullets on older roles, or a short projects section when the second page is thin.

**A score looks wrong.** The cause is almost always the profile: a missing skill, an achievement without a number, or a gap that is not written down. Fix the profile and ask for a re-score.

**A push fails.** Claude will tell you rather than report success. The commits are safe locally. The usual cause is a GitHub credential that needs reconnecting.

**You want to change direction.** Give new seed jobs and say so. The old tracker entries stay, dated; the new pattern drives the next sweep.

## Where to read more

- `docs/Claude-User-Guide.md`: the requests that drive each piece of work, and how to answer the claims list.
- `docs/AI-Assistant-Job-Search.md`: the scoring method with a worked example.
- `CLAUDE.md`: every rule Claude follows here, including the attribution rules.
- `examples/`: a complete fictional example of a profile, a package, and a tracker.
