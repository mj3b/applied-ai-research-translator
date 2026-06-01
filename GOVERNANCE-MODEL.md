# Governance Model

Applied AI research becomes risky when the translation path from source material to institutional action is invisible. A paper, PDF, report, benchmark, repository, policy memo, or source artifact can influence a decision long before anyone has recorded which claim was used, what assumption carried the claim, what safety or policy risk was implicated, what task was derived, what evidence was produced, who reviewed the output, and why the resulting decision was authorized.

This repository treats that translation path as the governed object.

The governance model is built around one constraint: AI-generated outputs may produce evidence inside a bounded workflow, while final decision authority remains assigned to a human decision record. The model governs the path from research source to decision artifact, rather than treating governance as a policy note around a model call.

The v1.1.1 safety-policy intake gate strengthens that model by adding a first classification step for AI safety and policy sources before claim extraction, task design, or execution.

---

## 1. Governance Thesis

Research translation is a decision system. It takes external knowledge, interprets it, operationalizes it, and turns it into a proposed course of action. That system needs controls because each translation step can introduce error, overreach, ambiguity, unsafe authority, or unsupported operational confidence.

The core thesis is:

```text
Research usefulness is not operational authorization.
```

A source may be valuable for analysis. It may be suitable for claim extraction. It may be useful for evaluation design. It may belong only in policy mapping. It may require restricted handling. It may also deserve rejection under the repository boundary.

The governance model therefore separates five questions:

| Governance Question | Repository Control | Resulting Artifact |
|---|---|---|
| What source material informed the decision? | Source capture and pack structure | `sources/paper_text.txt` |
| What kind of source is this, and what authority should it carry? | Safety-policy intake, where applicable | `safety_policy_intake.json` |
| Which claims were extracted? | Claim schema and claim typing | `claims.json` |
| Which claims were considered operationalizable? | Translation screening and verdict logic | `tasks.json`, `decision_summary.json` |
| What task was derived from the claim? | Locked task definition | `tasks.json` |
| What evidence was produced during execution or review? | Runloop artifact logging | `candidates.jsonl`, `proposed.json`, run logs |
| What conditions triggered abstention, restriction, rejection, or review? | Schema validation, safety-policy intake, task constraints | validation logs, intake verdict, run logs |
| Who authorized the final output? | Human gate | `human_gate.json` |
| How can the decision be reconstructed later? | Deterministic decision summary | `decision_summary.json` |

The system’s core contribution is the governed chain itself:

```text
source → safety-policy intake → claim → task → evaluation → run or review → human gate → decision summary
```

---

## 2. Scope of Governance

The model governs research-to-decision translation. It applies to source material from academic, technical, institutional, legal, standards, policy, and web-based contexts.

| Source Type | Governed Concern | Control Applied |
|---|---|---|
| Peer-reviewed papers | Claims may depend on population, dataset, benchmark, or experimental condition | Claims are extracted and tied to evidence before task design |
| Preprints | Findings may shift after revision, review, or replication | Version, source text, review status, and uncertainty are preserved in the pack |
| PDFs and reports | Narrative recommendations may mix evidence with institutional position | Evidence claims are separated from operational claims |
| Technical blogs | Useful implementation detail may lack formal review | Translation depends on task containment and human review |
| Vendor publications | Incentives may shape evidence selection and adoption framing | Source type remains visible in the decision trail |
| GitHub repositories | Code may differ from paper claims or lack reproducibility evidence | Implementation claims require separate validation |
| Standards and guidance | Governance requirements may lack computable implementation detail | Requirements are translated into controls, evidence fields, and review criteria |
| AI safety and policy sources | Claims may affect misuse, autonomy, capability, liability, compute, weights, or international governance | Safety-policy intake classifies risk domain and translation boundary before claim extraction |

The model does not assume that every source should become a governed task. Some sources should remain background evidence. Some should inform evaluation design. Some should inform policy mapping. Some require restricted handling. Some should produce a rejection decision.

---

## 3. Safety-Policy Intake Gate

The safety-policy intake gate is the first governance control for AI safety and policy sources.

It exists because safety-relevant research can become hazardous when it is made task-shaped too early. A source about capability forecasting, misuse, model-weight security, autonomous agents, loss of control, compute governance, or liability should not enter the same translation path as a low-risk usability paper.

The intake artifact answers this question:

```text
What kind of authority should this source be allowed to have?
```

The artifact lives inside each relevant pack:

```text
packs/<pack_id>/
└── safety_policy_intake.json
```

It classifies:

| Intake Field Group | Governance Function |
|---|---|
| `source_status` | Records review status, evidence type, epistemic status, and update condition |
| `ai_safety_domain` | Identifies capability forecasting, misuse, loss of control, structural risk, compute governance, model-weight security, liability, international governance, and concentration of power |
| `capability_and_autonomy` | Records model class, autonomy level, task horizon relevance, and tool-use scope |
| `risk_screen` | Records misuse pathways, dual-use status, loss-of-control indicators, oversight failure modes, and catastrophic-risk relevance |
| `governance_mapping` | Assigns decision lever, required reviewers, and translation boundary |
| `translation_verdict` | Records whether the source may proceed, proceed with constraints, remain evaluation-only, remain policy-mapping-only, require review, be restricted, be rejected, or abstain |

The intake gate changes the default order of translation for safety-relevant material:

```text
Research source
  ↓
Safety-policy intake
  ↓
Claim extraction
  ↓
Task design or rejection
```

A pack is not translation-ready for AI safety or policy work until `safety_policy_intake.json` validates.

---

## 4. Governed Execution Model

The system uses AI only inside bounded execution. The AI component can generate candidate evidence. It cannot approve its own output, expand the task, change the decision standard, classify legal authority, or write the final institutional record.

```text
Research source
  ↓
Safety-policy intake, where applicable
  ↓
Claim extraction
  ↓
Operationalization review
  ↓
Locked task definition
  ↓
Evaluation plan
  ↓
Governed runloop or manual review
  ↓
Schema validation
  ↓
Human gate
  ↓
Decision summary
```

| Layer | AI Role | Governance Boundary | Human Authority |
|---|---|---|---|
| Source review | Assist with quote location or structured candidate extraction | Source text and provenance remain preserved | Researcher or reviewer determines source relevance |
| Safety-policy intake | May suggest draft classifications | Required review authority and translation boundary remain human-owned | Reviewer accepts, revises, restricts, or rejects intake classification |
| Claim formation | Propose structured claims | Claims must validate against schema and remain source-linked | Reviewer decides whether claims are admissible |
| Task design | Support task derivation | Task boundary must be locked before execution | Reviewer owns task acceptance |
| Runtime execution | Generate bounded candidate outputs | Output must conform to schema and constraints | Reviewer decides whether output can proceed |
| Final decision | No final authority | Decision summary is assembled from logged artifacts | Human gate records accept, override, reject, abstain, or escalate |

This division prevents model output from becoming institutional authorization by default.

---

## 5. Control Architecture

The governance model uses file-level controls rather than informal review. Each file type carries a specific accountability function.

| Control Layer | File or Directory | Governance Function |
|---|---|---|
| Source provenance | `packs/<pack_id>/sources/` | Preserves the material used for translation |
| Safety-policy intake | `safety_policy_intake.json` | Classifies source status, safety domain, autonomy relevance, risk screen, required review, and translation boundary |
| Claim discipline | `claims.json` | Records claims, evidence references, scope, and operationalization status |
| Task containment | `tasks.json` | Defines inputs, outputs, constraints, failure conditions, and review points |
| Evaluation planning | `eval_plan.json` | Establishes success criteria before run outputs appear |
| Schema enforcement | `schemas/` | Converts governance requirements into machine-checkable contracts |
| Validation scripts | `scripts/` | Tests whether artifacts satisfy declared contracts |
| Runtime logging | `runloop/` | Creates a traceable record of execution |
| Human authorization | `human_gate.json` | Records the decision made by the reviewer |
| Final artifact | `decision_summary.json` | Provides the audit-facing reconstruction record |

The repository uses architecture to force the governance sequence. A reviewer should be able to inspect the final decision summary and trace the decision back to source material and intermediate artifacts.

---

## 6. Authority Boundary

The central boundary is between evidence production and decision authority.

AI output is treated as candidate evidence. Human review determines whether the candidate evidence is accepted, overridden, rejected, restricted, or escalated. The final artifact records that decision.

| Activity | Evidence Production | Decision Authority |
|---|---:|---:|
| Extract candidate claims from source text | AI-assisted | Human-reviewed |
| Draft safety-policy intake fields | AI-assisted or manual | Human-reviewed |
| Determine whether a claim is admissible | Supported by schema | Human-owned |
| Convert a claim into a task | AI-assisted | Human-approved |
| Generate candidate outputs | AI-assisted | Human-reviewed |
| Resolve schema or constraint failures | Logged by system | Human-owned |
| Assign translation boundary | Supported by intake schema | Human-owned |
| Accept final output | No | Human-owned |
| Override final output | No | Human-owned |
| Reject translation or execution | No | Human-owned |
| Produce audit record | Deterministic assembly | Human-authored decision fields |

The governance model assigns responsibility to an accountable reviewer at the point where research becomes operational recommendation.

---

## 7. Human Gate

The human gate is the system’s primary authority control. It prevents candidate output from becoming final output without an explicit decision.

| Gate Outcome | Meaning | Required Record |
|---|---|---|
| `accept` | The reviewer accepts the proposed output as final | Reviewer identity, timestamp, rationale |
| `override` | The reviewer modifies or replaces the proposed output | Reviewer identity, override content, rationale |
| `reject` | The reviewer rejects the proposed output or translation path | Reviewer identity, rejection basis, decision effect |
| `abstain` | The system or reviewer declines to proceed under current evidence | Failure condition, uncertainty, required next evidence |
| `escalate` | The reviewer routes the decision to a stronger authority | Escalation target, reason, unresolved issue |

The human gate creates a reconstruction point. It shows the proposed output, the human action, and the reason the final decision took its recorded form.

---

## 8. Abstention and Restriction Model

A governed translation system must be able to stop. This repository treats abstention, restriction, and rejection as valid outcomes.

| Trigger | Why It Matters | Expected System Behavior |
|---|---|---|
| Source ambiguity | The source does not support a stable claim | Record uncertainty and halt claim promotion |
| Missing evidence | The claim lacks adequate support in the source text | Reject or mark claim as unready |
| Safety-policy uncertainty | AI safety or policy relevance cannot be classified | Require human review before claim extraction |
| Dual-use concern | Translation may lower misuse barriers | Restrict, redact, or route to expert review |
| Loss-of-control concern | Source implies agency, deception, oversight failure, or power-seeking | Require safety review and block task translation unless bounded |
| Task overreach | The task requires autonomy or open-ended action outside the system boundary | Produce translation-negative verdict |
| Schema failure | Output fails required structure | Halt before human gate or require correction |
| Constraint violation | Output exceeds defined task bounds | Record failure and prevent finalization |
| Review uncertainty | Human reviewer cannot authorize the output on available evidence | Record abstention and required evidence |

The ability to halt is part of the governance contribution. A system that always produces an implementation path functions as an adoption mechanism rather than a control system.

---

## 9. Translation Verdicts

Translation verdicts classify the relationship between a research source and an operational pathway.

| Verdict | Governance Meaning | Typical Use |
|---|---|---|
| `translation_positive` | A source claim can be converted into a bounded task with evidence, constraints, and human review | Measurement, classification, review, or evaluation tasks |
| `proceed_to_task_design` | Source appears suitable for bounded task design after review | Early translation-positive packs |
| `approve_with_conditions` | Execution may proceed only under specified constraints | Human-reviewed outputs with limited downstream use |
| `evaluation_only` | Source should inform evaluation design without execution | Benchmarks, measurement methods, safety eval design |
| `policy_mapping_only` | Source should inform governance analysis without operationalization | Legal, policy, multi-agent autonomy, structural risk |
| `restricted` | Source requires constrained handling due to safety, misuse, legal, or security concerns | Dual-use or sensitive AI safety sources |
| `human_review_required` | Source or artifact requires designated review before progression | Frontier, safety, legal, or high-impact sources |
| `translation_negative` | The research contribution cannot be safely bounded within the system’s control surface | Autonomous multi-agent coordination, open-ended deployment, unverifiable causal claims |
| `reject_translation` | The source may remain useful as research evidence while being excluded from operationalization | Claims requiring authority, autonomy, or evidence beyond the repository boundary |
| `abstain` | Evidence is insufficient to classify or translate responsibly | Weak provenance, missing source, unresolved uncertainty |

Negative translation is an intended governance result. It shows that the system preserves the distinction between research relevance and operational readiness.

---

## 10. Audit Reconstruction

The model supports post-hoc reconstruction by requiring every decision to leave an artifact trail.

```text
Source material
  └── safety-policy intake, where applicable
        └── evidence extracted into claims
              └── claims selected or rejected for operationalization
                    └── tasks defined before execution
                          └── evaluation criteria declared
                                └── model candidates or reviewer outputs generated under constraints
                                      └── proposed output validated
                                            └── human gate recorded
                                                  └── final decision summary assembled
```

| Reconstruction Question | Evidence Location |
|---|---|
| What was the original source? | `sources/paper_text.txt` |
| What kind of source and risk class was recorded? | `safety_policy_intake.json` |
| What claims were extracted? | `claims.json` |
| Which claim became a task? | `tasks.json` |
| What evaluation standard was applied? | `eval_plan.json` |
| What did the model or reviewer produce? | `candidates.jsonl`, `proposed.json`, reviewer notes |
| Did the output validate? | schema validation logs |
| What did the reviewer decide? | `human_gate.json` |
| What is the final decision record? | `decision_summary.json` |

An audit-ready decision record should allow a reviewer to reconstruct the chain without relying on memory, Slack messages, or a model-generated explanation.

---

## 11. Governance Failure Modes

The repository is designed around specific failure modes in AI-assisted research translation.

| Failure Mode | Description | Control |
|---|---|---|
| Source laundering | A weak or unstable source gains authority because it appears in a research workflow | Preserve source type, source text, and provenance |
| Safety-policy underclassification | A safety-relevant source enters task design before risk domain or review authority is assigned | Require `safety_policy_intake.json` |
| Claim inflation | A narrow finding becomes a broad operational recommendation | Require claim extraction and operationalization review |
| Context collapse | Study conditions disappear during task design | Record assumptions, scope, and translation limits |
| Dual-use normalization | Misuse-relevant content becomes ordinary task material | Route to restricted handling or human review |
| Loss-of-control normalization | Agentic, deceptive, or oversight-failure material becomes executable too early | Require safety review and policy-mapping boundary |
| Task drift | The task expands after model output appears | Lock task definitions before execution |
| Model authority creep | Candidate output becomes final decision by convenience | Require human gate before finalization |
| Evidence ambiguity | Reviewers cannot tell which evidence supports which decision | Use traceable artifacts and decision summaries |
| Negative-result suppression | Failed translations disappear from the record | Treat rejection and abstention as recorded outcomes |
| Audit failure | The organization cannot reconstruct why a research-based action was authorized | Assemble deterministic decision summaries |

The model treats these failure modes as design constraints. The repository’s architecture exists to make each one harder to hide.

---

## 12. Institutional Use Cases

The governance model supports several institutional review patterns.

| Use Case | Governance Need | Repository Fit |
|---|---|---|
| AI governance research | Study how research claims become controlled decision artifacts | Strong fit |
| AI safety evaluation | Examine how autonomy, task containment, and human oversight are enforced | Strong fit |
| AI policy translation | Convert standards, policy texts, and governance research into reviewable artifacts | Strong fit |
| Internal AI adoption review | Evaluate whether a paper-backed idea should become an implementation task | Strong fit |
| Vendor claim review | Separate vendor evidence from adoption authority | Strong fit |
| Safety-policy triage | Classify safety-relevant sources before claim extraction and task design | Strong fit |
| Autonomous deployment approval | Requires controls beyond this repository’s current boundary | Out of scope |
| Production system certification | Requires organizational controls, access management, monitoring, and legal review beyond this artifact | Out of scope |

The repository is best understood as a research-to-decision governance artifact. It can support institutional review, but it does not replace institutional authority.

---

## 13. Relationship to AI Governance and AI Safety

This governance model sits at the intersection of AI governance, AI safety, research operations, and institutional accountability.

| Field | Relationship |
|---|---|
| AI governance | Provides controls for translating AI research into decision records |
| AI safety | Blocks unbounded autonomy and preserves abstention for unsafe or unsupported translations |
| AI policy | Routes legal, standards, compute, model-weight, liability, and international governance material to reviewable artifacts |
| Responsible AI | Assigns human authority and preserves evidence for review |
| Research operations | Converts source material into structured, inspectable artifacts |
| Audit and compliance | Produces records that can be reconstructed after the decision |
| Institutional decision-making | Separates research evidence from authorization |

The model’s practical claim is narrow: institutions need a controlled path between research intake and operational action. This repository implements one reference pattern for that path.

---

## 14. Standards Alignment

The governance model is closest to a Govern and Map control pattern. It records source context, risk domain, review authority, evidence boundary, and decision ownership before measurement or management occurs.

| NIST AI RMF Function | Repository Support |
|---|---|
| Govern | Defines roles, artifact contracts, validation expectations, review authority, and human decision records |
| Map | Classifies source type, safety-policy domain, autonomy relevance, risk screen, and institutional context |
| Measure | Supports evaluation plans, schema validation, run outputs, and review artifacts |
| Manage | Supports accept, override, reject, abstain, restrict, and escalation decisions |

This repository does not claim full AI RMF implementation. It provides evidence artifacts that may support governance review.

---

## 15. Design Commitments

| Commitment | Implementation |
|---|---|
| Research claims require provenance | Source material is stored with the pack |
| Safety-relevant sources require intake classification | `safety_policy_intake.json` records risk domain and translation boundary |
| Operational tasks require containment | Tasks define boundaries before execution |
| AI output remains intermediate | Human gate must finalize or reject output |
| Rejection is a valid result | Translation-negative packs remain part of the repository |
| Governance must be inspectable | Artifacts are structured and schema-validated |
| Audit records should be deterministic | Decision summaries are assembled from logged artifacts |
| Institutional authority must remain human | Final decision state belongs to the reviewer |

These commitments define the governance model. They are intentionally conservative because the repository operates at the point where research can become action.

---

## 16. Current Limits

This repository governs translation artifacts and bounded AI-assisted runs. It does not provide a complete enterprise AI governance program.

| Limit | Reason |
|---|---|
| No production access control model | The repository is research software, not an enterprise platform |
| No continuous monitoring layer | The system governs discrete translation runs |
| No legal review workflow | Legal authority remains outside the repository |
| No automated source credibility scoring | Source evaluation requires human judgment |
| No autonomous multi-agent execution | The governance boundary excludes open-ended coordination |
| No universal safety claim | The method governs translation, not system safety itself |
| No claim of universal research validity | The method governs translation, not truth itself |

These limits are deliberate. The system governs the path from research artifact to decision record. Enterprise deployment requires additional organizational controls.

---

## 17. Summary

The Applied AI Research Translator implements governance at the research translation layer. It captures source material, classifies AI safety and policy relevance, extracts claims, tests operationalizability, locks task boundaries, validates outputs, requires human authorization, and produces decision summaries that can be reconstructed later.

The model’s strongest property is refusal capacity. It can convert research into a bounded task when the governance record supports that path. It can also restrict, abstain, or reject translation when the source claim requires autonomy, authority, evidence, or operational scope beyond the system boundary.
