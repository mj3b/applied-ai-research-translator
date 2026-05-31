# Specifications

The `docs/specifications/` directory defines the technical and governance specifications for Applied AI Research Translator. These documents explain how the repository turns research sources into governed artifacts, how verdicts are assigned, when the system should abstain or reject, how human authority is preserved, and how a reviewer reconstructs a completed decision path.

This directory is written for researchers, auditors, institutional reviewers, and technical contributors who need to inspect the control model without reading the entire codebase first.

---

## Specification Inventory

| Specification | Main Question | Primary Audience | Governance Function |
|---|---|---|---|
| `artifact-model.md` | What artifacts must exist from source capture through final decision? | Researchers, auditors, contributors | Defines the object model of governed research translation |
| `translation-verdicts.md` | How does the repository decide whether research can become a bounded task? | AI governance researchers, institutional reviewers | Defines positive, conditional, negative, and rejection outcomes |
| `abstention-model.md` | When should the system stop, decline, or require human review? | Safety researchers, technical contributors | Preserves abstention as a control, not a failure |
| `human-gate.md` | Where does human authority enter the workflow? | Institutional reviewers, auditors, governance teams | Defines accept, override, reject, and accountability records |
| `audit-reconstruction.md` | How can a later reviewer reconstruct the decision path? | Auditors, researchers, governance teams | Defines the trace from source material to decision summary |

---

## How to Read This Directory

Start with `artifact-model.md`. It defines the artifacts that every other specification assumes. Then read `translation-verdicts.md`, because verdicts explain how the system distinguishes research usefulness from operational readiness.

Read `abstention-model.md` and `human-gate.md` together. Abstention defines when the system must stop. The human gate defines who can authorize continuation, override a proposed result, or reject operationalization.

Read `audit-reconstruction.md` last. It shows how the artifacts, verdicts, abstention decisions, and human-gate records become an inspectable decision trail.

---

## Specification Layer

```text
research source
  ↓
artifact model
  ↓
translation verdict
  ↓
abstention or bounded execution
  ↓
human gate
  ↓
audit reconstruction
```

The specifications do not replace schemas or scripts. The schemas enforce artifact structure. The scripts test artifacts. These documents explain why the controls exist and how they should be interpreted.

---

## Relationship to Root Documentation

| Root Document | Relationship to Specifications |
|---|---|
| `RESEARCH-RATIONALE.md` | Explains why research translation requires governance |
| `TRANSLATION-METHOD.md` | Defines the method used to translate source material into claims, tasks, and decisions |
| `GOVERNANCE-MODEL.md` | Defines the control architecture and authority boundary |
| `TRACEABILITY.md` | Defines source-to-decision reconstruction across the repository |
| `LIMITATIONS.md` | Defines what the repository does not prove or certify |

The specifications sit between the root documents and the implementation. They translate the governance theory into artifact-level controls.

---

## Directory Structure

```text
docs/specifications/
├── README.md
├── artifact-model.md
├── translation-verdicts.md
├── abstention-model.md
├── human-gate.md
└── audit-reconstruction.md
```

---

## Status

This directory is a v1.1 research-grade documentation layer. It should be treated as part of the archival release because it explains the governed artifact model that makes the repository citable as research software rather than only as a code prototype.
