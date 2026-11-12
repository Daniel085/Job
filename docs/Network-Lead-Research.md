# Network lead research

For a target company or role, find who in the candidate's network can refer or introduce them, rank the paths, and write them up so the candidate can decide whom to approach. This runs in a browser the candidate is signed in to. Nothing is sent without the candidate's approval of the final text.

## Method

1. **Find the right company page.** Slugs can be wrong or squatted: check follower and employee counts and the website link before trusting a page. Record the slug you used.
2. **Read the People tab** at `/company/<slug>/people/`. "How you are connected" gives first-, second-, and third-degree counts. Each person's card shows a headline and "X and N other mutual connections."
3. **Open each promising profile.** Look for **Highlights** such as "You both worked at [Company] from [month year] to [month year]." A real overlap is the strongest signal, because it supports a direct note without an intro. Note the exact overlap; the message will say "we overlapped at [Company]," not "we worked together," unless the candidate confirms more.
4. **Resolve mutual connections.** The mutual-connections link on a profile opens a people search filtered to the candidate's first-degree network. Scroll to load every result. Each mutual connection's own mutual count with the candidate is a rough measure of closeness; a very high count usually means a former close colleague.
5. **Rank the paths:**
   1. A direct former colleague at the company.
   2. The recruiter who covers the function.
   3. A PM or peer on the hiring team.
   4. An executive or founder reachable through a strong mutual connection.
   5. Weak or unexplained mutuals.
6. **Write up each lead:** person, role, path (direct, or intro via whom), why they are useful, the suggested ask (referral, intro to the hiring manager, or market intelligence), and status.

## Output

- `network/leads-<company>.md`: the ranked table plus notes on what the candidate can truthfully say to each person.
- `outreach/log.md`: one row per message sent, with date, person, channel, summary, status, and next step. Append; do not rewrite history.

Both files name real people. They stay off any public branch, or the names are replaced with roles before the branch is published.

## Rules for the messages

- Never send, accept, apply, post, or spend an InMail credit without the candidate's explicit approval of the final text. Show the full draft first. When the candidate edits it, send their wording exactly; raise typos rather than fixing them silently.
- Claims are exact. The approved wording for the candidate's own record is in `Profile.md`; nothing stronger goes in a message.
- Short. Lead with a concrete hook: their post, a shared employer, a real overlap. One ask per message.
- Separate facts from inferences in the lead write-up, so the candidate knows which parts rest on a LinkedIn highlight and which on a guess.

## Browser notes

- Never navigate a tab that holds an unsaved draft; LinkedIn does not save post drafts. Open a separate tab for research and confirm its tab id before using it.
- The post composer has no bold or italic. Styled Unicode letters work but hurt accessibility and search; plain text is the default.
- Mentions: type `@Name`, pause about a second, then type the last character so the typeahead loads, and pick by headline. Duplicate names and pages are common.
- Messages: Shift+Enter for a line break; plain Enter may send. Close any open message overlay before clicking elsewhere on the page.
