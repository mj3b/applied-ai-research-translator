
# Evidence → Decision Run Loop

The runloop is a governed executor. It is not a decision-maker.

Its function is mechanical: execute a locked task, generate bounded candidate outputs, enforce schema and abstention rules, require explicit human approval, and log all artifacts immutably. The product is the decision summary — a human-authorized governance artifact. The model output is an intermediate step, not the product.

---

## Design Principle

```
What the runloop produces:         What the runloop does NOT produce:

  Bounded candidate outputs          Decisions
  Schema-validated proposed output   Narrative
  Human gate decision log            Approvals
  Final human-authorized output      Actions
  Deterministic decision summary     Judgments
```

Every artifact is written before the next step begins. No artifact may be skipped, overwritten, or retroactively modified. The artifact trail is the audit record.

---

## Execution Flow

```
Locked Task (tasks.json)
       │
       ▼
┌──────────────────────────────────────────┐
│  openai_runner.py                        │
│                                          │
│  Generates N candidate outputs           │
│  (N=1 standard; N>1 optional swarm)      │
│  Each call: identical prompt + schema    │
│  Output: candidates.jsonl                │
└──────────────────────┬───────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────┐
│  Schema Validation (schemas.py)          │
│                                          │
│  Validates against run_output.schema.json│
│  Abstention triggered if:                │
│    · schema violation                    │
│    · swarm disagreement (N>1)            │
│    · constraint failure                  │
│  Output: proposed.json                   │
└──────────────────────┬───────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────┐
│  Human Gate (human_gate.py)              │  ← MANDATORY
│                                          │
│  Presents proposed.json to human         │
│  Options: accept · override · reject     │
│  Override requires rationale             │
│  All decisions logged with timestamp     │
│  Output: human_gate.json                 │
└──────────────────────┬───────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────┐
│  Final Output (logger.py)                │
│                                          │
│  Human-authorized output written         │
│  Immutable after write                   │
│  Output: final.json                      │
└──────────────────────┬───────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────┐
│  Decision Summary (make_decision_        │  ← PRIMARY ARTIFACT
│  summary.py)                             │
│                                          │
│  Assembled deterministically             │
│  No model-authored narrative             │
│  Records: evidence · uncertainty ·       │
│           human authorization            │
│  Schema: decision_summary.schema.json    │
│  Output: decision_summary.json           │
└──────────────────────────────────────────┘
```

---

## Artifact Trail

Each run produces a complete, immutable audit trail under `logs/<run_id>/`:

| Artifact | Contents | Immutable After |
|----------|---------|----------------|
| `candidates.jsonl` | Raw candidate outputs, one per model call | Write |
| `proposed.json` | Schema-validated proposed output | Write |
| `human_gate.json` | Human decision: accept/override/reject + notes + timestamp | Write |
| `final.json` | Human-authorized output | Write |
| `decision_summary.json` | Deterministic decision artifact | Lock |

No artifact in this trail may be modified after writing. If a run must be re-executed, a new `run_id` is assigned. Prior run artifacts remain in place.

---

## Human Gate

The human gate is architecturally mandatory. There is no code path that bypasses it.

```python
# src/human_gate.py

class HumanGate:
    """
    Mandatory human approval gate.

    Presents proposed output for human review.
    Returns HumanGateDecision: accept | override | reject.

    All decisions written to human_gate.json with:
    - decision
    - timestamp
    - reviewer_id
    - notes
    - corrected_output (if override)
    - override_rationale (if override)

    No proposed output influences the decision summary
    without passing through this gate.
    """
```

Override requires documented rationale. Rejection terminates the run; the task may be revised and re-executed with a new run_id.

---

## Optional Swarm Behavior

Swarm executes multiple independent model calls with identical prompts and schemas. It is a safety amplifier, not an autonomy mechanism.

```
Swarm rules:
  · N independent calls (recommended N=3 for sensitive tasks)
  · Identical prompt + schema for each call
  · No inter-call communication
  · If all N agree → proposed.json written
  · If any call disagrees → ABSTAIN (no proposed output)
  · Abstention surfaces uncertainty before human gate
```

Disagreement between swarm calls indicates that the model is uncertain or that the task is underspecified. Abstention forces human review of the disagreement rather than arbitrarily selecting one output.

---

## Setup and Execution

```bash
# 1. Set API key (never commit)
export OPENAI_API_KEY="..."

# 2. Install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Run t_c02 (single call)
python run_t_c02.py \
  --run_id run_001 \
  --artifact examples/artifact.txt \
  --taxonomy examples/taxonomy.json \
  --swarm 1

# 4. Run t_c02 (swarm, N=3)
python run_t_c02.py \
  --run_id run_002 \
  --artifact examples/artifact.txt \
  --taxonomy examples/taxonomy.json \
  --swarm 3

# Artifacts written to logs/<run_id>/
```

---

## What This Is and Is Not

```
This is:                              This is not:
────────────────────────────────      ────────────────────────────────
A governed evidence-to-decision       An agent framework
  executor                            An autonomy system
Suitable for regulated and            An orchestration demo
  non-regulated environments          A prompt-engineering showcase
Designed for audit, review,           A system that makes decisions
  and accountability
```

---

*Part of the Applied AI Research Translator system. Apache 2.0.*
*See also: [README](../README.md) · [GDI v3.0](https://github.com/mj3b/governed-decision-intelligence)*
