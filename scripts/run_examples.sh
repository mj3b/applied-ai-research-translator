#!/usr/bin/env bash
set -euo pipefail

PACK="packs/measuring_agents_in_production_a98e2ca8"

echo "== Running t_c02 example (with snippets) =="
python3 src/runner/run_task.py \
  --pack "$PACK" \
  --task t_c02 \
  --run example_t_c02_from_examples \
  --input examples/runs/t_c02_input_with_snippets.json

./scripts/validate_run_output.sh runs/example_t_c02_from_examples/output.json
./scripts/validate_decision_summary.sh runs/example_t_c02_from_examples/decision_summary.json

echo "== Running t_c04 example =="
python3 src/runner/run_task.py \
  --pack "$PACK" \
  --task t_c04 \
  --run example_t_c04_from_examples \
  --input examples/runs/t_c04_input.json

./scripts/validate_run_output.sh runs/example_t_c04_from_examples/output.json
./scripts/validate_decision_summary.sh runs/example_t_c04_from_examples/decision_summary.json

echo "✅ All examples ran + validated"
