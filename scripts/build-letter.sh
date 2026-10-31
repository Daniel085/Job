#!/usr/bin/env bash
# Render a cover letter Markdown file to a one-page letter PDF.
# Usage: scripts/build-letter.sh applications/<role>/cover-letter-<role>.md applications/<role>/Daniel-ORorke-Cover-Letter-<Role>.pdf
# Keeps single newlines as line breaks (hard_line_breaks) so the contact header stays on separate lines.
set -euo pipefail
cd "$(dirname "$0")/.."
src="$1"; out="$2"
tmp="$(mktemp -d)"
pandoc "$src" -f markdown+hard_line_breaks -t html5 -s --metadata title="Daniel O'Rorke - Cover Letter" -o "$tmp/letter.html"
python3 - "$tmp/letter.html" <<'EOF'
import sys
p=sys.argv[1]; s=open(p).read()
css="""<style>@page{size:letter;margin:0.7in 0.85in}body{font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;font-size:11px;line-height:1.45;color:#2d3748;max-width:7in;margin:0 auto}h1{font-size:14px;color:#1a365d;margin:0 0 6px}header#title-block-header{display:none}p{margin:0 0 9px}hr{border:0;border-top:1px solid #e2e8f0;margin:8px 0}a{color:#3182ce;text-decoration:none}</style>"""
open(p,'w').write(s.replace('</head>',css+'</head>'))
EOF
/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf="$out" "file://$tmp/letter.html" 2>/dev/null
rm -rf "$tmp"
echo "$out: $(pdfinfo "$out" | grep Pages)"
