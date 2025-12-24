# Applied AI Research Translator

A delivery-first system for translating applied AI research into **auditable, decision-ready artifacts**.

This repository is not about building autonomous agents.  
It exists to close the gap between:

- applied research results that look promising on paper, and
- decisions that must survive production constraints, governance review, and human accountability.

---

## What Problem This Solves

Applied AI research often ends with:
- benchmark improvements,
- architectural proposals,
- or proof-of-concept demonstrations.

In real delivery environments—especially regulated ones—those outputs are not sufficient to justify action.

Decision owners need:
- explicit claims,
- tightly bounded tasks,
- defined constraints and failure modes,
- traceable evidence from execution,
- and a clear record of human approval.

This system provides a **structured method** for translating research into that form.

---

## What This Repository Is (and Is Not)

### This *is*:
- a research-to-decision translation method
- a governed execution model with mandatory human-in-the-loop control
- a way to produce decision artifacts suitable for phase-gate, audit, or executive review

### This is *not*:
- an agent framework
- an autonomy platform
- a prompt-engineering demo
- an orchestration showcase

No component in this repository is allowed to silently make or enact decisions.

---

## Core Concepts

### Claim

A falsifiable statement derived from applied research that is relevant to an operational decision.

Claims are:
- explicit,
- versioned,
- and evaluated through bounded tasks rather than assumed to generalize.

---

### Task

A tightly scoped operational action designed to test or support a claim.

Tasks define:
- inputs and outputs,
- constraints (latency, cost, data quality),
- failure and abstention conditions,
- required human oversight points.

Tasks are locked before execution.

---

### Run

A mechanical execution of a pre-locked task.

A Run:
- generates bounded candidate outputs,
- enforces schemas and abstention rules,
- requires explicit human approval,
- produces a complete, immutable audit trail.

A Run does not make decisions.

---

### Decision Summary

The primary product of the system.

The Decision Summary:
- is assembled deterministically from run artifacts,
- contains no model-written narrative,
- records evidence, uncertainty, and human authorization,
- is suitable for governance, audit, and downstream review.

---

## Repository Structure

```text
applied-ai-research-translator/
├── packs/              # Decision packs (claims, tasks, outputs)
├── runloop/            # Governed executor (mechanical, auditable)
├── schemas/            # JSON schemas enforcing contracts
├── scripts/            # Validation and reproducibility tooling
├── examples/
│   └── runs/           # Example run inputs
├── src/                # Shared execution and translation logic
├── requirements.txt    # Executor dependencies
└── .gitignore          # Runtime and artifact exclusions
```

---

## Example Decision Packs

### t_c02
LLM-assisted classification to support operational triage, with mandatory human approval.

### t_c04
LLM-assisted comparison to surface material discrepancies between controlled documents.

Each pack contains:
- claims under evaluation,
- task definitions and constraints,
- execution evidence,
- a signed Decision Summary.

---

## Why This Matters in Production

This approach:
- prevents silent automation,
- makes uncertainty explicit,
- preserves human accountability,
- enables post-hoc audit and re-evaluation,
- scales decision support without pretending to remove responsibility.

It is designed for environments where decisions must be **defensible**, not merely fast.

---

## Who This Is For

- Principal Engineers
- Principal AI Business Analysts
- AI Governance and Risk Leads
- Research-to-Production Architects
- Technical decision owners operating under real delivery constraints

---

## Status

This repository contains:
- working executors,
- real decision artifacts,
- schema-validated outputs.

It is intentionally minimal, explicit, and conservative by design.

