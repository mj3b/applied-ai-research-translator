# Research Rationale

**Applied AI Research Translator** exists because research artifacts increasingly move into operational AI decisions faster than institutions can reconstruct the reasoning that carried them there.

A paper, PDF, benchmark note, policy memo, online report, source repository, or vendor publication can contain useful evidence. It can also carry unstable assumptions, missing replication, incentive bias, incomplete methods, version drift, dual-use detail, or deployment conditions that disappear when a team turns the source into a task.

The governance problem begins at that conversion point.

This repository treats research translation as a controlled decision process. It converts source material into safety-policy intake classifications, falsifiable claims, bounded tasks, evaluation plans, schema-validated artifacts, human-gated decisions, and audit-ready summaries. The result is a research-to-decision record that can be inspected by researchers, principal investigators, governance teams, institutional boards, auditors, and technical implementers.

The shortest version:

```text
A research source can inform a decision.
It should not become decision authority by default.
```

---

## Reader Map

| Reader | Primary Question | Recommended Path |
|---|---|---|
| Principal investigator | What is the scholarly contribution, and why should this be treated as research software? | Read this file, then `README.md`, `CITATION.cff`, and `docs/release/v1.1-reviewer-brief.md`. |
| AI governance researcher | How does the system turn research into accountable institutional decisions? | Read this file, then `TRANSLATION-METHOD.md`, `GOVERNANCE-MODEL.md`, and `TRACEABILITY.md`. |
| AI safety researcher | Where are autonomy, misuse, loss of control, and unsupported operationalization constrained? | Start with `docs/governance/safety-policy-intake.md`, then inspect `packs/multi_agent_failure_modes_e0228882/`. |
| AI policy researcher | How are policy, standards, guidance, compute, model-weight, liability, and institutional review concerns routed? | Read `docs/governance/`, then compare `safety_policy_intake.json` with the standards mappings. |
| Institutional reviewer | What evidence supports a decision to translate, condition, restrict, reject, or defer? | Review `decision_summary.json`, source capture, safety-policy intake, claim extraction, and human-gate records. |
| Technical implementer | Which artifacts must exist before code execution or model calls begin? | Inspect `schemas/`, `scripts/`, `runloop/`, and `examples/runs/`. |
| Archivist or citation reviewer | Why should this repository be cited as software? | Read the research contribution statement, artifact model, release notes, and `CITATION.cff`. |

---

## Core Thesis

Research translation is a governance control point.

The institutional risk arises when a research artifact becomes an operational premise without a controlled record of how the artifact was interpreted, narrowed, classified, tested, rejected, or approved. Applied AI Research Translator addresses that gap by making each interpretive step explicit before downstream action occurs.

```mermaid
flowchart TD
    A[Research artifact] --> B[Source capture]
    B --> C[Safety-policy intake when applicable]
    C --> D[Claim extraction]
    D --> E[Operationalization analysis]
    E --> F[Translation verdict]
    F --> G[Locked task definition]
    G --> H[Evaluation plan]
    H --> I[Governed run or manual review]
    I --> J[Human gate]
    J --> K[Decision summary]

    A -. paper, PDF, report, repository, benchmark, policy source .-> A
    C -. capability, misuse, autonomy, loss of control, legal, compute, weights .-> C
    F -. positive, conditional, evaluation-only, policy-only, restricted, reject, abstain .-> F
    J -. accept, override, reject, abstain, escalate .-> J
```

This is a governance pattern before it is a software pattern. The software matters because it makes the pattern enforceable.

---

## The Research-to-Deployment Gap

Applied AI research often travels through a compressed path:

```text
Interesting paper → prototype idea → model-assisted task → workflow adoption → institutional reliance
```

That path is convenient. It is also governance-poor. Each arrow hides a decision: which claim was selected, which assumptions were preserved, which constraints were dropped, which safety concerns were ignored, which reviewer had authority, and which evidence justified movement to the next step.

Applied AI Research Translator replaces that compressed path with a governed path:

```text
Source
  ↓
Safety-policy intake, where applicable
  ↓
Claims
  ↓
Tasks
  ↓
Evaluation plan
  ↓
Governed execution or manual review
  ↓
Human gate
  ↓
Decision record
```

The system is built around a practical institutional finding: research does its best work when it informs decisions, and governance does its best work when it records how those decisions were made.

---

## Why Online Research Requires Governance

Research used in AI workflows now comes from a wide and uneven source surface. Some sources are peer reviewed. Some are preprints. Some are vendor claims. Some are policy guidance. Some are living web pages. Some are repositories with code, examples, dependencies, and undocumented assumptions.

A governance system must handle this source diversity before operational use.

| Source Type | Why Teams Use It | Main Governance Risk | Required Control |
|---|---|---|---|
| Peer-reviewed paper | Establishes scholarly basis for a method, evaluation, or risk control | Findings may depend on lab context, dataset boundary, population, or benchmark assumption | Extract claims, assumptions, limitations, and operational conditions before task design |
| Preprint | Provides early signal on emerging capability, failure mode, or mitigation | Review status, version drift, and replication status may remain unsettled | Record version, provenance, uncertainty, and review status in the pack |
| PDF report | Supplies board, policy, vendor, or institutional evidence | Narrative claims may combine empirical evidence, interpretation, and recommendation | Separate source claims from operational recommendations |
| Online publication | Identifies emerging patterns, field debate, or implementation insight | Content may change, disappear, or lack stable citation metadata | Capture source text, date, URL, and claim-level evidence |
| GitHub repository | Provides implementation detail, benchmark code, or reproducibility material | Code may diverge from the paper, omit constraints, or carry dependency and license risk | Validate license, dependency surface, reproducibility claim, and execution boundary |
| Vendor publication | Helps teams evaluate tools, platforms, and product categories | Incentives may favor capability claims and downplay failure cases | Label provenance, separate product claims from evidence, require independent review |
| Standards or guidance | Defines governance expectations and institutional duties | Guidance often states what must be governed while leaving evidence design open | Convert requirements into controls, owners, artifacts, and review thresholds |
| AI safety and policy source | Provides insight into capability, misuse, autonomy, governance, weights, compute, liability, or systemic risk | The source may become task-shaped before risk domain and review authority are assigned | Run safety-policy intake before claims become tasks |

The source may be useful. The source alone has limited institutional authority. Authority emerges from a governed record: what was extracted, why it was selected, how it was bounded, what evidence was produced, and who approved the result.

---

## The Added Safety-Policy Rationale

AI safety and policy sources require an earlier gate than ordinary research sources.

A paper about human-AI reliance can often be translated into bounded accept, override, calibration, and review tasks. A source about autonomous multi-agent failure modes, model-weight security, cyber misuse, frontier capability forecasting, or international verification has a different character. Its contribution may be analytically valuable while being unsafe or incoherent as an executable task.

That is why the repository adds `safety_policy_intake.json`.

The intake artifact asks:

```text
What kind of authority should this source be allowed to have?
```

It classifies the source before claim extraction and task design.

| Intake Dimension | Why It Matters |
|---|---|
| Source status | A peer-reviewed paper, preprint, policy memo, legal text, benchmark, and blog post carry different evidentiary force |
| Evidence type | Empirical findings, forecasts, scenarios, legal requirements, and policy arguments should not be treated as equivalent |
| AI safety domain | Misuse, loss of control, compute governance, model-weight security, and liability imply different review paths |
| Autonomy level | Advisory systems, bounded tool use, delegated tasks, and open-ended agents require different governance boundaries |
| Dual-use status | Some useful research lowers barriers for harmful actors |
| Oversight failure modes | Strategic deception, evaluation gaming, automation bias, and rubber-stamp review require stronger gates |
| Required review | AI safety, legal, security, governance, domain, or executive review may be necessary before translation |
| Translation boundary | The source may proceed, remain evaluation-only, remain policy-mapping-only, be restricted, be rejected, or abstain |

Without this gate, a safety-relevant source could enter task design too early. With it, the repository can preserve the research value while limiting operational authority.

---

## Failure Modes in Ungoverned Research Translation

Ungoverned research translation creates a familiar class of failures. The organization believes it is acting from evidence, while the evidence has already been transformed through informal interpretation.

| Failure Mode | What Happens | Institutional Consequence | Translator Control |
|---|---|---|---|
| Claim overextension | A narrow research finding becomes a broad operational premise | Deployment conditions exceed the evidence base | Require claim-level extraction and scope fields |
| Context collapse | Dataset, population, task setting, or benchmark assumptions vanish during adoption | The implemented task differs from the evaluated condition | Preserve source assumptions in `claims.json` and `eval_plan.json` |
| Authority laundering | A publication is treated as approval for implementation | Research evidence substitutes for institutional authorization | Require translation verdict and human gate |
| Safety-policy underclassification | Safety-relevant material enters task design without risk-domain classification | Misuse, autonomy, or loss-of-control concerns become ordinary execution details | Require `safety_policy_intake.json` |
| Version drift | A web source, repository, or preprint changes after review | Later reviewers cannot reconstruct the source state | Capture source text and version metadata |
| Incentive contamination | Vendor or advocacy material enters the workflow as neutral evidence | Procurement and governance decisions inherit source bias | Label provenance and require independent decision summary |
| Hidden task expansion | A bounded claim becomes an open-ended AI workflow | Autonomy and accountability surface expand silently | Lock task inputs, outputs, constraints, and failure conditions |
| Dual-use leakage | Useful details become operational instructions that lower barriers to harm | Research translation creates misuse surface | Route to restricted handling, redaction, or rejection |
| Audit gap | Reviewers see final output without the interpretive chain | Decision basis becomes irreconstructable | Produce deterministic `decision_summary.json` from artifacts |
| Rejection loss | Every research source becomes a candidate for implementation | Governance becomes adoption acceleration | Make negative translation and rejection first-class outcomes |

The most serious failure is rejection loss. A system that translates every source into action has already abandoned governance. A governed translator must preserve the ability to say: this research matters, and the system should still reject operational translation under current constraints.

---

## Governed Translation as Institutional Infrastructure

The repository treats governance as an execution architecture. Controls appear in files, schemas, run order, validation scripts, and decision artifacts.

| Governance Layer | Question Answered | Artifact Evidence |
|---|---|---|
| Provenance | What source material informed the decision? | `sources/paper_text.txt` and pack metadata |
| Safety-policy intake | What kind of evidence, risk domain, and translation boundary apply? | `safety_policy_intake.json` |
| Claim extraction | Which claims were selected from the source? | `claims.json` validated against `claims.schema.json` |
| Operationalization | Can the claim become a bounded task? | `tasks.json` and `eval_plan.json` |
| Translation verdict | Should the claim proceed, proceed with conditions, remain evaluation-only, remain policy-only, be restricted, or be rejected? | `decision_summary.json` |
| Execution boundary | What may the model do during a governed run? | `run_input.json`, task constraints, schema contracts |
| Validation | Did the output satisfy the expected structure? | `run_output.schema.json` and validation scripts |
| Human authority | Who accepted, overrode, rejected, abstained, or escalated the proposed output? | `human_gate.json` and final artifacts |
| Audit reconstruction | Can a reviewer rebuild the decision path later? | Logs, manifests, summaries, and traceability documentation |

This is why the repository is software rather than a framework memo. The governance claim is implemented as artifact discipline.

---

## Why Schema Validation Matters

Schema validation converts governance language into enforceable contracts. A policy can say that research claims should be traceable, scoped, and reviewed. A schema requires fields that make traceability, scope, review, and uncertainty visible.

| Schema | Governance Function |
|---|---|
| `safety_policy_intake.schema.json` | Requires source status, AI safety domain, autonomy profile, risk screen, governance mapping, and translation verdict |
| `agent_spec.schema.json` | Defines the permitted role, task boundary, and execution constraints |
| `claims.schema.json` | Requires claims to be structured, source-linked, and reviewable |
| `tasks.schema.json` | Locks task inputs, outputs, constraints, and failure conditions |
| `run_input.schema.json` | Captures the exact input state used in a governed run |
| `run_output.schema.json` | Requires model output to remain structured and machine-checkable |
| `decision_summary.schema.json` | Forces the final decision artifact to record outcome, rationale, and authority |

Schema enforcement gives researchers and reviewers a practical benefit: the system can fail closed. A missing intake field, malformed claim, incomplete task, invalid output, or incomplete decision record becomes a validation problem rather than an interpretive afterthought.

---

## Why Human-Gated Review Matters

The human gate is the authority boundary. The model may produce candidate evidence. It may produce structured output under a locked task. It may support classification, comparison, or extraction. It cannot authorize its own operational use.

| Decision State | Meaning | Record Required |
|---|---|---|
| Accept | The human reviewer approves the proposed output under stated constraints | Reviewer identity, timestamp, rationale, final artifact |
| Override | The human reviewer replaces or modifies the proposed output | Reviewer rationale, original proposal, revised final artifact |
| Reject | The human reviewer blocks the output from becoming final | Rejection reason, source evidence, unresolved issue |
| Abstain | The reviewer withholds approval because evidence, authority, or task fit is insufficient | Missing evidence, uncertainty, required follow-up |
| Escalate | The reviewer sends the decision to legal, security, governance, domain, executive, or regulatory authority | Escalation target, rationale, unresolved issue |

The human gate prevents a model-produced artifact from becoming institutional judgment through file movement alone. That distinction matters for AI safety, institutional accountability, and audit reconstruction.

---

## Translation-Positive, Restricted, and Translation-Negative Cases

The repository includes translation-positive, conditional, restricted, and translation-negative examples because all of these states are required for credible governance.

| Case Type | What It Demonstrates | Governance Value |
|---|---|---|
| Translation-positive | A research claim can become a bounded, schema-validated task | Shows how research can inform controlled operational work |
| Approve with conditions | A task can proceed only with constraints, review, and evidence limits | Preserves use while bounding reliance |
| Evaluation-only | A source can inform evaluation design without becoming operational task logic | Preserves research value without over-authorizing action |
| Policy-mapping-only | A source can inform governance reasoning without execution | Useful for legal, institutional, standards, and structural-risk material |
| Restricted | A source has value but requires constrained handling | Preserves review while reducing misuse, legal, or security exposure |
| Translation-negative | A research contribution exceeds the current governance boundary | Shows the system can block unsafe or unsupported translation |
| Reject translation | The source remains analytically useful while operational translation is refused | Protects the difference between learning from research and acting from research |

The negative case has special research value. It shows that the system’s output is constrained by governance criteria rather than by adoption bias.

---

## Relation to AI Governance and AI Safety

This project sits at the intersection of applied AI governance, AI safety, research translation, decision accountability, and human oversight. Its safety contribution is architectural: it constrains how research becomes action.

| Research Area | Repository Contribution |
|---|---|
| AI governance | Defines artifacts, schemas, and review stages for research-informed AI decisions |
| AI safety | Preserves boundaries around autonomy, uncertainty, failure conditions, and human control |
| AI policy | Routes standards, legal, liability, compute, model-weight, and international governance material into reviewable artifacts |
| Responsible AI | Requires provenance, scoped claims, reviewability, and human authorization |
| Decision accountability | Produces reconstructable records of why a system advanced, stalled, or was rejected |
| Institutional audit | Converts interpretive steps into files that can be reviewed after the decision |
| Applied research methods | Supplies a reusable translation model for papers, PDFs, reports, repositories, and online sources |

The repository does one narrow thing: it governs the translation layer between research and institutional action. That layer is often invisible. Here it becomes the primary object of design.

---

## Fit With Existing Research and Governance Norms

The repository is not trying to replace established AI governance or research-integrity frameworks. It implements a narrow control pattern that fits inside them.

| External Norm or Framework | Relevant Principle | Repository Response |
|---|---|---|
| NIST AI RMF | AI risk management requires Govern, Map, Measure, and Manage functions | The translator classifies source and safety-policy context before measurement or action |
| OECD AI Principles | Trustworthy AI should respect human-centred values, transparency, robustness, safety, and accountability | The translator makes evidence, review, rejection, and human authority visible |
| Reproducibility and replicability norms | Scientific confidence depends on transparent methods, inspectable evidence, and the ability to reproduce or challenge results | The translator preserves source, claims, tasks, evaluation plans, and decision artifacts |
| Software citation practice | Research software should be citable with machine-readable metadata | The repository includes `CITATION.cff`, Zenodo DOI metadata, release notes, and archival statements |
| Institutional review practice | High-impact decisions require accountable human review | The repository treats human gate records as authority artifacts |

This is an important note: the repository avoids saying it creates a complete governance program. It says it supplies one missing layer that many governance programs need.

---

## Boundaries of the Project

This repository is a reference implementation for governed research translation. It demonstrates artifact discipline, safety-policy intake, schema enforcement, human-gated review, and audit reconstruction.

It does no independent replication of source papers. It does no automatic truth certification of research findings. It does no live web verification during a run. It does no autonomous deployment. It does no replacement of institutional review boards, legal review, procurement review, security review, or domain expert judgment.

Those boundaries are deliberate. The system governs translation from source to decision artifact. Other institutional controls must still govern the surrounding environment.

---

## What Counts as Success

A successful governed translation produces a decision record that an external reviewer can inspect without needing to trust the original operator’s memory.

| Success Criterion | Evidence |
|---|---|
| The source is reconstructable | Captured source text and provenance metadata exist |
| Safety-policy relevance is classified | `safety_policy_intake.json` exists where applicable |
| Claims are inspectable | Each claim appears in structured form with evidence and scope |
| Tasks are bounded | Inputs, outputs, constraints, and failure conditions are explicit |
| Evaluation is defined before reliance | `eval_plan.json` exists before decision summary generation |
| AI output is intermediate | Candidate and proposed artifacts remain distinct from final output |
| Human authority is recorded | Accept, override, reject, abstain, or escalate decision is logged |
| Rejection remains available | Translation-negative outcomes are valid system outputs |
| The final decision can be audited | `decision_summary.json` links the artifact chain |

---

## Research Contribution Statement

Applied AI Research Translator contributes a governed reference model for converting research artifacts into institutional decision records. Its main contribution is the artifact chain: source capture, safety-policy intake, claim extraction, task bounding, evaluation planning, schema validation, human authorization, and deterministic decision summarization.

The project’s value for the research community is methodological. It gives researchers a concrete object for studying how applied AI findings enter institutional workflows, how translation can fail, how human authority can be preserved, how AI safety and policy sources should be routed before task design, and how decisions can be reconstructed after model-assisted work has occurred.

---

## Should the Repository Include References?

Yes.

The repository now has enough research, governance, standards, citation, and safety-policy material that a central reference file would make it more credible. The best structure is:

```text
REFERENCES.md
```

or:

```text
docs/references.md
```

Use one central reference file for stable external sources, then cite it from major documents such as `RESEARCH-RATIONALE.md`, `GOVERNANCE-MODEL.md`, `LIMITATIONS.md`, `TRACEABILITY.md`, and `docs/governance/*.md`.

A central references file should include:

| Reference Category | Examples |
|---|---|
| AI governance frameworks | NIST AI RMF, OECD AI Principles |
| Research integrity and reproducibility | National Academies reproducibility and replicability work |
| Software citation and archival metadata | Citation File Format, GitHub citation files, Zenodo GitHub integration |
| AI safety and policy sources | Capability evaluation, misuse, loss-of-control, model-weight security, compute governance, liability, international governance |
| Standards mappings | NIST, EU AI Act, ISO/IEC 42001 materials |
| Repository-specific sources | Zenodo DOI, release notes, pack-level source files |

The main documents should not become citation dumps. They should include a short **References** section with the most important sources and point readers to the central reference file for the full bibliography.

---

## Suggested Citation Context

Use this repository when citing research software that demonstrates governed research-to-decision translation, especially in work concerning AI governance, AI safety, responsible AI operations, human oversight, auditability, decision accountability, institutional review, and controlled use of AI-assisted research workflows.

---

## References

1. National Institute of Standards and Technology. *AI Risk Management Framework*. NIST AI Resource Center. https://www.nist.gov/itl/ai-risk-management-framework
2. National Institute of Standards and Technology. *AI RMF Core: Govern, Map, Measure, Manage*. NIST AI Resource Center. https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
3. OECD. *OECD AI Principles*. https://www.oecd.org/en/topics/sub-issues/ai-principles.html
4. National Academies of Sciences, Engineering, and Medicine. *Reproducibility and Replicability in Science*. The National Academies Press. https://nap.nationalacademies.org/catalog/25303/reproducibility-and-replicability-in-science
5. GitHub Docs. *About CITATION files*. https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files
6. Zenodo Help. *CITATION.cff file*. https://help.zenodo.org/docs/github/describe-software/citation-file/
7. Citation File Format. *Citation File Format documentation*. https://citation-file-format.github.io/

---

## Author

Mark Julius Banasihan  
AI Governance Specialist | Researcher in AI Safety & Policy  
ORCID: [0009-0001-8121-2878](https://orcid.org/0009-0001-8121-2878)

## License

Apache License 2.0.
