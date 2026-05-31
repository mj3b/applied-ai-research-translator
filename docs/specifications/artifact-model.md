# Artifact Model

A governed research translation system needs stable artifacts at each point where judgment changes form. Source material becomes claims. Claims become tasks. Tasks become run inputs. Run outputs become proposed evidence. Proposed evidence becomes a human-authorized decision summary.

The artifact model prevents those steps from collapsing into a single informal act of interpretation.

---

## Core Principle

Each artifact answers one governance question.

| Artifact | Governance Question |
|---|---|
| Source material | What material was used as the basis for translation? |
| Claim record | What did the source actually support? |
| Task definition | What bounded operation follows from the selected claim? |
| Evaluation plan | What evidence would count as success, failure, abstention, or rejection? |
| Run input | What information entered the governed run? |
| Run output | What did the system produce before human authorization? |
| Human-gate record | Who accepted, overrode, or rejected the proposed output? |
| Decision summary | What final decision was recorded and why? |

The model is intentionally conservative. It makes intermediate judgments visible before they become operational commitments.

---

## Artifact Chain

```text
sources/paper_text.txt
  ↓
claims.json
  ↓
tasks.json
  ↓
eval_plan.json
  ↓
run_input.json
  ↓
run_output.json or proposed.json
  ↓
human_gate.json
  ↓
final.json
  ↓
decision_summary.json
```

Not every development pack will contain every artifact. A decision-complete pack should contain enough of the chain for a reviewer to reconstruct the decision without relying on informal memory.

---

## Source Material

Source material is the preserved input to translation. It may be a paper excerpt, PDF text, report text, repository description, benchmark writeup, or other research-derived material.

| Requirement | Reason |
|---|---|
| Preserve the text or excerpt used for translation | Lets reviewers inspect what the translator saw |
| Record source location where available | Supports citation, retrieval, and version control |
| Record source caveats | Distinguishes peer-reviewed work, preprints, vendor claims, blogs, and mutable web sources |
| Treat external material as untrusted input | Reduces prompt injection, source poisoning, and overclaiming risk |

The source material does not carry decision authority by itself. It supplies evidence for the next artifact.

---

## Claim Record

The claim record decomposes the source into statements that can be assessed. A claim should be specific enough to test, reject, or use in task design.

| Claim Property | Required Function |
|---|---|
| `claim_id` | Allows later artifacts to reference the claim |
| Claim text | States the extracted proposition |
| Evidence reference | Links the claim to source material |
| Scope | Names where the claim applies |
| Assumptions | Names the conditions required for the claim to hold |
| Failure modes | Names how translation could fail |
| Testability | Indicates whether the claim can become a bounded task |

A weak claim record usually overgeneralizes. A strong claim record narrows the research source until a task boundary becomes inspectable.

---

## Task Definition

The task definition converts a selected claim into a bounded operational unit. It should define what the system may receive, produce, and decline.

| Task Element | Governance Function |
|---|---|
| Task ID | Supports traceability |
| Linked claim | Prevents ungrounded task creation |
| Inputs | Defines what information may enter the run |
| Outputs | Defines what the run may produce |
| Constraints | Prevents scope expansion |
| Failure conditions | Preserves abstention and rejection |
| Human-gate requirement | Preserves institutional authority |
| Evaluation link | Prevents informal quality judgment |

A task that cannot define inputs, outputs, constraints, and review conditions should remain below execution maturity.

---

## Evaluation Plan

The evaluation plan defines the test before the run occurs. It is the control that prevents post-hoc rationalization.

| Evaluation Element | Function |
|---|---|
| Metrics | Defines what will be assessed |
| Acceptance criteria | Defines what would count as sufficient output |
| Failure criteria | Defines what would require rejection or abstention |
| Reviewer questions | Defines what the human reviewer must judge |
| Confidence criteria | Defines how certainty should be assigned |
| Limitation notes | Defines what the evaluation cannot settle |

The evaluation plan does not need to be complex. It needs to be declared before the output is interpreted.

---

## Run Input

Run input records the actual material processed in a governed run. It should be treated as evidence.

| Requirement | Reason |
|---|---|
| Link to pack ID | Preserves research context |
| Link to task ID | Preserves task authorization |
| Record creation time | Supports chronology |
| Preserve input payload | Supports reproducibility |
| Avoid sensitive data unless approved | Reduces security and privacy exposure |

A run output cannot be evaluated responsibly when the input is missing.

---

## Run Output

Run output records the system result before final human authorization. It remains intermediate.

| Status | Meaning |
|---|---|
| `ok` | The system produced schema-valid output |
| `abstained` | The system declined or failed under the defined boundary |
| `error` | The run failed technically or structurally |

A schema-valid run output is eligible for review. It is not a decision.

---

## Human-Gate Record

The human-gate record captures the moment where institutional authority enters the process.

| Decision | Meaning |
|---|---|
| `accept` | Reviewer accepts the proposed output |
| `override` | Reviewer changes the proposed output and records the reason |
| `reject` | Reviewer rejects the proposed output and records the reason |

The human-gate record should make reviewer judgment visible enough that a later reader can understand why the model output was accepted, changed, or rejected.

---

## Decision Summary

The decision summary is the final audit-facing artifact. It should state the verdict, rationale, confidence, evidence basis, uncertainty, and any conditions.

| Field | Function |
|---|---|
| Decision | Records the final outcome |
| Rationale | Explains why the decision was made |
| Confidence | Calibrates the strength of the decision |
| Evidence | Links the decision to artifacts |
| Uncertainty | Names what remains unsettled |
| Conditions | Records required constraints for continuation |
| Rejection basis | Explains why translation stopped, when applicable |

The decision summary should be readable by someone who has not run the code.

---

## Maturity Levels

| Level | Name | Artifact Requirement |
|---:|---|---|
| 0 | Scaffold | Partial specification or example artifact |
| 1 | Source-captured | Source material is preserved |
| 2 | Claim-complete | Claims are extracted and source-linked |
| 3 | Task-bound | Tasks are defined with inputs, outputs, and constraints |
| 4 | Evaluation-ready | Evaluation plan is declared before execution |
| 5 | Decision-complete | Human decision and decision summary are present |

A pack should be labeled according to the lowest missing artifact in the chain.

---

## Design Standard

The artifact model succeeds when a skeptical reviewer can reconstruct five things:

1. What source was used.
2. What claim was extracted.
3. What task was authorized.
4. What evidence was produced.
5. What decision was recorded.

Anything else is supporting material.
