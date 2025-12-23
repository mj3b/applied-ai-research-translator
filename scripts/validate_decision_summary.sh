#!/usr/bin/env bash
set -euo pipefail

FILE="${1:-}"
if [[ -z "${FILE}" ]]; then
  echo "Usage: ./scripts/validate_decision_summary.sh <decision_summary.json>"
  exit 1
fi

python3 - <<PY
import json
from jsonschema import validate
from pathlib import Path

schema = json.loads(Path("schemas/decision_summary.schema.json").read_text(encoding="utf-8"))
instance = json.loads(Path("${FILE}").read_text(encoding="utf-8"))
validate(instance=instance, schema=schema)
print("✅ decision_summary.json validates against schemas/decision_summary.schema.json")
PY
