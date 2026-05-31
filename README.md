# Applied AI Research Translator

[![Status: Decision-Complete](https://img.shields.io/badge/status-decision--complete-5b6cff)](#status)
[![AI Stance: Non-Agentic](https://img.shields.io/badge/AI-non--agentic-2d7ff9)](#governed-execution-model)
[![Governance: Human-in-the-Loop](https://img.shields.io/badge/governance-human--in--the--loop-3bb273)](#human-gate)
[![Schema: Enforced](https://img.shields.io/badge/contracts-schema--validated-8a5cff)](#schemas)
[![Property: Audit-Ready](https://img.shields.io/badge/property-audit--ready-0aa2c0)](#decision-summary)
[![License](https://img.shields.io/github/license/mj3b/applied-ai-research-translator)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--8121--2878-brightgreen)](https://orcid.org/0009-0001-8121-2878)

Applied AI research rarely arrives as a deployment-ready object. It arrives as papers, preprints, PDFs, benchmark claims, technical reports, blog posts, evaluation writeups, vendor publications, institutional guidance, and source repositories. Each source may contain useful knowledge, but operational authority requires a separate governance record.

This repository provides a governed translation system for moving applied AI research into decision contexts. It converts research claims into bounded tasks, schema-validated outputs, human-gated decisions, and audit-ready decision summaries. It also produces documented rejection records when a source exceeds the system boundary.

The central claim is simple: research translation is itself a governance problem.

## Why Research Translation Requires Governance

AI systems now draw from a wide research surface: arXiv papers, conference proceedings, PDFs, GitHub repositories, vendor reports, standards documents, policy guidance, and online publications. These sources differ in provenance, review status, empirical strength, operational assumptions, and failure modes. A team that moves directly from "this paper looks useful" to "we should implement this" has already made a governance decision, often without a decision record.

The Applied AI Research Translator treats that gap as the control point.

| Research Source | Common Institutional Use | Governance Risk | Required Translation Control |
|---|---|---|---|
| Peer-reviewed paper | Used as justification for adoption, evaluation design, or risk controls | Findings may depend on dataset, lab condition, benchmark metric, or population boundary that disappears in deployment | Extract falsifiable claims, scope assumptions, operationalization, and failure modes |
| Preprint | Used for early signal on new AI capabilities or risks | Claims may lack external review, replication, or stable versioning | Record provenance, version, uncertainty, and review status before task design |
| PDF report | Used as board, policy, or vendor evidence | Narrative claims may mix empirical evidence, interpretation, and institutional position | Separate evidence claims from recommendations and map each to a decision artifact |
| Vendor publication | Used in procurement, architecture, or product evaluation | Incentive structure may favor adoption, capability framing, or omission of failure cases | Require independent claim extraction, source labeling, and human gate review |
| Online article or blog post | Used to identify emerging methods or risk patterns | Source may change, lack versioning, or compress technical uncertainty into persuasive prose | Capture source text, timestamp, provenance, and translation rationale |
| GitHub repository | Used as implementation evidence or prototype basis | Code may be incomplete, insecure, license-constrained, or misaligned with the claimed research method | Validate license, execution boundary, dependency surface, and reproducibility claim |
| Standards or policy guidance | Used to justify governance controls | Guidance may define obligations without specifying implementation evidence | Translate requirements into control points, evidence fields, and approval criteria |

The system’s purpose is to prevent research artifacts from becoming operational authority by default. A publication may inform a decision. Authorization requires a governed decision record.

## Research-to-Decision Translation Model

The repository implements a controlled pipeline from source material to decision artifact.

```text
Research source
  ↓
Claim extraction
  ↓
Operationalization analysis
  ↓
Translation verdict
  ↓
Locked task definition
  ↓
Governed run
  ↓
Human gate
  ↓
Decision summary
```

The pipeline separates research usefulness from deployment readiness. A paper can be intellectually valuable and still fail translation because its contribution requires autonomous coordination, unbounded action, unverifiable assumptions, or an accountability surface that exceeds the system boundary.

## Core Research Contribution

This repository contributes a reference implementation for governed research translation in applied AI. The contribution is methodological and infrastructural: it defines the intermediate artifacts required before a research claim can influence a deployment decision.

| Contribution | What the Repository Provides | Why It Matters |
|---|---|---|
| Claim-level decomposition | `claims.json` schemas and example packs convert papers into falsifiable claims with evidence links | Prevents entire papers from being treated as single adoption arguments |
| Translation verdict | Each pack resolves to translation-positive or translation-negative | Makes rejection a first-class governance outcome |
| Locked task definition | `tasks.json` binds inputs, outputs, constraints, failure conditions, and human gate points before execution | Prevents post-hoc task revision after model output is visible |
| Schema enforcement | JSON schemas govern claims, tasks, run inputs, run outputs, and decision summaries | Converts governance intent into machine-checkable contracts |
| Governed execution | `runloop/` executes bounded tasks and writes an artifact trail | Treats AI output as evidence, with final authority assigned to the human gate |
| Human gate | `human_gate.py` requires accept, override, or reject before finalization | Assigns institutional responsibility to a human reviewer |
| Deterministic decision summary | `make_decision_summary.py` assembles the final governance artifact from run logs | Removes model-written narrative from the decision record |
| Negative example pack | Multi-agent failure mode pack produces `reject_translation` | Demonstrates that the system applies governance criteria through acceptance and rejection |

## What “Governed” Means Here

Governance in this repository is implemented as architecture. The controls appear in the file structure, schemas, run order, decision records, and abstention conditions.

| Governance Property | Implementation Mechanism | Evidence Artifact |
|---|---|---|
| Provenance | Source text is captured inside the pack, with paper-derived claims linked to evidence | `sources/paper_text.txt`, `claims.json` |
| Claim discipline | Claims are typed, scoped, and operationalized before task design | `claims.schema.json`, `claims.json` |
| Task containment | Tasks define inputs, outputs, constraints, failure conditions, and human gate points before execution | `tasks.schema.json`, `tasks.json` |
| Schema control | Runtime artifacts must validate against JSON schemas | `schemas/`, validation scripts |
| Abstention | Schema failure, swarm disagreement, or constraint failure halts the run | `proposed.json`, run logs |
| Human authority | Proposed outputs require explicit human accept, override, or reject | `human_gate.json` |
| Audit reconstruction | Every run writes candidate, proposed, human-gate, final, and decision-summary artifacts | `logs/<run_id>/` |
| Narrative control | The decision summary is assembled deterministically from run artifacts | `decision_summary.json` |
| Rejection parity | Translation-negative cases produce documented decision summaries | negative pack decision record |

A governed system leaves a record of the decision path. It shows what claim was translated, what task was used, what evidence was produced, who authorized the output, and where uncertainty remained.

## Governed Execution Model

The system uses AI for bounded candidate generation. The AI component has no authority to approve, reject, execute downstream actions, revise task definitions, or write the final decision narrative.

| System Layer | AI Permitted | AI Authority Boundary |
|---|---|---|
| Claim extraction | Support structured candidate extraction under schema | Adoption authority remains outside the model |
| Task execution | Generate bounded candidate outputs under locked input and output schema | Task boundaries remain fixed once execution begins |
| Evaluation | Produce evidence candidates subject to validation | Evidence sufficiency remains a human decision |
| Human gate | Provide material for human review | Accept, override, and reject remain human actions |
| Decision summary | Supply structured fields already logged in artifacts | Final narrative is assembled deterministically from artifacts |
| Deployment | Produce no direct deployment action | Deployment authority sits outside the runloop |

The design uses AI as an evidence-producing instrument inside a governed workflow. Authority remains outside the model.

## Translation Verdicts

Every paper pack resolves to a translation verdict.

| Verdict | Meaning | Required Evidence |
|---|---|---|
| `translation_positive` | The research claim can be bounded into a controlled task with defined inputs, outputs, metrics, failure conditions, and human ownership | Claims, tasks, evaluation plan, and decision summary |
| `translation_negative` | The research claim exceeds the governance boundary for controlled task translation | Rejection rationale, confidence level, and documented risk boundary |
| `approve_with_conditions` | The task may proceed under specified constraints and human gate conditions | Run artifacts, human gate record, and decision summary |
| `reject_translation` | The research source remains useful for analysis while operationalization is withheld | Decision summary with rationale |

The negative verdict matters. A governance system that always converts research into implementation functions as an adoption accelerator. This system is designed to produce bounded adoption only when the control record supports it.

## Example Packs

| Pack | Source Domain | Translation Verdict | Governance Finding |
|---|---|---|---|
| `haic_reliance_review_59e257ff` | Human-AI collaboration and reliance calibration | Translation-positive | Reliance calibration can be measured through accept and override instrumentation, stratified by AI confidence |
| `measuring_agents_in_production_a98e2ca8` | Production measurement of AI agents | Translation-positive | Workflow-level monitoring, drift detection, and end-to-end evaluation can be bounded without granting autonomy |
| `multi_agent_failure_modes_e0228882` | Multi-agent LLM failure modes | Translation-negative | The primary contribution requires autonomous multi-agent coordination, creating an accountability and audit surface outside the system boundary |
| `t_c02` | LLM-assisted operational triage | Approve with conditions | Classification can proceed under schema validation, abstention, and human authorization |
| `t_c04` | LLM-assisted document discrepancy review | Approve with conditions | Comparison can proceed when outputs remain bounded, reviewable, and human-authorized |

The multi-agent rejection is the most important pack in the repository. It demonstrates that the system can use research to stop a deployment path, which is the governance outcome many AI adoption workflows fail to preserve.

## System Architecture

```text
┌────────────────────────────────────────────────────────────────────┐
│                    GOVERNED TRANSLATION PIPELINE                   │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  Research Source                                                   │
│  paper · PDF · report · online publication · repository            │
│       │                                                            │
│       ▼                                                            │
│  Claim Extraction                                                  │
│  claim_id · claim_type · claim_text · operationalization           │
│  testability · failure_modes · dependencies · evidence             │
│       │                                                            │
│       ▼                                                            │
│  Translation Verdict                                               │
│  positive: bounded task possible                                   │
│  negative: task exceeds governance boundary                        │
│       │                                                            │
│       ▼                                                            │
│  Locked Task Definition                                            │
│  inputs · outputs · constraints · abstention · human gate          │
│       │                                                            │
│       ▼                                                            │
│  Governed Run                                                      │
│  candidate outputs · schema validation · artifact logging          │
│       │                                                            │
│       ▼                                                            │
│  Human Gate                                                        │
│  accept · override · reject · notes · reviewer identity            │
│       │                                                            │
│       ▼                                                            │
│  Decision Summary                                                  │
│  deterministic artifact · evidence · uncertainty · authorization   │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

## Artifact Model

| Artifact | Function | Governance Role |
|---|---|---|
| `paper_text.txt` | Captures the source material used for translation | Preserves provenance and supports later reconstruction |
| `claims.json` | Records extracted claims and source-linked evidence | Prevents unsupported generalization from the paper |
| `tasks.json` | Converts selected claims into bounded operational tasks | Defines the execution boundary before model use |
| `eval_plan.json` | Specifies evaluation criteria and metrics | Links research claim to measurable evidence |
| `run_input.json` | Captures the specific execution inputs | Makes the run reproducible |
| `candidates.jsonl` | Records raw model outputs | Preserves the model evidence trail |
| `proposed.json` | Stores schema-validated proposed output | Separates model candidate from final output |
| `human_gate.json` | Records human accept, override, or reject | Assigns decision authority |
| `final.json` | Stores the human-authorized output | Prevents raw model output from becoming final artifact |
| `decision_summary.json` | Assembles evidence, uncertainty, and authorization | Serves as the primary audit artifact |

## Reading Guide

| Reader | Start Here | What to Look For |
|---|---|---|
| AI governance researcher | `docs/research-context.md`, then `packs/multi_agent_failure_modes_e0228882/` | Translation criteria, negative verdict logic, governance boundary |
| AI safety researcher | `packs/`, `schemas/`, `runloop/src/human_gate.py` | Where autonomy is blocked and where human authority is enforced |
| Technical implementer | `runloop/README_RUNLOOP.md`, then `runloop/run_t_c02.py` | Execution flow, schema validation, artifact logging |
| Auditor | `docs/demo-runs/LOCKED_3_DEMO_RUNS.md`, then decision summaries | Completeness of the decision trail |
| Institutional reviewer | `decision_summary.json` files | Whether evidence, uncertainty, rationale, and human authorization are visible |
| Research community | `claims.json`, `tasks.json`, and `eval_plan.json` across packs | How research claims become governed operational tasks |

## Repository Structure

```text
applied-ai-research-translator/
│
├── packs/                           # Decision packs, one per paper or task
│   ├── <pack_id>/
│   │   ├── agent_spec.json          # Agent specification, schema-validated
│   │   ├── claims.json              # Falsifiable claims extracted from source material
│   │   ├── tasks.json               # Locked task definitions
│   │   ├── eval_plan.json           # Evaluation criteria and metrics
│   │   ├── decision_summary.json    # Final human-authorized decision
│   │   └── sources/
│   │       └── paper_text.txt       # Source text used for translation
│
├── schemas/                         # JSON Schema contracts
│   ├── agent_spec.schema.json
│   ├── claims.schema.json
│   ├── decision_summary.schema.json
│   ├── run_input.schema.json
│   ├── run_output.schema.json
│   └── tasks.schema.json
│
├── runloop/                         # Governed executor
│   ├── README_RUNLOOP.md
│   ├── DECISIONS.md
│   ├── run_t_c02.py
│   ├── make_decision_summary.py
│   ├── make_decisions_index.py
│   └── src/
│       ├── human_gate.py
│       ├── openai_runner.py
│       ├── schemas.py
│       └── logger.py
│
├── docs/
│   ├── research-context.md
│   └── demo-runs/
│       └── LOCKED_3_DEMO_RUNS.md
│
├── scripts/                         # Validation tooling
├── src/                             # Shared execution logic
├── examples/runs/                   # Example run inputs
├── requirements.txt
└── .env.example
```

## Quick Start

Clone the repository.

```bash
git clone https://github.com/mj3b/applied-ai-research-translator.git
cd applied-ai-research-translator
```

Install dependencies.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r runloop/requirements.txt
```

Validate an example pack.

```bash
bash scripts/validate_pack.sh packs/haic_reliance_review_59e257ff
```

Run a governed example.

```bash
cd runloop
python run_t_c02.py
python make_decision_summary.py
```

Review the generated artifacts under the run logs, then inspect the decision summary.

## Status

v1.1 expands the research-community framing and release metadata for archival use.

| Version | Status | Main Purpose |
|---|---|---|
| v1.0 | Decision-complete reference implementation | Established core translation method, schemas, example packs, governed runloop, and human gate |
| v1.1 | Research-grade archival release | Strengthens research rationale, governance framing, citation metadata, and institutional README structure |

## Citation

```bibtex
@software{banasihan2026airt,
  author    = {Banasihan, Mark Julius},
  title     = {Applied {AI} Research Translator: A Governed Research-to-Decision Translation System},
  year      = {2026},
  version   = {1.1},
  url       = {https://github.com/mj3b/applied-ai-research-translator},
  license   = {Apache-2.0}
}
```

## Suggested Citation Description

Applied AI Research Translator is an open-source software artifact for converting applied AI research into governed, audit-ready decision records. The system addresses the research-to-deployment gap between academic findings and operational adoption by translating papers, PDFs, online publications, and related research artifacts into falsifiable claims, bounded tasks, schema-validated execution outputs, abstention conditions, human-gate review, and deterministic decision summaries. Version 1.1 strengthens the research-community framing by treating research translation as a governance control point: AI-generated outputs remain intermediate evidence artifacts while final authorization, override, rejection, and deployment conditions remain assigned to a human decision record. The repository includes schemas, runloop code, example research packs, demo decision summaries, validation scripts, and documentation for translation-positive and translation-negative cases. It is intended for researchers, governance practitioners, institutional reviewers, and applied AI teams studying auditability, decision accountability, human oversight, and controlled research translation in AI-assisted systems. Licensed under Apache 2.0.

## Author

Mark Julius Banasihan  
AI Governance Specialist | Researcher in AI Safety & Policy  
ORCID: https://orcid.org/0009-0001-8121-2878  
GitHub: https://github.com/mj3b  
LinkedIn: https://linkedin.com/in/markjuliusbanasihan

## License

Apache 2.0

