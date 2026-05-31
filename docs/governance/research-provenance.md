# Research Provenance

Research provenance is the record of where source material came from, what version was used, what evidentiary status it carried, and how it entered the translation workflow.

Applied AI research enters institutional workflows through papers, preprints, PDFs, reports, repositories, vendor publications, policy guidance, benchmark writeups, and web pages. These sources differ in review status, stability, incentives, licensing, and operational assumptions. Provenance controls make those differences visible before claims become tasks.

---

## Provenance Thesis

A research source should never enter task design as an untyped authority. It should enter as a governed source object with known limits.

```text
source identity
  ↓
source status
  ↓
source version
  ↓
source rights
  ↓
source assumptions
  ↓
source-derived claims
```

Provenance is the first control because every downstream artifact inherits its evidentiary strength from the source.

---

## Source Classification

| Source Type | Evidentiary Strength | Governance Concern | Required Provenance Record |
|---|---|---|---|
| Peer-reviewed paper | Higher scholarly review, bounded by venue and method | Findings may depend on study design, benchmark, dataset, or population | Citation, venue, publication date, source text, method limits |
| Preprint | Early research signal | Claims may change after review, revision, or replication | Version, retrieval date, source text, uncertainty note |
| PDF report | Institutional or technical evidence | Claims may mix evidence, interpretation, and recommendation | Publisher, date, source excerpt, claim separation |
| Vendor publication | Product or market evidence | Incentives may shape framing, omissions, or adoption claims | Publisher, product context, claim type, conflict note |
| Technical blog | Implementation insight | May lack peer review, stability, or complete methods | URL, retrieval date, author or organization, scope note |
| GitHub repository | Code or implementation evidence | Code may diverge from paper claims or carry dependency and license risks | Repository URL, commit or release, license, reproducibility note |
| Standard or guidance | Normative or control reference | May define obligations without implementation evidence | Version, issuing body, section, control translation note |
| Benchmark result | Comparative performance evidence | May depend on prompt, dataset, split, metric, or leaderboard conditions | Benchmark version, metric, date, configuration, caveat |

The classification does not decide whether a source is useful. It decides how much authority the translation process may assign to it.

---

## Minimum Provenance Fields

A mature pack should preserve these provenance fields where available.

| Field | Purpose |
|---|---|
| Source title | Identifies the source |
| Author or issuing body | Assigns origin |
| Publication venue or publisher | Indicates review and institutional context |
| Publication date | Supports chronology |
| Retrieval date | Handles mutable sources |
| Version, commit, DOI, or release | Supports stable citation |
| Source type | Distinguishes paper, preprint, PDF, report, web page, repository, or standard |
| License or rights note | Supports lawful reuse and redistribution |
| Source text path | Links to preserved text or excerpt |
| Scope note | Records where the source claims apply |
| Limitation note | Records known constraints before claim extraction |

These fields can live in `claims.json`, `decision_summary.json`, pack documentation, or a future dedicated `source_metadata.json`.

---

## Source Volatility

Online and pre-publication sources can change. A governed translation system should record what it used, not merely where it found it.

| Volatility Risk | Example | Control |
|---|---|---|
| Mutable web content | Blog post edited after translation | Preserve source excerpt and retrieval date |
| Preprint revision | arXiv version changes after claim extraction | Record version and date |
| Repository drift | GitHub main branch changes | Record commit hash or release tag |
| PDF replacement | Report is updated without clear version history | Preserve source file or excerpt used |
| Benchmark update | Leaderboard or metric changes | Record benchmark version and configuration |

A URL alone is weak provenance. A URL plus captured source text, version, and retrieval date is stronger.

---

## Provenance and Claim Strength

Source type should shape the claim’s strength.

| Source Condition | Appropriate Claim Strength |
|---|---|
| Peer-reviewed empirical paper with clear methods | Specific empirical claim within the study boundary |
| Preprint with limited replication | Provisional claim with version and uncertainty |
| Vendor report | Source-labeled claim requiring independent review |
| Blog post | Implementation observation, not generalizable evidence |
| Standard or guidance | Control or obligation translation, not empirical proof |
| Repository | Implementation evidence only after license, dependency, and reproducibility review |

The translation method should not flatten these distinctions. A claim extracted from a vendor report should not carry the same evidentiary weight as a replicated empirical finding.

---

## Provenance Failure Modes

| Failure Mode | Description | Governance Effect |
|---|---|---|
| Source laundering | A weak source gains authority because it appears inside a structured workflow | Downstream reviewers overtrust the artifact |
| Citation without capture | A source is named but the exact material used is missing | Reconstruction depends on external availability |
| Version ambiguity | The source changed after translation | Reviewers cannot know which claim was used |
| Incentive opacity | Vendor or institutional motive is hidden | Claims may be treated as neutral evidence |
| Context collapse | Study conditions disappear during task design | Claims become overgeneralized |
| Rights ambiguity | Source material is reused without license review | Redistribution risk increases |
| Repository drift | Code changes after extraction | Implementation evidence becomes unstable |

A provenance defect should be disclosed in the decision summary or limitation register.

---

## Recommended `source_metadata.json`

Future packs should consider adding a dedicated provenance file.

```json
{
  "source_id": "source_001",
  "source_type": "preprint",
  "title": "Example Applied AI Study",
  "authors": ["Author One", "Author Two"],
  "publisher_or_venue": "arXiv",
  "publication_date": "2026-01-15",
  "retrieved_at": "2026-05-31",
  "version": "v2",
  "url": "https://example.org/source",
  "doi": null,
  "license": "unknown",
  "captured_text_path": "sources/paper_text.txt",
  "known_limitations": [
    "Preprint status",
    "No independent replication recorded in pack"
  ],
  "translation_note": "Claims may support bounded evaluation tasks only after human review."
}
```

This file is optional for v1.1. It would strengthen v1.2 or later releases.

---

## Reviewer Checklist

Before accepting source material into translation, ask:

- What is the source type?
- Who produced it?
- What version was used?
- When was it retrieved?
- Can the exact source text be inspected later?
- Does the source carry licensing or redistribution limits?
- What assumptions constrain the source?
- What incentives may affect its claims?
- Which claims are empirical, normative, operational, or promotional?
- Does the decision summary preserve the source’s evidentiary status?

Provenance is adequate when the reviewer can identify exactly what material entered the translation process and how much authority it should carry.
