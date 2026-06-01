# Schema Contracts

The `schemas/` directory defines the machine-checkable contracts for governed research translation. These JSON Schemas specify what must exist before a research source can move from interpretation into bounded task execution, human review, and decision-summary reconstruction.

Schemas are not validation utilities only. In this repository, schemas are governance controls. They define what evidence must be present, what decisions must be recorded, what outputs can be accepted, and where the system must abstain, reject, or require human review.

---

## Why Schemas Matter

Research translation fails when the important assumptions stay implicit. A paper becomes a task, a task becomes an output, and an output becomes a decision without a record of what changed at each step.

The schema layer prevents that collapse.

```text
research source
  ↓
schema-bound safety and policy intake
  ↓
schema-bound claim record
  ↓
schema-bound task definition
  ↓
schema-bound run input
  ↓
schema-bound run output
  ↓
schema-bound decision summary
```

Each schema forces one step in the chain to become inspectable. A reviewer should be able to ask: what source was used, what safety or policy risk it carried, what claim was extracted, what task was authorized, what input was processed, what output was produced, and what decision was recorded?

---

## Schema Inventory

| Schema | Governs | Required Root Fields | Governance Function |
|---|---|---|---|
| `safety_policy_intake.schema.json` | Safety and policy source intake | `intake_version`, `pack_id`, `source_id`, `source_type`, `source_status`, `ai_safety_domain`, `capability_and_autonomy`, `risk_screen`, `governance_mapping`, `translation_verdict` | Classifies AI safety and policy relevance before claims become tasks |
| `agent_spec.schema.json` | Agent, task, or translation-unit specification | `spec_version`, `spec_id`, `created_at`, `status`, `decision`, `inputs`, `outputs`, `evaluation`, `governance` | Defines the bounded decision context before execution |
| `claims.schema.json` | Extracted research claims | `claims_version`, `pack_id`, `created_at`, `source`, `claims` | Converts source material into reviewable, falsifiable claim records |
| `tasks.schema.json` | Bounded task definitions | `tasks_version`, `pack_id`, `created_at`, `source`, `tasks` | Converts selected claims into controlled operational tasks |
| `run_input.schema.json` | Governed run inputs | `run_id`, `pack_id`, `task_id`, `created_at`, `inputs` | Records the exact input context for a run |
| `run_output.schema.json` | Governed run outputs | `run_id`, `pack_id`, `task_id`, `created_at`, `status`, `result`, `evidence` | Separates model or system output from final human authorization |
| `decision_summary.schema.json` | Final decision artifact | `run_id`, `task_id`, `decision`, `confidence`, `rationale` | Provides the minimum reconstructable decision record |

---

## Contract Sequence

The schemas should be understood as a chain. Later artifacts inherit accountability from earlier artifacts.

| Sequence | Artifact | Schema | Reviewer Question |
|---:|---|---|---|
| 1 | Safety and policy intake | `safety_policy_intake.schema.json` | What AI safety or policy risk class does the source carry before translation begins? |
| 2 | Specification | `agent_spec.schema.json` | What decision context is being governed? |
| 3 | Claims | `claims.schema.json` | What did the source actually support? |
| 4 | Tasks | `tasks.schema.json` | What bounded task follows from the selected claim? |
| 5 | Run input | `run_input.schema.json` | What exact input entered the governed run? |
| 6 | Run output | `run_output.schema.json` | What did the system produce, and what evidence did it provide? |
| 7 | Decision summary | `decision_summary.schema.json` | What final decision was recorded, at what confidence, and for what reasons? |

A valid downstream artifact cannot repair a missing upstream artifact. A clean decision summary with weak source provenance remains a weak governance record.

---

## `safety_policy_intake.schema.json`

The safety-policy intake schema governs the first review boundary for AI safety and policy sources. It classifies the source before the repository extracts claims, designs tasks, or treats a pack as translation-ready.

This schema exists because AI safety material does not enter the repository as a neutral document class. A benchmark, a frontier-model forecast, a dual-use report, a loss-of-control argument, a legal requirement, and a model-weight security analysis carry different evidence strength, review obligations, and translation boundaries.

| Field | Purpose | Governance Role |
|---|---|---|
| `intake_version` | Identifies the intake artifact format | Supports versioned review of the intake gate |
| `pack_id` | Links the intake to a research pack | Preserves pack-level traceability before claims are extracted |
| `source_id` | Identifies the source within the pack | Allows later artifacts to point back to the classified source |
| `source_type` | Classifies the source as paper, preprint, benchmark, legal text, repository, vendor report, or related source type | Prevents dissimilar sources from entering the same translation path by default |
| `source_status` | Records review status, evidence type, epistemic status, and update condition | Preserves the difference between empirical evidence, forecast, scenario, legal requirement, implementation evidence, and policy argument |
| `ai_safety_domain` | Marks capability forecasting, misuse, loss of control, structural risk, compute governance, model-weight security, liability, international governance, and concentration of power | Routes the source to the right safety or policy review frame |
| `capability_and_autonomy` | Records model class, autonomy level, task-horizon relevance, and tool-use scope | Prevents agentic or frontier-relevant sources from being translated as ordinary task material |
| `risk_screen` | Records misuse pathways, dual-use status, loss-of-control indicators, oversight failure modes, and catastrophic-risk relevance | Makes the safety concern visible before task design |
| `governance_mapping` | Records decision lever, required reviewers, and translation boundary | Assigns review authority and prevents over-authorized translation |
| `translation_verdict` | Records proceed, proceed with constraints, evaluation-only, policy-mapping-only, restricted, human-review-required, reject, or abstain | Converts source classification into an auditable routing decision |

A valid safety-policy intake file does not prove that the source is safe to operationalize. It proves that the pack has made a pre-translation risk classification. For AI safety and policy sources, that classification should occur before `claims.json` and before any task in `tasks.json` is treated as review-ready.

The most important field is `translation_boundary`. It determines whether the source may support claim extraction, evaluation design, governed task design, policy mapping, restricted handling, or rejection. A source can remain valuable for research while being blocked from task translation.

---

## `agent_spec.schema.json`

The agent specification defines the bounded decision context. It is the highest-level contract in the schema layer because it declares what the system is allowed to do, what it must produce, how evidence should be handled, and what governance controls apply.

| Field | Purpose | Governance Role |
|---|---|---|
| `spec_version` | Identifies the specification format | Supports versioned interpretation |
| `spec_id` | Identifies the specification instance | Supports traceability across packs and runs |
| `created_at` | Records when the specification was created | Supports audit timing |
| `updated_at` | Records later revision timing | Supports change tracking |
| `status` | Records lifecycle state: `draft`, `review`, `approved`, or `deprecated` | Prevents unapproved specifications from being treated as stable |
| `decision` | Defines the decision name, user persona, goal, scope, failure cost, and success criteria | Anchors the work to a governed decision |
| `inputs` | Defines modalities, required fields, optional fields, data assumptions, and redaction rules | Controls input boundaries and data exposure |
| `outputs` | Defines the output schema, evidence requirements, confidence labeling, and abstention behavior | Controls what the system may produce |
| `evaluation` | Defines how output quality and task success will be judged | Prevents informal evaluation after output generation |
| `governance` | Defines review, authority, and control expectations | Preserves the institutional authority boundary |
| `provenance` | Records source, authorship, and origin context where available | Supports audit reconstruction |

The `status` field has governance significance. A `draft` specification should remain a development artifact. A `review` specification requires scrutiny. An `approved` specification may be used for controlled runs. A `deprecated` specification should remain available for reconstruction while being withheld from future use.

---

## `claims.schema.json`

The claims schema governs the transition from source material to research claims. It prevents the repository from treating a paper, report, or PDF as a single undifferentiated authority.

| Field | Purpose | Governance Role |
|---|---|---|
| `claims_version` | Identifies the claim artifact format | Supports future schema evolution |
| `pack_id` | Links the claim artifact to a translation pack | Preserves pack-level traceability |
| `created_at` | Records claim extraction timing | Supports review chronology |
| `source.paper_text_path` | Points to the source text used for extraction | Anchors claims to inspectable material |
| `source.method` | Describes how claims were extracted | Distinguishes manual, assisted, or hybrid extraction |
| `source.notes` | Records source caveats or extraction notes | Preserves reviewer context |
| `claims` | Contains the extracted claim objects | Defines the claim set available for task design |

The claims file should make source dependence visible. A claim should remain narrow enough that a reviewer can trace it to specific source material and decide whether task translation preserves its meaning.

---

## `tasks.schema.json`

The tasks schema governs the move from research claim to bounded operational task. This is the point where research interpretation starts to become operationally consequential.

| Field | Purpose | Governance Role |
|---|---|---|
| `tasks_version` | Identifies the task artifact format | Supports versioned review |
| `pack_id` | Links the task artifact to its pack | Preserves source-to-task traceability |
| `created_at` | Records task definition timing | Shows that task design preceded execution |
| `source.claims_path` | Links tasks back to claim records | Prevents orphaned tasks |
| `source.method` | Describes how tasks were derived | Records the translation method |
| `source.notes` | Captures task derivation caveats | Preserves unresolved constraints |
| `tasks` | Contains bounded task objects | Defines what may be executed or reviewed |

A task should define a controlled input, expected output, evaluation pathway, and failure condition. Where the task requires autonomous coordination, open-ended action, unverifiable assumptions, or informal review, the correct governance outcome may be rejection.

---

## `run_input.schema.json`

The run input schema captures the exact execution context for a governed run.

| Field | Purpose | Governance Role |
|---|---|---|
| `run_id` | Identifies the specific run | Supports log and artifact linkage |
| `pack_id` | Links the run to the research pack | Preserves source context |
| `task_id` | Links the run to the bounded task | Prevents execution without task authorization |
| `created_at` | Records input creation timing | Supports run chronology |
| `inputs` | Stores the run input payload | Enables reproducibility and review |

The run input should be treated as evidence. A reviewer needs to know what information entered the system before interpreting the output.

---

## `run_output.schema.json`

The run output schema records what the governed system produced. It does not make the output final.

| Field | Purpose | Governance Role |
|---|---|---|
| `run_id` | Links output to a specific run | Supports artifact reconstruction |
| `pack_id` | Links output to a research pack | Preserves source context |
| `task_id` | Links output to the bounded task | Preserves task-level accountability |
| `created_at` | Records output creation timing | Supports chronology |
| `status` | Records `ok`, `abstained`, or `error` | Makes failure and abstention explicit |
| `result` | Stores the produced output | Keeps system output inspectable |
| `evidence` | Stores supporting evidence items | Prevents unsupported output acceptance |
| `notes` | Records output caveats or reviewer context | Preserves interpretive constraints |

The `status` field is a control point. `ok` means the system produced schema-valid output. It does not mean the output is approved. `abstained` means the system declined or failed to produce a usable result under the defined constraints. `error` means execution failed and should be reviewed before any downstream use.

---

## `decision_summary.schema.json`

The decision summary schema defines the minimum final decision record.

| Field | Purpose | Governance Role |
|---|---|---|
| `run_id` | Links the summary to the governed run | Supports reconstruction |
| `task_id` | Links the summary to the task | Preserves task authority |
| `decision` | Records the final decision | Makes the outcome explicit |
| `confidence` | Records `low`, `medium`, or `high` | Calibrates the decision |
| `rationale` | Lists the reasons supporting the decision | Makes the decision reviewable |
| `notes` | Records additional context | Preserves caveats |

The decision summary is the artifact a later reviewer should be able to inspect without replaying the whole run. It should disclose the decision, the reasons, the confidence level, and any remaining uncertainty.

---

## Validation Commands

Use the validation scripts from the repository root.

```bash
./scripts/validate_safety_policy_intake.sh packs/<pack_id>/safety_policy_intake.json
./scripts/validate_claims.sh packs/<pack_id>/claims.json
./scripts/validate_tasks.sh packs/<pack_id>/tasks.json
./scripts/validate_run_input.sh examples/runs/<run_input>.json
./scripts/validate_run_output.sh <path_to_run_output>.json
./scripts/validate_decision_summary.sh packs/<pack_id>/decision_summary.json
```

Where applicable, validate the full pack:

```bash
./scripts/validate_pack.sh packs/<pack_id>
```

The validation scripts should be run before a pack is described as review-ready, release-ready, or decision-complete.

---

## Governance Rules Enforced by the Schema Layer

| Rule | Enforced Through | Rationale |
|---|---|---|
| AI safety and policy sources should be classified before translation | `safety_policy_intake.translation_verdict`, `governance_mapping.translation_boundary` | Prevents high-risk or dual-use sources from becoming tasks by default |
| A task should trace to a claim | `tasks.source.claims_path` | Prevents ungrounded task design |
| A claim should trace to source material | `claims.source.paper_text_path` | Prevents source-free interpretation |
| A run should trace to a task | `run_input.task_id`, `run_output.task_id` | Prevents unauthorized execution |
| A run should trace to a pack | `run_input.pack_id`, `run_output.pack_id` | Preserves research context |
| Output status should be explicit | `run_output.status` | Preserves abstention and error states |
| Final decisions should state confidence | `decision_summary.confidence` | Prevents uncalibrated authorization |
| Final decisions should include rationale | `decision_summary.rationale` | Supports review and audit reconstruction |

These rules do not prove that a translation is correct. They force the decision path to leave a structured record.

---

## Schema Evolution

Schema changes should be conservative because artifact contracts affect the interpretability of existing packs.

| Change Type | Example | Review Requirement |
|---|---|---|
| Clarifying change | Better field descriptions or stricter examples | Confirm existing artifacts remain interpretable |
| Additive change | Optional field for reviewer identity, source version, or limitation note | Explain the governance purpose |
| Required-field change | New required field for provenance, confidence, or human-gate state | Provide migration guidance for existing packs |
| Breaking change | Renaming fields or changing artifact shape | Require release notes and versioned schema rationale |

A schema change should state what governance failure it prevents or what audit question it makes answerable.

---

## Recommended Future Schema Additions

The current schema layer is sufficient for v1.1 archival release. The next maturity step is to make human-gate and provenance fields more explicit.

| Candidate Addition | Target Schema | Governance Value |
|---|---|---|
| `source_risk_profile` cross-reference | `claims.schema.json` and `tasks.schema.json` | Links claim extraction and task design back to the safety-policy intake decision |
| `reviewer_id` or `reviewer_role` | `decision_summary.schema.json` | Records who held decision authority |
| `decision_timestamp` | `decision_summary.schema.json` | Separates run time from approval time |
| `source_version` | `claims.schema.json` | Handles mutable online sources and preprint updates |
| `retrieved_at` | `claims.schema.json` | Records when volatile source material was captured |
| `translation_verdict` | `decision_summary.schema.json` | Standardizes positive, conditional, and negative outcomes |
| `abstention_reason` | `run_output.schema.json` | Makes abstention analytically useful |
| `claim_ids` | `tasks.schema.json` | Links each task to specific claims rather than a claims file only |
| `risk_boundary` | `agent_spec.schema.json` or `tasks.schema.json` | Names where the task must stop |

These additions would strengthen audit reconstruction. They should be introduced deliberately, with migration notes.

---

## Review Checklist

Before accepting a schema-bound artifact, ask:

- Does the artifact validate against its schema?
- Does it point to the upstream artifact it depends on?
- Does it preserve the difference between source, claim, task, output, and decision?
- Does it make abstention, error, or rejection visible?
- Does it support a later reviewer reconstructing the decision path?
- Does it avoid giving raw model output final authority?
- Does the confidence label match the evidence quality?
- Does the rationale explain the decision rather than merely restating it?

A schema-valid artifact can still be methodologically weak. Schema validation is the floor, not the final review.

---

## Directory Structure

```text
schemas/
├── README.md
├── agent_spec.schema.json
├── claims.schema.json
├── decision_summary.schema.json
├── run_input.schema.json
├── run_output.schema.json
├── safety_policy_intake.schema.json
└── tasks.schema.json
```

---

## Status

The current schema layer establishes the minimum artifact contracts required for governed research translation. It is intentionally small. Its purpose is to make the decision path inspectable without turning the repository into a full governance platform.

The schema standard is direct: every artifact should help a later reviewer reconstruct what source was used, what safety-policy boundary was assigned, what claim was made, what task was authorized, what output was produced, and what decision was recorded.
