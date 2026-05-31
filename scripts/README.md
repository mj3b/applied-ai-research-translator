# Validation and Execution Scripts

The `scripts/` directory contains the repository’s validation and reproducibility utilities. These scripts make research translation artifacts testable before they are treated as review-ready, release-ready, or decision-complete.

In this repository, scripts are part of the governance boundary. They enforce artifact contracts, check schema compliance, run examples, and reduce the chance that a research pack becomes a decision record through informal judgment.

---

## Script Inventory

| Script | Purpose | Primary Artifact | Governance Function |
|---|---|---|---|
| `install-pre-commit-gitleaks.sh` | Installs local secret-scanning hooks | Repository commits | Reduces credential leakage risk before source material, logs, or examples are committed |
| `run_examples.sh` | Runs the example workflows | Example run inputs and runtime artifacts | Tests whether reference workflows remain executable and reproducible |
| `validate_claims.sh` | Validates extracted research claims | `claims.json` | Confirms claim artifacts follow the required structure |
| `validate_tasks.sh` | Validates bounded task definitions | `tasks.json` | Confirms task artifacts define controlled execution units |
| `validate_run_input.sh` | Validates governed run inputs | `run_input.json` | Confirms the run input is structured before execution |
| `validate_run_output.sh` | Validates governed run outputs | `run_output.json` | Confirms the output artifact is structured before review |
| `validate_decision_summary.sh` | Validates final decision summaries | `decision_summary.json` | Confirms the final decision artifact carries the required minimum record |
| `validate_pack.sh` | Validates a pack as a grouped translation unit | `packs/<pack_id>/` | Checks whether a pack’s artifacts are present and schema-valid |

---

## Why the Scripts Matter

A governed research translation system needs a repeatable way to distinguish a structured artifact from an informal file. The scripts provide that distinction.

```text
artifact written
  ↓
schema selected
  ↓
validation script run
  ↓
pass, fail, or revise
  ↓
artifact becomes eligible for review
```

A passing script result does not prove that the research translation is correct. It proves that the artifact has the minimum structure needed for review, reconstruction, and challenge.

That distinction matters. Schema-valid artifacts can still contain weak claims, poor evidence, incomplete reasoning, or overbroad conclusions. Validation is the floor.

---

## Recommended Validation Order

Use this sequence when preparing a pack for review.

| Step | Command | What It Tests |
|---:|---|---|
| 1 | `./scripts/validate_claims.sh packs/<pack_id>/claims.json` | Source-derived claims are structured and reviewable |
| 2 | `./scripts/validate_tasks.sh packs/<pack_id>/tasks.json` | Tasks are bounded and linked to the pack |
| 3 | `./scripts/validate_decision_summary.sh packs/<pack_id>/decision_summary.json` | Final decision record has required fields |
| 4 | `./scripts/validate_pack.sh packs/<pack_id>` | Pack-level artifact set is coherent |
| 5 | `./scripts/run_examples.sh` | Reference examples still execute |

Run input and run output validation should be used whenever a governed run is created or replayed.

```bash
./scripts/validate_run_input.sh examples/runs/<run_input>.json
./scripts/validate_run_output.sh <path_to_run_output>.json
```

---

## Quick Start

From the repository root:

```bash
chmod +x scripts/*.sh
```

Validate a claim file:

```bash
./scripts/validate_claims.sh packs/<pack_id>/claims.json
```

Validate a task file:

```bash
./scripts/validate_tasks.sh packs/<pack_id>/tasks.json
```

Validate a decision summary:

```bash
./scripts/validate_decision_summary.sh packs/<pack_id>/decision_summary.json
```

Validate a full pack:

```bash
./scripts/validate_pack.sh packs/<pack_id>
```

Run examples:

```bash
./scripts/run_examples.sh
```

Install the local secret-scanning hook:

```bash
./scripts/install-pre-commit-gitleaks.sh
```

---

## Script Responsibilities

### `validate_claims.sh`

This script validates a `claims.json` file against the claim schema.

Use it when a research source has been decomposed into extracted claims.

```bash
./scripts/validate_claims.sh packs/<pack_id>/claims.json
```

Review question:

```text
Do these claims have the structure required for source-grounded review?
```

The script should be run before any claim is used to justify task design.

---

### `validate_tasks.sh`

This script validates a `tasks.json` file against the task schema.

Use it after converting selected claims into bounded tasks.

```bash
./scripts/validate_tasks.sh packs/<pack_id>/tasks.json
```

Review question:

```text
Does this task artifact define a bounded execution or review unit?
```

The script helps prevent task definitions from becoming open-ended implementation instructions.

---

### `validate_run_input.sh`

This script validates a governed run input.

Use it before executing or replaying a run.

```bash
./scripts/validate_run_input.sh examples/runs/<run_input>.json
```

Review question:

```text
Is the input context structured enough to support reproducibility and review?
```

Run inputs should be treated as decision evidence. An output cannot be interpreted responsibly when the input context is missing or malformed.

---

### `validate_run_output.sh`

This script validates a governed run output.

Use it after execution and before human review.

```bash
./scripts/validate_run_output.sh <path_to_run_output>.json
```

Review question:

```text
Is the system output structured enough for review, abstention, rejection, or finalization?
```

A valid run output remains intermediate. It does not become a final decision until human review and decision-summary assembly are complete.

---

### `validate_decision_summary.sh`

This script validates the final decision-summary artifact.

Use it before describing a pack or run as decision-complete.

```bash
./scripts/validate_decision_summary.sh packs/<pack_id>/decision_summary.json
```

Review question:

```text
Does the final artifact record the decision, rationale, confidence, and traceability fields required for reconstruction?
```

The decision summary is the artifact most likely to be read by researchers, auditors, and institutional reviewers. It should pass validation before release.

---

### `validate_pack.sh`

This script validates a pack as a grouped translation unit.

Use it when preparing a pack for review, release, or archival citation.

```bash
./scripts/validate_pack.sh packs/<pack_id>
```

Review question:

```text
Do the pack artifacts cohere as a research-to-decision record?
```

A pack-level validation script should be treated as a readiness check, not as a methodological endorsement.

---

### `run_examples.sh`

This script runs the repository’s example workflows.

Use it before release, after runtime changes, or after schema changes.

```bash
./scripts/run_examples.sh
```

Review question:

```text
Do the reference workflows still execute under the current repository state?
```

This script supports reproducibility. It also catches drift between schemas, runtime code, and examples.

---

### `install-pre-commit-gitleaks.sh`

This script installs local secret-scanning support using the repository’s Gitleaks configuration.

Use it before working with source material, example logs, run artifacts, or environment variables.

```bash
./scripts/install-pre-commit-gitleaks.sh
```

Review question:

```text
Has the local environment reduced the risk of committing secrets?
```

Research translation can involve copied text, examples, logs, and configuration. Secret scanning is a minimal guardrail, especially when researchers test workflows locally.

---

## Governance Interpretation of Script Results

| Result | Meaning | Appropriate Action |
|---|---|---|
| Pass | Artifact satisfies the declared schema or script check | Proceed to human review or next validation step |
| Fail | Artifact violates the schema or script expectation | Revise the artifact or schema before review |
| Script error | Tooling failed or expected dependency is missing | Fix the script environment before interpreting artifact quality |
| Missing file | Required artifact is absent | Decide whether the pack is development-stage or incomplete |
| Partial validation | Some artifacts pass and others fail | Treat the pack as below decision-complete maturity |

A failed validation is useful evidence. It identifies where the translation record cannot yet support review.

---

## When to Run Scripts

| Situation | Scripts to Run |
|---|---|
| Adding a new research pack | `validate_claims.sh`, `validate_tasks.sh`, `validate_decision_summary.sh`, `validate_pack.sh` |
| Editing schemas | All validation scripts and `run_examples.sh` |
| Editing runloop code | `run_examples.sh`, `validate_run_input.sh`, `validate_run_output.sh`, `validate_decision_summary.sh` |
| Preparing a release | `validate_pack.sh` for mature packs, `run_examples.sh`, secret scan |
| Updating examples | `run_examples.sh`, run input/output validation |
| Adding source material | Secret scan, claim validation after extraction |
| Preparing Zenodo archival release | Full validation of packs cited in the README and release notes |

---

## Pre-Release Validation Checklist

Before a release, run this sequence from the repository root:

```bash
chmod +x scripts/*.sh

./scripts/validate_claims.sh packs/haic_reliance_review_59e257ff/claims.json
./scripts/validate_tasks.sh packs/haic_reliance_review_59e257ff/tasks.json
./scripts/validate_decision_summary.sh packs/haic_reliance_review_59e257ff/decision_summary.json

./scripts/validate_claims.sh packs/multi_agent_failure_modes_e0228882/claims.json
./scripts/validate_tasks.sh packs/multi_agent_failure_modes_e0228882/tasks.json
./scripts/validate_decision_summary.sh packs/multi_agent_failure_modes_e0228882/decision_summary.json

./scripts/run_examples.sh
```

For packs that remain development scaffolds, document their maturity level in `packs/README.md` instead of forcing them to appear decision-complete.

---

## Failure Modes the Scripts Help Detect

| Failure Mode | Likely Script Signal | Governance Concern |
|---|---|---|
| Missing provenance | Claim validation failure or pack validation failure | The reviewer cannot trace the claim to source material |
| Orphaned task | Task validation failure | The task may have no source-grounded claim |
| Informal run input | Run input validation failure | The execution context cannot be reconstructed |
| Unstructured output | Run output validation failure | Human review lacks a stable artifact |
| Missing final rationale | Decision-summary validation failure | The decision cannot be defended or reconstructed |
| Example drift | `run_examples.sh` failure | Runtime code, schemas, and examples no longer align |
| Secret exposure | Gitleaks hook finding | Repository may contain credentials or sensitive data |

These failures should be fixed before release unless the repository explicitly labels the affected artifact as development-stage.

---

## Script Design Principles

Scripts should remain small, inspectable, and conservative.

| Principle | Meaning |
|---|---|
| Validate artifacts, do not infer approval | A script can say whether structure is valid. It should not decide whether a research claim is true |
| Fail visibly | Errors should stop the workflow and return useful information |
| Preserve human review | Script success should move an artifact to review, not replace review |
| Keep paths explicit | Commands should show which artifact is being validated |
| Avoid hidden mutation | Validation scripts should not silently rewrite governed artifacts |
| Support release reconstruction | Script output should help a release reviewer reproduce the validation path |

The scripts are intentionally modest. Their value comes from enforcing stable contracts in the source-to-decision chain.

---

## Adding a New Script

New scripts should explain which governance control they enforce.

Recommended header pattern:

```bash
#!/usr/bin/env bash
set -euo pipefail

# Purpose:
#   Validate or reproduce a specific governed artifact.
#
# Governance control:
#   Explain which part of the source → claim → task → run → decision chain this script protects.
#
# Usage:
#   ./scripts/<script_name>.sh <artifact_path>
```

A new script should include:

| Requirement | Reason |
|---|---|
| Explicit input path | Prevents accidental validation of the wrong artifact |
| Non-zero exit on failure | Makes automation and release checks reliable |
| Clear error message | Reduces reviewer ambiguity |
| No hidden writes during validation | Preserves artifact integrity |
| Schema or control reference | Shows which governance rule is being enforced |

---

## Directory Structure

```text
scripts/
├── README.md
├── install-pre-commit-gitleaks.sh
├── run_examples.sh
├── validate_claims.sh
├── validate_decision_summary.sh
├── validate_pack.sh
├── validate_run_input.sh
├── validate_run_output.sh
└── validate_tasks.sh
```

The current script set corresponds to the repository’s core artifact chain: claims, tasks, run inputs, run outputs, decision summaries, pack readiness, examples, and secret scanning. The governing standard is direct: a script is useful when it makes a research translation artifact harder to misread as more complete than it is.
