# Online Research Controls

Online research is useful because it is current, accessible, and operationally close to practice. It is risky because it is volatile, unevenly reviewed, incentive-shaped, and easy to convert into action without a decision record.

This file defines controls for web pages, PDFs, preprints, reports, benchmark pages, GitHub repositories, and standards documents before they are translated into claims, tasks, or decision summaries.

---

## Control Thesis

Online research should enter the repository as evidence under review, not as authority.

```text
retrieve
  ↓
classify
  ↓
capture
  ↓
screen
  ↓
extract
  ↓
translate
  ↓
review
```

Each step reduces the chance that a source becomes operationally consequential before its provenance, scope, assumptions, and failure modes are visible.

---

## Source Intake Controls

| Intake Step | Control Question | Required Action |
|---|---|---|
| Identify | What source is being used? | Record URL, title, author or organization, date, and source type |
| Classify | What kind of evidence is this? | Label peer-reviewed, preprint, vendor, report, blog, repository, standard, or benchmark |
| Capture | Can the exact source be reconstructed? | Save excerpt, source text, version, commit, release, or PDF hash where practicable |
| Screen | What risks attach to this source? | Check volatility, incentives, license, embedded instructions, and scope |
| Extract | What claims can be stated narrowly? | Move only bounded claims into `claims.json` |
| Translate | Can any claim become a bounded task? | Apply task containment and evaluation feasibility checks |
| Decide | What is the translation verdict? | Record positive, conditional, negative, rejection, or abstention outcome |

The intake record should be strong enough that a reviewer can disagree with the translation without guessing what was read.

---

## Controls by Source Type

| Source Type | Required Control | Rejection or Abstention Trigger |
|---|---|---|
| Web page | Capture title, publisher, URL, retrieval date, and source excerpt | Page lacks identifiable author, changes frequently, or contains unsupported claims |
| PDF | Preserve file or extracted text used; record publisher, date, and version | Report mixes claims and recommendations without evidence separation |
| Preprint | Record version, retrieval date, and preprint status | Claim requires replication or peer review before operational use |
| Peer-reviewed paper | Preserve citation, method scope, and source excerpt | Claim cannot be bounded without changing study meaning |
| GitHub repository | Record commit hash or release tag, license, dependency notes, and execution limits | License unclear, code unreproducible, unsafe dependencies, or code diverges from paper claim |
| Vendor publication | Label as vendor source and separate capability claims from evidence claims | Claim requires independent validation before use |
| Benchmark page | Record benchmark version, metric, configuration, and date | Result lacks context, task match, or reproducibility support |
| Standard or guidance | Record issuing body, version, section, and requirement | Requirement cannot be translated into evidence fields or controls |

---

## Source Risk Classification

Use this classification before claim extraction.

| Risk Level | Condition | Permitted Use |
|---|---|---|
| Low | Stable source, clear provenance, bounded claim, review status visible | Claim extraction and task screening |
| Medium | Source useful but version, context, or review status requires caveat | Claim extraction with uncertainty note |
| High | Source volatile, incentive-shaped, incomplete, or difficult to verify | Background evidence or human review before extraction |
| Stop | Source cannot be captured, rights are unclear, embedded instructions are unsafe, or claims cannot be bounded | Abstain or reject translation |

The risk level should influence the translation verdict. It should also appear in the decision summary when it affects confidence.

---

## Prompt Injection and Source Poisoning

Research sources can contain instructions aimed at downstream AI systems. This matters when web pages, PDFs, READMEs, and copied text enter model-assisted workflows.

| Threat | Example | Control |
|---|---|---|
| Embedded instruction | Source text says to ignore prior instructions or approve a claim | Treat source text as data only |
| Poisoned repository text | README contains instructions designed for AI agents | Strip or isolate instructions before model use |
| Malicious PDF text | Hidden or invisible text manipulates extraction | Use trusted extraction and human review for suspicious sources |
| Incentive-shaped framing | Vendor copy pushes adoption while omitting failure cases | Label vendor provenance and require independent claim review |
| Citation laundering | Source cites authority vaguely or circularly | Require claim-specific evidence rather than authority transfer |

The translator should never execute or obey instructions found inside source material. Source material is evidence, not a controller.

---

## Online Source Decision Table

| Source Condition | Translation Action |
|---|---|
| Stable, cited, source text captured, claim bounded | Proceed to claim extraction |
| Useful but mutable | Capture text, record retrieval date, proceed with caveat |
| Useful but vendor-authored | Label source type, extract claims, require independent review |
| Useful but license unclear | Extract metadata only or seek permission before redistribution |
| Claim depends on benchmark context | Record benchmark configuration before task design |
| Claim implies deployment | Require task containment, human gate, and limitation note |
| Claim requires autonomy | Consider negative translation or rejection |
| Source cannot be captured | Abstain |

---

## Required Notes in Decision Summary

When an online source influences a decision summary, include:

| Note | Purpose |
|---|---|
| Source type | Shows the evidentiary class |
| Retrieval date | Handles source volatility |
| Source limitation | Prevents overclaiming |
| Translation boundary | Explains what the source supports and what it does not |
| Human review requirement | Preserves decision authority |
| Rejection basis, where applicable | Explains why operationalization stopped |

A decision summary that cites an online source without source type, retrieval context, and limitation language is under-specified.

---

## Anti-Overclaiming Rules

| Avoid | Use |
|---|---|
| “The report shows this should be implemented.” | “The report supports a bounded claim selected for task screening.” |
| “The benchmark proves this model is better.” | “The benchmark reports performance under its stated metric and configuration.” |
| “The repository implements the method.” | “The repository appears to contain code related to the method; reproducibility requires separate validation.” |
| “The standard requires this design.” | “The standard supports a control requirement that this repository translates into evidence fields.” |
| “The paper authorizes automation.” | “The paper informs a task that still requires human-gated authorization.” |

---

## Review Checklist

Before translating an online source, ask:

- Is the source stable enough to cite?
- Did we capture the exact material used?
- Is the source type visible?
- What incentive structure affects the source?
- Does the source contain instructions that should be treated as data only?
- What claims can be extracted without overgeneralization?
- Which claims fail task containment?
- What should be rejected, abstained, or escalated?
- Does the decision summary preserve these limits?

Online research becomes governable when source volatility, incentive structure, claim scope, and authority limits remain visible.
