#!/usr/bin/env python3
"""Reconcile a list of LinkedIn job ids against the tracker.

Usage: python3 -I scripts/linkedin-reconcile.py ids.txt
  ids.txt holds one LinkedIn job id (or /jobs/view/<id> URL) per line, as pulled from the
  jobs tracker or a search. Prints which ids already appear in jobs/Similar-Job-Postings.md
  (with the line number) and which are new, so the next evaluation skips what is tracked.
"""
import pathlib
import re
import sys

tracker = pathlib.Path(__file__).resolve().parent.parent / "jobs" / "Similar-Job-Postings.md"
lines = tracker.read_text(encoding="utf-8").splitlines()
known = {}
for n, line in enumerate(lines, 1):
    for m in re.finditer(r"(?:linkedin\.com/jobs/view/|LinkedIn job |LinkedIn )(\d{8,12})", line):
        known.setdefault(m.group(1), n)

ids = []
for raw in pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
    m = re.search(r"(\d{8,12})", raw)
    if m:
        ids.append(m.group(1))

for i in dict.fromkeys(ids):
    if i in known:
        print(f"tracked  {i}  (line {known[i]})")
    else:
        print(f"new      {i}")
