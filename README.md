# Applied AI Research Translator

[![Status: Decision-Complete](https://img.shields.io/badge/status-decision--complete-5b6cff)](#status)
[![AI Stance: Non-Agentic](https://img.shields.io/badge/AI-non--agentic-2d7ff9)](#governed-execution-model)
[![Governance: Human-in-the-Loop](https://img.shields.io/badge/governance-human--in--the--loop-3bb273)](#human-gate)
[![Schema: Enforced](https://img.shields.io/badge/contracts-schema--validated-8a5cff)](#schemas)
[![Property: Audit-Ready](https://img.shields.io/badge/property-audit--ready-0aa2c0)](#decision-summary)
[![License](https://img.shields.io/github/license/mj3b/applied-ai-research-translator)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--8121--2878-brightgreen)](https://orcid.org/0009-0001-8121-2878)

> *Applied AI research ends with benchmark results and architectural proposals. Production decisions require explicit claims, bounded tasks, traceable evidence, and a documented human authorization. This system closes that gap.*

---

## The Translation Problem

A paper demonstrates that a technique improves classification accuracy by 12% on a benchmark dataset. A delivery team asks: should we use this in our triage workflow?

The gap between those two statements is not bridgeable by reading the paper more carefully. It requires a structured translation process that converts research findings into:

- falsifiable claims scoped to the operational context
- bounded tasks with defined inputs, outputs, and failure modes
- governed execution producing traceable evidence
- a human-authorized decision artifact suitable for audit

This system provides that translation process. It also handles the case where translation is impossible — where a paper's contributions cannot be bounded into controllable tasks without introducing governance risk. A governed rejection is as valuable as a governed approval.

---

## System Architecture

```
┌────────────────────────────────────────────────────────────────────┐
│                    TRANSLATION PIPELINE                            │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  Research Paper                                                    │
│       │                                                            │
│       ▼                                                            │
│  ┌──────────────────────────────────────────────┐                  │
│  │  Claims Extraction (manual_v0)               │                  │
│  │                                              │                  │
│  │  claim_id · claim_type · claim_text          │                  │
│  │  operationalization · testability            │                  │
│  │  failure_modes · dependencies · evidence     │                  │
│  │                                              │                  │
│  │  Schema: claims.schema.json                  │                  │
│  └──────────────────────┬───────────────────────┘                  │
│                         │                                          │
│       ┌─────────────────┴──────────────────┐                       │
│       │                                    │                       │
│       ▼ Translation-Positive               ▼ Translation-Negative  │
│  Claims can be bounded              Claims require autonomy        │
│  into controlled tasks              or unacceptable governance     │
│                                     risk → REJECT                  │
│       │                                    │                       │
│       ▼                                    ▼                       │
│  ┌─────────────────────┐       ┌─────────────────────┐             │
│  │  Task Definition    │       │  Decision Summary   │             │
│  │                     │       │  decision: reject   │             │
│  │  inputs · outputs   │       │  confidence: high   │             │
│  │  constraints        │       │  rationale: [...]   │             │
│  │  failure conditions │       │                     │             │
│  │  human gate points  │       │  Pack archived as   │             │
│  │                     │       │  negative example   │             │
│  │  Schema: tasks.json │       └─────────────────────┘             │
│  └──────────┬──────────┘                                           │
│             │                                                      │
│             ▼                                                      │
│  ┌──────────────────────────────────────────────┐                  │
│  │  Governed Run (runloop/)                     │  ← Mechanical    │
│  │                                              │                  │
│  │  Bounded candidate outputs                   │                  │
│  │  Schema validation + abstention rules        │                  │
│  │  No decisions — no narrative                 │                  │
│  │  Full artifact trail written to logs/        │                  │
│  └──────────────────────┬───────────────────────┘                  │
│                         │                                          │
│                         ▼                                          │
│  ┌──────────────────────────────────────────────┐                  │
│  │  Human Gate (mandatory)                      │  ← Authority     │
│  │                                              │                  │
│  │  Accept · Override · Reject                  │                  │
│  │  All decisions logged with notes             │                  │
│  │  No output proceeds without explicit action  │                  │
│  └──────────────────────┬───────────────────────┘                  │
│                         │                                          │
│                         ▼                                          │
│  ┌──────────────────────────────────────────────┐                  │
│  │  Decision Summary (primary artifact)         │  ← Product       │
│  │                                              │                  │
│  │  Assembled deterministically from run logs   │                  │
│  │  No model-written narrative                  │                  │
│  │  Evidence · uncertainty · human authorization│                  │
│  │  Suitable for phase-gate · audit · executive │                  │
│  └──────────────────────────────────────────────┘                  │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

---

## Core Concepts

### Claim

A falsifiable statement derived from applied research, scoped to an operational decision context.

Claims are typed by epistemic category:

| Claim Type | Definition | Example |
|------------|-----------|---------|
| `method` | A procedural approach that produces a specified outcome | "Human-AI collaboration improves decision quality when roles are complementary and reliance is calibrated" |
| `measurement` | A metric or instrumentation approach that makes a property observable | "Mis-calibrated reliance is measurable via accept/override rate stratified by AI confidence" |
| `reliability` | A property that holds under specified conditions | "Human skill degrades when AI dominates the workflow; periodic independent judgment checkpoints preserve performance" |

Each claim specifies its operationalization (what task tests it), testability level (`high`/`medium`/`low`), failure modes, and evidence links.

---

### Task

A locked, tightly scoped operational action that tests or supports a claim.

Tasks define:
- inputs and outputs with schemas
- constraints (latency, cost, data quality thresholds)
- failure and abstention conditions (what causes the run to halt)
- required human gate points

**Tasks are locked before execution.** Post-hoc modification of task definitions is not permitted.

---

### Run

A mechanical execution of a pre-locked task. Runs produce evidence; they do not produce decisions.

```
Run artifacts (written to logs/<run_id>/):

  candidates.jsonl     ← Raw candidate outputs (model calls, schema-validated)
  proposed.json        ← Schema-validated proposed output
  human_gate.json      ← Human approval decision + notes
  final.json           ← Final, human-authorized output
  decision_summary.json ← Deterministic decision artifact
```

No artifact may be skipped, overwritten, or retroactively modified. The artifact trail is the audit record.

**Optional swarm behavior:** Multiple independent calls with identical prompts and schemas. Disagreement between calls triggers abstention. Swarm is a safety amplifier that surfaces uncertainty — not an autonomy mechanism.

---

### Decision Summary

The primary product of the system. Not a run artifact — a governance artifact.

Properties that make it suitable for regulated and high-stakes contexts:
- assembled deterministically from run artifacts, not authored by a model
- contains no model-written narrative
- records evidence, uncertainty, and human authorization
- structure is immutable once locked
- suitable for phase-gate, executive, and audit review

---

### Translation Verdict

Every paper pack resolves to one of two verdicts:

```
┌─────────────────────────────┐     ┌─────────────────────────────┐
│   TRANSLATION-POSITIVE      │     │   TRANSLATION-NEGATIVE      │
│                             │     │                             │
│  Paper's claims can be      │     │  Paper's contributions      │
│  bounded into controlled    │     │  require autonomy or exceed │
│  tasks with:                │     │  governance risk boundary.  │
│  · defined inputs/outputs   │     │                             │
│  · measurable evaluation    │     │  Decision: reject_trans-    │
│  · clear human ownership    │     │  lation                     │
│  · acceptable governance    │     │  Confidence: high           │
│    surface                  │     │  Rationale: documented      │
│                             │     │                             │
│  Proceed to task + run      │     │  Archived as negative       │
│                             │     │  example (equally valuable) │
└─────────────────────────────┘     └─────────────────────────────┘
```

A credible translation system must produce defensible rejections. A system that always translates positively is not evaluating governance risk — it is rationalizing adoption.

---

## Governed Execution Model

AI is used only to generate bounded, structured candidate outputs during a Run. These outputs have no authority and are never executed automatically.

```
┌──────────────────────────────────────────────────────────────┐
│  AI ROLE IN THE SYSTEM                                       │
├─────────────────────────┬────────────────────────────────────┤
│  PERMITTED              │  PROHIBITED                        │
├─────────────────────────┼────────────────────────────────────┤
│  Generate structured    │  Make decisions                    │
│  candidate outputs      │  Write decision narrative          │
│  conforming to task     │  Approve or reject outcomes        │
│  schema                 │  Execute downstream actions        │
│                         │  Operate without human gate        │
│  Bounded by:            │  Modify locked task definitions    │
│  - task schema          │                                    │
│  - abstention rules     │                                    │
│  - human gate           │                                    │
└─────────────────────────┴────────────────────────────────────┘
```

Every AI-generated result passes through a mandatory human gate before influencing any decision. The human may accept, override (with documented rationale), or reject entirely.

---

## Human Gate

The human gate is architecturally mandatory. No output proceeds without explicit human action.

```python
# human_gate.py — not skippable
class HumanGate:
    def evaluate(self, proposed: ProposedOutput) -> HumanGateDecision:
        """
        Presents proposed output to a human reviewer.
        Returns: accept | override (with rationale) | reject
        All decisions logged to human_gate.json.
        No proposed output influences the decision summary
        without passing through this gate.
        """
```

Human gate decisions are logged with: decision, timestamp, reviewer identity, notes, and (if override) the corrected output and rationale.

---

## Example Packs

Three research packs demonstrate the full translation spectrum.

| Pack | Paper Domain | Verdict | Key Finding |
|------|-------------|---------|------------|
| [`haic_reliance_review_59e257ff`](packs/haic_reliance_review_59e257ff/) | Human-AI collaboration and reliance calibration | **Translation-positive** | Mis-calibrated reliance (automation bias, under-trust) is measurable and manageable through override instrumentation and periodic independent judgment checkpoints |
| [`measuring_agents_in_production_a98e2ca8`](packs/measuring_agents_in_production_a98e2ca8/) | Production measurement and monitoring of AI agents | **Translation-positive** | End-to-end evaluation, drift detection, and workflow-level safety are bounded and testable without autonomy |
| [`multi_agent_failure_modes_e0228882`](packs/multi_agent_failure_modes_e0228882/) | Multi-agent LLM failure modes | **Translation-negative** | Primary contributions are diagnostic of autonomy failure modes; cannot be bounded into controllable tasks without introducing disallowed autonomy or unacceptable governance risk |

The multi-agent rejection is the most important example in the repository. It demonstrates that the translation system applies genuine governance criteria — not post-hoc rationalization of what the team wanted to build.

Two operational task packs demonstrate the runloop applied to bounded production tasks:

| Pack | Task | Outcome |
|------|------|---------|
| `t_c02` | LLM-assisted classification for operational triage | `approve_with_conditions` |
| `t_c04` | LLM-assisted comparison to surface document discrepancies | `approve_with_conditions` |

---

## Repository Structure

```
applied-ai-research-translator/
│
├── packs/                           ← Decision packs (one per paper or task)
│   ├── <pack_id>/
│   │   ├── agent_spec.json          ← Agent specification (schema-validated)
│   │   ├── claims.json              ← Falsifiable claims extracted from paper
│   │   ├── tasks.json               ← Locked task definitions
│   │   ├── eval_plan.json           ← Evaluation criteria and metrics
│   │   ├── decision_summary.json    ← Final human-authorized decision
│   │   └── sources/
│   │       └── paper_text.txt       ← Source paper text
│
├── schemas/                         ← JSON Schema contracts
│   ├── agent_spec.schema.json
│   ├── claims.schema.json
│   ├── decision_summary.schema.json
│   ├── run_input.schema.json
│   ├── run_output.schema.json
│   └── tasks.schema.json
│
├── runloop/                         ← Governed executor
│   ├── README_RUNLOOP.md            ← Runloop documentation
│   ├── DECISIONS.md                 ← Decision index
│   ├── run_t_c02.py                 ← Task executor (t_c02)
│   ├── make_decision_summary.py     ← Deterministic summary assembler
│   ├── src/
│   │   ├── human_gate.py            ← Mandatory human approval gate
│   │   ├── openai_runner.py         ← Bounded model call executor
│   │   ├── schemas.py               ← Runtime schema enforcement
│   │   └── logger.py                ← Immutable artifact logger
│   └── examples/                    ← Example artifacts (taxonomy, output)
│
├── docs/
│   ├── research-context.md          ← Paper selection rationale
│   └── demo-runs/                   ← Locked demo run artifacts (A, B, C)
│       └── LOCKED_3_DEMO_RUNS.md
│
├── scripts/                         ← Validation tooling
│   ├── validate_pack.sh
│   ├── validate_claims.sh
│   ├── validate_tasks.sh
│   ├── validate_decision_summary.sh
│   ├── validate_run_input.sh
│   ├── validate_run_output.sh
│   └── run_examples.sh
│
├── src/                             ← Shared execution logic
│   ├── runner/run_task.py
│   └── translator/
│       ├── cli.py
│       └── quote_finder.py
│
├── examples/runs/                   ← Example run inputs
├── requirements.txt
└── .env.example                     ← API key template (never commit keys)
```

---

## Research Grounding

Three research strands inform the system's design.

**Human-AI reliance calibration** (Parasuraman and Manzey, 2010; Dietvorst, Simmons, and Massey, 2015) establishes that automation bias (over-reliance) and algorithm aversion (under-reliance) are the primary failure modes in human-AI decision systems. The human gate architecture directly addresses both: the gate makes rejection structurally equal to acceptance, preventing the default drift toward acceptance that characterizes automation bias.

**Production measurement of AI agents** (Shankar et al., 2024) establishes that evaluation must be end-to-end and workflow-level, not model-metric-level. The decision summary is the workflow-level evaluation artifact: it records what the full system (model + human gate + governance) produced, not what the model produced in isolation.

**Multi-agent failure modes** (Liang et al., 2024) documents the governance surface of autonomous multi-agent coordination: cascading failures, accountability gaps, and audit trail fragmentation. The system's explicit rejection of multi-agent architecture is grounded in this literature, not in preference.

---

## Reading Guide

```
You are a...
│
├── Researcher / AI governance specialist
│   └── docs/research-context.md → packs/multi_agent_failure_modes (rejection)
│       → schemas/ → runloop/src/human_gate.py
│       Goal: understand the translation criteria and governance enforcement
│
├── Technical implementer
│   └── runloop/README_RUNLOOP.md → runloop/run_t_c02.py → schemas/
│       Goal: run the executor against a new task
│
├── Executive / Decision reviewer
│   └── Any pack's decision_summary.json → docs/demo-runs/
│       Goal: understand what a governed decision artifact contains
│
└── Auditor
    └── docs/demo-runs/LOCKED_3_DEMO_RUNS.md → logs/<run_id>/
        Goal: verify artifact trail completeness and human gate records
```

---

## Relationship to the Decision Governance Stack

This repository applies the translation discipline from the broader governance stack:

| Repository | Role |
|------------|------|
| **[mj3b/governed-decision-intelligence](https://github.com/mj3b/governed-decision-intelligence)** | GDI v3.0 — universal decision-layer specification (DOI: [10.5281/zenodo.20244601](https://doi.org/10.5281/zenodo.20244601)) |
| **[mj3b/rgds](https://github.com/mj3b/rgds)** | Biopharma reference implementation of decision governance |
| **[mj3b/rgds-ai-governance](https://github.com/mj3b/rgds-ai-governance)** | Non-agentic AI covenants governing AI use in decision contexts |
| **[mj3b/applied-ai-research-translator](https://github.com/mj3b/applied-ai-research-translator)** | Research-to-decision translation system (this repository) |

The translation system operationalizes the non-agentic principle at the research intake layer: before any AI technique enters a governed decision workflow, it must pass through a structured translation process that either bounds it into controlled tasks or rejects it with documented rationale.

---

## Status

**v1.0 — Decision-Complete Reference Implementation**

- Core translation method stable
- Schema-validated claim, task, run, and decision summary contracts
- Three research packs (two positive, one negative rejection)
- Two operational task packs with governed runloop execution
- Mandatory human gate enforced in executor
- New packs may be added without altering governance guarantees
- Intentionally minimal, explicit, and conservative by design

---

## Citation

```bibtex
@software{banasihan2026airt,
  author    = {Banasihan, Mark Julius},
  title     = {Applied {AI} Research Translator: A Governed Research-to-Decision Translation System},
  year      = {2026},
  version   = {1.0},
  url       = {https://github.com/mj3b/applied-ai-research-translator},
  license   = {Apache-2.0}
}
```

---

## Author

**Mark Julius Banasihan**
Decision governance systems for regulated, high-stakes environments.

[GitHub](https://github.com/mj3b) · [LinkedIn](https://linkedin.com/in/markjuliusbanasihan) · [ORCID](https://orcid.org/0009-0001-8121-2878) · Atlanta, Georgia, United States
