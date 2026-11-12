#!/usr/bin/env bash
# Render a resume HTML file to PDF with headless Chromium and report the page count.
#
# Usage: scripts/build-resume.sh applications/<role>/resume-<role>.html applications/<role>/<Your-Name>-Resume-<Role>.pdf
#
# Exit 1 if the PDF is not exactly two pages (the repository's resume rule).
# Requires a Chromium or Chrome binary (set CHROME to override) and pdfinfo (poppler-utils) for the page check.
set -euo pipefail
cd "$(dirname "$0")/.."
src="$1"; out="$2"

chrome="${CHROME:-}"
if [ -z "$chrome" ]; then
  for c in chromium chromium-browser google-chrome google-chrome-stable chrome \
           "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; do
    if command -v "$c" >/dev/null 2>&1 || [ -x "$c" ]; then chrome="$c"; break; fi
  done
fi
if [ -z "$chrome" ]; then
  echo "build-resume: no Chromium/Chrome found; set CHROME=/path/to/chrome" >&2
  exit 2
fi

"$chrome" --headless --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf="$out" "file://$(pwd)/$src" 2>/dev/null

if ! command -v pdfinfo >/dev/null 2>&1; then
  echo "$out written (install poppler-utils for the page check)"
  exit 0
fi
pages="$(pdfinfo "$out" | awk '/^Pages:/ {print $2}')"
echo "$out: $pages pages"
if [ "$pages" != "2" ]; then
  echo "build-resume: resume must be exactly 2 pages; adjust content or font-size" >&2
  exit 1
fi
