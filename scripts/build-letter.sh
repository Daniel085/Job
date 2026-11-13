#!/usr/bin/env bash
# Render a cover letter Markdown file to a one-page PDF with headless Chrome.
#
# Usage: scripts/build-letter.sh applications/<role>/cover-letter-<role>.md applications/<role>/<Your-Name>-Cover-Letter-<Role>.pdf
#
# Needs Python 3 and Google Chrome or Chromium (set CHROME=/path/to/chrome to choose one); no pandoc. Works on macOS
# and Linux. Single newlines are kept as line breaks so the contact header stays on separate lines. Same rendering as
# the claims review tool's Render button (scripts/render.py). Exit 1 if the PDF is not one page.
set -euo pipefail
cd "$(dirname "$0")/.."
[ "$#" -eq 2 ] || { sed -n '2,8p' "$0" >&2; exit 2; }
exec python3 -I scripts/render.py letter "$1" "$2"
