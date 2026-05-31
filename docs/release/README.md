# Release Documentation

The `docs/release/` directory records release-level decisions for Applied AI Research Translator. These documents explain what changed, why the release exists, what evidence supports the release, what remains limited, and how the release should be cited or reviewed.

Release notes in this repository are governance artifacts. They should make method changes, documentation changes, schema changes, example-pack changes, validation status, and archival metadata visible to researchers and institutional reviewers.

---

## Release Inventory

| Release File | Purpose | Primary Reader |
|---|---|---|
| `v1.0-release-notes.md` | Records the initial decision-complete reference implementation | Researchers, reviewers, early adopters |
| `v1.1-release-notes.md` | Records the research-grade archival release and documentation expansion | Zenodo, ORCID, researchers, governance reviewers |
| `v1.1-release-checklist.md` | Provides the pre-release validation and publication checklist | Repository maintainer |
| `v1.1-archival-statement.md` | Explains why v1.1 is a scholarly archival release rather than a cosmetic update | Zenodo, ORCID, research community |
| `v1.1-reviewer-brief.md` | Gives reviewers a compressed guide to what should be inspected | External reviewers, collaborators, institutional readers |

---

## Why Release Documentation Matters

A research software release needs more than a tag. It needs a record of what the release means.

```text
code state
  ↓
artifact state
  ↓
documentation state
  ↓
validation state
  ↓
citation state
  ↓
archival state
```

The release directory keeps those states separate. That matters because the repository is not only software. It is a governed research-to-decision artifact.

---

## Release Classification

| Release Type | Meaning | Example |
|---|---|---|
| Implementation release | Changes runtime, schemas, scripts, or pack behavior | New runloop feature, schema revision, validation script |
| Documentation release | Changes the research explanation, governance model, traceability, or limitations | v1.1 documentation expansion |
| Archival release | Prepares the repository for citation, DOI, ORCID, Zenodo, or scholarly review | v1.1 |
| Method release | Changes the translation method or verdict logic | Future v2.0 candidate |
| Evidence release | Adds packs, demo runs, validation results, or decision summaries | Future pack expansion |

v1.1 is best described as a research-grade archival and documentation release. It strengthens interpretability, citation, and review without claiming that the repository has become a production platform.

---

## Relationship to Root Documentation

| Root File | Release Role |
|---|---|
| `README.md` | Public-facing project overview |
| `RESEARCH-RATIONALE.md` | Release rationale for why research translation requires governance |
| `TRANSLATION-METHOD.md` | Method statement for source-to-decision translation |
| `GOVERNANCE-MODEL.md` | Governance architecture for authority, abstention, human gate, and audit record |
| `TRACEABILITY.md` | Source-to-decision reconstruction model |
| `LIMITATIONS.md` | Limitation register and anti-overclaiming boundary |
| `CITATION.cff` | Machine-readable citation metadata |
| `NOTICE` | Attribution, legal, research, and governance notice |

The release notes should not repeat these documents in full. They should explain how each document changes the release’s scholarly and governance status.

---

## Directory Structure

```text
docs/release/
├── README.md
├── v1.0-release-notes.md
├── v1.1-release-notes.md
├── v1.1-release-checklist.md
├── v1.1-archival-statement.md
└── v1.1-reviewer-brief.md
```

---

## Release Standard

A release is ready when a reviewer can answer these questions:

- What changed?
- Why did the change matter?
- Which artifacts support the change?
- Which claims remain limited?
- What should be cited?
- What should not be inferred from the release?

The final standard is simple: a release note should make the repository easier to trust because it makes the repository easier to inspect.
