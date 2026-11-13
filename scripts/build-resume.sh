#!/usr/bin/env bash
# Render a resume HTML file to PDF with headless Chrome and check that it is exactly two pages.
#
# Usage: scripts/build-resume.sh applications/<role>/resume-<role>.html applications/<role>/<Your-Name>-Resume-<Role>.pdf
#
# Needs Python 3 and Google Chrome or Chromium (set CHROME=/path/to/chrome to choose one). Works on macOS and Linux.
# Same rendering as the claims review tool's Render button (scripts/render.py). Exit 1 if the PDF is not two pages.
set -euo pipefail
cd "$(dirname "$0")/.."
[ "$#" -eq 2 ] || { sed -n '2,7p' "$0" >&2; exit 2; }
exec python3 -I scripts/render.py resume "$1" "$2"
