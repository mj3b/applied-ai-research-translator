# Institutional Review Template

This template helps an institution review a research translation pack before relying on it for governance, implementation, procurement, evaluation, policy translation, or AI adoption decisions.

The template is designed for governance boards, AI review committees, research teams, compliance teams, technical reviewers, and AI safety reviewers.

---

## Review Header

| Field | Entry |
|---|---|
| Pack ID |  |
| Review date |  |
| Reviewer name or role |  |
| Review body or team |  |
| Source title |  |
| Source type |  |
| Source version or retrieval date |  |
| Proposed use |  |
| Decision requested |  |
| Review status | Draft / Reviewed / Approved with conditions / Rejected / Escalated |

---

## 1. Source Review

| Question | Reviewer Finding |
|---|---|
| What source material was used? |  |
| Is the source captured or reconstructable? |  |
| What is the source type? |  |
| What evidentiary status does the source carry? |  |
| What incentives or conflicts may affect the source? |  |
| What licensing or rights constraints apply? |  |
| What source limitations must be preserved? |  |

Review judgment:

```text
Source is adequate / Source requires caveat / Source is inadequate / Source requires escalation
```

---

## 2. Claim Review

| Question | Reviewer Finding |
|---|---|
| Which claims were extracted? |  |
| Are the claims source-linked? |  |
| Are the claims falsifiable? |  |
| Are the claims scoped to the source evidence? |  |
| Which claims are excluded from task design? |  |
| Which claims require additional evidence? |  |
| Does any claim overstate the source? |  |

Review judgment:

```text
Claims are adequate / Claims require revision / Claims are too broad / Claim extraction should stop
```

---

## 3. Task Boundary Review

| Question | Reviewer Finding |
|---|---|
| What task is proposed? |  |
| Which claim supports the task? |  |
| Are inputs defined? |  |
| Are outputs defined? |  |
| Are constraints defined? |  |
| Are failure conditions defined? |  |
| Does the task require autonomy beyond the repository boundary? |  |
| Can a human reviewer meaningfully accept, override, or reject the result? |  |

Review judgment:

```text
Task is bounded / Task requires conditions / Task exceeds boundary / Reject translation
```

---

## 4. Evaluation Review

| Question | Reviewer Finding |
|---|---|
| What evidence would count as success? |  |
| What evidence would count as failure? |  |
| What should trigger abstention? |  |
| Are metrics or review criteria declared before execution? |  |
| Does the evaluation plan match the claim? |  |
| Does the evaluation plan require domain expertise? |  |
| What uncertainty remains? |  |

Review judgment:

```text
Evaluation is adequate / Evaluation requires revision / Evaluation is insufficient / Escalate
```

---

## 5. Human Oversight Review

| Question | Reviewer Finding |
|---|---|
| Who has authority to approve the final output? |  |
| Is reviewer competence sufficient for the domain? |  |
| Can the reviewer override the output? |  |
| Can the reviewer reject the output? |  |
| Is escalation required? |  |
| Is the human gate recorded in the artifact trail? |  |

Review judgment:

```text
Human oversight is meaningful / Human oversight requires stronger authority / Human gate is insufficient
```

---

## 6. Security and Rights Review

| Question | Reviewer Finding |
|---|---|
| Does the pack contain confidential, personal, proprietary, or regulated data? |  |
| Does the source contain embedded instructions or injection risk? |  |
| Are repository dependencies safe for the intended use? |  |
| Are credentials excluded from source, logs, and examples? |  |
| Can the source material be stored and redistributed? |  |
| Do logs require redaction or retention controls? |  |

Review judgment:

```text
Security cleared / Security cleared with conditions / Security requires escalation / Do not proceed
```

---

## 7. Standards and Policy Mapping

| Framework or Standard | Relevant Question | Reviewer Finding |
|---|---|---|
| NIST AI RMF | Does the pack support Govern, Map, Measure, or Manage evidence? |  |
| EU AI Act | Does the pack support documentation, oversight, record-keeping, or risk evidence? |  |
| ISO/IEC 42001 | Does the pack support an AI management system process? |  |
| Internal AI policy | Which institutional requirement does the pack support? |  |
| Domain-specific rule | Does the intended use require legal, clinical, financial, educational, or other domain review? |  |

Review judgment:

```text
Mapping useful / Mapping incomplete / Mapping requires legal or compliance review / Mapping out of scope
```

---

## 8. Decision

Choose one.

| Decision | Meaning |
|---|---|
| Approve translation | The pack supports continued bounded task work |
| Approve with conditions | The pack may proceed only under the stated conditions |
| Reject translation | The source should not become an operational task under this repository boundary |
| Abstain | Evidence is insufficient to decide |
| Escalate | Decision requires legal, security, compliance, ethics, domain, or executive review |

Decision selected:

```text

```

Conditions:

```text

```

Rationale:

```text

```

Remaining uncertainty:

```text

```

Required next evidence:

```text

```

---

## 9. Final Reviewer Statement

Use or adapt:

```text
Based on the source material, extracted claims, task boundary, evaluation plan, security review, and human oversight record, this pack is [approved / approved with conditions / rejected / abstained / escalated]. The decision is limited to governed research-to-decision translation and does not authorize production deployment, legal compliance, regulatory classification, or institutional adoption outside the recorded scope.
```

---

## Review Standard

The review is complete when the decision can be reconstructed by a later reviewer from the pack artifacts and this review record.

A weak review says whether the reviewer likes the output. A strong review shows where authority entered the decision.
