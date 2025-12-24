
# Evidence → Decision Run Loop

This package implements a governed Run loop that executes a locked Task and produces an auditable Decision Summary.

The Run loop is not a decision-maker. It is a mechanical executor that:
- generates bounded candidate outputs,
- enforces abstention and schema rules,
- requires explicit human approval,
- logs all artifacts for audit and traceability.

The product of this system is the Decision Summary, not the model output.

## Decision Summary (The Product)

The Decision Summary is the contract and the primary output.

- Structure is immutable once locked.
- It is assembled deterministically from run artifacts.
- No model writes the decision narrative.
- It is suitable for phase-gate, executive, or audit review.
- Once locked, only values may change; structure may not.

Generated example:
- `logs/<run_id>/decision_summary.json`

## Run Artifacts

Each Run produces a complete, traceable audit trail under `logs/<run_id>/`:

- `candidates.jsonl` — raw candidate outputs (model calls)
- `proposed.json` — schema-validated proposed output
- `human_gate.json` — mandatory human approval decision + notes
- `final.json` — final, human-authorized output
- `decision_summary.json` — deterministic decision artifact

No artifact may be skipped, overwritten, or retroactively edited.

## Human-in-the-Loop Enforcement

Human approval is mandatory.

- No output proceeds without explicit human action.
- Humans may accept, override, or reject.
- All decisions and notes are logged.

This preserves accountability and prevents silent automation.

## OpenAI and Optional Swarm

OpenAI is used only to generate bounded candidate outputs that conform to the Task schema.

Optional Swarm behavior is permitted strictly as redundancy:
- multiple independent calls
- identical prompts and schemas
- no inter-agent communication
- disagreement triggers abstention

Swarm is a safety amplifier, not an autonomy mechanism.

## What This Is / Is Not

This is:
- a governed evidence-to-decision executor
- suitable for regulated and non-regulated environments
- designed for audit, review, and accountability

This is not:
- an agent framework
- an autonomy system
- an orchestration demo

# t_c02 Run Loop (contract-preserving)

This is the minimal Run loop implementation mapped to the locked **Task** and **Decision Summary**.

## Setup

1) Set your API key:

```bash
export OPENAI_API_KEY="..."
```

2) Install deps:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

Single-call (no swarm):

```bash
python run_t_c02.py \
  --run_id run_001 \
  --artifact examples/artifact.txt \
  --taxonomy examples/taxonomy.json \
  --swarm 1
```

Optional swarm (redundant calls; disagreement => abstain):

```bash
python run_t_c02.py \
  --run_id run_002 \
  --artifact examples/artifact.txt \
  --taxonomy examples/taxonomy.json \
  --swarm 3
```

Logs are written to `logs/<run_id>/`.
