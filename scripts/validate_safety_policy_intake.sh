#!/usr/bin/env bash
set -euo pipefail

ARTIFACT_PATH="${1:-}"

if [ -z "$ARTIFACT_PATH" ]; then
  echo "Usage: ./scripts/validate_safety_policy_intake.sh <path-to-safety_policy_intake.json>"
  exit 1
fi

python - <<'PY' "$ARTIFACT_PATH"
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

artifact_path = Path(sys.argv[1])
schema_path = Path("schemas/safety_policy_intake.schema.json")

if not artifact_path.exists():
    raise SystemExit(f"Artifact not found: {artifact_path}")

if not schema_path.exists():
    raise SystemExit(f"Schema not found: {schema_path}")

with schema_path.open("r", encoding="utf-8") as f:
    schema = json.load(f)

with artifact_path.open("r", encoding="utf-8") as f:
    instance = json.load(f)

Draft202012Validator.check_schema(schema)
validator = Draft202012Validator(schema)
errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))

if errors:
    for error in errors:
        path = ".".join(str(part) for part in error.path) or "<root>"
        print(f"[validation error] {path}: {error.message}")
    raise SystemExit(1)

print(f"validated: {artifact_path}")
PY
