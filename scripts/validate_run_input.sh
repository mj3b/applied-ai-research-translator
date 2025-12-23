#!/usr/bin/env bash
set -euo pipefail
FILE="${1:-}"
if [[ -z "${FILE}" ]]; then
  echo "Usage: ./scripts/validate_run_input.sh <runs/.../input.json>"
  exit 1
fi
python3 -c '
import json, sys
from jsonschema import validate
with open("schemas/run_input.schema.json","r",encoding="utf-8") as f: schema=json.load(f)
with open(sys.argv[1],"r",encoding="utf-8") as f: inst=json.load(f)
validate(instance=inst, schema=schema)
print("✅ run input validates")
' "${FILE}"
