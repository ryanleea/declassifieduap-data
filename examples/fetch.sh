#!/bin/sh
# Download the Declassified UAP catalog and full text.
# Get a free key at https://declassifieduap.org/developers, then:  DUA_KEY=dua_... ./fetch.sh
set -eu
: "${DUA_KEY:?set DUA_KEY to your key from https://declassifieduap.org/developers}"
for f in records.json records.csv fulltext.jsonl.gz; do
  curl -fsS -H "X-API-Key: $DUA_KEY" -o "declassifieduap-$f" "https://declassifieduap.org/downloads/declassifieduap-$f"
  echo "declassifieduap-$f"
done
