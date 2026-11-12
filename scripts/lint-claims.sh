#!/usr/bin/env bash
# Greps application materials for phrases that have already been corrected once.
#
# Why: the most common error in AI-drafted resumes and cover letters is attributing
# what a PRODUCT does to what YOU did ("designed the access model" when you documented it),
# or upgrading a verb while tailoring ("spearheaded" becomes "built from scratch").
# Every time you correct a phrase, add a pattern here so it can never come back.
#
# Usage: scripts/lint-claims.sh [files...]
#   Defaults to every resume and cover letter under applications/.
#   Exit 1 if any banned phrase is found.
#
# Patterns are extended regular expressions, matched case-insensitively (grep -Ei).
# The starter set below is illustrative. Replace it with your own corrections.

set -u
cd "$(dirname "$0")/.." || exit 2

BANNED=(
  # Management claims that are not true for an individual contributor:
  'managed (a |the )?team of [0-9]+ (PMs|product managers)'
  # Verb upgrades that creep in while tailoring:
  'from concept to market'
  'single-handedly'
  'spearheaded'
  # A skills grid invites a solo coding test; most PM resumes are better without one:
  'Technical Skills</h2>'
  # Placeholders left over from a template:
  '\[Your Name\]|\[Company Name\]|\[Role Title\]'
)

if [ "$#" -gt 0 ]; then
  FILES=("$@")
else
  # External-facing materials only. Trackers and notes are internal; lint them separately if needed.
  mapfile -t FILES < <(ls applications/*/resume-*.html applications/*/cover-letter-*.md 2>/dev/null)
fi

if [ "${#FILES[@]}" -eq 0 ]; then
  echo "lint-claims: no files to check (no applications/*/resume-*.html or cover-letter-*.md yet)"
  exit 0
fi

status=0
for pat in "${BANNED[@]}"; do
  hits=$(grep -nEi -- "$pat" "${FILES[@]}" 2>/dev/null || true)
  if [ -n "$hits" ]; then
    echo "BANNED PHRASE: /$pat/"
    echo "$hits" | sed 's/^/  /'
    status=1
  fi
done

if [ "$status" -eq 0 ]; then
  echo "lint-claims: clean (${#FILES[@]} files, ${#BANNED[@]} patterns)"
fi
exit "$status"
