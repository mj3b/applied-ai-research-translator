# Research Translation Packs

The `packs/` directory contains the governed research translation units for this repository. Each pack takes one research source, research question, or bounded task family and turns it into inspectable artifacts: source text, falsifiable claims, task definitions, evaluation criteria, translation verdicts, and decision summaries.

A pack is not a folder of examples. It is the repository’s core governance object.

---

## What a Pack Does

A research pack records the path from source material to institutional decision. It makes each translation step reviewable before the system moves from research interpretation into operational use.

```text
source material
  ↓
claims
  ↓
tasks
  ↓
evaluation plan
  ↓
governed run or manual review
  ↓
human gate
  ↓
decision summary
```

The purpose is to prevent a paper, PDF, online publication, or repository from being treated as deployment justification without a record of what was actually extracted, bounded, tested, rejected, or approved.

---

## Pack Inventory

| Pack | Status | Source Domain | Main Governance Question | Current Verdict |
|---|---:|---|---|---|
| `example_paper_001` | Minimal scaffold | Demonstration source | What is the smallest valid agent specification? | Development example |
| `haic_reliance_review_59e257ff` | Research translation pack | Human-AI collaboration and reliance calibration | Can reliance behavior be measured in a bounded decision-support workflow? | `proceed_to_task_design` |
| `measuring_agents_in_production_a98e2ca8` | Research translation pack | Production measurement of AI agents | Can agent evaluation be translated into bounded monitoring and evidence artifacts? | Translation-positive candidate |
| `multi_agent_failure_modes_e0228882` | Negative translation pack | Multi-agent LLM failure modes | Can multi-agent autonomy be converted into a bounded decision-support task without expanding the accountability surface? | `reject_translation` |
| `test_paper_agent_translation_d0702c41` | Development test pack | Agent translation workflow testing | Does the pack structure support schema and evaluation workflow testing? | Development example |

The negative translation pack is part of the research contribution. It demonstrates that the translator can stop operationalization when the research source requires autonomy, creates diffuse accountability, or exceeds the repository’s governance boundary.

---

## Required Pack Structure

A mature research translation pack should use this structure:

```text
packs/<pack_id>/
├── agent_spec.json
├── claims.json
├── tasks.json
├── eval_plan.json
├── decision_summary.json
└── sources/
    └── paper_text.txt
```

| Artifact | Purpose | Governance Function |
|---|---|---|
| `sources/paper_text.txt` | Captures the source text, excerpt, or source-derived material used for translation | Preserves provenance and supports later reconstruction |
| `agent_spec.json` | Defines the bounded role, system behavior, or translation unit | Prevents open-ended model authority from entering the pack |
| `claims.json` | Extracts falsifiable claims from the source material | Separates research evidence from interpretation and operational use |
| `tasks.json` | Converts selected claims into bounded tasks | Locks task boundaries before execution or review |
| `eval_plan.json` | Defines metrics, review questions, acceptance criteria, and failure conditions | Makes evidence requirements explicit before the output is judged |
| `decision_summary.json` | Records the final verdict, rationale, confidence, uncertainty, and human decision | Provides the audit-ready decision artifact |

Development packs may omit some artifacts while the workflow is being tested. Archival packs should include the full artifact set.

---

## Pack Maturity Levels

Not every pack has the same evidentiary status. The maturity level should be clear to readers and reviewers.

| Level | Name | Required Evidence | Appropriate Use |
|---:|---|---|---|
| 0 | Scaffold | `agent_spec.json` or partial structure only | Development and schema testing |
| 1 | Source-captured | Source material is preserved in `sources/` | Early claim extraction |
| 2 | Claim-complete | `claims.json` validates and claims are source-linked | Research review |
| 3 | Task-bound | `tasks.json` defines bounded operational tasks | Translation feasibility review |
| 4 | Evaluation-ready | `eval_plan.json` defines metrics, acceptance, and failure logic | Controlled run preparation |
| 5 | Decision-complete | `decision_summary.json` records verdict and rationale | Archival release, audit review, ORCID or Zenodo citation support |

A pack should not be described as decision-complete unless the final verdict can be reconstructed from its source, claims, tasks, evaluation plan, and decision summary.

---

## Translation Verdicts

The repository supports positive, conditional, and negative translation outcomes.

| Verdict | Meaning | Typical Evidence |
|---|---|---|
| `translation_positive` | The research source supports at least one bounded task under the repository’s governance controls | Claims, tasks, evaluation plan, and reviewable artifact trail |
| `proceed_to_task_design` | The source appears translatable, but task design or evaluation requires further refinement | Claims and initial decision summary |
| `approve_with_conditions` | The task may proceed only under specified constraints, review conditions, or human-gate requirements | Run artifacts, human-gate notes, and final summary |
| `translation_negative` | The source remains analytically useful, but cannot be converted into a bounded operational task under this system | Rejection rationale and boundary analysis |
| `reject_translation` | Operationalization should stop because the translation would exceed scope, accountability, evidence, safety, or audit limits | Decision summary with explicit rejection rationale |

A rejection verdict should be treated as a successful governance outcome when the evidence supports it.

---

## What Makes a Claim Translatable

A research claim can move toward task design only when it can be bounded without changing its meaning.

| Criterion | Reviewer Question | Pass Signal | Fail Signal |
|---|---|---|---|
| Source grounding | Does the claim trace to identifiable source material? | Source text or excerpt supports the claim | Claim is inferred from the paper’s general theme |
| Falsifiability | Can the claim be tested, contradicted, or measured? | Claim has observable conditions | Claim is aspirational, normative, or too broad |
| Scope control | Are the population, setting, workflow, or system limits clear? | Pack names where the claim applies | Claim generalizes beyond the source evidence |
| Task containment | Can the claim become a bounded task with defined inputs and outputs? | Task has fixed input, fixed output, and known review path | Task requires open-ended action or autonomous coordination |
| Evaluation fit | Can the task be evaluated with pre-declared criteria? | Metrics, acceptance conditions, and failure states exist | Output quality depends on unrecorded human judgment |
| Human authority | Can a human reviewer accept, override, or reject the output? | Human gate is meaningful and documented | Model output effectively becomes the decision |
| Audit reconstruction | Can a later reviewer reconstruct why the decision happened? | Source, claim, task, evaluation, and verdict are linked | Decision depends on missing context or informal judgment |

A source may pass as research and fail as translation. That distinction is central to the repository.

---

## Current Pack Notes

### `haic_reliance_review_59e257ff`

This pack translates human-AI collaboration research into reliance calibration artifacts. Its decision summary identifies the source as suitable for task design because reliance calibration maps to bounded decision-support review, override behavior, and auditability.

The core translation logic is that reliance can be observed through human interaction with AI recommendations. That makes the research source suitable for tasks that measure over-reliance, under-reliance, override quality, and audit completeness.

### `measuring_agents_in_production_a98e2ca8`

This pack examines production measurement for AI agents. It supports translation into bounded monitoring, evidence coverage, workflow measurement, and decision-summary artifacts.

The pack is useful because it treats production behavior as a measurement problem rather than an adoption claim. Its translation value depends on whether end-to-end agent behavior can be represented through bounded metrics and reviewable outputs without granting the agent operational authority.

### `multi_agent_failure_modes_e0228882`

This pack records a negative translation outcome. The source material concerns systemic failure modes in multi-agent LLM systems, including coordination and accountability concerns. The decision summary rejects translation because the primary contribution requires a degree of autonomous multi-agent interaction that exceeds this repository’s bounded decision-support model.

This is the strongest governance example in the directory. It shows that a research source can be useful for analysis while being unsuitable for operational translation under the repository’s current control boundary.

### `example_paper_001` and `test_paper_agent_translation_d0702c41`

These packs are development scaffolds. They support schema, translation, and evaluation workflow testing. They should not be treated as decision-complete research translations unless the missing artifacts are added.

---

## Pack Creation Workflow

Use this sequence when adding a new research pack.

| Step | Action | Output |
|---:|---|---|
| 1 | Identify the source and capture its usable text or excerpt | `sources/paper_text.txt` |
| 2 | Extract claims that are specific enough to test or reject | `claims.json` |
| 3 | Screen claims for translatability | Claim review notes or verdict |
| 4 | Convert selected claims into bounded tasks | `tasks.json` |
| 5 | Define evaluation questions, metrics, acceptance criteria, and failure states | `eval_plan.json` |
| 6 | Run the bounded workflow or conduct manual review | Run artifacts or reviewer notes |
| 7 | Record accept, override, reject, or stop decision | Human gate record, where applicable |
| 8 | Assemble final decision summary | `decision_summary.json` |

Do not skip from source text to task design. That jump hides the governance decision the repository is designed to expose.

---

## Naming Convention

Pack names should be descriptive, stable, and reviewable.

Recommended pattern:

```text
<source_or_topic_slug>_<short_hash>
```

Examples:

```text
haic_reliance_review_59e257ff
measuring_agents_in_production_a98e2ca8
multi_agent_failure_modes_e0228882
```

Use lowercase letters, numbers, and underscores. Avoid spaces, dates as the only identifier, and vague names such as `paper1` or `test_final`.

---

## Validation

Run validation before treating a pack as review-ready.

```bash
./scripts/validate_claims.sh packs/<pack_id>/claims.json
./scripts/validate_tasks.sh packs/<pack_id>/tasks.json
./scripts/validate_decision_summary.sh packs/<pack_id>/decision_summary.json
```

Where a pack lacks an artifact, state whether the omission is temporary, intentional, or evidence that the pack remains below decision-complete maturity.

---

## Review Checklist

A reviewer should be able to answer these questions from the pack itself:

- What source material was used?
- Which claims were extracted?
- Which claims were selected for task design?
- What assumptions constrain the translation?
- What task boundary was defined before execution?
- What evidence would count as success or failure?
- Where can the system abstain or reject?
- Who has authority to accept, override, or reject the output?
- What final verdict was recorded?
- What uncertainty remains?

A pack that cannot answer these questions should remain in development status.

---

## Anti-Overclaiming Rules

Do not use a pack to claim more than the artifacts support.

| Avoid Claiming | Use Instead |
|---|---|
| “The paper proves this workflow should be deployed.” | “The pack translates selected paper claims into bounded tasks for review.” |
| “The model is safe.” | “The run produced schema-valid output under the recorded task boundary.” |
| “The research supports automation.” | “The research supports a bounded decision-support task with human review.” |
| “The system validated the claim.” | “The system produced a decision record based on the available source, task, and evaluation artifacts.” |
| “The pack is complete.” | “The pack is decision-complete under the current schema and documented limitations.” |

The repository’s credibility depends on keeping the claim at the level of the evidence.

---

## Relationship to Root Documentation

| Root Document | How It Relates to Packs |
|---|---|
| `RESEARCH-RATIONALE.md` | Explains why research translation requires governance before operational use |
| `TRANSLATION-METHOD.md` | Defines the method used to move from source material to claims, tasks, and verdicts |
| `GOVERNANCE-MODEL.md` | Defines the authority boundary, human gate, abstention model, and audit logic |
| `TRACEABILITY.md` | Explains how a reviewer reconstructs the source-to-decision pathway |
| `LIMITATIONS.md` | Names the limits that constrain how packs should be interpreted |
| `CONTRIBUTING.md` | Defines how researchers and practitioners should add or modify packs |

Read this directory together with the root documents. The packs provide the concrete evidence trail; the root documents define the governance theory and method.

---

## Directory Structure

```text
packs/
├── README.md
├── example_paper_001/
│   └── agent_spec.json
├── haic_reliance_review_59e257ff/
│   ├── agent_spec.json
│   ├── claims.json
│   ├── tasks.json
│   ├── eval_plan.json
│   ├── decision_summary.json
│   └── sources/
│       └── paper_text.txt
├── measuring_agents_in_production_a98e2ca8/
│   ├── agent_spec.json
│   ├── claims.json
│   ├── tasks.json
│   ├── eval_plan.json
│   └── sources/
│       └── paper_text.txt
├── multi_agent_failure_modes_e0228882/
│   ├── agent_spec.json
│   ├── claims.json
│   ├── tasks.json
│   ├── eval_plan.json
│   ├── decision_summary.json
│   └── sources/
│       └── paper_text.txt
└── test_paper_agent_translation_d0702c41/
    ├── agent_spec.json
    └── eval_plan.json
```

---

## Status

The current directory contains both research translation packs and development scaffolds. For v1.1, the primary archival value is the presence of translation-positive and translation-negative examples that demonstrate how the repository separates research usefulness from operational authorization.

The governing standard is direct: a pack is successful when it makes the decision path reconstructable.
