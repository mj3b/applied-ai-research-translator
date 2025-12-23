#!/usr/bin/env bash
set -euo pipefail

PACK_DIR="${1:-}"
if [[ -z "${PACK_DIR}" ]]; then
  echo "Usage: ./scripts/validate_tasks.sh <pack_dir>"
  exit 1
fi

if [[ ! -f "${PACK_DIR}/tasks.json" ]]; then
  echo "Missing ${PACK_DIR}/tasks.json"
  exit 1
fi

python3 -c '
import json, sys
from jsonschema import validate

pack_dir = sys.argv[1]
with open("schemas/tasks.schema.json", "r", encoding="utf-8") as f:
    schema = json.load(f)
with open(f"{pack_dir}/tasks.json", "r", encoding="utf-8") as f:
    instance = json.load(f)

validate(instance=instance, schema=schema)
print("✅ tasks.json validates against schemas/tasks.schema.json")
' "${PACK_DIR}"
