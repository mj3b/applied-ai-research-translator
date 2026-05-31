# Governance Model

Applied AI research becomes risky when the translation path from source material to institutional action is invisible. A paper, PDF, report, benchmark, or repository can influence a decision long before anyone has recorded which claim was used, what assumption carried the claim, what task was derived from it, what evidence was produced, who reviewed the output, and why the resulting decision was authorized.

This repository treats that translation path as the governed object.

The governance model is built around one constraint: AI-generated outputs may produce evidence inside a bounded workflow, while final decision authority remains assigned to a human decision record. The model therefore governs the path from research source to decision artifact, rather than treating governance as a policy note around a model call.

---

## 1. Governance Thesis

Research translation is a decision system. It takes external knowledge, interprets it, operationalizes it, and turns it into a proposed course of action. That system needs controls because each translation step can introduce error, overreach, ambiguity, or unsupported authority.

| Governance Question | Repository Control | Resulting Artifact |
|---|---|---|
| What source material informed the decision? | Source capture and pack structure | `sources/paper_text.txt` |
| Which claims were extracted? | Claim schema and claim typing | `claims.json` |
| Which claims were considered operationalizable? | Translation screening and verdict logic | `decision_summary.json` |
| What task was derived from the claim? | Locked task definition | `tasks.json` |
| What evidence was produced during execution? | Runloop artifact logging | `candidates.jsonl`, `proposed.json` |
| What conditions triggered abstention or review? | Schema validation and task constraints | run logs, validation results |
| Who authorized the final output? | Human gate | `human_gate.json` |
| How can the decision be reconstructed later? | Deterministic decision summary | `decision_summary.json` |

The system’s core contribution is the governed chain itself: source → claim → task → run → human gate → decision summary.

---

## 2. Scope of Governance

The model governs research-to-decision translation. It does this for source material that may come from academic, technical, institutional, or web-based contexts.

| Source Type | Governed Concern | Control Applied |
|---|---|---|
| Peer-reviewed papers | Claims may depend on population, dataset, benchmark, or experimental condition | Claims are extracted and tied to evidence before task design |
| Preprints | Findings may shift after revision, review, or replication | Version, source text, and uncertainty are preserved in the pack |
| PDFs and reports | Narrative recommendations may mix evidence with institutional position | Evidence claims are separated from operational claims |
| Technical blogs | Useful implementation detail may lack formal review | Translation depends on task containment and human review |
| Vendor publications | Incentives may shape evidence selection and adoption framing | Source type remains visible in the decision trail |
| GitHub repositories | Code may differ from paper claims or lack reproducibility evidence | Implementation claims require separate validation |
| Standards and guidance | Governance requirements may lack computable implementation detail | Requirements are translated into controls, evidence fields, and review criteria |

The model does **not** claim that every source can become a governed task. Some sources should remain background evidence. Some should produce a rejection decision. Some may require human review before task design begins.

---

## 3. Governed Execution Model

The system uses AI only inside bounded execution. The AI component can generate candidate evidence. It cannot approve its own output, expand the task, change the decision standard, or write the final institutional record.

```text
Research source
  ↓
Claim extraction
  ↓
Operationalization review
  ↓
Locked task definition
  ↓
Governed runloop
  ↓
Schema validation
  ↓
Human gate
  ↓
Decision summary
```

| Layer | AI Role | Governance Boundary | Human Authority |
|---|---|---|---|
| Source review | Assist with claim extraction | Source text and provenance remain preserved | Researcher or reviewer determines source relevance |
| Claim formation | Propose structured claims | Claims must validate against schema | Reviewer decides whether claims are admissible |
| Task design | Support task derivation | Task boundary must be locked before execution | Reviewer owns task acceptance |
| Runtime execution | Generate bounded candidate outputs | Output must conform to schema and constraints | Reviewer decides whether output can proceed |
| Final decision | No final authority | Decision summary is assembled from logged artifacts | Human gate records accept, override, or reject |

This division prevents model output from becoming institutional authorization by default.

---

## 4. Control Architecture

The governance model uses file-level controls rather than informal review. Each file type carries a specific accountability function.

| Control Layer | File or Directory | Governance Function |
|---|---|---|
| Source provenance | `packs/<pack_id>/sources/` | Preserves the material used for translation |
| Claim discipline | `claims.json` | Records claims, evidence references, scope, and operationalization status |
| Task containment | `tasks.json` | Defines inputs, outputs, constraints, failure conditions, and review points |
| Evaluation planning | `eval_plan.json` | Establishes success criteria before run outputs appear |
| Schema enforcement | `schemas/` | Converts governance requirements into machine-checkable contracts |
| Runtime logging | `runloop/` | Creates a traceable record of execution |
| Human authorization | `human_gate.json` | Records the decision made by the reviewer |
| Final artifact | `decision_summary.json` | Provides the audit-facing reconstruction record |

The repository uses architecture to force the governance sequence. A reviewer should be able to inspect the final decision summary and trace the decision back to source material and intermediate artifacts.

---

## 5. Authority Boundary

The central boundary is between evidence production and decision authority.

AI output is treated as candidate evidence. Human review determines whether the candidate evidence is accepted, overridden, or rejected. The final artifact records that decision.

| Activity | Evidence Production | Decision Authority |
|---|---:|---:|
| Extract candidate claims from source text | AI-assisted | Human-reviewed |
| Determine whether a claim is admissible | Supported by schema | Human-owned |
| Convert a claim into a task | AI-assisted | Human-approved |
| Generate candidate outputs | AI-assisted | Human-reviewed |
| Resolve schema or constraint failures | Logged by system | Human-owned |
| Accept final output | No | Human-owned |
| Override final output | No | Human-owned |
| Reject translation or execution | No | Human-owned |
| Produce audit record | Deterministic assembly | Human-authored decision fields |

The governance model therefore assigns responsibility to an accountable reviewer at the point where research becomes operational recommendation.

---

## 6. Human Gate

The human gate is the system’s primary authority control. It prevents candidate output from becoming final output without an explicit decision.

| Gate Outcome | Meaning | Required Record |
|---|---|---|
| `accept` | The reviewer accepts the proposed output as final | Reviewer identity, timestamp, rationale |
| `override` | The reviewer modifies or replaces the proposed output | Reviewer identity, override content, rationale |
| `reject` | The reviewer rejects the proposed output or translation path | Reviewer identity, rejection basis, decision effect |
| `abstain` | The system or reviewer declines to proceed under current evidence | Failure condition, uncertainty, required next evidence |

The human gate creates a reconstruction point. It shows the proposed output, the human action, and the reason the final decision took its recorded form.

---

## 7. Abstention Model

A governed translation system must be able to stop. This repository treats abstention as a valid output, not as a failure of the workflow.

| Abstention Trigger | Why It Matters | Expected System Behavior |
|---|---|---|
| Source ambiguity | The source does not support a stable claim | Record uncertainty and halt claim promotion |
| Missing evidence | The claim lacks adequate support in the source text | Reject or mark claim as unready |
| Task overreach | The task requires autonomy or open-ended action outside the system boundary | Produce translation-negative verdict |
| Schema failure | Output fails required structure | Halt before human gate or require correction |
| Constraint violation | Output exceeds defined task bounds | Record failure and prevent finalization |
| Review uncertainty | Human reviewer cannot authorize the output on available evidence | Record abstention and required evidence |

The ability to halt is part of the governance contribution. A system that always produces an implementation path functions as an adoption mechanism rather than a control system.

---

## 8. Translation Verdicts

Translation verdicts classify the relationship between a research source and an operational pathway.

| Verdict | Governance Meaning | Typical Use |
|---|---|---|
| `translation_positive` | A source claim can be converted into a bounded task with evidence, constraints, and human review | Measurement, classification, review, or evaluation tasks |
| `translation_negative` | The research contribution cannot be safely bounded within the system’s control surface | Autonomous multi-agent coordination, open-ended deployment, unverifiable causal claims |
| `approve_with_conditions` | Execution may proceed only under specified constraints | Human-reviewed outputs with limited downstream use |
| `reject_translation` | The source may remain useful as research evidence while being excluded from operationalization | Claims requiring authority, autonomy, or evidence beyond the repository boundary |

Negative translation is an intended governance result. It shows that the system can preserve the distinction between research relevance and operational readiness.

---

## 9. Audit Reconstruction

The model supports post-hoc reconstruction by requiring every decision to leave an artifact trail.

```text
Source material
  └── evidence extracted into claims
        └── claims selected or rejected for operationalization
              └── tasks defined before execution
                    └── model candidates generated under constraints
                          └── proposed output validated
                                └── human gate recorded
                                      └── final decision summary assembled
```

| Reconstruction Question | Evidence Location |
|---|---|
| What was the original source? | `sources/paper_text.txt` |
| What claims were extracted? | `claims.json` |
| Which claim became a task? | `tasks.json` |
| What evaluation standard was applied? | `eval_plan.json` |
| What did the model produce? | `candidates.jsonl`, `proposed.json` |
| Did the output validate? | schema validation logs |
| What did the reviewer decide? | `human_gate.json` |
| What is the final decision record? | `decision_summary.json` |

An audit-ready decision record should allow a reviewer to reconstruct the chain without relying on memory, Slack messages, or a model-generated explanation.

---

## 10. Governance Failure Modes

The repository is designed around specific failure modes in AI-assisted research translation.

| Failure Mode | Description | Control |
|---|---|---|
| Source laundering | A weak or unstable source gains authority because it appears in a research workflow | Preserve source type, source text, and provenance |
| Claim inflation | A narrow finding becomes a broad operational recommendation | Require claim extraction and operationalization review |
| Context collapse | Study conditions disappear during task design | Record assumptions, scope, and translation limits |
| Task drift | The task expands after model output appears | Lock task definitions before execution |
| Model authority creep | Candidate output becomes final decision by convenience | Require human gate before finalization |
| Evidence ambiguity | Reviewers cannot tell which evidence supports which decision | Use traceable artifacts and decision summaries |
| Negative-result suppression | Failed translations disappear from the record | Treat rejection and abstention as recorded outcomes |
| Audit failure | The organization cannot reconstruct why a research-based action was authorized | Assemble deterministic decision summaries |

The model treats these failure modes as design constraints. The repository’s architecture exists to make each one harder to hide.

---

## 11. Institutional Use Cases

The governance model supports several institutional review patterns.

| Use Case | Governance Need | Repository Fit |
|---|---|---|
| AI governance research | Study how research claims become controlled decision artifacts | Strong fit |
| AI safety evaluation | Examine how autonomy, task containment, and human oversight are enforced | Strong fit |
| Policy translation | Convert standards or guidance into operational evidence requirements | Strong fit |
| Internal AI adoption review | Evaluate whether a paper-backed idea should become an implementation task | Strong fit |
| Vendor claim review | Separate vendor evidence from adoption authority | Strong fit |
| Autonomous deployment approval | Requires controls beyond this repository’s current boundary | Out of scope |
| Production system certification | Requires organizational controls, access management, monitoring, and legal review beyond this artifact | Out of scope |

The repository is best understood as a research-to-decision governance artifact. It can support institutional review, but it does not replace institutional authority.

---

## 12. Relationship to AI Governance and AI Safety

This governance model sits at the intersection of AI governance, AI safety, research operations, and institutional accountability.

| Field | Relationship |
|---|---|
| AI governance | Provides controls for translating AI research into decision records |
| AI safety | Blocks unbounded autonomy and preserves abstention for unsafe or unsupported translations |
| Responsible AI | Assigns human authority and preserves evidence for review |
| Research operations | Converts source material into structured, inspectable artifacts |
| Audit and compliance | Produces records that can be reconstructed after the decision |
| Institutional decision-making | Separates research evidence from authorization |

The model’s practical claim is narrow: institutions need a controlled path between research intake and operational action. This repository implements one reference pattern for that path.

---

## 13. Design Commitments

| Commitment | Implementation |
|---|---|
| Research claims require provenance | Source material is stored with the pack |
| Operational tasks require containment | Tasks define boundaries before execution |
| AI output remains intermediate | Human gate must finalize or reject output |
| Rejection is a valid result | Translation-negative packs remain part of the repository |
| Governance must be inspectable | Artifacts are structured and schema-validated |
| Audit records should be deterministic | Decision summaries are assembled from logged artifacts |
| Institutional authority must remain human | Final decision state belongs to the reviewer |

These commitments define the governance model. They are intentionally conservative because the repository operates at the point where research can become action.

---

## 14. Current Limits

This repository governs translation artifacts and bounded AI-assisted runs. It does not provide a complete enterprise AI governance program.

| Limit | Reason |
|---|---|
| No production access control model | The repository is research software, not an enterprise platform |
| No continuous monitoring layer | The system governs discrete translation runs |
| No legal review workflow | Legal authority remains outside the repository |
| No automated source credibility scoring | Source evaluation requires human judgment |
| No autonomous multi-agent execution | The governance boundary excludes open-ended coordination |
| No claim of universal research validity | The method governs translation, not truth itself |

These limits are deliberate. The system governs the path from research artifact to decision record. Enterprise deployment requires additional organizational controls.

---

## 15. Summary

The Applied AI Research Translator implements governance at the research translation layer. It captures source material, extracts claims, tests operationalizability, locks task boundaries, validates outputs, requires human authorization, and produces decision summaries that can be reconstructed later.

The model’s strongest property is refusal capacity. It can convert research into a bounded task when the governance record supports that path. It can also reject translation when the source claim requires autonomy, authority, evidence, or operational scope beyond the system boundary.
