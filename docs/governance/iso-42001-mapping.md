# ISO/IEC 42001 Mapping

This file maps Applied AI Research Translator to selected AI management system concerns associated with ISO/IEC 42001:2023. The mapping is interpretive. It does not claim certification, audit readiness under an accredited scheme, or conformity with ISO/IEC 42001.

ISO/IEC 42001 specifies requirements and guidance for establishing, implementing, maintaining, and continually improving an AI management system within an organization. This repository addresses a narrower problem: governed translation of applied AI research into decision artifacts.

---

## Mapping Thesis

The repository can support an AI management system by producing evidence for research intake, decision accountability, controlled task design, human oversight, and reviewable records.

```text
AI management system
  ↓
research intake process
  ↓
translation controls
  ↓
human-gated decision record
  ↓
review and improvement evidence
```

The repository supplies artifact discipline. The organization must supply policy, roles, risk appetite, monitoring, supplier governance, internal audit, and management review.

---

## AI Management System Alignment

| AI Management System Concern | Repository Support | Evidence Artifact |
|---|---|---|
| Organizational context | Research sources and intended task context are recorded | pack documentation, `claims.json`, `tasks.json` |
| AI policy and objectives | Translation method can support policy-level control objectives | root governance documents |
| Risk management | Rejection, abstention, conditional approval, and limitation records | `decision_summary.json`, `LIMITATIONS.md` |
| AI system lifecycle controls | Source-to-claim-to-task-to-decision artifacts support controlled lifecycle handoff | pack artifacts |
| Data governance | Source and run input records show what material entered review | `sources/`, `run_input.json` |
| Transparency and information | Decision summaries expose rationale, confidence, and limits | `decision_summary.json` |
| Human oversight | Human gate preserves reviewer decision states | `human_gate.json`, `human-gate.md` |
| Performance evaluation | Evaluation plans and validation scripts support evidence review | `eval_plan.json`, `schemas/`, scripts |
| Continual improvement | Limitations, validation failures, and negative translations identify improvement areas | `LIMITATIONS.md`, rejection packs |

---

## Evidence Fit

| Repository Artifact | AI Management System Value |
|---|---|
| `RESEARCH-RATIONALE.md` | Explains why research intake requires governance |
| `TRANSLATION-METHOD.md` | Defines repeatable process for source-to-decision translation |
| `GOVERNANCE-MODEL.md` | Defines authority boundary and controls |
| `TRACEABILITY.md` | Supports auditability and decision reconstruction |
| `LIMITATIONS.md` | Supports transparent limitation management |
| `packs/` | Provides evidence units for applied review |
| `schemas/` | Converts artifact expectations into machine-checkable contracts |
| `scripts/` | Supports validation and reproducibility |
| `docs/governance/` | Provides institutional review and standards-mapping support |

The repository is best used as supporting evidence for a specific process inside a larger AI management system.

---

## Control Objectives Supported

| Control Objective | Repository Mechanism |
|---|---|
| Research sources are reviewed before operational use | Source provenance and claim extraction |
| Claims are bounded before task design | `claims.json` and translation screening |
| Tasks are defined before execution | `tasks.json` |
| Evaluation criteria are declared before output review | `eval_plan.json` |
| AI outputs remain intermediate | Human gate and decision-summary assembly |
| Rejections are preserved | Negative translation packs |
| Decisions are reconstructable | Traceability model and decision summaries |
| Limitations are visible | Limitation register and pack notes |

These objectives can be adopted into an organization’s internal AI governance procedure.

---

## Gaps Requiring Organizational Controls

| Gap | Required External Control |
|---|---|
| Roles and responsibilities | AI governance charter, RACI, approval routing |
| AI system inventory | Enterprise AI register or model inventory |
| Supplier governance | Vendor risk management and contractual controls |
| Data protection | Privacy, security, retention, and data rights review |
| Production monitoring | Runtime monitoring, incident management, drift detection |
| Internal audit | Audit plan, sampling method, review authority |
| Management review | Executive review cadence and decision escalation |
| Certification | Accredited ISO/IEC 42001 audit process, where pursued |

The repository should not be described as an AI management system by itself.

---

## Review Use

An organization can use this repository inside an AI management system as:

| Use | Description |
|---|---|
| Research intake control | Govern external research before adoption |
| Evidence artifact generator | Produce structured decision records |
| Pre-implementation review tool | Decide whether research supports bounded task design |
| Negative-result register | Preserve rejected or abstained translations |
| Audit support | Reconstruct why a research-backed decision occurred |
| Training artifact | Teach reviewers how research claims become governance artifacts |

---

## Required Boundary Language

Use this language when mapping the repository to ISO/IEC 42001:

```text
Applied AI Research Translator may support selected AI management system processes by producing governed research translation artifacts. It is not an AI management system by itself and does not establish ISO/IEC 42001 conformity or certification.
```

---

## Reviewer Checklist

Before using the repository in an AI management system context, ask:

- Which AI management process does this pack support?
- Who owns the process outside the repository?
- What organizational policy does the pack support?
- What risks remain outside the translation record?
- Does the pack produce evidence suitable for internal review?
- Does the decision summary preserve authority, rationale, and limits?
- How will findings feed continual improvement?

The repository’s value is strongest when it is assigned to a defined process: research intake, translation review, evidence generation, or decision reconstruction.
