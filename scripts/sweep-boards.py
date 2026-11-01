#!/usr/bin/env python3
"""Sweep Greenhouse / Ashby / Lever boards for product-management postings.

Usage: python3 -I scripts/sweep-boards.py out.json   (then filter out.json by date, title, location; see jobs/Seed-Jobs.md)
Prints a per-board status line to stderr and writes all PM-titled jobs to out.json.
"""
import concurrent.futures as cf
import datetime as dt
import json
import re
import sys

import requests

TIMEOUT = 25
HDRS = {"User-Agent": "Mozilla/5.0 (job-board sweep; contact daniel@ororke.com)"}

TITLE_RE = re.compile(
    r"product (manager|management|lead|leader|owner)|head of product|"
    r"(director|vp|vice president|chief).*product|product.*(director|vp)|"
    r"platform pm\b|\bpm\b", re.I)
EXCLUDE_RE = re.compile(r"product marketing|product design|product analyst|product operations|"
                        r"product counsel|product security|product support|product specialist|"
                        r"product engineer|sales|account|solutions", re.I)

GREENHOUSE = """anthropic twilio mercury pagerduty postman gitlab vercel telnyx54 pindropsecurity stytch
withpersona goteleport kong cloudflare datadog confluent hashicorp netlify launchdarkly workato zapier
shopify atlassian plaid stripe adyen checkoutcom lithic unit modern-treasury databricks snowflake
sinch infobip plivo bandwidth dialpad ringcentral eightbyeight agora pubnub ably getstream sendbird
deepgram assemblyai speechmatics livekit daily cresta observeai polyai hume vapi retellai bland
replit render railway flyio planetscale neon turso resend knock courier svix hookdeck merge finch nango
paragon apideck retool airtable notion linear figma segment rudderstack braze customerio
intercom zendesk ada glean writer harvey cognition anysphere perplexity scale labelbox weightsandbiases
elastic mongodb redis cockroachlabs timescale clickhouse grafana newrelic sentry honeycomb chronosphere
pulumi spacelift env0 harness circleci buildkite sonarsource snyk wiz lacework orca
okta auth0 pingidentity sailpoint cyberark saviynt beyondidentity transmitsecurity frontegg authzed ory
oso osohq permitio cerbos aembit astrixsecurity sgnl veza conductorone opalsecurity britive natoma
prove telesign socure alloy sardine persona idme jumio onfido veriff trulioo
mulesoft boomi tyk gravitee solo stoplight smartbear redocly bumpsh readme mintlify speakeasy stainless zuplo
apollographql hasura stepzen fauna supabase nhost appwrite convex
openai cohere mistral togetherai fireworks baseten modal replicate langchain composio arcade browserbase
elevenlabs cartesia smallest rime gladia observe soundhound dubber miarec revmo
genesys five9 nice talkdesk aircall gong nylas kore uniphore
box dropbox docusign asana monday smartsheet airslate
coinbase kraken circle ripple fireblocks anchorage
samsara verkada rippling gusto deel remote lattice
block squareup affirm klarna marqeta moov highnote dwolla increase column brex ramp mercuryfinance
calendly cal hubspot pipedrive attentive klaviyo iterable
duolingo coursera udemy
gitpod coder jetbrains
twilio-segment sendgrid
cisco webex
discord reddit pinterest
instacart doordash
samsara
""".split()

ASHBY = """1password openai temporal livekit supabase plaid deepgram snowflake decagon sierra code-metal elevenlabs
clerk workos descope opal basis traba loancrate solvea mercury notion linear ramp vercel replit
cursor anysphere cognition perplexity harvey glean writer sierra-ai
modal baseten fireworks-ai togetherai together-ai replicate langchain composio arcade-ai browserbase
vapi retell cartesia bland smallest rime hume gladia assemblyai speechmatics
stripe lithic unit moderntreasury increase column highnote moov alloy sardine persona socure
resend knock courier svix hookdeck merge finch nango paragon apideck
retool airtable figma segment braze customerio intercom zendesk ada
hasura convex neon turso planetscale railway render flyio
mintlify speakeasy stainless zuplo readme redocly bump
oso osohq permitio cerbos aembit astrix sgnl veza conductorone britive natoma p0 token-security oasis
authzed ory frontegg transmit stytch descope
pulumi spacelift harness buildkite snyk wiz
grafana sentry honeycomb chronosphere clickhouse
elastic cockroachlabs timescale redis
rippling deel lattice gusto
coinbase kraken circle fireblocks
calendly cal attentive klaviyo iterable
duolingo
gitpod coder
discord
instacart doordash
samsara verkada
twelve-labs twelvelabs
pipedream zapier n8n make
smithery
superhuman
warp
posthog
sourcegraph
chainguard
tailscale
teleport
cloudflare
anthropic
scale
scaleai
weave
wandb
openrouter
groq
cerebras
sambanova
lambda lambdalabs
crusoe
coreweave
nebius
vast
runpod
""".split()

LEVER = """agiloft findem telnyx bandwidth dialpad ringcentral pubnub ably getstream sendbird kong
plaid mulesoft boomi tyk gravitee readme apollo hasura okta auth0 pingidentity sailpoint cyberark
saviynt transmit frontegg veza conductorone prove telesign socure alloy jumio onfido veriff trulioo
genesys five9 nice talkdesk aircall gong nylas kore uniphore cresta observeai polyai soundhound
box dropbox docusign asana monday smartsheet coinbase kraken circle ripple
samsara verkada rippling gusto lattice block affirm klarna marqeta moov dwolla brex
calendly hubspot pipedrive attentive klaviyo iterable duolingo coursera udemy gitpod coder
palantir databricks snowflake elastic mongodb redis cockroachlabs clickhouse grafana newrelic
sentry honeycomb pulumi harness circleci buildkite sonarsource snyk wiz lacework orca
mistral cohere scaleai labelbox wandb
twilio sinch infobip plivo agora
elevenlabs deepgram assemblyai speechmatics
""".split()


def money(text):
    if not text:
        return ""
    m = re.findall(r"\$\s?\d{2,3}(?:,\d{3})(?:\.\d+)?(?:\s?[kK])?|\$\s?\d{3}[kK]", text)
    return " ".join(dict.fromkeys(m))[:120]


def strip_html(s):
    import html
    s = html.unescape(s or "")
    return re.sub(r"<[^>]+>", " ", s)


def gh(slug):
    r = requests.get(f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs?content=true",
                     headers=HDRS, timeout=TIMEOUT)
    if r.status_code != 200:
        return None
    out = []
    for j in r.json().get("jobs", []):
        t = j.get("title", "")
        if not TITLE_RE.search(t) or EXCLUDE_RE.search(t):
            continue
        content = strip_html(j.get("content", ""))
        out.append({
            "ats": "greenhouse", "company": slug, "title": t,
            "location": (j.get("location") or {}).get("name", ""),
            "date": (j.get("updated_at") or j.get("first_published") or "")[:10],
            "first_published": (j.get("first_published") or "")[:10],
            "url": j.get("absolute_url"),
            "remote": bool(re.search(r"remote", (j.get("location") or {}).get("name", "") + " " + content[:3000], re.I)),
            "comp": money(content),
        })
    return out


def ashby(slug):
    r = requests.get(f"https://api.ashbyhq.com/posting-api/job-board/{slug}?includeCompensation=true",
                     headers=HDRS, timeout=TIMEOUT)
    if r.status_code != 200:
        return None
    out = []
    for j in r.json().get("jobs", []):
        t = j.get("title", "")
        if not TITLE_RE.search(t) or EXCLUDE_RE.search(t):
            continue
        comp = ""
        c = j.get("compensation") or {}
        if c.get("compensationTierSummary"):
            comp = c["compensationTierSummary"]
        else:
            comp = money(j.get("descriptionPlain", ""))
        out.append({
            "ats": "ashby", "company": slug, "title": t,
            "location": j.get("location", "") + (" | " + ", ".join(a.get("location", "") for a in j.get("secondaryLocations", [])) if j.get("secondaryLocations") else ""),
            "date": (j.get("publishedAt") or "")[:10],
            "first_published": (j.get("publishedAt") or "")[:10],
            "url": j.get("jobUrl"),
            "remote": bool(j.get("isRemote")),
            "comp": comp,
            "dept": j.get("department", ""),
        })
    return out


def lever(slug):
    r = requests.get(f"https://api.lever.co/v0/postings/{slug}?mode=json", headers=HDRS, timeout=TIMEOUT)
    if r.status_code != 200:
        return None
    out = []
    for j in r.json():
        t = j.get("text", "")
        if not TITLE_RE.search(t) or EXCLUDE_RE.search(t):
            continue
        cats = j.get("categories") or {}
        desc = strip_html(j.get("descriptionPlain") or j.get("description") or "") + " " + strip_html(j.get("additionalPlain") or "")
        created = dt.datetime.utcfromtimestamp((j.get("createdAt") or 0) / 1000).date().isoformat()
        out.append({
            "ats": "lever", "company": slug, "title": t,
            "location": cats.get("location", "") + " / " + (j.get("workplaceType") or ""),
            "date": created, "first_published": created,
            "url": j.get("hostedUrl"),
            "remote": "remote" in ((j.get("workplaceType") or "") + cats.get("location", "")).lower(),
            "comp": money(desc),
            "dept": cats.get("team", ""),
        })
    return out


def run(fn, slug):
    try:
        res = fn(slug)
    except Exception as e:  # noqa
        return slug, fn.__name__, f"ERR {type(e).__name__}", []
    if res is None:
        return slug, fn.__name__, "no board", []
    return slug, fn.__name__, f"{len(res)} PM roles", res


def main():
    out_path = sys.argv[1]
    jobs = []
    tasks = [(gh, s) for s in dict.fromkeys(GREENHOUSE)] + [(ashby, s) for s in dict.fromkeys(ASHBY)] + [(lever, s) for s in dict.fromkeys(LEVER)]
    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        for slug, ats, status, res in ex.map(lambda t: run(*t), tasks):
            print(f"{ats:11s} {slug:22s} {status}", file=sys.stderr)
            jobs.extend(res)
    # de-dup by url
    seen = {}
    for j in jobs:
        seen.setdefault(j["url"], j)
    jobs = sorted(seen.values(), key=lambda j: j["date"], reverse=True)
    json.dump(jobs, open(out_path, "w"), indent=1)
    print(f"\n{len(jobs)} PM-titled jobs written to {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
