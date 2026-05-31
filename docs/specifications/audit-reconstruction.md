# Audit Reconstruction

Audit reconstruction is the ability to inspect a completed translation and determine what source was used, what claim was extracted, what task was authorized, what output was produced, what human decision was made, and why.

A governed system should leave enough evidence that a later reviewer can reconstruct the decision without interviewing the original author.

---

## Reconstruction Question

The central audit question is:

```text
How did this research source become this decision?
```

The repository answers that question through linked artifacts rather than narrative memory.

---

## Reconstruction Chain

```text
source material
  ↓
claim record
  ↓
task definition
  ↓
evaluation plan
  ↓
run input
  ↓
run output or proposed output
  ↓
human-gate record
  ↓
final output
  ↓
decision summary
```

Each artifact should answer a different part of the audit question.

---

## Audit Questions by Artifact

| Artifact | Audit Question | Failure Signal |
|---|---|---|
| `sources/paper_text.txt` | What source material was used? | Source text missing or unclear |
| `claims.json` | What claims were extracted from the source? | Claims too broad, unsupported, or source-free |
| `tasks.json` | What bounded task was authorized? | Task lacks input, output, constraint, or claim link |
| `eval_plan.json` | How was success or failure defined? | Evaluation criteria absent or post-hoc |
| `run_input.json` | What entered the run? | Input missing or cannot be reproduced |
| `run_output.json` or `proposed.json` | What did the system produce? | Output missing, malformed, or unsupported |
| `human_gate.json` | Who accepted, overrode, or rejected the output? | Human decision absent or ceremonial |
| `final.json` | What became final? | Final output cannot be distinguished from proposed output |
| `decision_summary.json` | What decision was recorded and why? | Rationale, confidence, or verdict missing |

The more links that are missing, the more the decision depends on trust in the author rather than evidence.

---

## Minimum Reconstructable Record

A pack or run is minimally reconstructable when it contains:

| Required Item | Why It Matters |
|---|---|
| Source reference or captured source text | Establishes provenance |
| Extracted claim or stated translation basis | Shows what was taken from the source |
| Bounded task or rejection basis | Shows how the source was operationalized or stopped |
| Evaluation criteria or reason evaluation was unavailable | Shows how judgment was structured |
| Proposed output or abstention record | Shows what the system produced or declined |
| Human decision or documented absence of human decision | Shows where authority entered |
| Decision summary | Provides the final audit-facing artifact |

A record can be transparent about incompletion. Hidden incompletion is the problem.

---

## Decision Summary as Audit Artifact

The decision summary should allow a reviewer to understand the outcome quickly.

| Field | Audit Function |
|---|---|
| `decision` | Names the outcome |
| `confidence` | Calibrates the outcome |
| `rationale` | Explains the decision |
| `evidence` | Links decision to artifacts |
| `conditions` | Constrains any permitted use |
| `limitations` | Names unresolved questions |
| `rejection_basis` | Explains why translation stopped, where applicable |

The decision summary should avoid persuasive language. Its job is reconstruction.

---

## Traceability Defects

Traceability defects are gaps that weaken reconstruction.

| Defect | Description | Risk |
|---|---|---|
| Missing source | Source material cannot be inspected | Claims cannot be verified |
| Orphaned claim | Claim lacks source support | Research interpretation becomes opaque |
| Orphaned task | Task lacks claim link | Operationalization may be ungrounded |
| Missing evaluation plan | Success was defined after output | Post-hoc rationalization |
| Missing run input | Output cannot be reproduced | Review depends on memory |
| Missing proposed output | Human decision cannot be compared to system output | Override or acceptance cannot be inspected |
| Missing human gate | Model output may have become final by default | Accountability failure |
| Missing rationale | Decision exists without explanation | Audit record is incomplete |
| Overbroad confidence | Decision certainty exceeds evidence | Reviewer may overtrust result |

A traceability defect does not always invalidate a pack. It should be disclosed.

---

## Reconstruction Procedure

A reviewer can reconstruct a pack in this order.

| Step | Action | Evidence |
|---:|---|---|
| 1 | Identify pack ID and maturity level | Pack directory, `packs/README.md` |
| 2 | Inspect source material | `sources/paper_text.txt` |
| 3 | Review extracted claims | `claims.json` |
| 4 | Check claim-to-task linkage | `tasks.json` |
| 5 | Review evaluation plan | `eval_plan.json` |
| 6 | Inspect run artifacts, where present | Run logs, input, output, proposed artifacts |
| 7 | Inspect human-gate decision, where present | `human_gate.json` or decision-summary notes |
| 8 | Read final decision summary | `decision_summary.json` |
| 9 | Compare verdict to evidence | All upstream artifacts |
| 10 | Record remaining uncertainty | Limitation notes or review memo |

This procedure should work even when the reviewer disagrees with the verdict.

---

## Reconstruction of Negative Translation

Negative translation requires the same discipline as positive translation.

For a rejection, the reviewer should reconstruct:

| Question | Evidence |
|---|---|
| What source was considered? | Source material |
| What claim triggered interest? | Claim record |
| What task boundary failed? | Task record or rejection rationale |
| What governance boundary was exceeded? | Evaluation plan, governance notes, decision summary |
| Why did operationalization stop? | Rejection verdict |
| What research value remains? | Decision-summary notes or pack documentation |

A rejection without an evidence trail looks like preference. A rejection with traceability is governance.

---

## Audit Maturity Levels

| Level | Name | Audit Capability |
|---:|---|---|
| 0 | Informal | Reviewer depends on author explanation |
| 1 | Source-visible | Reviewer can inspect source material |
| 2 | Claim-visible | Reviewer can inspect extracted claims |
| 3 | Task-visible | Reviewer can inspect operationalization boundary |
| 4 | Evidence-visible | Reviewer can inspect run or evaluation evidence |
| 5 | Decision-visible | Reviewer can inspect human decision and final summary |
| 6 | Reconstruction-complete | Reviewer can trace source to decision without external explanation |

The repository’s v1.1 goal is to make mature packs approach Level 6.

---

## Common Reviewer Findings

| Finding | Interpretation |
|---|---|
| The verdict is supported by artifacts | Decision path is reconstructable |
| The verdict is plausible but evidence is thin | Pack may remain useful with disclosed limits |
| Source supports claims but task is weak | Translation should stop or return to task design |
| Task is bounded but evaluation is weak | Pack should remain below execution maturity |
| Run output is valid but human gate is missing | Output should remain intermediate |
| Human decision exists but rationale is weak | Decision summary needs revision |
| Negative verdict is well supported | Governance boundary is functioning |

The audit record should make disagreement precise. That is the value of reconstruction.

---

## Design Standard

Audit reconstruction succeeds when the final decision can be challenged at the right point: source, claim, task, evaluation, output, human gate, or summary.

A reviewer should never have to guess where the decision happened.
