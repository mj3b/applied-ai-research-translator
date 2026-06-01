# Applied AI Research Translator

[![DOI](https://zenodo.org/badge/1121938011.svg)](https://doi.org/10.5281/zenodo.20478120)
[![Release: v1.1.1](https://img.shields.io/badge/release-v1.1.1-0aa2c0)](https://github.com/mj3b/applied-ai-research-translator/releases/tag/v1.1.1)
[![Status: Research-Grade Archival Release](https://img.shields.io/badge/status-research--grade%20archival%20release-5b6cff)](#status)
[![AI Stance: Non-Agentic](https://img.shields.io/badge/AI-non--agentic-2d7ff9)](#where-ai-assistance-enters)
[![Governance: Human-in-the-Loop](https://img.shields.io/badge/governance-human--in--the--loop-3bb273)](#human-gate)
[![Schema: Enforced](https://img.shields.io/badge/contracts-schema--validated-8a5cff)](#schema-and-validation-layer)
[![Property: Audit-Ready](https://img.shields.io/badge/property-audit--ready-0aa2c0)](#decision-summary)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--8121--2878-brightgreen)](https://orcid.org/0009-0001-8121-2878)

Applied AI research rarely arrives as something an institution can safely act on. It arrives as papers, preprints, PDFs, benchmark claims, technical reports, vendor publications, standards guidance, online commentary, and source repositories. Those sources may be useful. They still require a separate record before they influence deployment, evaluation, procurement, policy, or oversight decisions.

**Applied AI Research Translator** is an open-source research software artifact for converting applied AI research into governed, audit-ready decision records. It decomposes research sources into safety-policy intake classifications, falsifiable claims, bounded tasks, evaluation plans, schema-validated artifacts, abstention conditions, human-gated decisions, and deterministic decision summaries.

The central claim is simple:

```text
Research usefulness is not operational authorization.
```

This repository makes that distinction inspectable.

---

## Contents

- [The Problem](#the-problem)
- [What This Repository Provides](#what-this-repository-provides)
- [How the Translator Works](#how-the-translator-works)
- [Where AI Assistance Enters](#where-ai-assistance-enters)
- [Why the Safety-Policy Intake Gate Matters](#why-the-safety-policy-intake-gate-matters)
- [Quick Start](#quick-start)
- [Worked Example](#worked-example)
- [Core Artifacts](#core-artifacts)
- [Governance Model](#governance-model)
- [Schema and Validation Layer](#schema-and-validation-layer)
- [Example Packs](#example-packs)
- [Repository Structure](#repository-structure)
- [Reading Guide](#reading-guide)
- [Status](#status)
- [Citation](#citation)
- [Author](#author)
- [License](#license)

---

## The Problem

A research source can be persuasive without being decision-ready.

A paper may show a result under bounded laboratory conditions. A benchmark may report performance without capturing deployment behavior. A policy memo may identify a governance concern without defining evidence fields. A GitHub repository may implement a technique without showing license fitness, dependency safety, or institutional accountability. A vendor report may describe a capability while leaving out conditions where it fails.

The failure mode is quiet. A team reads something useful and turns it into action. The governance decision has already happened, even though no one recorded what claim was extracted, what assumptions were carried forward, what task was authorized, what evidence would count as success, who had review authority, or what would force abstention.

This repository treats that gap as the control point.

| Source enters as | Without translation | With governed translation |
|---|---|---|
| Paper, preprint, report, PDF, repository, benchmark, guidance | Informal justification for action | Source-controlled evidence |
| Research claim | Broad adoption argument | Falsifiable, scoped claim |
| Interesting method | Implementation pressure | Bounded task candidate |
| Model output | Apparent answer | Intermediate evidence |
| Human approval | Informal judgment | Recorded decision artifact |
| Rejection | Lost or undocumented | First-class governance outcome |

A governed translator should let a reviewer reconstruct how a source became a decision, and where that path stopped.

---

## What This Repository Provides

Applied AI Research Translator provides a reference implementation for **research-to-decision governance**.

It supplies:

| Layer | Repository mechanism | Why it matters |
|---|---|---|
| Source intake | `sources/paper_text.txt` and provenance controls | Preserves the material used for translation |
| Safety-policy triage | `safety_policy_intake.json` | Classifies risk domain, autonomy relevance, dual-use status, required review, and translation boundary |
| Claim extraction | `claims.json` | Prevents whole papers from becoming single adoption arguments |
| Task design | `tasks.json` | Converts selected claims into bounded work units with defined input, output, constraints, and failure conditions |
| Evaluation | `eval_plan.json` | Declares success, failure, and abstention criteria before outputs are judged |
| Schema enforcement | `schemas/` and `scripts/` | Turns governance expectations into machine-checkable contracts |
| Governed execution | `runloop/` | Uses AI assistance only inside a bounded artifact-producing workflow |
| Human gate | `human_gate.py` and `human_gate.json` | Records accept, override, reject, and review authority |
| Decision summary | `decision_summary.json` | Produces the audit-facing record of what was decided and why |
| Negative translation | `multi_agent_failure_modes_e0228882/` | Shows that stopping a translation path can be the correct governance result |

The contribution is methodological and infrastructural. It defines the intermediate artifacts required before a research source can influence an institutional decision.

---

## How the Translator Works

At a high level, the translator asks seven questions.

| Step | Question | Artifact |
|---:|---|---|
| 1 | What source is being used? | `sources/paper_text.txt` |
| 2 | What safety or policy risk does the source touch? | `safety_policy_intake.json` |
| 3 | What claims does the source actually support? | `claims.json` |
| 4 | Which claims can become bounded tasks? | `tasks.json` |
| 5 | What evidence would count as success or failure? | `eval_plan.json` |
| 6 | What did the governed run or reviewer produce? | run artifacts |
| 7 | Who accepted, overrode, rejected, or constrained the result? | `human_gate.json`, `decision_summary.json` |

The artifact chain is deliberately conservative:

```text
Research source
  ↓
Safety-policy intake
  ↓
Claim extraction
  ↓
Translation verdict
  ↓
Locked task definition
  ↓
Evaluation plan
  ↓
Governed AI-assisted run or manual review
  ↓
Human gate
  ↓
Decision summary
```

The translator separates three things that are often collapsed:

| Concept | Meaning |
|---|---|
| Research usefulness | The source contains insight worth examining |
| Translation readiness | The source supports scoped claims, bounded tasks, and reviewable evidence |
| Operational authorization | A human decision record permits action under stated conditions |

A source can pass the first test and fail the second. That failure is evidence that governance is working.

---

## Where AI Assistance Enters

AI assistance enters only after the task boundary has been defined.

The AI component may help produce candidate artifacts, such as extracted claims, structured outputs, classifications, summaries, or run outputs. It has no authority to revise the task boundary, approve evidence sufficiency, authorize deployment, or write the final decision narrative.

| Workflow stage | AI may assist with | Authority remains with |
|---|---|---|
| Source review | Candidate extraction, quote location, structure support | Researcher or reviewer |
| Claim extraction | Drafting claim candidates under schema | Claim reviewer |
| Task execution | Producing bounded candidate output | Locked task specification and human gate |
| Evaluation support | Generating evidence candidates | Evaluation plan and reviewer |
| Human gate | Supplying material for review | Human reviewer |
| Decision summary | Providing structured fields already logged in artifacts | Deterministic assembler and human-authorized record |
| Deployment | No direct action | Institution outside this repository |

The system uses AI as an evidence-producing instrument. It does not use AI as the decision authority.

That design choice is the governance boundary.

---

## Why the Safety-Policy Intake Gate Matters

AI safety and policy sources need a stronger first gate than ordinary research sources.

A source may concern capability forecasting, misuse, loss of control, compute governance, model-weight security, liability, international governance, concentration of power, or structural risk. Those topics require different reviewers and different translation boundaries. Treating them as ordinary research input would allow a safety-relevant source to become a task before the repository has classified what kind of authority the source should carry.

The new intake artifact solves that problem:

```text
packs/<pack_id>/
└── safety_policy_intake.json
```

It records:

| Field group | What it answers |
|---|---|
| `source_status` | What kind of evidence is this source? |
| `ai_safety_domain` | Which safety or policy domains does it touch? |
| `capability_and_autonomy` | Does the source concern frontier capability, open-ended agency, tools, or task horizon? |
| `risk_screen` | Does it raise misuse, dual-use, loss-of-control, oversight, or catastrophic-risk concerns? |
| `governance_mapping` | Who must review it and what decision lever does it affect? |
| `translation_verdict` | May it proceed, proceed with constraints, remain evaluation-only, remain policy-mapping-only, require human review, be restricted, be rejected, or abstain? |

Minimum rule:

```text
A pack is not translation-ready for AI safety or policy work until safety_policy_intake.json validates.
```

This makes the translator more serious. It asks whether a source should become a claim, an evaluation, a policy mapping, a bounded task, a restricted artifact, or a rejection record.

---

## Quick Start

This quick start is designed for reviewers who want to inspect the governance path, not merely run code.

### 1. Clone the repository

```bash
git clone https://github.com/mj3b/applied-ai-research-translator.git
cd applied-ai-research-translator
```

### 2. Create a Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m pip install -r runloop/requirements.txt
python3 -m pip install jsonschema
```

### 4. Validate the safety-policy intake gate

```bash
chmod +x scripts/*.sh
./scripts/validate_safety_policy_intake.sh packs/multi_agent_failure_modes_e0228882/safety_policy_intake.json
```

Expected result:

```text
validated: packs/multi_agent_failure_modes_e0228882/safety_policy_intake.json
```

### 5. Validate an example pack

```bash
./scripts/validate_pack.sh packs/haic_reliance_review_59e257ff
./scripts/validate_claims.sh packs/haic_reliance_review_59e257ff
./scripts/validate_tasks.sh packs/haic_reliance_review_59e257ff
./scripts/validate_decision_summary.sh packs/haic_reliance_review_59e257ff/decision_summary.json
```

### 6. Run a governed example

```bash
cd runloop
python3 run_t_c02.py
python3 make_decision_summary.py
```

Then inspect the generated run artifacts and decision summary. The goal is to see the artifact chain, not just the output.

### 7. Read the negative translation example

```text
packs/multi_agent_failure_modes_e0228882/
```

This is the most important pack for AI safety and policy reviewers. It shows how the repository preserves a rejection path when source material exceeds the bounded decision-support model.

---

## Worked Example

The `multi_agent_failure_modes_e0228882` pack demonstrates the safety-policy intake gate.

```text
packs/multi_agent_failure_modes_e0228882/
├── safety_policy_intake.json
├── agent_spec.json
├── claims.json
├── tasks.json
├── eval_plan.json
├── decision_summary.json
└── sources/
    └── paper_text.txt
```

The pack concerns autonomous multi-agent failure modes. The intake file classifies the source as relevant to loss-of-control and structural risk. It assigns a policy-mapping boundary and requires researcher, AI safety, and governance review before any narrower task translation proceeds.

The important point is the verdict. The translator preserves research value without turning the source into an autonomous execution path.

That is the intended behavior.

---

## Core Artifacts

| Artifact | Function | Governance role |
|---|---|---|
| `sources/paper_text.txt` | Captures source material used for translation | Preserves provenance and auditability |
| `safety_policy_intake.json` | Classifies AI safety and policy relevance | Sets review authority and translation boundary before claims become tasks |
| `claims.json` | Records extracted claims and source-linked evidence | Prevents unsupported generalization from the source |
| `tasks.json` | Converts selected claims into bounded operational tasks | Defines execution boundary before AI assistance |
| `eval_plan.json` | Specifies evaluation criteria, metrics, and failure states | Links research claims to measurable evidence |
| `run_input.json` | Captures specific execution inputs | Makes the run reproducible |
| `candidates.jsonl` | Records raw model outputs | Preserves candidate evidence |
| `proposed.json` | Stores schema-validated proposed output | Separates model output from final artifact |
| `human_gate.json` | Records human accept, override, reject, or escalation | Assigns authority |
| `final.json` | Stores the human-authorized output | Preserves the authorized artifact |
| `decision_summary.json` | Assembles evidence, uncertainty, rationale, and authorization | Serves as the primary audit artifact |

---

## Governance Model

Governance in this repository is implemented as architecture.

| Governance property | Implementation mechanism | Evidence artifact |
|---|---|---|
| Provenance | Source text is captured inside each pack | `sources/paper_text.txt` |
| Safety-policy classification | Risk domain and translation boundary are recorded before claims become tasks | `safety_policy_intake.json` |
| Claim discipline | Claims are typed, scoped, and source-linked | `claims.json`, `claims.schema.json` |
| Task containment | Inputs, outputs, constraints, and failure conditions are defined before execution | `tasks.json`, `tasks.schema.json` |
| Evaluation discipline | Acceptance, failure, and abstention criteria are declared before review | `eval_plan.json` |
| Schema control | Artifacts validate against JSON schemas | `schemas/`, `scripts/` |
| Abstention | Failures can halt translation or route to human review | `abstention-model.md`, run artifacts |
| Human authority | Proposed outputs require accept, override, reject, or escalation | `human_gate.json` |
| Audit reconstruction | The chain from source to decision can be inspected | `TRACEABILITY.md`, decision summaries |
| Rejection parity | Negative translation produces a decision record | `multi_agent_failure_modes_e0228882/decision_summary.json` |

This aligns with a broader governance pattern: Govern and Map should occur before Measure and Manage. NIST AI RMF describes Govern, Map, Measure, and Manage as the four Core functions, with governance infused through the other functions. The safety-policy intake gate is closest to Govern and Map because it classifies source context, risk domain, review authority, and translation boundary before evaluation or action.

---

## Translation Verdicts

Every mature pack should resolve to a translation verdict.

| Verdict | Meaning | Typical use |
|---|---|---|
| `translation_positive` | The source supports at least one bounded task under governance controls | Controlled task design |
| `proceed_to_task_design` | The source appears suitable for task design with further specification work | Early translation-positive pack |
| `approve_with_conditions` | The task may proceed under recorded constraints | Human-gated run output |
| `evaluation_only` | The source should inform evaluation design without becoming an operational task | Benchmarks, measurement papers, safety eval methods |
| `policy_mapping_only` | The source should inform governance or policy mapping without execution | Legal, policy, structural risk, or multi-agent autonomy sources |
| `restricted` | The source raises dual-use, security, or governance concerns | Misuse, model-weight security, hazardous capability discussion |
| `human_review_required` | The source requires expert review before translation proceeds | Frontier, safety, legal, or high-impact sources |
| `translation_negative` | The source is analytically useful but fails bounded task translation | Boundary cases |
| `reject_translation` | Operationalization should stop under the repository boundary | Unsafe or unbounded translation |
| `abstain` | Evidence is insufficient to classify or translate | Unclear provenance, weak evidence, missing source text |

A governance system that always converts research into implementation is an adoption accelerator. This repository treats rejection and abstention as legitimate outputs.

---

## Schema and Validation Layer

Schemas define the artifact contracts. Scripts enforce them.

```text
schemas/
├── safety_policy_intake.schema.json
├── agent_spec.schema.json
├── claims.schema.json
├── tasks.schema.json
├── run_input.schema.json
├── run_output.schema.json
└── decision_summary.schema.json
```

```text
scripts/
├── validate_safety_policy_intake.sh
├── validate_pack.sh
├── validate_claims.sh
├── validate_tasks.sh
├── validate_run_input.sh
├── validate_run_output.sh
└── validate_decision_summary.sh
```

Validation does not prove truth. It proves that the artifact has the minimum structure required for review.

Run the first-gate validator:

```bash
./scripts/validate_safety_policy_intake.sh packs/multi_agent_failure_modes_e0228882/safety_policy_intake.json
```

Run the pack validators:

```bash
./scripts/validate_claims.sh packs/haic_reliance_review_59e257ff
./scripts/validate_tasks.sh packs/haic_reliance_review_59e257ff
./scripts/validate_decision_summary.sh packs/haic_reliance_review_59e257ff/decision_summary.json
```

---

## Example Packs

| Pack | Source domain | Intake or verdict | Governance finding |
|---|---|---|---|
| `haic_reliance_review_59e257ff` | Human-AI collaboration and reliance calibration | Translation-positive | Reliance calibration can be bounded through accept and override instrumentation |
| `measuring_agents_in_production_a98e2ca8` | Production measurement of AI agents | Translation-positive candidate | Monitoring and workflow-level evaluation can be represented through bounded evidence artifacts |
| `multi_agent_failure_modes_e0228882` | Multi-agent LLM failure modes | Safety-policy intake, policy-mapping boundary, human review required | Autonomous multi-agent coordination expands the accountability and audit surface beyond this repository’s bounded model |
| `example_paper_001` | Minimal demonstration pack | Development scaffold | Used for structure and schema demonstration |
| `test_paper_agent_translation_d0702c41` | Translation workflow testing | Development scaffold | Used for test workflow validation |

The multi-agent rejection is the clearest governance example. It shows that the system can use research to stop a deployment path.

---

## Repository Structure

```text
applied-ai-research-translator/
│
├── README.md                                   ← Project overview, research-to-decision model, quick start, citation, and repository map
├── RESEARCH-RATIONALE.md                       ← Why papers, PDFs, reports, repositories, and online research require governance before operational use
├── REFERENCES.md                               ← Curated bibliography for AI governance, AI safety, research integrity, software citation, standards, laws, and repository-specific sources
├── TRANSLATION-METHOD.md                       ← How research sources become claims, tasks, verdicts, and decision records
├── GOVERNANCE-MODEL.md                         ← Governance boundary: provenance, schema control, abstention, human gate, and audit trail
├── TRACEABILITY.md                             ← Source material → safety-policy intake → claims → tasks → run artifacts → decision summary
├── LIMITATIONS.md                              ← Known limits, excluded use cases, unresolved questions, and disclosure language
├── CHANGELOG.md                                ← Version history, release notes, and archival release rationale
├── CITATION.cff                                ← Machine-readable citation metadata for GitHub, ORCID, and Zenodo
├── CONTRIBUTING.md                             ← How researchers and practitioners can adapt packs, schemas, and runloop logic
├── LICENSE                                     ← Apache License 2.0
├── NOTICE                                      ← Attribution, reuse, and derivative-use notice
├── requirements.txt                            ← Root Python dependencies
├── .env.example                                ← Environment variable template for local execution
├── .gitleaks.toml                              ← Secret-scanning configuration
│
├── .github/                                    ← GitHub automation and repository workflow configuration
│   └── workflows/
│       └── validate-artifacts.yml              ← CI workflow for validating governed artifacts on push and pull request
│
├── packs/                                      ← Governed research translation packs, one source or task family per pack
│   ├── README.md                               ← Pack model, maturity levels, verdict logic, required files, and reviewer instructions
│   │
│   ├── _template_safety_policy_intake/         ← Reusable template for AI safety and policy source classification
│   │   └── safety_policy_intake.json           ← Draft intake artifact for source status, risk domain, review authority, and translation boundary
│   │
│   ├── haic_reliance_review_59e257ff/          ← Translation-positive pack: human-AI reliance calibration
│   │   ├── agent_spec.json                     ← Agent or task specification with bounded role and constraints
│   │   ├── claims.json                         ← Falsifiable claims extracted from source material
│   │   ├── tasks.json                          ← Locked tasks derived from selected claims
│   │   ├── eval_plan.json                      ← Evaluation criteria, metrics, and review conditions
│   │   ├── decision_summary.json               ← Final human-authorized translation decision
│   │   └── sources/
│   │       └── paper_text.txt                  ← Captured source text used for claim extraction and audit reconstruction
│   │
│   ├── measuring_agents_in_production_a98e2ca8/ ← Translation-positive candidate: production measurement for AI agents
│   │   ├── agent_spec.json                     ← Agent or task specification
│   │   ├── claims.json                         ← Extracted claims with source-grounded evidence
│   │   ├── tasks.json                          ← Bounded operational tasks
│   │   ├── eval_plan.json                      ← Measurement and evaluation plan
│   │   └── sources/
│   │       └── paper_text.txt                  ← Source text preserved for audit reconstruction
│   │
│   ├── multi_agent_failure_modes_e0228882/     ← Translation-negative pack: autonomous multi-agent failure modes
│   │   ├── safety_policy_intake.json           ← AI safety and policy intake gate for loss-of-control and structural-risk classification
│   │   ├── agent_spec.json                     ← Specification showing the governance boundary problem
│   │   ├── claims.json                         ← Extracted claims and failure-mode evidence
│   │   ├── tasks.json                          ← Proposed task boundary and rejection basis
│   │   ├── eval_plan.json                      ← Evaluation criteria used to test translation feasibility
│   │   ├── decision_summary.json               ← Human-authorized rejection decision
│   │   └── sources/
│   │       └── paper_text.txt                  ← Source text preserved for review
│   │
│   ├── example_paper_001/                      ← Minimal demonstration pack
│   │   └── agent_spec.json                     ← Schema-validated agent or task specification
│   │
│   └── test_paper_agent_translation_d0702c41/  ← Development test pack for translation workflow validation
│       ├── agent_spec.json                     ← Test specification
│       └── eval_plan.json                      ← Test evaluation plan
│
├── schemas/                                    ← JSON Schema contracts for governed translation artifacts
│   ├── README.md                               ← Contract index, validation rules, artifact order, and schema dependency map
│   ├── safety_policy_intake.schema.json        ← Required structure for AI safety and policy source intake
│   ├── agent_spec.schema.json                  ← Required structure for agent or task specifications
│   ├── claims.schema.json                      ← Required structure for extracted, falsifiable research claims
│   ├── tasks.schema.json                       ← Required structure for bounded task definitions
│   ├── run_input.schema.json                   ← Required structure for governed run inputs
│   ├── run_output.schema.json                  ← Required structure for governed run outputs
│   └── decision_summary.schema.json            ← Required structure for final decision artifacts
│
├── runloop/                                    ← Governed execution layer for bounded AI-assisted tasks
│   ├── README_RUNLOOP.md                       ← Execution model, run order, artifact trail, and human gate logic
│   ├── DECISIONS.md                            ← Runloop design decisions and governance trade-offs
│   ├── requirements.txt                        ← Runtime-specific dependencies
│   ├── run_t_c02.py                            ← Reference governed run for task t_c02
│   ├── make_decision_summary.py                ← Deterministic decision-summary assembler
│   ├── make_decision_summary_t_c04.py          ← Deterministic summary assembler for task t_c04
│   ├── make_decisions_index.py                 ← Decision index generator for completed runs
│   │
│   ├── examples/                               ← Runtime examples used by governed runs
│   │   ├── artifact.txt                        ← Example input artifact
│   │   ├── artifact_t_c04.txt                  ← Example input artifact for discrepancy review
│   │   ├── taxonomy.json                       ← Example taxonomy
│   │   └── taxonomy_t_c04.json                 ← Example taxonomy for t_c04
│   │
│   └── src/                                    ← Runtime support modules
│       ├── __init__.py                         ← Package initialization
│       ├── human_gate.py                       ← Human accept, override, reject, and escalation control point
│       ├── openai_runner.py                    ← Bounded model-call runner
│       ├── schemas.py                          ← Runtime schema loading and validation
│       └── logger.py                           ← Artifact logging and run trace support
│
├── src/                                        ← Shared translation and task execution logic
│   ├── runner/
│   │   └── run_task.py                         ← Generic task runner for schema-bound execution
│   │
│   └── translator/
│       ├── __init__.py                         ← Translator package initialization
│       ├── cli.py                              ← Command-line interface for research translation workflow
│       └── quote_finder.py                     ← Source quote and evidence extraction support
│
├── scripts/                                    ← Validation, security, and reproducibility tooling
│   ├── README.md                               ← Script index, validation order, failure interpretation, and release checks
│   ├── validate_safety_policy_intake.sh        ← Safety-policy intake validator for AI safety and policy source classification
│   ├── validate_pack.sh                        ← Pack-level validation wrapper
│   ├── validate_claims.sh                      ← Claim schema validation
│   ├── validate_tasks.sh                       ← Task schema validation
│   ├── validate_run_input.sh                   ← Run-input schema validation
│   ├── validate_run_output.sh                  ← Run-output schema validation
│   ├── validate_decision_summary.sh            ← Decision-summary schema validation
│   ├── run_examples.sh                         ← Reproducible example-run script
│   └── install-pre-commit-gitleaks.sh          ← Local secret-scanning hook installation
│
├── docs/                                       ← Research context, demonstrations, specifications, governance notes, and release materials
│   ├── research-context.md                     ← Research background and institutional problem statement
│   │
│   ├── demo-runs/                              ← Locked demonstration runs and audit artifacts
│   │   ├── LOCKED_3_DEMO_RUNS.md               ← Three locked demo runs with review notes
│   │   ├── A/
│   │   │   ├── run-manifest.json               ← Run A manifest
│   │   │   └── decision_summary.json           ← Run A decision artifact
│   │   ├── B/
│   │   │   ├── run-manifest.json               ← Run B manifest
│   │   │   └── decision_summary.json           ← Run B decision artifact
│   │   └── C/
│   │       ├── run-manifest.json               ← Run C manifest
│   │       └── decision_summary.json           ← Run C decision artifact
│   │
│   ├── specifications/                         ← Technical and governance specifications
│   │   ├── artifact-model.md                   ← Required artifacts from source text through decision summary
│   │   ├── translation-verdicts.md             ← Positive, negative, conditional, restricted, and rejection verdict definitions
│   │   ├── abstention-model.md                 ← When the system halts, rejects, restricts, or requires human review
│   │   ├── human-gate.md                       ← Human authorization, override, rejection, and accountability record
│   │   └── audit-reconstruction.md             ← How a reviewer reconstructs a completed decision path
│   │
│   ├── governance/                             ← Institutional governance documentation
│   │   ├── README.md                           ← Governance documentation map and recommended review order
│   │   ├── research-provenance.md              ← Source capture, source volatility, and versioning controls
│   │   ├── safety-policy-intake.md             ← AI safety and policy intake gate for risk-domain and translation-boundary classification
│   │   ├── online-research-controls.md         ← Controls for web pages, PDFs, reports, repositories, and preprints
│   │   ├── security-considerations.md          ← Secrets, prompt injection, source poisoning, dependency, and logging risks
│   │   ├── institutional-review-template.md    ← Template for research, governance, or audit reviewers
│   │   ├── nist-ai-rmf-mapping.md              ← Mapping to NIST AI RMF functions and governance outcomes
│   │   ├── eu-ai-act-mapping.md                ← Mapping to high-risk system obligations and oversight logic
│   │   └── iso-42001-mapping.md                ← Mapping to AI management system controls
│   │
│   └── release/                                ← Release-level documentation and archival review materials
│       ├── README.md                           ← Release documentation map
│       ├── v1.0-release-notes.md               ← Initial decision-complete implementation
│       ├── v1.1-release-notes.md               ← Research-grade archival and metadata release
│       ├── v1.1-release-checklist.md           ← Pre-release checklist for archival and citation readiness
│       ├── v1.1-archival-statement.md          ← Scholarly archival statement for GitHub, Zenodo, and ORCID
│       └── v1.1-reviewer-brief.md              ← Concise reviewer guide for v1.1 inspection
│
├── examples/                                   ← Example governed run inputs and reproducibility material
│   └── runs/
│       ├── t_c02_input_with_snippets.json      ← Example run input with source snippets
│       └── t_c04_input.json                    ← Example discrepancy-review run input
│
└── assets/                                     ← Visual diagrams and publication assets
    ├── research-to-decision-pipeline.svg       ← Visual overview of governed research-to-decision translation
    ├── governance-boundary.svg                 ← Non-agentic boundary: AI evidence generation vs. human authority
    ├── artifact-traceability-map.svg           ← Source → intake → claim → task → run → decision summary
    └── human-gate-decision-record.svg          ← Human accept, override, reject, and abstain control model
```

---

## Reading Guide

| Reader | Start here | What to inspect |
|---|---|---|
| Principal investigator | `README.md`, then `RESEARCH-RATIONALE.md` | Research contribution, artifact chain, and scholarly boundaries |
| AI safety researcher | `packs/multi_agent_failure_modes_e0228882/`, then `docs/governance/safety-policy-intake.md` | Autonomy boundary, loss-of-control routing, and rejection logic |
| AI policy researcher | `docs/governance/`, then `TRANSLATION-METHOD.md` | How policy and governance sources become reviewable artifacts |
| Technical implementer | `runloop/README_RUNLOOP.md`, then `runloop/src/` | Execution path, schema validation, artifact logging, and human gate |
| Auditor | `TRACEABILITY.md`, then decision summaries | Source-to-decision reconstruction |
| Contributor | `CONTRIBUTING.md`, `schemas/README.md`, `packs/README.md` | How to add packs, schemas, and governed artifacts |

---

## What This Repository Does Not Claim

This repository is research software. It supports governed research translation and decision-record construction. It does not provide legal advice, regulatory certification, production safety assurance, ISO/IEC 42001 certification, EU AI Act conformity, NIST AI RMF implementation, or empirical proof that a translated system is safe.

Its purpose is narrower and more useful:

```text
Make the path from research source to decision artifact visible enough to review, challenge, accept, reject, or improve.
```

---

## Status

| Version | Status | Main purpose |
|---|---|---|
| v1.0 | Decision-complete reference implementation | Established core translation method, schemas, example packs, governed runloop, and human gate |
| v1.1 | Research-grade archival release | Strengthened research rationale, governance framing, citation metadata, specifications, governance docs, release docs, and institutional README structure |
| v1.1.1 | Safety-policy intake enhancement | Adds first-gate classification for AI safety and policy sources before claim extraction and task translation |

---

## AI-Assisted Research Disclosure

This repository was developed with AI assistance as part of the author’s research, drafting, documentation, and software-construction workflow. AI tools, including Claude and ChatGPT, were used to support methodology refinement, document drafting, schema and artifact design, repository organization, validation-script development, diagram planning, and review of governance language.

All AI-assisted outputs were treated as draft or candidate material. They did not determine the repository’s research claims, governance model, translation method, safety-policy intake design, schema boundaries, pack verdicts, citation metadata, release decisions, or final public language. Those decisions were selected, revised, accepted, rejected, or integrated by the author.

The author assumes sole responsibility for the repository’s contents, including the research framing, artifact architecture, source selection, safety-policy classification logic, human-gate model, translation verdict structure, limitations, citations, and release metadata.

This disclosure is consistent with the repository’s central governance position: AI systems may assist in producing intermediate artifacts, but they do not hold authorship, accountability, or final decision authority.

---

## Citation

```bibtex
@software{banasihan2026airt,
  author    = {Banasihan, Mark Julius},
  title     = {Applied {AI} Research Translator: A Governed Research-to-Decision Translation System},
  year      = {2026},
  version   = {1.1.1},
  doi       = {10.5281/zenodo.20478121},
  url       = {https://github.com/mj3b/applied-ai-research-translator},
  license   = {Apache-2.0}
}
```

---

## Author

Mark Julius Banasihan  
AI Governance Specialist | Researcher in AI Safety & Policy  
ORCID: <https://orcid.org/0009-0001-8121-2878>  
GitHub: <https://github.com/mj3b>  
LinkedIn: <https://linkedin.com/in/markjuliusbanasihan>

---

## License

Apache 2.0. See [`LICENSE`](LICENSE).

