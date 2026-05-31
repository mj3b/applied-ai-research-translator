# Human Gate

The human gate is the control point where model-produced or system-produced material becomes a human-authorized decision artifact. It preserves the boundary between AI-generated evidence and institutional authority.

The model can propose. The human reviewer decides.

---

## Purpose

The human gate exists because schema-valid output can still be wrong, unsupported, overbroad, unsafe, or institutionally unauthorized.

| Without Human Gate | With Human Gate |
|---|---|
| Model output can become final by default | Model output remains proposed evidence |
| Approval may be implicit | Approval is recorded |
| Override rationale may be lost | Override becomes a documented decision |
| Rejection may disappear | Rejection is preserved as an outcome |
| Accountability may diffuse into the system | Accountability remains assigned to a reviewer |

The human gate does not make the system safe by itself. It creates the decision record required for accountability.

---

## Decision States

| State | Meaning | Required Record |
|---|---|---|
| `accept` | Reviewer accepts the proposed output as final | Reviewer identity or role, timestamp, rationale |
| `override` | Reviewer modifies the proposed output | Original proposal, revised output, reason for override |
| `reject` | Reviewer rejects the proposed output | Rejection reason and downstream stop condition |
| `abstain` | Reviewer cannot decide under current evidence | Missing evidence, authority gap, or escalation requirement |

The current implementation centers accept, override, and reject. `abstain` is recommended for future schema expansion where reviewer uncertainty needs more explicit treatment.

---

## What the Human Reviewer Is Responsible For

A reviewer should assess whether the proposed output is adequate under the task boundary, evaluation plan, and institutional context.

| Reviewer Question | Reason |
|---|---|
| Does the output answer the bounded task? | Prevents scope drift |
| Does the output cite or preserve required evidence? | Prevents unsupported finalization |
| Does the output respect constraints and failure conditions? | Preserves task containment |
| Does the output overstate confidence? | Preserves calibration |
| Does the output require expertise or authority the reviewer lacks? | Prevents invalid approval |
| Should the result be accepted, overridden, rejected, or escalated? | Assigns decision responsibility |

The reviewer is not merely checking grammar or formatting. The reviewer holds the decision boundary.

---

## Accept

Accept means the proposed output becomes final under the declared task boundary.

Use accept when:

| Condition | Requirement |
|---|---|
| Output matches task scope | No unauthorized expansion |
| Required evidence is present | Source or artifact support exists |
| Evaluation criteria are satisfied | Acceptance conditions are met |
| Confidence is calibrated | Confidence matches evidence strength |
| Limitations are recorded | Remaining uncertainty is visible |

An accepted output should still carry limitations and conditions where relevant.

---

## Override

Override means the reviewer changes the proposed output before finalization.

Use override when:

| Condition | Example |
|---|---|
| Output is structurally valid but substantively incomplete | Reviewer adds missing limitation or evidence caveat |
| Output overstates confidence | Reviewer lowers confidence from high to medium |
| Output misses a boundary condition | Reviewer adds scope constraint |
| Output contains a minor factual error | Reviewer corrects the field and records the correction |
| Output requires institutional phrasing | Reviewer updates final wording while preserving evidence |

Override should preserve both the original proposal and the reviewer’s reason. Otherwise the audit trail loses the most important decision.

---

## Reject

Reject means the proposed output should not become final.

Use reject when:

| Condition | Reason |
|---|---|
| Output violates task constraints | The run exceeded its authorized boundary |
| Evidence is missing | The result cannot support a decision |
| Source grounding is weak | Claim or output cannot be reconstructed |
| Confidence is unjustified | The result overstates certainty |
| Output implies unauthorized action | The model is crossing from evidence into authority |
| Reviewer lacks required authority | Approval would be institutionally invalid |

Reject should stop downstream use unless a new source, task, evaluation plan, or review authority is established.

---

## Abstain or Escalate

Some decisions require a fourth state: abstain or escalate.

Use abstain or escalation when:

| Condition | Governance Response |
|---|---|
| Evidence is incomplete | Request additional evidence |
| Domain expertise is missing | Escalate to qualified reviewer |
| Risk level exceeds the pack | Escalate to governance, security, legal, ethics, or domain authority |
| Source rights are unclear | Escalate for legal or licensing review |
| Output affects consequential decisions | Require institutional review |

A future schema version should represent this state explicitly. For v1.1, these cases can be recorded in decision-summary notes or rejection rationale.

---

## Human Gate Record

A strong human-gate record includes:

| Field | Function |
|---|---|
| Reviewer identity or role | Assigns decision authority |
| Decision state | Accept, override, reject, or abstain |
| Timestamp | Separates generation time from authorization time |
| Proposed output reference | Links the decision to the system output |
| Final output reference | Shows what became final |
| Rationale | Explains the decision |
| Conditions | Records constraints on use |
| Uncertainty | Names what remains unresolved |

Reviewer identity can be role-based when privacy or institutional policy requires it.

---

## Human Gate as Accountability Architecture

The human gate works because it separates three layers:

| Layer | Actor | Function |
|---|---|---|
| Evidence generation | AI system or runtime | Produces candidate output under schema and task constraints |
| Judgment | Human reviewer | Assesses adequacy, risk, scope, and authority |
| Record | Decision summary | Preserves the final decision and rationale |

A system that merges these layers cannot support meaningful accountability.

---

## Common Failure Modes

| Failure Mode | Consequence |
|---|---|
| Reviewer accepts without rationale | Decision cannot be defended later |
| Reviewer overrides without preserving original output | Audit trail loses the comparison point |
| Reviewer lacks authority | Approval may be invalid |
| Human gate occurs after downstream action | Review becomes retrospective justification |
| Model writes final rationale | Decision narrative may launder model assumptions |
| Rejection is treated as an exception | System becomes biased toward approval |

These failures turn human review into ceremony. The repository is designed to make review substantive.

---

## Review Checklist

Before finalizing a human-gate decision, the reviewer should be able to answer:

- What was the proposed output?
- What task authorized it?
- What source and claim supported the task?
- What evidence supports acceptance?
- What limitation remains?
- What decision state is being recorded?
- What rationale explains the decision?
- Does the reviewer have authority to make this decision?

The gate closes only when these answers are visible.

---

## Design Standard

The human gate succeeds when a later reviewer can distinguish model output from human authorization.

That distinction is the accountability boundary.
