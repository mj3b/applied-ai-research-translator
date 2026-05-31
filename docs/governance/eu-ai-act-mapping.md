# EU AI Act Mapping

This file maps Applied AI Research Translator to selected evidence concerns associated with Regulation (EU) 2024/1689, the Artificial Intelligence Act. The mapping is interpretive. It does not claim legal compliance, conformity assessment readiness, certification, or regulatory approval.

The repository is research software. It may support evidence preparation and governance reasoning. It does not determine whether a system is high-risk, whether an obligation applies, or whether a provider or deployer has satisfied legal requirements.

---

## Mapping Thesis

The repository is most relevant to evidence discipline: risk records, technical documentation support, record-keeping, transparency to reviewers, human oversight, and accuracy or cybersecurity review boundaries.

```text
source evidence
  ↓
claim record
  ↓
task boundary
  ↓
evaluation criteria
  ↓
human-gated decision summary
```

This chain can support institutional review where AI Act obligations require documentation, oversight, and risk reasoning. It is not a substitute for legal analysis.

---

## High-Risk Requirement Orientation

Articles 9 through 15 of the EU AI Act concern requirements for high-risk AI systems, including risk management, data governance, technical documentation, record-keeping, transparency, human oversight, and accuracy, robustness, and cybersecurity.

| EU AI Act Concern | Repository Support | Evidence Artifact |
|---|---|---|
| Risk management | Translation verdicts, abstention, rejection, limitation notes | `decision_summary.json`, `LIMITATIONS.md` |
| Data governance | Source and input documentation, where provided | `sources/`, `run_input.json` |
| Technical documentation | Artifact chain documenting source, claim, task, evaluation, and decision | pack files, schemas, README documents |
| Record-keeping | Run artifacts, proposed outputs, human gate, decision summaries | run logs, `human_gate.json`, `decision_summary.json` |
| Transparency to deployers or reviewers | Decision summaries and limitation language | `decision_summary.json`, docs |
| Human oversight | Human gate and accept, override, reject controls | `human_gate.json`, `human-gate.md` |
| Accuracy, robustness, cybersecurity | Evaluation plan, schema validation, security considerations | `eval_plan.json`, `schemas/`, `security-considerations.md` |

The repository’s role is evidentiary. It helps record why a translation was permitted, conditioned, rejected, or stopped.

---

## Classification Boundary

The repository does not classify AI systems as high-risk. Classification requires legal and domain analysis involving intended purpose, use context, product role, Annex I or Annex III categories, provider and deployer status, and applicable law.

What the repository can do:

| Supported | Not Supported |
|---|---|
| Record intended task and source-to-decision pathway | Determine legal high-risk classification |
| Preserve evidence for human review | Perform conformity assessment |
| Record human authorization | Replace legal, regulatory, or domain review |
| Document abstention and rejection | Certify compliance |
| Identify governance limits | Authorize market placement or deployment |

A pack may support classification analysis by making intended use and task boundary visible. It does not decide classification.

---

## Article-Oriented Mapping

| Article-Oriented Concern | Repository Evidence | Limit |
|---|---|---|
| Risk management system | Translation verdicts and rejection records show risk treatment at the research translation layer | Continuous lifecycle risk management must be supplied by the institution |
| Data and data governance | Source capture and run inputs show what material entered translation | Dataset quality, representativeness, bias, and data rights require separate review |
| Technical documentation | Pack artifacts document translation method and decision path | Full system documentation for production AI requires broader artifacts |
| Record-keeping | Run logs and decision summaries preserve reviewable evidence | Logging requirements for production systems are outside this reference implementation |
| Transparency and information | Decision summaries disclose rationale, confidence, and limitations | User-facing notices and deployer instructions require context-specific drafting |
| Human oversight | Human gate preserves accept, override, reject decisions | Oversight effectiveness depends on reviewer competence and institutional authority |
| Accuracy, robustness, cybersecurity | Evaluation plans, validation scripts, and security notes support review | Formal testing, red teaming, cybersecurity controls, and monitoring require additional systems |

---

## Evidence Use Cases

| Institutional Use Case | How the Repository Helps |
|---|---|
| Pre-deployment review | Shows how a research source was translated into a bounded task |
| Vendor claim review | Separates vendor evidence from adoption authority |
| Research-backed control design | Converts guidance into control points and evidence artifacts |
| Human oversight evidence | Shows that candidate output required human authorization |
| Rejection documentation | Shows why a research idea was not operationalized |
| Audit preparation | Provides reconstructable decision summaries |

The repository is strongest before deployment, where organizations decide whether research evidence supports a controlled implementation path.

---

## Required Legal Boundary Language

Use this language in institutional settings:

```text
This repository provides research software for governed research-to-decision translation. It does not provide legal advice, regulatory classification, conformity assessment, CE marking support, or compliance certification. Any EU AI Act analysis requires independent legal, technical, domain, security, and governance review by the responsible organization.
```

---

## Reviewer Checklist

Before using a pack as evidence in an EU AI Act oriented review, ask:

- What intended use does the task record?
- Does the source-to-decision path preserve provenance?
- Does the task boundary make human oversight meaningful?
- Does the decision summary record confidence and limitations?
- Does the pack identify whether the source was accepted, conditioned, rejected, or excluded?
- What legal or regulatory questions remain outside the repository?
- Which Article 9 through 15 evidence concerns are supported by actual artifacts?
- Which evidence concerns require external controls?

The mapping is useful only when the repository’s limits remain visible.
