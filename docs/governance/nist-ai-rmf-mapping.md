# NIST AI RMF Mapping

This file maps Applied AI Research Translator to the NIST AI Risk Management Framework 1.0. The mapping is interpretive. It does not claim certification, conformity, or NIST endorsement.

The NIST AI RMF Core is organized around four functions: Govern, Map, Measure, and Manage. Govern applies across the AI risk management process, while Map, Measure, and Manage apply in system-specific contexts and lifecycle stages.

---

## Mapping Thesis

The repository contributes most directly to the point where research evidence becomes a decision artifact.

```text
NIST Govern: accountability and risk process
NIST Map: context and risk identification
NIST Measure: evidence, evaluation, and uncertainty
NIST Manage: treatment, acceptance, rejection, and monitoring decisions
```

Applied AI Research Translator does not implement a full enterprise AI risk management program. It provides a governed artifact path that can support such a program.

---

## Function-Level Mapping

| NIST AI RMF Function | Repository Control | Evidence Artifact |
|---|---|---|
| Govern | Authority boundary, human gate, translation verdicts, limitation register | `GOVERNANCE-MODEL.md`, `human_gate.json`, `decision_summary.json` |
| Map | Source classification, claim extraction, task scoping, risk-boundary identification | `sources/paper_text.txt`, `claims.json`, `tasks.json` |
| Measure | Evaluation plan, schema validation, run outputs, confidence labels, abstention conditions | `eval_plan.json`, `schemas/`, validation scripts, run artifacts |
| Manage | Conditional approval, rejection, abstention, decision summary, release limitations | `decision_summary.json`, `LIMITATIONS.md`, negative translation packs |

The repository’s strongest alignment is traceability: it records the chain from source evidence to decision artifact.

---

## Govern Mapping

Govern concerns organizational accountability, policies, processes, roles, responsibilities, and oversight. This repository operationalizes a narrow slice of Govern: authority over research-to-decision translation.

| Govern Concern | Repository Mechanism | Gap |
|---|---|---|
| Accountability | Human gate assigns accept, override, or reject authority | Reviewer identity and role should become more explicit in future schemas |
| Policies and processes | Translation method defines source, claim, task, evaluation, and decision steps | Enterprise policy integration remains outside the repo |
| Risk tolerance | Translation verdicts allow rejection and conditional approval | Risk appetite thresholds must be set by the adopting institution |
| Documentation | Decision summaries record rationale, confidence, and limitations | Organization-level policy records must be maintained elsewhere |
| Oversight | Root governance documents and pack review support human scrutiny | Workflow assignment and approval routing require institutional process |

The repository helps Govern by making decision authority explicit at the artifact level.

---

## Map Mapping

Map concerns context, intended use, system boundaries, and risk identification.

| Map Concern | Repository Mechanism | Evidence Artifact |
|---|---|---|
| Context | Source type, pack ID, task scope | `packs/<pack_id>/`, `claims.json` |
| Intended use | Task definitions and decision summaries | `tasks.json`, `decision_summary.json` |
| Risk identification | Failure modes, assumptions, rejection basis | `claims.json`, `eval_plan.json`, `LIMITATIONS.md` |
| Stakeholder context | Human-gate and institutional review templates | `human_gate.json`, `institutional-review-template.md` |
| Boundary conditions | Translation verdict and abstention model | `decision_summary.json`, `abstention-model.md` |

The Map function is where research usefulness is separated from operational readiness.

---

## Measure Mapping

Measure concerns methods, metrics, analysis, evaluation, and risk assessment.

| Measure Concern | Repository Mechanism | Evidence Artifact |
|---|---|---|
| Evaluation criteria | Pre-declared evaluation plan | `eval_plan.json` |
| Output assessment | Schema validation and run artifacts | `schemas/`, validation scripts |
| Confidence | Decision-summary confidence fields | `decision_summary.json` |
| Failure detection | Abstention, schema failure, constraint violation | run logs, validation output |
| Evidence sufficiency | Human-gate review | `human_gate.json` |
| Limitations | Limitation register and decision notes | `LIMITATIONS.md`, pack summaries |

The repository treats measurement as a precondition for authority. An output that cannot be measured against declared criteria should not become final.

---

## Manage Mapping

Manage concerns risk treatment, prioritization, response, and ongoing risk decisions.

| Manage Concern | Repository Mechanism | Evidence Artifact |
|---|---|---|
| Risk response | Accept, override, reject, abstain | `human_gate.json`, `decision_summary.json` |
| Risk treatment | Conditional approval and task constraints | `tasks.json`, `decision_summary.json` |
| Residual risk | Confidence and limitation notes | `decision_summary.json`, `LIMITATIONS.md` |
| Incident or failure response | Rejection records and abstention rationale | negative packs, run logs |
| Monitoring handoff | Decision summaries identify conditions for continued review | `decision_summary.json` |

The repository supports Manage by recording what the institution decided to do with the evidence.

---

## Mapping Limits

| Limit | Explanation |
|---|---|
| No enterprise inventory | The repository does not maintain an organization-wide AI system inventory |
| No continuous monitoring | It governs discrete translation runs and packs |
| No risk appetite framework | Institutions must define thresholds |
| No incident response program | Failures can be recorded, but enterprise response sits outside the repo |
| No certification | The mapping is interpretive and does not assert compliance |

This mapping should be used as evidence-supporting documentation, not as a compliance claim.

---

## Reviewer Use

A governance reviewer can use this mapping to ask:

- Which AI RMF function is supported by this artifact?
- What evidence exists for that function?
- Where does the repository stop?
- Which controls must be supplied by the institution?
- Does the decision summary preserve source, claim, task, evaluation, and authorization evidence?

The repository’s value under NIST AI RMF is its decision traceability, not broad enterprise coverage.
