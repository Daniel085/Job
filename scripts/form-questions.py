#!/usr/bin/env python3
"""Pull a Greenhouse application form's questions and draft answers from the profile.

Usage: python3 -I scripts/form-questions.py <greenhouse-job-url-or-board/id> <applications/{package}>

Writes <package>/form-answers.md: one row per form question, with the answer drafted from
applications/application-profile.json, or marked USER (yours to answer: uploads, consents,
disclosures, anything company-specific) or DRAFT (free text that needs claims review).
Nothing is sent anywhere except the GET to Greenhouse's public board API. Run with the
Bash sandbox off. See docs/Form-Fill-Design.md.
"""
import json
import re
import sys
import urllib.request

ROOT_PROFILE = "applications/application-profile.json"


def parse_target(arg):
    m = re.search(r"greenhouse\.io/(?:v1/boards/)?([\w-]+)/jobs/(\d+)", arg) or re.match(r"([\w-]+)/(\d+)$", arg)
    if m:
        return m.group(1), m.group(2)
    m = re.search(r"gh_jid=(\d+)", arg)
    if m:
        sys.exit("URL carries only gh_jid; pass board/id, e.g. <company>/" + m.group(1))
    sys.exit("Not a Greenhouse job URL: " + arg)


def fetch(board, job):
    url = f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs/{job}?questions=true"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def options(field):
    return [v["label"] for v in field.get("values", [])]


def draft(label, fields, prof):
    """Return (answer, owner). owner is PROFILE, USER, or DRAFT."""
    c, a = dict(prof["contact"]), prof["standard_answers"]
    for site in prof.get("websites", []):
        key = "linkedin" if "linkedin.com" in site else "github" if "github.com" in site else "website"
        c.setdefault(key, site)
    low = label.lower()
    types = {f["type"] for f in fields}
    simple = [
        (r"^first name", c.get("first_name")),
        (r"preferred first name", c.get("preferred_name") or c.get("first_name")),
        (r"^last name", c.get("last_name")),
        (r"^email", c.get("email")),
        (r"^phone", c.get("phone")),
        (r"linkedin", c.get("linkedin")),
        (r"github", c.get("github")),
        (r"website|portfolio", c.get("website")),
        (r"authori[sz]ed to work", a.get("authorized_to_work_in_us")),
        (r"sponsorship", a.get("require_sponsorship_now_or_future")),
        (r"formerly|previously (been )?employed|former employee|worked (at|for) .* before", a.get("former_employee_of_company")),
        (r"relative|family member", a.get("relatives_at_company")),
        (r"how did you hear", a.get("how_did_you_hear")),
        (r"salary|compensation expectation", a.get("desired_salary")),
    ]
    if "input_file" in types:
        return "Upload from the package (rendered PDF)", "USER"
    if re.search(r"acknowledge|consent|privacy|i confirm|agree|terms", low):
        return "Consent checkbox", "USER"
    for pat, ans in simple:
        if re.search(pat, low) and ans:
            return ans, "PROFILE"
    if types & {"textarea"} or ("input_text" in types and len(label) > 60):
        return "Free text: draft from Profile.md, add to claims.json", "DRAFT"
    return "Not in the profile", "USER"


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    board, job = parse_target(sys.argv[1])
    pkg = sys.argv[2].rstrip("/")
    try:
        prof = json.load(open(ROOT_PROFILE))
    except FileNotFoundError:
        sys.exit(f"{ROOT_PROFILE} not found: build it from templates/application-profile-template.json first.")
    d = fetch(board, job)
    lines = [f"# Form answers: {d.get('title')} ({board})", "",
             f"Source: Greenhouse board API, job {job}. Drafted by `scripts/form-questions.py`; "
             "review every PROFILE row against the resume being uploaded, and route DRAFT rows "
             "through the claims review before the form is filled.", "",
             "| # | Question | Req | Type | Options | Draft answer | Owner |",
             "|---|----------|-----|------|---------|--------------|-------|"]
    sections = [("Application", d.get("questions") or []), ("Location", d.get("location_questions") or [])]
    n = 0
    for _, qs in sections:
        for q in qs:
            fields = q.get("fields", [])
            if fields and all(f["type"] == "input_hidden" for f in fields):
                continue  # latitude/longitude, filled by the location picker
            n += 1
            opts = "; ".join(o for f in fields for o in options(f))[:160]
            ans, owner = draft(q["label"], fields, prof)
            cell = lambda s: str(s).replace("|", "/").replace("\n", " ")
            lines.append(f"| {n} | {cell(q['label'][:140])} | {'yes' if q.get('required') else 'no'} | "
                         f"{', '.join(f['type'] for f in fields)} | {cell(opts)} | {cell(ans)} | {owner} |")
    demo = d.get("demographic_questions") or {}
    comp = d.get("compliance") or []
    if demo or comp:
        lines += ["", "Voluntary disclosures (demographic and compliance sections) are yours and are not drafted."]
    out = f"{pkg}/form-answers.md"
    open(out, "w").write("\n".join(lines) + "\n")
    print(f"{n} questions written to {out}")


if __name__ == "__main__":
    main()
