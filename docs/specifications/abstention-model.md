# Abstention Model

Abstention is a governance control. It is the system’s ability to stop when source evidence, task boundaries, schema validation, output quality, or human review conditions fail.

A system that cannot abstain will convert uncertainty into action.

---

## Core Principle

The repository should stop before a research artifact becomes operationally misleading.

```text
uncertain source
  ↓
weak claim
  ↓
unbounded task
  ↓
schema failure
  ↓
unsupported output
  ↓
human rejection
```

Any step in this chain can trigger abstention or rejection. That is intentional.

---

## Abstention Types

| Abstention Type | Trigger | Artifact Where It Should Appear |
|---|---|---|
| Source abstention | Source material is unavailable, unstable, weakly cited, or unusable | Claim record or decision summary |
| Claim abstention | Claims are too broad, vague, normative, or unsupported | `claims.json`, decision summary |
| Task abstention | The claim cannot be converted into bounded inputs, outputs, and constraints | `tasks.json`, decision summary |
| Evaluation abstention | Success and failure cannot be defined before execution | `eval_plan.json`, decision summary |
| Runtime abstention | The governed run cannot produce valid output under schema or task conditions | Run output or proposed artifact |
| Human-gate abstention | The reviewer cannot accept or override because evidence is insufficient | `human_gate.json`, decision summary |
| Translation rejection | The source should not be operationalized under the repository’s governance boundary | `decision_summary.json` |

Abstention should be recorded with a reason. A silent stop is hard to audit.

---

## Source-Level Abstention

Source-level abstention occurs before claim extraction or during claim review.

Use it when:

| Condition | Reason |
|---|---|
| Source text cannot be preserved | Later reviewers cannot reconstruct the basis for extraction |
| Source version is unstable | Web or preprint content may change after translation |
| Source license is unclear | Pack redistribution may create rights or compliance issues |
| Source contains embedded instructions | Prompt injection or source poisoning risk may affect translation |
| Source is too thin | Claims would depend on inference rather than evidence |

Source-level abstention does not say the source is worthless. It says the repository cannot responsibly translate it under current controls.

---

## Claim-Level Abstention

Claim-level abstention occurs when extracted claims cannot support task design.

Use it when a claim is:

| Claim Problem | Example |
|---|---|
| Too broad | “AI agents improve organizational productivity” |
| Too normative | “Systems should promote responsible AI” |
| Too underspecified | “The approach works better in practice” |
| Too dependent on hidden conditions | “The method generalizes across deployments” without deployment details |
| Too detached from source evidence | Claim reflects interpretation more than source text |
| Too difficult to test | No observable condition could confirm or falsify it |

A claim can remain in the pack as research context while being excluded from task design.

---

## Task-Level Abstention

Task-level abstention occurs when a claim cannot become a bounded task.

Use it when:

| Task Problem | Governance Risk |
|---|---|
| Inputs cannot be defined | The system may ingest uncontrolled or sensitive material |
| Outputs cannot be constrained | Model output may become open-ended recommendation or action |
| Failure conditions are undefined | The system has no principled stopping point |
| Task requires autonomous coordination | Accountability diffuses across agents |
| Review requires unstated expertise | Human gate becomes symbolic |
| Downstream action is implied | The task begins to authorize operational behavior |

Task-level abstention is especially important for agentic and multi-agent research.

---

## Evaluation-Level Abstention

Evaluation-level abstention occurs when the repository cannot define a pre-run test of output adequacy.

Use it when:

| Evaluation Problem | Consequence |
|---|---|
| Success criteria are ambiguous | Reviewer judgment becomes informal |
| Failure criteria are missing | Output can be rationalized after the fact |
| Confidence cannot be calibrated | Decision summary overstates certainty |
| Evidence requirement is unclear | Output may lack support |
| Metrics do not match the claim | Evaluation tests a different proposition |

The evaluation plan is a guard against post-hoc approval. If evaluation cannot be declared before output, abstention is appropriate.

---

## Runtime Abstention

Runtime abstention occurs during or after execution.

| Trigger | Required Response |
|---|---|
| Schema validation fails | Stop and record failure |
| Required evidence is missing | Abstain or route to human review |
| Output conflicts with task constraints | Reject proposed output |
| Confidence threshold is unmet | Abstain or require reviewer decision |
| Input lacks required fields | Stop before execution |
| Model output attempts unauthorized action | Reject and record boundary violation |

Runtime abstention should leave an artifact. A failure without a record cannot support audit reconstruction.

---

## Human-Gate Abstention

Human reviewers may also abstain.

Use human-gate abstention when:

| Condition | Reason |
|---|---|
| Reviewer lacks domain authority | The decision would exceed reviewer competence |
| Evidence is incomplete | Accept or override would be under-supported |
| Output is plausible but unverified | The decision needs independent review |
| Risk level exceeds repository scope | Higher institutional authority is required |
| Source limitations remain unresolved | Final decision would overstate certainty |

Human abstention is a valid governance outcome. It preserves accountability better than forced approval.

---

## Abstention vs. Rejection

| Outcome | Meaning | Use When |
|---|---|---|
| Abstention | The system or reviewer cannot proceed under current evidence or constraints | Missing evidence, validation failure, insufficient confidence |
| Rejection | The artifact should not proceed because it violates the governance boundary | Unbounded autonomy, poor provenance, invalid task, unsupported conclusion |
| Conditional approval | Proceed only under explicit constraints | Evidence supports narrow use with controls |
| Approval | Proceed within declared boundary | Evidence, task, evaluation, and human authority align |

Abstention leaves room for further evidence. Rejection records a boundary.

---

## Required Abstention Record

An abstention should include:

| Field | Purpose |
|---|---|
| Abstention point | Source, claim, task, evaluation, runtime, or human gate |
| Reason | Specific failure or uncertainty |
| Evidence | Artifact or source that triggered the stop |
| Required next step | What would be needed to proceed |
| Reviewer or system actor | Who or what triggered the abstention |
| Time | When the abstention occurred |

The minimum acceptable abstention record explains why the system stopped.

---

## Anti-Pattern: Forced Completion

Forced completion occurs when the workflow produces an output because it is expected to produce one.

Signals:

| Signal | Governance Concern |
|---|---|
| Output exists despite missing source evidence | Research authority is being inferred |
| Task has no failure condition | System cannot stop itself |
| Reviewer accepts without rationale | Human gate becomes ceremonial |
| Low confidence appears as an approved summary | Uncertainty is being laundered |
| Negative translation is avoided | The system is biased toward adoption |

The repository should prefer visible incompletion over false closure.

---

## Design Standard

The abstention model succeeds when the system can say, with evidence:

```text
This source may be useful, but this translation should stop here.
```

That sentence is a governance function.
