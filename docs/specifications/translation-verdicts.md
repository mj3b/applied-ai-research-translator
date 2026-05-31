# Translation Verdicts

A translation verdict determines whether a research source can become a bounded task under the repository’s governance controls. The verdict separates intellectual usefulness from operational readiness.

A paper can be valuable and still fail translation.

---

## Verdict Model

| Verdict | Meaning | Decision Implication |
|---|---|---|
| `translation_positive` | The source supports at least one bounded task under governance controls | Proceed to task design, evaluation planning, and controlled execution |
| `proceed_to_task_design` | The source appears suitable for task design, with remaining specification work | Continue translation, with limits recorded |
| `approve_with_conditions` | A task or output may proceed under specified constraints | Proceed only under recorded conditions |
| `translation_negative` | The source cannot become a bounded task under current controls | Preserve research value, stop operationalization |
| `reject_translation` | Translation should stop because scope, evidence, autonomy, or accountability limits are exceeded | Record rejection and prevent downstream use as an approved task |

A verdict is a governance artifact. It should be explained, linked to evidence, and preserved.

---

## Positive Translation

A positive verdict means the research source supports a bounded decision-support task. It does not mean the research claim is universally true or deployment-ready.

| Criterion | Positive Signal |
|---|---|
| Source grounding | Claim traces to identifiable source text |
| Falsifiability | Claim can be tested, contradicted, or evaluated |
| Scope control | Population, context, system, or workflow boundary is clear |
| Task containment | Inputs, outputs, and constraints can be defined |
| Evaluation fit | Success and failure can be declared before execution |
| Human review | A reviewer can accept, override, or reject the output |
| Audit reconstruction | The decision path can be reconstructed later |

Positive translation authorizes continued controlled work. It does not authorize production deployment.

---

## Conditional Approval

`approve_with_conditions` should be used when a task or output is useful only under explicit restrictions.

| Condition Type | Example |
|---|---|
| Scope condition | Valid only for document discrepancy review, not autonomous adjudication |
| Evidence condition | Requires source snippets for every proposed classification |
| Human-gate condition | Requires reviewer approval before final output |
| Abstention condition | Must abstain when confidence is low or evidence is incomplete |
| Security condition | Excludes confidential, personal, or regulated data |
| Evaluation condition | Requires manual review against pre-declared criteria |

The condition is part of the decision. A conditional approval without recorded conditions is under-specified.

---

## Negative Translation

A negative verdict means the source remains useful for analysis while failing operationalization under this repository’s control model.

| Failure Basis | Why It Blocks Translation |
|---|---|
| Open-ended autonomy | The system would need to act beyond bounded review |
| Multi-agent coordination | Accountability becomes distributed across interacting agents |
| Missing evaluation criteria | Review would depend on informal judgment |
| Weak provenance | Source cannot be reconstructed or verified |
| Scope ambiguity | Claim generalizes beyond the source evidence |
| Unverifiable assumptions | The task depends on conditions the reviewer cannot inspect |
| High-risk decision impact | Output could affect consequential decisions without adequate controls |

A negative verdict should be treated as evidence of governance function. The system is doing its job when it stops an unsafe or poorly bounded translation.

---

## Rejection Verdict

`reject_translation` is stronger than `translation_negative`. It records that operationalization should stop under the current governance boundary.

Use `reject_translation` when:

| Condition | Explanation |
|---|---|
| The task requires autonomous execution | The repository is designed for bounded decision-support workflows |
| The source cannot be decomposed into testable claims | The pack cannot support claim-level review |
| The evaluation method cannot be defined before execution | The output would be judged after the fact |
| The human gate would be symbolic | A reviewer could not meaningfully accept, override, or reject |
| The decision path cannot be reconstructed | The final artifact would be audit-weak |
| The use case requires legal, regulatory, clinical, or institutional authorization outside the repository | The repository cannot certify deployment authority |

A rejection verdict should include a rationale and the evidence that triggered the boundary.

---

## Verdict Assignment Workflow

```text
source captured
  ↓
claims extracted
  ↓
claims screened for testability
  ↓
task boundary evaluated
  ↓
evaluation feasibility checked
  ↓
human authority checked
  ↓
verdict assigned
```

The verdict should be assigned before execution. Execution should not be used to discover whether the task had a valid boundary.

---

## Verdict Evidence

Every verdict should preserve evidence in the decision summary.

| Evidence Type | Purpose |
|---|---|
| Source evidence | Shows what material supported the claim |
| Claim evidence | Shows which claim entered task design |
| Boundary evidence | Shows why the task was or was not containable |
| Evaluation evidence | Shows how success or failure could be judged |
| Human-gate evidence | Shows whether review authority was meaningful |
| Limitation evidence | Shows what remains unresolved |

A verdict without evidence becomes an opinion.

---

## Examples

| Pack | Verdict Pattern | Reason |
|---|---|---|
| `haic_reliance_review_59e257ff` | Positive translation pathway | Reliance behavior can be observed through bounded decision-support review and override behavior |
| `measuring_agents_in_production_a98e2ca8` | Positive translation candidate | Production measurement can be represented as monitoring, evidence coverage, and workflow-level evaluation |
| `multi_agent_failure_modes_e0228882` | `reject_translation` | The source’s primary concern requires autonomous multi-agent interaction that exceeds the repository’s bounded governance model |

The negative example is part of the method, not an edge case.

---

## Anti-Overclaiming Rules

| Verdict | Does Not Mean |
|---|---|
| `translation_positive` | The paper is proven, the system is safe, or deployment is approved |
| `proceed_to_task_design` | The task is ready to run |
| `approve_with_conditions` | The conditions can be ignored later |
| `translation_negative` | The source lacks scholarly value |
| `reject_translation` | The source should be discarded |

The verdict concerns translatability under this repository’s controls. It does not settle the full scholarly or operational value of the source.

---

## Reviewer Checklist

Before accepting a verdict, ask:

- Does the verdict follow from source-linked claims?
- Is the task boundary explicit?
- Are evaluation criteria declared?
- Is human authority meaningful?
- Is abstention or rejection available?
- Does the decision summary preserve the rationale?
- Does the verdict avoid claiming more than the evidence supports?

A strong verdict makes the next decision easier. A weak verdict hides the decision that matters.
