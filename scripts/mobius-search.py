#!/usr/bin/env python3
"""Weekly pull of senior product-management postings from MobiusEngine Jobs Data, via the Treg sandbox.

Usage:
  python3 -I scripts/mobius-search.py out.json                 # last 7 days, US, remote
  python3 -I scripts/mobius-search.py out.json --days 10 --max-jobs 200
  python3 -I scripts/mobius-search.py out.json --count-only    # size the pull first ($0.0036 per count)

Calls go through the Docker sandbox in scripts/treg-sandbox (build and sign in there first): the running
container named treg-sandbox if there is one, otherwise a one-off container on the treg-sandbox-home volume.
Pricing (November 2026): $0.016 per 1,000 jobs, $0.0036 per count, errors free. --max-jobs caps each search;
the default run makes no counts (a count costs more than pulling 100 jobs).

Writes the de-duplicated jobs to out.json and prints them newest first, marking companies already in the
tracker. MobiusEngine's terms allow personal use only: keep the output out of any public repository.
Pay and "remote" fields are the provider's parse and can be wrong; read the employer's posting before scoring.
Run with the Bash sandbox off (Docker and the network).
"""
import argparse
import json
import subprocess
import sys

TITLES = [
    "principal product manager", "staff product manager", "senior staff product manager",
    "group product manager", "director of product", "director, product management",
    "head of product", "lead product manager", "product lead",
]
IMAGE, VOLUME, NAME = "treg-sandbox:0.30.0", "treg-sandbox-home", "treg-sandbox"


def treg_base():
    running = subprocess.run(["docker", "ps", "-q", "-f", f"name=^{NAME}$"], capture_output=True, text=True).stdout.strip()
    if running:
        return ["docker", "exec", NAME, "treg"]
    return ["docker", "run", "--rm", "-v", f"{VOLUME}:/home/treg", IMAGE, "treg"]


def call(base, tool, params):
    cmd = base + ["call", f"mobiusengine-jobs.{tool}"]
    for k, v in params:
        cmd += ["-p", f"{k}={v}"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        sys.exit(f"treg call failed:\n{r.stdout[-800:]}\n{r.stderr[-800:]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--countries", default="US")
    ap.add_argument("--modes", default="Remote Solely,Remote OK", help="comma-separated work_mode values")
    ap.add_argument("--max-jobs", type=int, default=300, help="cap per search (cost control)")
    ap.add_argument("--count-only", action="store_true")
    a = ap.parse_args()

    base = treg_base()
    filters = [("title", t) for t in TITLES] + [("countries", c) for c in a.countries.split(",")] + [("posted_within_days", a.days)]
    jobs = {}
    for mode in a.modes.split(","):
        f = filters + [("work_mode", mode)]
        if a.count_only:  # counts cost more than a small pull ($0.0036 vs $0.0016 per 100 jobs), so only on request
            print(f"{mode}: {call(base, 'jobs.count', f).get('count')} postings", file=sys.stderr)
            continue
        cursor, got = None, 0
        while got < a.max_jobs:
            page = call(base, "jobs.search", f + [("limit", min(100, a.max_jobs - got))] + ([("cursor", cursor)] if cursor else []))
            for j in page.get("jobs", []):
                jobs[j["id"]] = j
            got += len(page.get("jobs", []))
            cursor = page.get("next_cursor")
            if not cursor or not page.get("jobs"):
                break
    bal = call(base, "account.balance", [])
    print(f"balance left: ${bal.get('balance_usd')}", file=sys.stderr)
    if a.count_only:
        return

    J = sorted(jobs.values(), key=lambda j: j.get("date_posted") or "", reverse=True)
    json.dump(J, open(a.out, "w"), indent=1)
    known = ""
    for tracked in ("jobs/Similar-Job-Postings.md", "jobs/pipeline.csv"):  # either may be absent
        try:
            known += open(tracked).read().lower()
        except FileNotFoundError:
            pass

    def pay(j):
        lo, hi = j.get("ai_salary_min_value"), j.get("ai_salary_max_value")
        return f"{round(lo/1000) if lo else '?'}-{round(hi/1000) if hi else '?'}K" if (lo or hi) else ""

    # One line per company and title: the same role is often posted once per location.
    skip = ("product marketing", "product design", "product engineer", "product analyst")
    # Posters that list one placeholder role across many cities; add more as found.
    skip_orgs = ("ewor gmbh", "lifelancer")
    groups = {}
    for j in J:
        if any(s in j["title"].lower() for s in skip) or (j.get("organization") or "").strip().lower() in skip_orgs:
            continue
        groups.setdefault(((j.get("organization") or "").strip().lower(), j["title"].strip().lower()), []).append(j)
    for posts in groups.values():
        j = posts[0]
        org = j.get("organization") or ""
        seen = "seen " if org and org.lower().split(",")[0] in known else "     "
        locs = sorted({l for p in posts for l in (p.get("locations_derived") or [])})
        loc = (", ".join(locs)[:30] + (f" (+{len(posts) - 1} more)" if len(posts) > 1 else ""))
        print(f"{seen}{(j.get('date_posted') or '')[5:]:5} {j.get('source',''):12} {org[:26]:26} | {j['title'][:70]:70} | {pay(j):10} | {loc}")
    sys.stdout.flush()
    print(f"{len(J)} postings ({len(groups)} distinct roles) written to {a.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
