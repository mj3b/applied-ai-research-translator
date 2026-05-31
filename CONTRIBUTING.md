# Contributing to Applied AI Research Translator

Applied AI Research Translator accepts contributions that strengthen the governed translation of applied AI research into decision-ready artifacts. The project is designed for researchers, governance practitioners, auditors, and applied AI teams who need a controlled method for moving from source material to bounded tasks, human review, and audit-ready decision summaries.

This repository is not an adoption accelerator. It is a research-to-decision governance system. Contributions should preserve that boundary.

---

## Contribution Standard

A contribution belongs in this repository when it improves one of five properties:

| Property | Contribution Question | Evidence Required |
|---|---|---|
| Provenance | Does the change make source material easier to identify, preserve, or reconstruct? | Source path, version, citation, timestamp, or captured source text |
| Claim discipline | Does the change make research claims more falsifiable, scoped, or testable? | Updated claim schema, example claim, or review note |
| Task containment | Does the change make task boundaries clearer before execution? | Task schema change, bounded example, or failure condition |
| Human authority | Does the change preserve human accept, override, or reject authority? | Human-gate artifact, review logic, or decision-summary field |
| Audit reconstruction | Does the change make the decision path easier to inspect after the fact? | Traceability link, run artifact, validation output, or decision record |

Changes that add capability while weakening these properties should not be merged.

---

## What This Project Is Trying to Protect

Research translation creates risk because source material is often treated as operational justification before it has been decomposed into claims, assumptions, scope boundaries, and failure conditions. A paper may support a bounded task. It does not authorize deployment by itself.

This repository protects the decision boundary between research interpretation and institutional action.

| Risk | How Contributions Should Address It |
|---|---|
| Research claim inflation | Keep claims narrow, falsifiable, and linked to source evidence |
| Source volatility | Preserve source text, version, citation, and retrieval context where possible |
| Benchmark overgeneralization | Record the conditions under which a finding applies |
| Model-output authority drift | Keep model outputs intermediate until human review completes |
| Post-hoc rationalization | Lock tasks and evaluation conditions before governed execution |
| Unreviewable adoption | Produce a decision summary that reconstructs the source-to-decision path |
| Unsafe operationalization | Preserve rejection and abstention as valid outcomes |

A useful contribution should make at least one of these risks easier to detect, constrain, or document.

---

## Contribution Types

| Contribution Type | Examples | Review Standard |
|---|---|---|
| Research pack | New paper, PDF, report, preprint, or repository translated into claims and tasks | Source is captured, claims are scoped, tasks are bounded, verdict is justified |
| Negative translation pack | Research source that should not become a bounded task under this system | Rejection rationale is explicit, evidence-linked, and reproducible |
| Schema improvement | New required field, stricter validation, clearer artifact contract | Change improves auditability without breaking existing packs unnecessarily |
| Runloop improvement | Better logging, validation, deterministic summary generation, or human-gate handling | Change preserves the authority boundary and artifact trail |
| Documentation | Clarifies method, governance model, traceability, or limitations | Text distinguishes observation, inference, and unresolved questions |
| Security improvement | Secret scanning, dependency review, injection controls, provenance checks | Change reduces source, runtime, credential, or dependency exposure |
| Evaluation improvement | Better criteria for claim feasibility, task fit, abstention, or human review | Evaluation logic is tied to a specific governance decision |

---

## Contribution Requirements

Every contribution should answer these questions before review:

1. What source, artifact, or control does this change affect?
2. What governance property does the change improve?
3. What artifact proves that improvement?
4. What failure mode remains after the change?
5. Does the change preserve human authority over accept, override, and reject decisions?

Pull requests that introduce new functionality should also explain how the change affects traceability from source material to decision summary.

---

## Adding a New Research Pack

A research pack is a governed translation unit. It should represent one research source or one bounded task family. Each pack should make the translation path inspectable.

Recommended structure:

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

Required elements:

| File | Required Content | Review Question |
|---|---|---|
| `sources/paper_text.txt` | Captured source text or source excerpt used for translation | Can a reviewer inspect the material that informed the claims? |
| `claims.json` | Falsifiable claims, source evidence, scope, and limitations | Are the claims narrow enough to test or reject? |
| `tasks.json` | Bounded tasks with inputs, outputs, constraints, failure conditions, and human gate | Could the task run without silently expanding authority? |
| `eval_plan.json` | Evaluation criteria, metrics, and review logic | Does the evaluation test the claim that justified the task? |
| `decision_summary.json` | Final verdict, evidence, uncertainty, human decision, and rationale | Can the decision be reconstructed after the fact? |

Use a descriptive pack ID. A good pack ID gives the reviewer a clue about the source domain and includes a short hash or unique suffix.

Example:

```text
multi_agent_failure_modes_e0228882
```

---

## Positive and Negative Translation

This repository treats rejection as a valid research outcome.

A translation-positive pack shows that a research claim can be converted into a bounded task under governance controls. A translation-negative pack shows that the research source remains analytically useful while failing the system’s operationalization criteria.

| Verdict | When to Use |
|---|---|
| `translation_positive` | The source supports a bounded task with defined inputs, outputs, metrics, failure conditions, and human review |
| `translation_negative` | The source cannot be operationalized without exceeding the governance boundary |
| `approve_with_conditions` | The task may proceed only under specified constraints |
| `reject_translation` | The system should record the research source and stop operationalization |

Negative translation should explain the boundary condition precisely. Strong rejection rationales usually involve autonomy, unverifiable assumptions, missing evaluation criteria, unbounded action space, poor provenance, or insufficient task containment.

---

## Schema and Validation Expectations

Schema validation is part of the governance model. It converts methodological intent into enforceable artifact contracts.

Before submitting a pull request, run the available validation scripts for the files you changed.

```bash
./scripts/validate_claims.sh packs/<pack_id>/claims.json
./scripts/validate_tasks.sh packs/<pack_id>/tasks.json
./scripts/validate_decision_summary.sh packs/<pack_id>/decision_summary.json
```

For example runs:

```bash
./scripts/run_examples.sh
```

A contribution that bypasses schema validation should explain why the schema needs revision. The preferred fix is to improve the schema or artifact, not to disable the check.

---

## Documentation Style

Documentation in this repository should be written for an intelligent reviewer who may disagree with the design. The goal is to make the reasoning inspectable.

Use this standard:

| Documentation Requirement | Implementation |
|---|---|
| State the decision problem first | Begin with the failure mode or governance question |
| Separate observation from inference | Name what the artifact shows and what the reviewer should infer from it |
| Avoid adoption rhetoric | Describe what the system controls, rejects, or records |
| Include limitations | Name what the contribution does not settle |
| Use tables when classification matters | Tables should clarify reviewer judgment, not decorate the page |
| Preserve audit language | Prefer source, claim, task, evidence, verdict, reviewer, decision, and uncertainty |

Avoid promotional language. The project’s credibility comes from controlled claims, explicit limits, and reconstructable artifacts.

---

## Human Gate Requirements

The human gate is a core control. Contributions should not allow raw model output to become final output without explicit human action.

Human-gate logic must preserve these decision states:

| Human Decision | Meaning |
|---|---|
| `accept` | The reviewer accepts the proposed output as final |
| `override` | The reviewer changes the proposed output and records the reason |
| `reject` | The reviewer rejects the proposed output and records the reason |

A contribution that changes the human gate should explain how the change preserves reviewer accountability, artifact traceability, and final decision reconstruction.

---

## Security and Source Integrity

Research translation can be attacked through source poisoning, prompt injection, manipulated PDFs, unsafe repository dependencies, hidden instructions in source text, credential leakage, and unreviewed runtime changes.

Contributors should treat all external source material as untrusted input.

Security-sensitive contributions should consider:

| Surface | Control Expectation |
|---|---|
| PDFs and web text | Preserve source text and avoid executing embedded instructions |
| GitHub repositories | Review license, dependency, and execution risk before use |
| Model prompts | Keep task instructions bounded and inspectable |
| Credentials | Never commit secrets, API keys, or private tokens |
| Logs | Avoid storing sensitive personal data or confidential source material |
| Dependencies | Prefer minimal dependencies with clear purpose |
| Runtime changes | Preserve artifact logging and human review |

Use the repository’s secret-scanning configuration before submitting changes.

---

## Pull Request Checklist

Before opening a pull request, confirm the following:

- The change improves provenance, claim discipline, task containment, human authority, audit reconstruction, security, or documentation clarity.
- New research packs include source material, claims, tasks, evaluation logic, and a decision summary.
- Translation-positive packs define bounded tasks and human review conditions.
- Translation-negative packs explain the rejection boundary.
- Schema validation passes for changed artifacts.
- Documentation names current limitations.
- No secrets, private credentials, or confidential data are committed.
- The pull request explains the governance effect of the change.

---

## Issue Reports

Good issues describe a failure mode, not just a desired feature.

Use this structure:

```text
Problem:
What governance, translation, validation, traceability, or security issue did you observe?

Artifact:
Which file, pack, schema, run, or decision summary is affected?

Expected behavior:
What should the system preserve, reject, validate, or record?

Observed behavior:
What happened instead?

Suggested fix:
What change would make the decision path more controlled or reconstructable?
```

---

## Versioning

This project uses releases to mark changes in method, artifact contracts, and archival metadata.

| Version Type | Meaning |
|---|---|
| Patch | Documentation correction, typo fix, small validation improvement |
| Minor | New research packs, schema clarifications, improved traceability, documentation expansion |
| Major | Material change to governance model, artifact contracts, translation method, or human-gate logic |

A release should explain whether the change affects method, software behavior, schemas, research examples, or citation metadata.

---

## Review Philosophy

The review standard is conservative because the repository models governed translation. A change that makes the system easier to use while making decisions harder to reconstruct weakens the project.

The strongest contributions make the system more willing to say no.

That is the point of the project: source material can inform a decision, but governed translation determines whether it can become one.
