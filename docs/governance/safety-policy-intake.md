# Safety and Policy Intake Gate

The safety-policy intake gate classifies an AI safety or policy source before the translator extracts claims, designs tasks, or produces decision artifacts.

The gate exists because AI safety material is not ordinary research input. A paper about benchmark performance, a policy memo about liability, a report about model-weight security, and a loss-of-control argument may all be useful. They should not receive the same translation path. The intake artifact forces the pack to record what kind of evidence the source provides, what risk domain it touches, what autonomy surface it implies, what review authority is required, and what translation boundary applies.

## Required Artifact

Each safety-relevant pack should include:

```text
packs/<pack_id>/
└── safety_policy_intake.json
```

A top-level template is included at:

```text
packs/_template_safety_policy_intake/safety_policy_intake.json
```

The pack-local file is the governed artifact. The template is only a drafting aid.

## Governance Function

The intake gate should be read as a Govern and Map artifact in the NIST AI RMF sense. It records context, risk class, evidence status, review authority, and translation boundary before the repository moves into measurement, task design, or final decision records.

## Minimum Decision Rule

```text
A pack is not translation-ready until safety_policy_intake.json classifies the source by evidence type, AI safety domain, autonomy level, dual-use status, loss-of-control relevance, required review authority, and translation boundary.
```

## What the Gate Classifies

| Field group | Purpose |
|---|---|
| `source_status` | Distinguishes empirical research, forecasts, scenarios, benchmarks, policy arguments, legal requirements, and implementation evidence |
| `ai_safety_domain` | Routes the source across capability forecasting, misuse, loss of control, structural risk, compute governance, model-weight security, liability, international governance, and concentration of power |
| `capability_and_autonomy` | Records model class, autonomy level, task horizon, and tool-use scope |
| `risk_screen` | Records misuse pathways, dual-use status, loss-of-control indicators, oversight failure modes, and catastrophic-risk relevance |
| `governance_mapping` | Records the decision lever, required reviewers, and translation boundary |
| `translation_verdict` | Records whether the pack may proceed, proceed with constraints, remain evaluation-only, remain policy-mapping-only, require review, be restricted, be rejected, or abstain |

## Validation

Run:

```bash
./scripts/validate_safety_policy_intake.sh packs/<pack_id>/safety_policy_intake.json
```

The validator uses `schemas/safety_policy_intake.schema.json`.

## Translation Boundaries

| Boundary | Meaning |
|---|---|
| `claim_extraction_only` | The source may be decomposed into claims but should not yet produce tasks |
| `evaluation_design` | The source may inform eval criteria or test design |
| `governed_task` | The source may become a bounded task under existing governance controls |
| `policy_mapping_only` | The source should inform policy or governance mapping without execution |
| `restricted` | The source has dual-use, security, or governance concerns requiring restricted handling |
| `reject` | The source should not be translated under the repository boundary |

## Reviewer Standard

A serious reviewer should be able to answer five questions from the intake file:

1. What kind of evidence is this source?
2. Which AI safety or policy domain does it touch?
3. Does it increase autonomy, misuse, or loss-of-control concern?
4. Who must review it before it becomes a task?
5. What is the allowed translation boundary?

The intake gate succeeds when it prevents a useful source from becoming an over-authorized artifact.
