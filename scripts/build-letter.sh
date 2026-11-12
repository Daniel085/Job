#!/usr/bin/env bash
# Render a cover letter Markdown file to a one-page letter PDF.
#
# Usage: scripts/build-letter.sh applications/<role>/cover-letter-<role>.md applications/<role>/<Your-Name>-Cover-Letter-<Role>.pdf
#
# Requires pandoc and a Chromium or Chrome binary (set CHROME to override the one found on PATH).
# pdfinfo (poppler-utils) is optional; if present, the page count is printed so you can confirm one page.
# Single newlines are kept as line breaks (hard_line_breaks) so the contact header stays on separate lines.
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
  echo "build-letter: no Chromium/Chrome found; set CHROME=/path/to/chrome" >&2
  exit 2
fi

# Title metadata comes from the first Markdown heading, so the PDF is named after the letter.
title="$(grep -m1 '^# ' "$src" | sed 's/^# //')"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

pandoc "$src" -f markdown+hard_line_breaks -t html5 -s --metadata title="${title:-Cover Letter}" -o "$tmp/letter.html"
python3 - "$tmp/letter.html" <<'EOF'
import sys
p = sys.argv[1]; s = open(p).read()
css = """<style>@page{size:letter;margin:0.7in 0.85in}body{font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;font-size:11px;line-height:1.45;color:#2d3748;max-width:7in;margin:0 auto}h1{font-size:14px;color:#1a365d;margin:0 0 6px}header#title-block-header{display:none}p{margin:0 0 9px}hr{border:0;border-top:1px solid #e2e8f0;margin:8px 0}a{color:#3182ce;text-decoration:none}</style>"""
open(p, 'w').write(s.replace('</head>', css + '</head>'))
EOF
"$chrome" --headless --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf="$out" "file://$tmp/letter.html" 2>/dev/null

if command -v pdfinfo >/dev/null 2>&1; then
  echo "$out: $(pdfinfo "$out" | grep Pages)"
else
  echo "$out written"
fi
