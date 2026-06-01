# Contributing to Applied AI Research Translator

Applied AI Research Translator accepts contributions that make research-to-decision translation more inspectable. A useful change should make source material easier to reconstruct, claims easier to test, tasks easier to bound, safety-policy risks easier to classify, human decisions easier to review, or final records easier to audit.

This repository is a governed translation system. It is not an adoption accelerator. Contributions should preserve the boundary between research interpretation and institutional action.

---

## Contribution Standard

A contribution belongs here when it improves at least one governance property.

| Property | Contribution Question | Evidence Required |
|---|---|---|
| Provenance | Does the change make source material easier to identify, preserve, version, or reconstruct? | Source path, citation, version, timestamp, retrieval note, or captured source text |
| Safety-policy classification | Does the change classify AI safety or policy risk before claims become tasks? | `safety_policy_intake.json`, schema update, reviewer note, or translation-boundary rationale |
| Claim discipline | Does the change make research claims more falsifiable, scoped, or testable? | Updated claim schema, example claim, source evidence, or review note |
| Task containment | Does the change make task boundaries clearer before execution? | Task schema change, bounded example, failure condition, or abstention condition |
| Human authority | Does the change preserve human accept, override, reject, or escalation authority? | Human-gate artifact, review logic, or decision-summary field |
| Audit reconstruction | Does the change make the decision path easier to inspect after the fact? | Traceability link, run artifact, validation output, or decision record |
| Security and source integrity | Does the change reduce source, runtime, credential, dependency, or logging risk? | Security check, dependency note, redaction, source-handling control, or secret-scan evidence |

Changes that add capability while making decisions harder to reconstruct should be rejected.

---

## What This Project Protects

Research translation creates risk when source material becomes operational justification before it has been decomposed into source status, claims, assumptions, task boundaries, review authority, and failure conditions. A paper may support a bounded task. A benchmark may support an evaluation plan. A policy memo may support a governance mapping. None of those sources authorizes action by itself.

This repository protects the decision boundary between research interpretation and institutional action.

| Risk | How Contributions Should Address It |
|---|---|
| Research claim inflation | Keep claims narrow, falsifiable, and linked to source evidence |
| Source volatility | Preserve source text, version, citation, and retrieval context where possible |
| Safety-policy underclassification | Classify AI safety and policy relevance before task design |
| Benchmark overgeneralization | Record the conditions under which a finding applies |
| Dual-use leakage | Route misuse-relevant or hazardous sources to restricted handling or human review |
| Loss-of-control normalization | Treat autonomy, strategic behavior, oversight failure, and power-seeking as review triggers |
| Model-output authority drift | Keep model outputs intermediate until human review completes |
| Post-hoc rationalization | Lock tasks and evaluation conditions before governed execution |
| Unreviewable adoption | Produce a decision summary that reconstructs the source-to-decision path |
| Unsafe operationalization | Preserve restriction, rejection, and abstention as valid outcomes |

A useful contribution makes at least one of these risks easier to detect, constrain, or document.

---

## Contribution Types

| Contribution Type | Examples | Review Standard |
|---|---|---|
| Research pack | New paper, PDF, report, preprint, benchmark, policy memo, or repository translated into governed artifacts | Source is captured, safety-policy relevance is classified where applicable, claims are scoped, tasks are bounded, verdict is justified |
| Safety-policy intake pack | AI safety or policy source classified before translation | Evidence type, risk domain, autonomy relevance, dual-use status, required review, and translation boundary are recorded |
| Negative translation pack | Research source that should stop at analysis, evaluation design, policy mapping, or rejection | Rejection rationale is explicit, evidence-linked, and reproducible |
| Schema improvement | New required field, stricter validation, clearer artifact contract | Change improves auditability without breaking existing packs unnecessarily |
| Runloop improvement | Better logging, validation, deterministic summary generation, or human-gate handling | Change preserves the authority boundary and artifact trail |
| Documentation | Clarifies method, governance model, traceability, limitations, or review path | Text distinguishes artifact evidence, inference, and unresolved questions |
| Security improvement | Secret scanning, dependency review, injection controls, provenance checks | Change reduces source, runtime, credential, dependency, or logging exposure |
| Evaluation improvement | Better criteria for claim feasibility, task fit, abstention, or human review | Evaluation logic is tied to a specific governance decision |

---

## Contribution Requirements

Every contribution should answer these questions before review:

1. What source, artifact, or control does this change affect?
2. What governance property does the change improve?
3. What artifact proves that improvement?
4. What failure mode remains after the change?
5. Does the change preserve human authority over accept, override, reject, and escalation decisions?
6. Does the change affect safety-policy intake, translation boundary, or review authority?
7. Does the change preserve traceability from source material to decision summary?

Pull requests that introduce new functionality should explain how the change affects the artifact chain.

```text
source material
  ↓
safety-policy intake, where applicable
  ↓
claims
  ↓
tasks
  ↓
evaluation plan
  ↓
run or manual review artifacts
  ↓
human gate
  ↓
decision summary
```

---

## Adding a New Research Pack

A research pack is a governed translation unit. It should represent one research source or one bounded task family. Each pack should make the translation path inspectable.

Recommended structure for mature packs:

```text
packs/<pack_id>/
├── safety_policy_intake.json
├── agent_spec.json
├── claims.json
├── tasks.json
├── eval_plan.json
├── decision_summary.json
└── sources/
    └── paper_text.txt
```

`Safety_policy_intake.json` is required for AI safety and policy sources. It may be omitted for narrow development scaffolds or non-safety examples, but the omission should be treated as a maturity limit.

| File | Required Content | Review Question |
|---|---|---|
| `sources/paper_text.txt` | Captured source text or source excerpt used for translation | Can a reviewer inspect the material that informed the claims? |
| `safety_policy_intake.json` | Source status, AI safety domain, autonomy relevance, risk screen, required review, and translation boundary | Has the source been classified before claims become tasks? |
| `agent_spec.json` | Bounded agent or task specification | Could the system operate without expanding the role or authority boundary? |
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

## Safety-Policy Intake Requirements

AI safety and policy sources require classification before claim extraction and task design. The intake gate prevents the repository from treating capability forecasts, misuse research, loss-of-control arguments, model-weight security reports, legal texts, and policy memos as ordinary research input.

Use `safety_policy_intake.json` when a source touches any of these domains:

| Domain | Intake Concern |
|---|---|
| Capability forecasting | The source may affect preparedness, deployment timing, escalation, or evaluation priorities |
| Misuse | The source may lower barriers to harmful cyber, bio, chemical, persuasion, fraud, surveillance, or infrastructure activity |
| Loss of control | The source may involve agency, deception, power-seeking, toolchain takeover, collusion, or oversight failure |
| Structural or gradual risk | The source may describe cumulative institutional, economic, political, or coordination risk |
| Compute governance | The source may affect compute reporting, allocation, verification, or policy control |
| Model-weight security | The source may affect release policy, access controls, exfiltration risk, or monitoring |
| Liability or private governance | The source may affect legal responsibility, contract design, or institutional accountability |
| International governance | The source may affect cross-border coordination, monitoring, or verification |
| Concentration of power | The source may affect infrastructure, market, institutional, or geopolitical concentration |

The intake artifact should answer one question before the pack proceeds:

```text
What kind of authority should this source be allowed to have?
```

Valid translation boundaries include:

| Boundary | Meaning |
|---|---|
| `claim_extraction_only` | The source may be decomposed into claims, with task design withheld |
| `evaluation_design` | The source may inform evaluation criteria or test design |
| `governed_task` | The source may become a bounded task under existing controls |
| `policy_mapping_only` | The source may inform governance or policy mapping without execution |
| `restricted` | The source requires constrained handling because of safety, misuse, legal, or security concerns |
| `reject` | The source should not be translated under this repository boundary |

---

## Positive, Restricted, and Negative Translation

This repository treats rejection as a valid research outcome.

A translation-positive pack shows that a research claim can be converted into a bounded task under governance controls. A restricted pack shows that the source has value but requires constrained handling. A translation-negative pack shows that the research source remains analytically useful while failing the system’s operationalization criteria.

| Verdict | When to Use |
|---|---|
| `translation_positive` | The source supports a bounded task with defined inputs, outputs, metrics, failure conditions, and human review |
| `evaluation_only` | The source should inform evaluation design without becoming an operational task |
| `policy_mapping_only` | The source should inform governance or policy mapping without execution |
| `restricted` | The source has dual-use, safety, legal, security, or governance concerns requiring restricted handling |
| `human_review_required` | The source requires designated reviewer authority before translation proceeds |
| `translation_negative` | The source cannot be operationalized without exceeding the governance boundary |
| `reject_translation` | The system should record the research source and stop operationalization |
| `abstain` | Evidence is insufficient to classify or translate the source responsibly |

Strong rejection rationales usually involve autonomy, unverifiable assumptions, missing evaluation criteria, unbounded action space, poor provenance, dual-use risk, loss-of-control indicators, or insufficient task containment.

---

## Schema and Validation Expectations

Schema validation is part of the governance model. It converts methodological intent into enforceable artifact contracts.

Before submitting a pull request, run the validation scripts for the files you changed.

For AI safety and policy sources, run the intake validator first:

```bash
./scripts/validate_safety_policy_intake.sh packs/<pack_id>/safety_policy_intake.json
```

Then validate the downstream artifacts:

```bash
./scripts/validate_claims.sh packs/<pack_id>/claims.json
./scripts/validate_tasks.sh packs/<pack_id>/tasks.json
./scripts/validate_decision_summary.sh packs/<pack_id>/decision_summary.json
```

For example runs:

```bash
./scripts/run_examples.sh
```

A contribution that bypasses schema validation should explain why the schema needs revision. The preferred fix is to improve the schema or artifact.

The GitHub Actions workflow validates safety-policy intake files under `packs/` on push and pull request:

```text
.github/workflows/validate-artifacts.yml
```

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
| Use tables when classification matters | Tables should clarify reviewer judgment |
| Preserve audit language | Prefer source, intake, claim, task, evidence, verdict, reviewer, decision, and uncertainty |

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
| `abstain` | The reviewer withholds approval because evidence, authority, or task fit is insufficient |
| `escalate` | The reviewer routes the decision to legal, security, governance, domain, executive, or regulatory review |

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
| Safety-policy sources | Classify dual-use, misuse, loss-of-control, and restricted-handling concerns before translation |
| Model prompts | Keep task instructions bounded and inspectable |
| Credentials | Never commit secrets, API keys, or private tokens |
| Logs | Avoid storing sensitive personal data or confidential source material |
| Dependencies | Prefer minimal dependencies with clear purpose |
| Runtime changes | Preserve artifact logging and human review |

Use the repository’s secret-scanning configuration before submitting changes.

---

## Pull Request Checklist

Before opening a pull request, confirm the following:

- The change improves provenance, safety-policy classification, claim discipline, task containment, human authority, audit reconstruction, security, or documentation clarity.
- New AI safety and policy packs include `safety_policy_intake.json`.
- New research packs include source material, claims, tasks, evaluation logic, and a decision summary unless clearly labeled as scaffolds.
- Translation-positive packs define bounded tasks and human review conditions.
- Restricted packs explain the safety, dual-use, legal, or security basis for restriction.
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
What governance, translation, validation, traceability, safety-policy, or security issue did you observe?

Artifact:
Which source, pack, schema, run, workflow, or decision summary is affected?

Expected behavior:
What should the system preserve, classify, restrict, reject, validate, or record?

Observed behavior:
What happened instead?

Suggested fix:
What change would make the decision path more controlled or reconstructable?
```

---

## Versioning

This project uses releases to mark changes in method, artifact contracts, validation behavior, and archival metadata.

| Version Type | Meaning |
|---|---|
| Patch | Documentation correction, small validation improvement, safety-policy intake refinement, or metadata correction |
| Minor | New research packs, schema clarifications, traceability expansion, governance documentation, or new validation gates |
| Major | Material change to governance model, artifact contracts, translation method, human-gate logic, or authority boundary |

A release should explain whether the change affects method, software behavior, schemas, research examples, validation, safety-policy intake, or citation metadata.

---

## Review Philosophy

The review standard is conservative because the repository models governed translation. A change that makes the system easier to use while making decisions harder to reconstruct weakens the project.

The strongest contributions improve the system’s ability to stop.

That is the point of the repository: source material can inform a decision, while governed translation determines whether it can become one.
