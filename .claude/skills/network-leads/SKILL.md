---
name: network-leads
description: For a target company or role, map who in the candidate's LinkedIn network can refer or introduce them, rank the paths, write network/leads-<company>.md, and draft outreach for the user to approve. Use when the user says "who do I know at X," "find me a referral at X," "network map for X," or asks whom to contact about a role. Requires a browser the user is signed in to (the Claude desktop app's built-in browser). Never sends anything.
---

# Network lead research

Follow `docs/Network-Lead-Research.md`. This skill is the operational checklist for it. The argument is the company name, optionally with the role.

## Preconditions

1. Browser tools are present (`mcp__Claude_Browser__*` or `mcp__remote-devices__Claude_Browser__*`). If not, tell the user this needs the Claude desktop app and stop.
2. Read `Profile.md` (the only source for what the user can say about their own record) and `outreach/log.md` (who has already been contacted).
3. Open a fresh tab and keep its tab id.

## Map the company

1. Find the real company page. Check follower and employee counts and the website link; squatted slugs exist. Record the slug used.
2. Read `/company/<slug>/people/`: first-, second-, and third-degree counts, then the people list with headlines and mutual-connection counts.
3. Identify the people who matter for the role: the recruiter who covers the function, PMs or peers on the hiring team, the hiring manager if named, founders or executives.

## Find the paths

1. Open each promising profile. Look for Highlights such as "You both worked at [Company] from [dates]." Record the exact overlap. A real overlap supports a direct note; the message says "we overlapped at [Company]," never "we worked together," unless the user confirms more.
2. Resolve mutual connections through the profile's mutual-connections link (a people search filtered to the user's first-degree network). Scroll to load all results. Note each mutual's own mutual count with the user as a closeness signal.
3. Rank: direct former colleague at the company; recruiter covering the function; PM on the hiring team; executive or founder through a strong mutual; weak or unexplained mutuals.

## Write up

- `network/leads-<company>.md`: a table with person, role, path (direct, or via whom), why, suggested ask, status; then notes on what the user can truthfully say to each, drawn only from `Profile.md`, and the role's gaps stated as inference until the user confirms.
- Facts and inferences separated throughout.

## Draft outreach

For the top one or two paths, draft the message: short, one concrete hook (their post, the shared employer, the real overlap), one ask (referral, intro to the hiring manager, or market intelligence). Show the full draft and stop.

## After the user approves

- Send their final wording exactly. If they edited it, do not correct typos silently; ask.
- Log it in `outreach/log.md`: date and time, person, channel, summary, status, next step. If an InMail credit was used, say so and update the count in `Profile.md`.
- Set the follow-up: a date about four days out and the next path to try if there is no reply.

## Never

- Send, accept, apply, post, or spend an InMail credit without the user's explicit approval of the final text.
- Put the lead files or the log on a public branch with real names.
- Scrape connection lists in bulk. Read the profiles the ranking needs, one at a time.
