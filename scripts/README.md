# Script Validation Layer

The `scripts/` directory contains the repository’s validation, reproducibility, and local security utilities. These scripts turn governed artifacts into checkable files: a claim file either satisfies its schema or it fails; a task file either declares a bounded task correctly or it fails; a safety-policy intake file either classifies the source before translation or it fails.

This directory should be treated as part of the governance boundary. The scripts do not decide whether a research claim is true. They decide whether the artifact has enough structure to be reviewed.

## Script inventory

| Script | Artifact checked | Governance function |
|---|---|---|
| `validate_safety_policy_intake.sh` | `safety_policy_intake.json` | Confirms AI safety and policy sources are classified before claims become tasks |
| `validate_pack.sh` | `agent_spec.json` inside a pack | Confirms the pack has a schema-valid agent or task specification |
| `validate_claims.sh` | `claims.json` inside a pack | Confirms extracted research claims satisfy the claim contract |
| `validate_tasks.sh` | `tasks.json` inside a pack | Confirms task definitions satisfy the bounded-task contract |
| `validate_run_input.sh` | run-input JSON file | Confirms governed execution input satisfies the run-input contract |
| `validate_run_output.sh` | run-output JSON file | Confirms governed execution output satisfies the run-output contract |
| `validate_decision_summary.sh` | `decision_summary.json` | Confirms final decision artifacts satisfy the decision-summary contract |
| `run_examples.sh` | example runs | Runs reference examples and validates their output artifacts |
| `install-pre-commit-gitleaks.sh` | local Git hooks | Installs local secret-scanning support before source material or logs are committed |

## Validation order

For AI safety and policy sources, run the safety-policy intake check first.

```text
safety_policy_intake.json
  ↓
agent_spec.json
  ↓
claims.json
  ↓
tasks.json
  ↓
run input
  ↓
run output
  ↓
decision_summary.json
```

That order matters. `safety_policy_intake.json` asks what kind of authority the source should be allowed to have. `claims.json` asks what the source says. `tasks.json` asks what bounded work may follow. The intake gate should happen before the repository turns a source into executable or reviewable tasks.

## Quick start

From the repository root:

```bash
chmod +x scripts/*.sh
```

Install validation dependencies:

```bash
python3 -m pip install jsonschema
```

Validate the safety-policy intake artifact for the first worked example:

```bash
./scripts/validate_safety_policy_intake.sh packs/multi_agent_failure_modes_e0228882/safety_policy_intake.json
```

Validate a pack’s agent specification:

```bash
./scripts/validate_pack.sh packs/haic_reliance_review_59e257ff
```

Validate claims:

```bash
./scripts/validate_claims.sh packs/haic_reliance_review_59e257ff
```

Validate tasks:

```bash
./scripts/validate_tasks.sh packs/haic_reliance_review_59e257ff
```

Validate a run input:

```bash
./scripts/validate_run_input.sh examples/runs/t_c02_input_with_snippets.json
```

Validate a run output:

```bash
./scripts/validate_run_output.sh runs/example_t_c02_from_examples/output.json
```

Validate a decision summary:

```bash
./scripts/validate_decision_summary.sh packs/haic_reliance_review_59e257ff/decision_summary.json
```

Run the example workflow:

```bash
./scripts/run_examples.sh
```

## `validate_safety_policy_intake.sh`

This script validates `safety_policy_intake.json` against `schemas/safety_policy_intake.schema.json`.

Use it when a source touches AI safety, AI policy, frontier capability, misuse, loss of control, compute governance, model-weight security, liability, international governance, or concentration of power.

```bash
./scripts/validate_safety_policy_intake.sh packs/<pack_id>/safety_policy_intake.json
```

A passing result means the intake artifact has the required structure. It does not mean the source is safe to operationalize. It means the source has been classified well enough for review.

A failing result means the pack should remain below translation-ready status until the missing or invalid fields are corrected.

## `validate_pack.sh`

This script validates `agent_spec.json` inside a pack.

```bash
./scripts/validate_pack.sh packs/<pack_id>
```

The script currently checks for the required agent specification and validates it against `schemas/agent_spec.schema.json`. It is a pack-entry check, not a complete audit of every artifact in the pack.

## `validate_claims.sh`

This script validates `claims.json` inside a pack.

```bash
./scripts/validate_claims.sh packs/<pack_id>
```

Use it after source material has been decomposed into falsifiable, source-linked claims. A passing result means the claim file satisfies the claim schema. It does not prove that the claims are correct, complete, or sufficiently evidenced.

## `validate_tasks.sh`

This script validates `tasks.json` inside a pack.

```bash
./scripts/validate_tasks.sh packs/<pack_id>
```

Use it after selected claims have been converted into bounded tasks. A passing result means the task file satisfies the task schema. It does not approve the task for deployment or autonomous execution.

## `validate_run_input.sh`

This script validates a governed run input.

```bash
./scripts/validate_run_input.sh examples/runs/<input_file>.json
```

Use it before execution or replay. The run input records what entered the governed execution path.

## `validate_run_output.sh`

This script validates a governed run output.

```bash
./scripts/validate_run_output.sh runs/<run_id>/output.json
```

Use it after execution and before decision-summary assembly. The run output remains an intermediate artifact until human review and deterministic decision-summary generation occur.

## `validate_decision_summary.sh`

This script validates a decision-summary artifact.

```bash
./scripts/validate_decision_summary.sh packs/<pack_id>/decision_summary.json
```

Use it before calling a translation decision complete. The decision summary is the audit-facing artifact that records the final outcome, rationale, confidence, limits, and human authorization state.

## `run_examples.sh`

This script runs the repository’s reference examples and validates the resulting outputs.

```bash
./scripts/run_examples.sh
```

Use it before release, after changing runner logic, after changing schemas, or after adding new validation checks that may affect reproducibility.

## `install-pre-commit-gitleaks.sh`

This script installs local secret-scanning support.

```bash
./scripts/install-pre-commit-gitleaks.sh
```

Use it before committing source text, run artifacts, logs, or environment files. Research translation can involve copied material, snippets, and configuration. Secret scanning reduces the chance that credentials or tokens are committed.

## GitHub Actions

The safety-policy intake patch also adds:

```text
.github/workflows/validate-artifacts.yml
```

GitHub Actions workflows live under `.github/workflows/` and are written as YAML files. This workflow validates every `safety_policy_intake.json` file found under `packs/` and can be extended later to validate every governed artifact in the repository.

## Failure interpretation

| Failure | Meaning | Correct response |
|---|---|---|
| Missing file | The expected artifact is absent | Add the artifact or keep the pack below the relevant maturity level |
| Schema validation error | The artifact violates the declared contract | Correct the artifact or revise the schema deliberately |
| Missing dependency | The local environment lacks a required package | Install the dependency with `python3 -m pip install jsonschema` |
| Permission error | The script is not executable | Run `chmod +x scripts/<script>.sh` |
| Path error | The command is being run from the wrong directory or the file path is wrong | Run commands from the repository root and verify the file path |

## Release standard

Before a release, run the validation chain on every mature pack that the release notes describe as review-ready or decision-complete. Development scaffolds may remain partial, but their status should be labeled clearly in `packs/README.md`.

The standard is strict: a governed artifact should fail early when its structure is incomplete. Silent success is more dangerous than visible failure.

