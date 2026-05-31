# Assets

The `assets/` directory contains visual reference material for Applied AI Research Translator. These diagrams support the repository’s research, governance, and reviewer documentation by making the decision architecture visible.

The assets are intended for README sections, release notes, ORCID or Zenodo descriptions, presentations, and institutional review discussions.

---

## Asset Inventory

| Asset | Purpose | Best Placement |
|---|---|---|
| `research-to-decision-pipeline.svg` | Shows the full pathway from research source to decision summary | `README.md`, `RESEARCH-RATIONALE.md`, `TRANSLATION-METHOD.md` |
| `governance-boundary.svg` | Shows the boundary between AI evidence generation and human decision authority | `GOVERNANCE-MODEL.md`, `docs/specifications/human-gate.md` |
| `artifact-traceability-map.svg` | Shows source-to-decision traceability across repository artifacts | `TRACEABILITY.md`, `docs/specifications/audit-reconstruction.md` |
| `human-gate-decision-record.svg` | Shows accept, override, reject, and abstain as human-gated decision states | `GOVERNANCE-MODEL.md`, `docs/specifications/human-gate.md` |

---

## How to Embed

Use standard Markdown image syntax.

```markdown
![Research-to-decision pipeline](assets/research-to-decision-pipeline.svg)
```

From a document inside `docs/`, use the relative path back to the repository root.

```markdown
![Governance boundary](../../assets/governance-boundary.svg)
```

From a document inside `docs/specifications/` or `docs/governance/`, use:

```markdown
![Artifact traceability map](../../assets/artifact-traceability-map.svg)
```

---

## Visual Design Logic

The diagrams use a restrained research-documentation style. Each graphic is designed to communicate a control structure rather than decorate the repository.

| Design Choice | Reason |
|---|---|
| Linear artifact flow | Makes the source-to-decision pathway inspectable |
| Separate evidence and authority zones | Prevents model output from being visually implied as final authority |
| Reconstructable artifact labels | Helps auditors locate the relevant files |
| Explicit rejection and abstention states | Preserves stop conditions as first-class governance outcomes |

---

## Governance Interpretation

These assets should be read as visual summaries of repository controls.

They do not expand the repository’s authority. They do not claim production safety, regulatory compliance, certification, or empirical validation. They show the governance model documented in the root files and specifications.

The governing question for every asset is:

```text
What prevents research evidence from becoming operational authority by default?
```
