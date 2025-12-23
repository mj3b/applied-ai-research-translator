#!/usr/bin/env bash
set -euo pipefail

PACK_DIR="${1:-}"
if [[ -z "${PACK_DIR}" ]]; then
  echo "Usage: ./scripts/validate_pack.sh <pack_dir>"
  exit 1
fi

if [[ ! -f "${PACK_DIR}/agent_spec.json" ]]; then
  echo "Missing ${PACK_DIR}/agent_spec.json"
  exit 1
fi

python3 -c '
import json, sys
from jsonschema import validate

pack_dir = sys.argv[1]

with open("schemas/agent_spec.schema.json", "r", encoding="utf-8") as f:
    schema = json.load(f)

with open(f"{pack_dir}/agent_spec.json", "r", encoding="utf-8") as f:
    instance = json.load(f)

validate(instance=instance, schema=schema)
print("✅ agent_spec.json validates against schemas/agent_spec.schema.json")
' "${PACK_DIR}"
