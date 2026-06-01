# Limitations

> Applied AI Research Translator is a governed research-to-decision translation system. Its purpose is to convert research artifacts into bounded decision records when the evidence, source classification, task boundary, and human accountability path support translation. It is also designed to restrict, abstain, or reject translation when those conditions fail.

## Purpose of This File

This file defines the known limits of the repository, the conditions under which its outputs should be treated as provisional, and the disclosure language that should accompany institutional or scholarly use.

A limitation register is part of the governance model. It prevents the repository from being read as a general AI deployment framework, a universal research evaluator, a legal compliance instrument, or a substitute for domain review.

The v1.1.1 safety-policy intake gate adds a new boundary condition: AI safety and policy sources require classification before they become claims, tasks, evaluation plans, or decision records.

---

## Scope Boundary

| Boundary | What the Repository Covers | What Remains Outside Scope |
|---|---|---|
| Research translation | Converts papers, PDFs, reports, repositories, online research artifacts, benchmark claims, and policy materials into source-controlled claims, tasks, verdicts, and decision summaries | Full literature review, systematic review, meta-analysis, scientific replication, or field validation |
| Safety-policy intake | Classifies AI safety and policy sources by evidence type, safety domain, autonomy relevance, dual-use status, oversight risk, required review, and translation boundary | Automated safety certification, comprehensive threat assessment, legal determination, or expert consensus |
| AI use | Uses AI as a bounded evidence-producing component inside schema-controlled workflows | AI approval authority, autonomous deployment, self-revision of governance criteria, or self-authorization |
| Governance control | Creates structured records for provenance, safety-policy intake, claim extraction, task containment, human gate review, and audit reconstruction | Regulatory certification, institutional approval, legal sign-off, or production authorization |
| Execution | Runs bounded demonstration tasks through a controlled runloop | Production AI platform, enterprise GRC tool, autonomous agent system, or continuous monitoring service |
| Evidence | Preserves source-derived claims, intake classifications, task rationale, validation outputs, and human decisions | Proof that the underlying research claim holds across contexts |
| Review | Supports human reviewers by making the decision path visible | Replacement for expert judgment, IRB review, legal review, ethics review, security review, or domain validation |

The core boundary is this: the repository governs translation from research artifact to decision artifact. It does not establish universal validity of the underlying research.

---

## Summary of Known Limitations

| ID | Limitation | Why It Matters | Current Control | Residual Risk |
|---|---|---|---|---|
| L1 | Source dependence | Translation quality depends on the accuracy, completeness, and provenance of source material | Source text is captured and linked to claims | Weak source evidence can still produce well-structured but fragile claims |
| L2 | Safety-policy intake judgment | AI safety and policy classification requires expert judgment, especially for dual-use, autonomy, and loss-of-control material | `safety_policy_intake.json` records evidence type, risk domain, required review, and translation boundary | Reviewers may underclassify risk or assign a permissive boundary too early |
| L3 | Claim extraction judgment | Claim extraction requires interpretation, especially for dense papers and mixed-method reports | Claims are schema-bound and reviewable | Reviewers may disagree about which claims matter or how they should be operationalized |
| L4 | Domain validation | The system structures claims; it does not verify domain truth independently | Human gate and decision summary preserve accountability | A valid decision record can still rest on domain assumptions needing expert review |
| L5 | Limited pack corpus | Current packs demonstrate method behavior across selected cases | Positive, negative, and safety-policy classified examples are included | Coverage remains too small for broad performance claims across research domains |
| L6 | Evaluation depth | Demo tasks show bounded operationalization, not full empirical validation | Evaluation plans specify criteria and limits | Evaluation outputs may be insufficient for high-stakes deployment decisions |
| L7 | Model dependence | AI-generated candidate outputs depend on model behavior, prompts, and runtime configuration | Outputs remain intermediate artifacts subject to schema validation and human review | Model drift can alter candidate quality across time |
| L8 | Human gate quality | Human review is only as strong as reviewer expertise, incentives, and institutional authority | Accept, override, reject, abstain, and escalation decisions are recorded | A reviewer can approve weak evidence or miss domain-specific failure modes |
| L9 | Security exposure | Online research, PDFs, repositories, and source text may contain adversarial or poisoned content | Source capture, bounded tasks, schema checks, and safety-policy intake reduce exposure | Prompt injection, malicious code, or poisoned claims require additional security controls |
| L10 | Regulatory mapping | The architecture aligns conceptually with governance frameworks but is not a legal compliance instrument | Documentation separates governance artifact from certification | Institutions still need legal, regulatory, and sector-specific review |
| L11 | Production readiness | The repo is research software and reference implementation | Runloop, schemas, and validators demonstrate controlled execution | Production deployment requires access control, monitoring, logging hardening, and security review |

---

## L1. Source Dependence

The system can only translate the source material it receives. A source may contain incomplete methods, overstated findings, missing limitations, unstable URLs, outdated benchmark references, ambiguous claims, or selectively framed evidence. The translator can preserve provenance and expose assumptions, but it cannot repair a weak source.

Current controls include source capture in `sources/paper_text.txt`, explicit claim extraction in `claims.json`, and traceability from source material into tasks and decision summaries.

Residual risk remains when a source looks technically credible while omitting deployment assumptions that matter in institutional use.

---

## L2. Safety-Policy Intake Requires Judgment

The safety-policy intake gate improves the repository, but it also introduces a judgment point. Classifying a source as capability forecasting, misuse, loss of control, compute governance, model-weight security, liability, international governance, structural risk, or concentration of power requires reviewer competence.

The intake schema can force fields to exist. It cannot guarantee that the classification is correct.

| Intake Area | Reviewer Judgment Required | Failure Mode |
|---|---|---|
| Evidence type | Is the source empirical, theoretical, forecast-based, legal, benchmark-based, or mixed? | Forecasts may be treated as measurements |
| AI safety domain | Which safety or policy category does the source touch? | Loss-of-control or dual-use relevance may be missed |
| Autonomy profile | Does the source imply advisory, bounded tool use, delegated tasking, or open-ended agency? | Agentic capability may be normalized as ordinary task support |
| Misuse pathway | Does translation lower barriers for harmful use? | Operational details may be made too accessible |
| Translation boundary | Should the source proceed, remain evaluation-only, remain policy-mapping-only, be restricted, be rejected, or abstain? | A permissive boundary may allow premature task design |
| Required review | Which expertise must review the source before progression? | Legal, security, domain, or AI safety review may be skipped |

The intake artifact should therefore be read as a review scaffold. It makes the classification visible and contestable. It does not replace expert judgment.

---

## L3. Claim Extraction Requires Judgment

A paper rarely states every operational claim in a form that can be executed. Translating research into a task requires judgment about which claim is central, which assumptions travel with that claim, and which evidence counts as sufficient support.

The repository controls this by requiring claims to be written as structured records, bound to source material, and reviewed before task creation. The schema forces specificity, but it cannot eliminate interpretive disagreement.

This limitation is expected. The goal is to make judgment visible, inspectable, and contestable.

---

## L4. Domain Validity Is Separate From Translation Validity

A translation can be structurally valid while the underlying research claim still requires expert validation. For example, a human-AI reliance claim may translate cleanly into an accept, override, and calibration task. That does not prove the original result generalizes across institutions, populations, model families, or workflow settings.

The repository therefore separates translation validity from domain truth.

| Validity Type | Question | Evidence Location |
|---|---|---|
| Source validity | Is the source credible, complete, and appropriately versioned? | `sources/`, source metadata, citation record |
| Safety-policy validity | Was AI safety and policy relevance classified appropriately? | `safety_policy_intake.json`, reviewer notes |
| Claim validity | Is the claim stated clearly enough to evaluate? | `claims.json` |
| Translation validity | Can the claim become a bounded task with reviewable outputs? | `tasks.json`, `eval_plan.json` |
| Run validity | Did the system execute the task under the defined boundary? | run artifacts and logs |
| Decision validity | Did a human reviewer authorize, override, reject, abstain, or escalate with recorded rationale? | `human_gate.json`, `decision_summary.json` |
| Domain validity | Does the claim hold in the target environment? | external expert review, replication, field evaluation |

The repository mainly addresses the middle of this chain: safety-policy validity, claim validity, translation validity, run validity, and decision validity.

---

## L5. Demonstration Corpus Is Limited

The current pack set is deliberately small. It demonstrates the method across translation-positive, translation-negative, and safety-policy classified cases, including human-AI reliance calibration, production measurement of agents, and multi-agent failure modes. That corpus is enough to show the architecture of the method. It is too small to support broad claims about performance across disciplines.

Future work should expand the pack corpus across fields such as medicine, education, finance, law, software engineering, AI safety evaluation, climate analysis, public-sector decision support, biosecurity governance, cyber risk, and model-weight security.

---

## L6. Evaluation Plans Are Bounded

The repository uses evaluation plans to define what evidence a task should produce. These plans are method controls, not exhaustive empirical studies.

A bounded evaluation plan can answer questions such as:

| Evaluation Question | Suitable for This Repo? | Reason |
|---|---:|---|
| Can this claim be converted into a bounded task? | Yes | This is the primary translation question |
| Did the source receive safety-policy classification where needed? | Yes | This is controlled by the intake schema |
| Did the run produce schema-valid artifacts? | Yes | This is directly controlled by validation tooling |
| Did a human reviewer authorize the final output? | Yes | This is captured by the human gate |
| Does this research claim generalize across populations? | Limited | Requires external empirical study |
| Is this method safe for high-impact production use? | Limited | Requires institutional risk review, security review, and domain validation |

For high-impact systems, a positive translation verdict should be treated as a readiness signal for deeper review, not as deployment approval.

---

## L7. Model Behavior Can Drift

The governed runloop may use model outputs as candidate evidence. Candidate quality can change when the model version, provider behavior, prompt template, temperature setting, or context window changes.

The repository reduces this risk by treating model output as intermediate evidence. The final decision artifact should come from deterministic assembly and human authorization, not from model-written approval language.

Future releases should strengthen model-version capture, provider metadata, prompt hashing, seed capture where available, runtime environment capture, and reproducibility checks.

---

## L8. Human Gate Quality Depends on Reviewer Competence

The human gate is an accountability mechanism. It records who accepted, overrode, rejected, abstained, or escalated a proposed output. It does not guarantee that the reviewer has sufficient domain expertise, institutional authority, or incentive alignment.

This matters because a weak human gate can convert procedural review into approval theater.

The repository addresses this by making human decisions explicit. It records the decision path, but institutions must define reviewer qualifications, escalation rules, conflict-of-interest controls, approval authority, and required expertise for safety-policy intake.

---

## L9. Online Research and PDF Inputs Carry Security Risk

Research inputs can be adversarial. PDFs may contain hidden text, misleading metadata, embedded instructions, or compromised links. Web pages may change after capture. GitHub repositories may contain unsafe code or dependency risk. Vendor reports may frame claims in ways that make adoption seem lower-risk than the evidence supports.

The repository currently uses source capture, schema enforcement, task containment, safety-policy intake, and human review as governance controls. Additional security work is needed for production use.

| Risk | Example | Additional Control Needed for Production |
|---|---|---|
| Prompt injection | Hidden instructions inside a PDF or web page | Content isolation, instruction stripping, source sanitization |
| Source volatility | Web page changes after translation | Archival capture, timestamped hash, immutable source snapshot |
| Malicious repository | Code sample introduces unsafe dependency | Dependency scanning, sandbox execution, software supply-chain review |
| Source poisoning | Research text embeds misleading or selectively framed claims | Independent source review, cross-source comparison, expert review |
| Metadata ambiguity | Missing version, author, or publication date | Mandatory source metadata fields and rejection rules |
| Dual-use exposure | Source details could lower barriers to misuse | Restricted handling, redaction, security review, or rejection |

The system should treat online material as evidence requiring provenance controls, not as self-authorizing input.

---

## L10. Regulatory Alignment Is Informative, Not Certification

The repository is relevant to AI governance frameworks because it creates evidence for traceability, human oversight, decision reconstruction, safety-policy classification, and task containment. It should not be described as certifying compliance with NIST AI RMF, the EU AI Act, ISO/IEC 42001, institutional review requirements, or sector-specific law.

A governance artifact can support a compliance argument. It does not become the compliance determination.

---

## L11. Production Deployment Requires Additional Controls

The repository is research software. Production deployment would require additional engineering and organizational controls.

| Production Need | Required Expansion |
|---|---|
| Identity and access control | Role-based access, reviewer authorization, least-privilege execution |
| Immutable logs | Tamper-evident storage, log signing, retention policy |
| Model metadata capture | Model version, provider, prompt hash, configuration, timestamp |
| Safety-policy review workflow | Reviewer assignment, conflict-of-interest checks, domain-specific escalation, restricted handling |
| Secure execution | Sandboxing, dependency scanning, file sanitization, secrets management |
| Workflow integration | Review queues, escalation paths, issue tracking, evidence export |
| Monitoring | Drift tracking, validation failure rates, abstention rates, override rates, restriction rates |
| Governance reporting | Reviewer dashboards, decision indexes, recurring audit summaries |
| Institutional authority | Policy mapping, accountable owner, approval matrix, appeals path |

These additions would move the repository from reference implementation toward institutional control system.

---

## Anti-Overclaiming Rules

The following claims are supported by the repository:

| Supported Claim | Basis |
|---|---|
| The repository implements a governed translation pattern from source material to decision artifact | Pack structure, schemas, runloop, human gate, decision summaries |
| The repository adds a safety-policy intake gate for classifying AI safety and policy sources before translation | `safety_policy_intake.json`, schema, validator, governance documentation |
| The repository treats negative translation as a valid governance outcome | Multi-agent failure-mode pack and rejection summary |
| The repository separates model-generated candidates from human-authorized final outputs | Human gate and deterministic decision summary architecture |
| The repository creates an audit trail for selected demonstration runs | Demo-run manifests and decision summaries |
| The repository provides a research software artifact for studying decision accountability in AI-assisted research translation | Full repo architecture and documentation |

The following claims should be avoided unless supported by later validation work:

| Claim to Avoid | Reason |
|---|---|
| The system proves whether research findings are true | Domain truth requires external validation and replication |
| The system certifies AI governance compliance | Compliance requires institutional and legal determination |
| The system safely enables autonomous research agents | The architecture is explicitly non-agentic |
| The system automatically classifies all AI safety risks correctly | Safety-policy intake requires expert review |
| The system generalizes across all research domains | Current pack corpus is limited |
| The system removes the need for expert review | Human, safety, legal, security, and domain review remain central controls |
| The system is production-ready | Additional security, access, monitoring, and governance controls are required |

---

## Required Disclosure Language

Use the following language when citing or adapting the repository in academic, institutional, or applied governance settings.

### Short Disclosure

Applied AI Research Translator is research software for governed research-to-decision translation. It structures source material into safety-policy intake classifications, claims, bounded tasks, validation artifacts, human-gate decisions, and decision summaries. It does not verify the scientific truth of source claims, certify regulatory compliance, or authorize production deployment.

### Institutional Disclosure

This repository provides a reference implementation for converting applied AI research artifacts into governed decision records. Its outputs should be interpreted as structured translation artifacts: source-grounded claims, safety-policy intake classifications, task boundaries, evaluation criteria, validation results, human-gate records, and decision summaries. A positive translation verdict indicates that a claim can be operationalized under the repository’s control model. It does not establish domain validity, regulatory compliance, safety for high-impact deployment, or institutional approval. Those determinations require qualified human review and organization-specific authority.

### Scholarly Disclosure

The repository is intended as research software for studying controlled research translation, auditability, human oversight, safety-policy intake, and decision accountability in AI-assisted workflows. Its methodological contribution is the conversion of research sources into bounded, schema-validated decision artifacts, including documented rejection, restriction, or abstention when translation exceeds the governance boundary. The current release demonstrates the pattern through a limited set of example packs and governed runs. Broader claims about validity, reliability, cross-domain performance, or production fitness require further empirical evaluation.

---

## Version-Specific Limitations for v1.1.1

v1.1.1 strengthens the repository’s AI safety and policy handling by adding safety-policy intake classification before claim extraction and task design. It should be treated as a research-software governance enhancement, not a production hardening release.

| Area | v1.1.1 Status | Future Work |
|---|---|---|
| Documentation | Research rationale, method, governance model, traceability, limitations, safety-policy intake, and review guidance are defined | Add more worked reviewer examples and cross-source comparison guidance |
| Pack coverage | Selected positive, negative, and safety-policy classified examples | Expand cross-domain corpus |
| Safety-policy intake | Schema, validator, template, and worked example are included | Add inter-reviewer comparison, reviewer qualification fields, and restricted-handling examples |
| Runtime | Demonstration runloop with human gate | Add stronger metadata capture and tamper-evident logs |
| Security | Source containment, safety-policy intake, and secret-scanning support | Add PDF sanitization, prompt-injection screening, dependency scanning |
| Evaluation | Pack-level evaluation plans and decision summaries | Add inter-reviewer reliability, benchmark suite, error taxonomy, and failure-rate reporting |
| Institutional use | Governance architecture is visible | Add role model, approval matrix, escalation workflow, and review queue |

---

## Failure Conditions

A research artifact should fail translation when the system cannot create a bounded, reviewable decision path.

| Failure Condition | Expected Verdict |
|---|---|
| The source touches AI safety or policy concerns but lacks intake classification | `human_review_required` or `abstain` |
| The claim depends on autonomous multi-agent coordination outside the control boundary | `reject_translation` |
| The source lacks enough evidence to identify a falsifiable claim | `reject_translation` or `abstain` |
| The task cannot define bounded inputs and outputs | `reject_translation` |
| The expected output cannot be schema-validated | `reject_translation` |
| The task requires the model to revise its own approval criteria | `reject_translation` |
| The source presents dual-use detail that may lower misuse barriers | `restricted` or `human_review_required` |
| The decision requires domain authority absent from the reviewer role | `approve_with_conditions`, `human_review_required`, or `reject_translation` |
| The evidence supports limited trial only | `approve_with_conditions` |
| The source remains useful for analysis but unsuitable for operationalization | `policy_mapping_only` or `reject_translation` |

Rejection is a successful governance outcome when it prevents weak evidence from becoming institutional action.

---

## Recommended Reader Interpretation

Researchers should read this repository as a method for making research translation inspectable. Governance practitioners should read it as a control pattern for separating source evidence, AI-generated candidate outputs, safety-policy intake, human authorization, and final decision records. Institutional reviewers should read it as a prototype for audit reconstruction, not as an approval system.

The repository is strongest where the research question concerns decision accountability: who classified the source, which claim was translated, what task was created, what evidence was produced, who approved or rejected the final output, and how the decision can be reconstructed later.

---

## Closing Statement

The main limitation is also the main design choice: the system refuses to let research artifacts, model outputs, or translation workflows authorize themselves. That refusal narrows the system’s autonomy, but it strengthens its value as a governance artifact.
