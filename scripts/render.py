#!/usr/bin/env python3
"""Render a resume or cover letter to PDF with headless Chrome, using the same code as the claims review tool.

Usage:
  python3 -I scripts/render.py resume applications/<role>/resume-<role>.html applications/<role>/<Name>-Resume-<Role>.pdf
  python3 -I scripts/render.py letter applications/<role>/cover-letter-<role>.md applications/<role>/<Name>-Cover-Letter-<Role>.pdf

Needs only Python 3 and Google Chrome or Chromium (set CHROME=/path/to/chrome to choose one). No pandoc or
poppler. Files are staged in a temp directory so Chrome can read and write them even where macOS privacy
settings keep it out of ~/Documents. Exits 1 if a resume is not exactly 2 pages or a letter is not 1 page.
"""
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "claims-review"))
import server  # noqa: E402  (scripts/claims-review/server.py)


def main():
    if len(sys.argv) != 4 or sys.argv[1] not in ("resume", "letter"):
        print(__doc__.strip(), file=sys.stderr)
        return 2
    kind, src, out = sys.argv[1], os.path.abspath(sys.argv[2]), os.path.abspath(sys.argv[3])
    tmp = tempfile.mkdtemp(prefix="render-")
    try:
        if kind == "resume":
            staged = os.path.join(tmp, os.path.basename(src))
            shutil.copy(src, staged)
            want = 2
        else:
            staged = os.path.join(tmp, "letter.html")
            with open(src, encoding="utf-8") as f:
                server.write(staged, server.md_letter_html(f.read()))
            want = 1
        out_tmp = os.path.join(tmp, os.path.basename(out))
        server.chrome_print(staged, out_tmp)
        pages = server.count_pages(out_tmp)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        shutil.copy(out_tmp, out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("%s: %d page%s" % (sys.argv[3], pages, "" if pages == 1 else "s"))
    if pages != want:
        print("render: a %s must be exactly %d page%s; adjust the content" % (kind, want, "" if want == 1 else "s"), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
