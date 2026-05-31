# Governance Documentation

The `docs/governance/` directory translates the repository’s governance model into institutional review controls. It is designed for researchers, AI governance reviewers, AI safety teams, auditors, policy translators, and institutional decision-makers who need to understand how research-derived evidence should be controlled before it influences operational action.

The root `GOVERNANCE-MODEL.md` defines the architecture. This directory applies that architecture to source provenance, online research intake, standards alignment, security review, and institutional evaluation.

---

## Directory Purpose

Research translation is a decision pathway. It begins when a person or system treats external research as relevant to an institutional question. It becomes risky when the pathway from source to claim, task, output, and decision is invisible.

This directory exists to make that pathway inspectable.

| Governance File | Primary Question | Reviewer Use |
|---|---|---|
| `research-provenance.md` | What source was used, under what version, and with what evidentiary status? | Source intake, citation review, audit reconstruction |
| `online-research-controls.md` | How should PDFs, web pages, repositories, reports, and preprints be governed before translation? | Research intake, source screening, source-risk classification |
| `nist-ai-rmf-mapping.md` | How does the repository align with NIST AI RMF functions? | AI governance mapping and control explanation |
| `eu-ai-act-mapping.md` | How does the repository support evidence relevant to high-risk AI system review? | EU AI Act oriented traceability and oversight mapping |
| `iso-42001-mapping.md` | How does the repository support AI management system evidence? | AI management system governance and continual improvement mapping |
| `security-considerations.md` | What security risks arise when research sources enter AI-assisted workflows? | Security review, source poisoning review, prompt injection review |
| `institutional-review-template.md` | How should an institution review a pack before relying on it? | Governance board, research committee, compliance review |

---

## Governance Layer

```text
root governance model
  ↓
source provenance controls
  ↓
online research controls
  ↓
standards mappings
  ↓
security review
  ↓
institutional review template
```

The files in this directory should be read with the root-level documents:

| Root Document | Relationship |
|---|---|
| `README.md` | States the repository’s central claim: research translation is a governance problem |
| `GOVERNANCE-MODEL.md` | Defines the authority boundary, human gate, abstention model, translation verdicts, and audit reconstruction |
| `RESEARCH-RATIONALE.md` | Explains why research sources require control before operational use |
| `TRANSLATION-METHOD.md` | Defines the source-to-claim-to-task method |
| `TRACEABILITY.md` | Defines how a reviewer reconstructs the decision path |
| `LIMITATIONS.md` | Defines what the repository does not prove, certify, or authorize |

---

## Governance Claim

The repository does not govern AI in the abstract. It governs a narrower and more inspectable problem: the translation of applied AI research into decision artifacts.

That scope matters. A research paper can inform institutional judgment. It cannot authorize operational action by itself. A governed translation system must preserve the steps that sit between the paper and the decision.

---

## Directory Structure

```text
docs/governance/
├── README.md
├── research-provenance.md
├── online-research-controls.md
├── nist-ai-rmf-mapping.md
├── eu-ai-act-mapping.md
├── iso-42001-mapping.md
├── security-considerations.md
└── institutional-review-template.md
```

---

## Review Standard

A governance document in this directory succeeds when it lets a reviewer answer one question with evidence:

```text
What prevents this research source from becoming operational authority by default?
```

The answer should point to source capture, claim extraction, task containment, evaluation criteria, schema validation, abstention, human-gate authorization, and decision-summary reconstruction.
