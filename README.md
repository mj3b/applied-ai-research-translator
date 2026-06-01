# Applied AI Research Translator

[![DOI](https://zenodo.org/badge/1121938011.svg)](https://doi.org/10.5281/zenodo.20478120)
[![Release: v1.1](https://img.shields.io/badge/release-v1.1-0aa2c0)](https://github.com/mj3b/applied-ai-research-translator/releases/tag/v1.1)
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
├── README.md
├── RESEARCH-RATIONALE.md
├── TRANSLATION-METHOD.md
├── GOVERNANCE-MODEL.md
├── TRACEABILITY.md
├── LIMITATIONS.md
├── CHANGELOG.md
├── CITATION.cff
├── .zenodo.json
├── CONTRIBUTING.md
├── LICENSE
├── NOTICE
├── requirements.txt
├── .env.example
├── .gitleaks.toml
│
├── .github/
│   └── workflows/
│       └── validate-artifacts.yml
│
├── packs/
│   ├── README.md
│   ├── _template_safety_policy_intake/
│   │   └── safety_policy_intake.json
│   ├── haic_reliance_review_59e257ff/
│   ├── measuring_agents_in_production_a98e2ca8/
│   ├── multi_agent_failure_modes_e0228882/
│   │   ├── safety_policy_intake.json
│   │   ├── agent_spec.json
│   │   ├── claims.json
│   │   ├── tasks.json
│   │   ├── eval_plan.json
│   │   ├── decision_summary.json
│   │   └── sources/
│   │       └── paper_text.txt
│   ├── example_paper_001/
│   └── test_paper_agent_translation_d0702c41/
│
├── schemas/
│   ├── README.md
│   ├── safety_policy_intake.schema.json
│   ├── agent_spec.schema.json
│   ├── claims.schema.json
│   ├── tasks.schema.json
│   ├── run_input.schema.json
│   ├── run_output.schema.json
│   └── decision_summary.schema.json
│
├── runloop/
│   ├── README_RUNLOOP.md
│   ├── DECISIONS.md
│   ├── requirements.txt
│   ├── run_t_c02.py
│   ├── make_decision_summary.py
│   ├── make_decision_summary_t_c04.py
│   ├── make_decisions_index.py
│   ├── examples/
│   └── src/
│
├── src/
│   ├── runner/
│   └── translator/
│
├── scripts/
│   ├── README.md
│   ├── validate_safety_policy_intake.sh
│   ├── validate_pack.sh
│   ├── validate_claims.sh
│   ├── validate_tasks.sh
│   ├── validate_run_input.sh
│   ├── validate_run_output.sh
│   ├── validate_decision_summary.sh
│   ├── run_examples.sh
│   └── install-pre-commit-gitleaks.sh
│
├── docs/
│   ├── research-context.md
│   ├── demo-runs/
│   ├── specifications/
│   ├── governance/
│   │   ├── README.md
│   │   ├── research-provenance.md
│   │   ├── safety-policy-intake.md
│   │   ├── online-research-controls.md
│   │   ├── security-considerations.md
│   │   ├── institutional-review-template.md
│   │   ├── nist-ai-rmf-mapping.md
│   │   ├── eu-ai-act-mapping.md
│   │   └── iso-42001-mapping.md
│   └── release/
│
├── examples/
│   └── runs/
│
└── assets/
    ├── research-to-decision-pipeline.svg
    ├── governance-boundary.svg
    ├── artifact-traceability-map.svg
    └── human-gate-decision-record.svg
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
| v1.1.x | Safety-policy intake enhancement | Adds first-gate classification for AI safety and policy sources before claim extraction and task translation |

---

## Citation

```bibtex
@software{banasihan2026airt,
  author    = {Banasihan, Mark Julius},
  title     = {Applied {AI} Research Translator: A Governed Research-to-Decision Translation System},
  year      = {2026},
  version   = {1.1},
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

