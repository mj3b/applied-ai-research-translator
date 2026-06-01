# Governance Documentation

The `docs/governance/` directory contains the institutional governance documentation for Applied AI Research Translator. These files explain how external research sources enter the repository, how source risk is classified, how online research is controlled, how security concerns are handled, how standards-facing evidence is mapped, and how reviewers should evaluate a pack before relying on it.

This directory is the bridge between the repository’s root governance model and the concrete pack artifacts.

---

## Directory Purpose

Applied AI research often enters practice through papers, preprints, PDFs, benchmark claims, technical reports, vendor materials, standards guidance, source repositories, and online commentary. The governance problem begins before a model runs. It begins when a source starts to influence an institutional decision.

This directory defines the controls that should exist before source material becomes a claim, task, evaluation plan, or decision summary.

```text
source material
  ↓
provenance controls
  ↓
safety-policy intake
  ↓
online research controls
  ↓
security review
  ↓
standards mapping
  ↓
institutional review
```

The ordering matters. Provenance says what the source is. Safety-policy intake says what risk domain it touches and what translation boundary applies. Security review says whether the source or workflow creates unsafe handling conditions. Standards mapping explains which governance evidence the artifact may support. Institutional review decides whether the result can be used.

---

## Governance File Inventory

| File | Primary Question | Main Reader | Governance Function |
|---|---|---|---|
| `research-provenance.md` | What source was used, under what version, and with what evidentiary status? | Researchers, auditors, citation reviewers | Defines source capture, versioning, source volatility, and evidence status |
| `safety-policy-intake.md` | How should AI safety and policy sources be classified before translation? | AI safety researchers, policy reviewers, governance practitioners | Defines the intake gate for evidence type, risk domain, autonomy relevance, review authority, and translation boundary |
| `online-research-controls.md` | How should PDFs, web pages, reports, repositories, and preprints be governed before translation? | Researchers, governance reviewers, security reviewers | Defines intake controls for mutable, online, and externally authored sources |
| `security-considerations.md` | What security risks arise when external source material enters AI-assisted workflows? | Security reviewers, repository maintainers, institutional users | Defines risks around prompt injection, source poisoning, secrets, dependencies, logs, and sensitive data |
| `institutional-review-template.md` | How should an institution review a pack before relying on it? | Governance boards, review committees, auditors | Provides a structured review template for source, claim, task, evaluation, oversight, security, and final decision |
| `nist-ai-rmf-mapping.md` | How does the repository support NIST AI RMF evidence? | Governance teams, AI risk reviewers, auditors | Maps repository artifacts to Govern, Map, Measure, and Manage support |
| `eu-ai-act-mapping.md` | How does the repository support EU AI Act oriented evidence review? | Policy teams, legal reviewers, governance teams | Maps artifacts to selected documentation, record-keeping, transparency, oversight, and risk-management concerns |
| `iso-42001-mapping.md` | How can the repository support an AI management system process? | AI management system owners, auditors, governance teams | Maps repository artifacts to selected AI management system evidence without claiming certification |

---

## Why `safety-policy-intake.md` Belongs Here

The safety-policy intake gate is governance documentation, not only schema documentation. The schema validates the structure of `safety_policy_intake.json`. The governance document explains why the artifact exists and how reviewers should interpret it.

The intake file answers a question that the rest of the pack cannot answer on its own:

```text
What kind of authority should this source be allowed to have?
```

For ordinary research translation, provenance and claim extraction may be sufficient to begin review. For AI safety and policy work, that is too weak. A source may touch capability forecasting, misuse, loss of control, model-weight security, compute governance, liability, international governance, or concentration of power. Each category implies a different review path and translation boundary.

The intake gate prevents these sources from entering a uniform task-conversion pipeline.

---

## Relationship to Root Documents

| Root Document | Relationship to this Directory |
|---|---|
| `RESEARCH-RATIONALE.md` | Explains why research translation needs governance before operational use |
| `TRANSLATION-METHOD.md` | Defines the source-to-claim-to-task-to-decision method |
| `GOVERNANCE-MODEL.md` | Defines the authority boundary, human gate, abstention, and audit logic |
| `TRACEABILITY.md` | Defines how a reviewer reconstructs the source-to-decision path |
| `LIMITATIONS.md` | Defines what the repository does not prove, certify, or authorize |
| `CONTRIBUTING.md` | Defines how contributors should add packs, schemas, and governance artifacts |

The root documents state the method. This directory specifies institutional controls around that method.

---

## Relationship to Specifications

| Specification File | Governance Connection |
|---|---|
| `docs/specifications/artifact-model.md` | Defines the artifact chain that governance files help interpret |
| `docs/specifications/translation-verdicts.md` | Defines positive, negative, conditional, and rejection verdicts used by governance review |
| `docs/specifications/abstention-model.md` | Defines when the translator should stop, reject, or require human review |
| `docs/specifications/human-gate.md` | Defines the human authorization boundary used in institutional review |
| `docs/specifications/audit-reconstruction.md` | Defines how the decision path can be reconstructed from artifacts |

The specifications define artifact logic. The governance documents define institutional use.

---

## Governance Reading Order

Read the documents in this order when reviewing a safety-relevant pack:

| Step | Read | Reason |
|---:|---|---|
| 1 | `research-provenance.md` | Establish source identity, version, evidentiary status, and source volatility |
| 2 | `safety-policy-intake.md` | Classify AI safety and policy relevance before translation |
| 3 | `online-research-controls.md` | Assess controls for web, PDF, repository, benchmark, report, and preprint sources |
| 4 | `security-considerations.md` | Check prompt injection, source poisoning, secret exposure, dependency, and logging risks |
| 5 | Relevant standards mapping | Understand what evidence the pack may support without overstating compliance |
| 6 | `institutional-review-template.md` | Conduct structured review before relying on the pack |

This order mirrors the governance path from source to institutional decision.

---

## Standards Mapping Boundary

The mappings in this directory are interpretive evidence maps. They should not be read as compliance assertions.

| Mapping | What it Supports | What it Does Not Claim |
|---|---|---|
| NIST AI RMF | Evidence support for Govern, Map, Measure, and Manage | Enterprise-wide AI RMF implementation |
| EU AI Act | Documentation, record-keeping, human oversight, transparency, and risk-evidence support | Legal classification, conformity assessment, or regulatory compliance |
| ISO/IEC 42001 | Selected AI management system evidence | Certification, audit readiness, or full AI management system coverage |

NIST AI RMF is organized around Govern, Map, Measure, and Manage. The safety-policy intake gate is closest to Govern and Map because it records source context, risk domain, required review, and translation boundary before evaluation or management decisions occur.

---

## Governance Review Questions

A reviewer should be able to answer these questions before relying on a pack:

- What source material was used?
- Is the source version stable and reconstructable?
- What kind of evidence does the source provide?
- Does the source touch AI safety or policy domains?
- Does the source raise misuse, autonomy, loss-of-control, security, legal, compute, or model-weight concerns?
- What translation boundary applies?
- Who must review the source before task design?
- What standards-facing evidence does the pack support?
- What claims remain unsupported?
- Where should the translator abstain, restrict, or reject?
- What final decision can be reconstructed from the artifacts?

A pack that cannot answer these questions should remain below decision-complete maturity.

---

## Directory Structure

```text
docs/governance/
├── README.md
├── research-provenance.md
├── safety-policy-intake.md
├── online-research-controls.md
├── security-considerations.md
├── institutional-review-template.md
├── nist-ai-rmf-mapping.md
├── eu-ai-act-mapping.md
└── iso-42001-mapping.md
```

---

## Status

This directory is part of the repository’s governance layer. It should be updated whenever a new governed artifact changes how source material enters the pack, how risks are classified, how review authority is assigned, or how decisions are reconstructed.

The safety-policy intake gate strengthens the repository for AI safety and policy research by adding a review step before claim extraction and task design. That step is necessary because safety-relevant sources can be analytically valuable while still being unsuitable for bounded task translation.
