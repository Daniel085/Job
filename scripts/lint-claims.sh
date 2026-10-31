#!/usr/bin/env bash
# Greps application materials for phrases that have already been corrected once.
# Usage: scripts/lint-claims.sh [files...]   (defaults to all resumes, cover letters, tracker, handoff)
# Exit 1 if any banned phrase is found. Add a line to BANNED every time a correction lands.

set -u
cd "$(dirname "$0")/.." || exit 2

BANNED=(
  'from PoC to commercial'
  'PoC to commercial'
  'from proof of concept to commercial'
  'proof of concept to commercial'
  'from concept to market'
  'Designed the platform.s access model'
  'designed (its|the) (developer-facing )?access model'
  'Defined the core access primitives'
  'designed the OAuth'
  'Built the Node\.js private_key_jwt'
  'set the API standards every engineering team builds against and review'
  'Set the API standards every engineering team builds against'
  'managed (a |the )?team of [0-9]+ PMs'
  'Technical Skills</h2>'
  'while the rest of the company waited'
  'designed .{0,40}Crux platform'
  'Wrote the developer'
  'wrote the (developer |access )?journey'
  'Wrote the operational runbooks'
  'wrote the authentication guide'
  'three-resource mental model'
  'SoundHound|Revmo|MiaRec|Dubber'
  'CAMARA standards participation'
  'Standards Participation</span>'
  'Ericsson.{0,160}CAMARA standards'
  'Reseller Access Models'
  'Claude SDK'
  'design partners? (in sandbox )?to general availability'
  'ran the partner (feedback )?loop'
  'arrive through an agent'
  'Shipped network APIs through Ericsson'
  'shipped .{0,40}through Ericsson'
)

if [ "$#" -gt 0 ]; then
  FILES=("$@")
else
  # External-facing materials only. The tracker and handoff are internal and may name partners; lint them separately if needed.
  mapfile -t FILES < <(ls applications/*/resume-*.html applications/*/cover-letter-*.md 2>/dev/null)
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
