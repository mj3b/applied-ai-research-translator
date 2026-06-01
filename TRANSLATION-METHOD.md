# Translation Method

**Applied AI Research Translator** converts research artifacts into governed decision artifacts. The method applies when a paper, PDF, online publication, technical report, repository, benchmark claim, policy source, or standards document appears useful, while the institution still needs to know what claim was selected, what safety or policy classification was assigned, what task was derived, what assumptions were preserved, what constraints were imposed, what evidence was required, and who authorized the result.

The method treats translation as a sequence of controlled reductions. A source is captured. Safety and policy relevance is classified where applicable. Claims are extracted. Claims are screened for operational fit. Candidate tasks receive a translation verdict. Approved tasks enter a bounded run or manual review. The run produces structured evidence. A human reviewer accepts, overrides, rejects, abstains, or escalates. The final decision summary records the path.

```mermaid
flowchart TD
    A[Source artifact] --> B[Source capture]
    B --> C[Safety-policy intake when applicable]
    C --> D[Claim extraction]
    D --> E[Claim screening]
    E --> F[Task derivation]
    F --> G[Translation verdict]
    G --> H[Locked task definition]
    H --> I[Evaluation plan]
    I --> J[Governed run or manual review]
    J --> K[Human gate]
    K --> L[Decision summary]

    C -. evidence type, safety domain, autonomy, dual use .-> C
    E -. scope, evidence, assumptions, failure modes .-> E
    G -. positive, conditional, evaluation-only, policy-only, restricted, reject, abstain .-> G
    K -. accept, override, reject, abstain, escalate .-> K
```

---

## Reader Map

| Reader | Main Question | Recommended Path |
|---|---|---|
| Principal investigator | What is the method, and what makes it citable research software? | Read this file, then inspect `README.md`, `RESEARCH-RATIONALE.md`, and `CITATION.cff`. |
| AI governance researcher | How does the system convert research into accountable decisions? | Read the full method, then inspect `claims.json`, `tasks.json`, `eval_plan.json`, and `decision_summary.json` across packs. |
| AI safety researcher | Where does the method classify autonomy, misuse, loss of control, and task expansion? | Start with `safety_policy_intake.json`, translation verdicts, and the negative multi-agent pack. |
| AI policy researcher | How does the method route legal, standards, liability, compute, model-weight, or international governance sources? | Inspect `docs/governance/safety-policy-intake.md` and the governance mappings. |
| Institutional reviewer | What evidence supports a decision to translate, condition, restrict, reject, or defer? | Review the artifact chain from source text through safety-policy intake and final decision summary. |
| Technical implementer | Which artifacts must exist before execution begins? | Inspect schema contracts, validation scripts, and `runloop/README_RUNLOOP.md`. |
| Auditor | Can the decision path be reconstructed after the fact? | Review provenance capture, safety-policy intake, run manifests, human-gate files, and deterministic summaries. |

---

## Method Thesis

Research translation requires governance because the act of translating research into action changes the research object.

A publication presents a claim within a scholarly, technical, experimental, legal, policy, or institutional setting. An implementation team needs a task, input, output, evaluation condition, failure rule, owner, reviewer, and decision record. The translation from source to claim to task can introduce overreach, remove assumptions, widen the deployment context, normalize risk, or treat scholarly evidence as operational approval.

This method prevents that collapse by separating six functions that are often blended together:

| Function | Question | Artifact |
|---|---|---|
| Source capture | What material informed the translation? | `sources/paper_text.txt` |
| Safety-policy intake | What kind of authority should this source be allowed to have? | `safety_policy_intake.json` |
| Claim extraction | What exactly did the source claim? | `claims.json` |
| Task derivation | What bounded task can be built from the claim? | `tasks.json` |
| Evaluation design | What evidence would show that the task performed acceptably or should stop? | `eval_plan.json` |
| Decision authorization | Who accepted, overrode, rejected, abstained, escalated, or conditioned the result? | `decision_summary.json`, `human_gate.json` |

The method’s contribution is the controlled boundary between research interpretation and operational authority.

---

## Core Definitions

| Term | Definition | Methodological Role |
|---|---|---|
| Source artifact | The paper, PDF, report, repository, web page, benchmark note, policy source, standard, or publication used for translation | Provides the evidence base, provenance record, and claim surface |
| Safety-policy intake | The first-gate classification of source type, evidence status, AI safety domain, autonomy relevance, dual-use status, review authority, and translation boundary | Prevents safety-relevant sources from entering task design before risk and authority are visible |
| Claim | A discrete proposition extracted from the source that can be scoped, tested, or rejected | Prevents whole-source adoption and forces local interpretation |
| Operationalization | The conversion of a claim into an executable or reviewable task | Exposes where assumptions, metrics, and failure modes enter the workflow |
| Task | A bounded unit of work with inputs, outputs, constraints, abstention conditions, and review points | Defines the execution boundary before model use |
| Evaluation plan | A pre-declared standard for what counts as success, failure, uncertainty, restriction, or abstention | Prevents model output from becoming self-validating |
| Translation verdict | The decision that a source or claim can proceed, proceed with conditions, remain evaluation-only, remain policy-mapping-only, be restricted, be rejected, or abstain | Preserves both adoption and refusal as governed outcomes |
| Governed run | A schema-bound execution that produces logged artifacts and avoids direct deployment authority | Generates evidence under a fixed task boundary |
| Human gate | The review point where a person accepts, overrides, rejects, abstains, or escalates the proposed output | Assigns decision authority outside the model |
| Decision summary | The final audit artifact that records source, intake, claim, task, evidence, uncertainty, and authorization | Makes the translation path reconstructable |

---

## Translation Pipeline

The method has ten stages. Each stage narrows the source material while preserving the information a later reviewer needs to reconstruct the decision.

| Stage | Action | Primary Output | Control Question |
|---:|---|---|---|
| 1 | Capture source | `paper_text.txt` | Can the reviewer inspect the same source material used by the translator? |
| 2 | Classify safety-policy relevance | `safety_policy_intake.json` | What authority, risk domain, review path, and translation boundary apply? |
| 3 | Extract claims | `claims.json` | Which claims were selected, and what evidence supports each one? |
| 4 | Screen claims | annotated claim records | Does each claim have scope, assumptions, testability, and failure conditions? |
| 5 | Derive tasks | `tasks.json` | Can the claim become a bounded task without expanding autonomy or institutional reliance? |
| 6 | Design evaluation | `eval_plan.json` | What evidence would support acceptance, restriction, rejection, or abstention? |
| 7 | Assign verdict | pack-level decision | Should translation proceed, proceed with conditions, remain evaluation-only, remain policy-only, be restricted, or stop? |
| 8 | Execute bounded run or manual review | run or review artifacts | Did the work remain inside the locked task, schema, and review boundary? |
| 9 | Apply human gate | `human_gate.json` where present | What did the reviewer decide, and on what authority? |
| 10 | Assemble decision record | `decision_summary.json` | Can the decision be reconstructed after the fact? |

---

## Stage 1: Source Capture

The method begins by freezing the research material used for translation. Source capture matters because online publications change, PDFs circulate in multiple versions, GitHub repositories evolve, preprints may shift after review, and policy sources may be superseded.

The repository stores the working source text inside each pack:

```text
packs/<pack_id>/sources/paper_text.txt
```

Source capture answers three questions:

| Question | Why It Matters |
|---|---|
| What text was used for claim extraction? | Later reviewers need the same source state, especially for web and preprint sources |
| Which source boundaries were included or excluded? | A PDF, repository, appendix, benchmark table, and policy memo may carry different claims |
| What kind of evidence is the source allowed to provide? | A peer-reviewed article, vendor report, legal text, and policy memo carry different evidentiary weight |

The method treats source capture as the first governance artifact. The source provides evidence. It does not authorize implementation.

---

## Stage 2: Safety-Policy Intake

Safety-policy intake is the first-gate classification step for AI safety and policy sources. It exists because some sources should be classified before any claim is made task-shaped.

The output lives in:

```text
packs/<pack_id>/safety_policy_intake.json
```

Use this stage when a source touches capability forecasting, misuse, loss of control, structural risk, compute governance, model-weight security, liability, international governance, concentration of power, high-impact deployment, or safety evaluation.

A complete intake record should classify:

| Intake Dimension | Method Function |
|---|---|
| Source status | Distinguishes peer-reviewed, preprint, institutional, legal, benchmark, implementation, or informal source status |
| Evidence type | Distinguishes empirical evidence, theory, forecast, scenario, legal requirement, policy argument, benchmark, or implementation evidence |
| AI safety domain | Identifies capability forecasting, misuse, loss of control, structural risk, compute governance, model-weight security, liability, international governance, or concentration of power |
| Capability and autonomy | Records model class, autonomy level, tool-use scope, and task-horizon relevance |
| Risk screen | Records dual-use status, misuse pathways, oversight failure modes, and catastrophic-risk relevance |
| Governance mapping | Assigns decision lever, required reviewers, and translation boundary |
| Translation verdict | Determines whether the source proceeds, proceeds with constraints, remains evaluation-only, remains policy-mapping-only, is restricted, is rejected, or abstains |

The central rule:

```text
For AI safety and policy sources, claim extraction should not be treated as translation-ready until safety_policy_intake.json validates.
```

The intake gate does not prove that a source is safe. It makes the classification visible enough to review.

---

## Stage 3: Claim Extraction

Claim extraction decomposes the source into discrete propositions. This is the first controlled reduction after intake.

A weak translation process asks: “What is this paper about?”

This method asks a narrower question: “Which claims in this source can be represented, scoped, and tested without losing the conditions that made the claim meaningful?”

A claim record should preserve at least four things:

| Field Type | Purpose |
|---|---|
| Claim text | States the extracted proposition in a bounded form |
| Evidence reference | Links the claim back to source material |
| Scope boundary | Names the setting, population, dataset, task, model class, system boundary, or deployment condition |
| Failure mode | Names what would make the claim unsafe, unsupported, or unsuitable for translation |

The output lives in:

```text
packs/<pack_id>/claims.json
```

The method rejects whole-paper adoption. A paper can contain a strong evaluation claim, a weaker policy implication, and a speculative deployment recommendation. Claim extraction prevents those from merging into a single adoption argument.

---

## Stage 4: Claim Screening

Claim screening evaluates whether an extracted claim is a viable candidate for operational translation. Screening happens before task creation because task design can make a weak claim appear more actionable than the source supports.

| Screening Dimension | Question | Translation Implication |
|---|---|---|
| Specificity | Does the claim state a concrete relation, mechanism, behavior, or result? | Vague claims require narrowing before task design |
| Evidence link | Can the claim be tied to source text or reported evidence? | Unsupported claims should stop or be marked as interpretation |
| Source status | Does the evidence type support the proposed use? | Forecasts, legal claims, and empirical findings need different treatment |
| Safety-policy boundary | Does the intake verdict allow task translation? | Policy-only, restricted, reject, or abstain verdicts block ordinary task design |
| Scope | Does the claim identify the condition under which it holds? | Missing scope creates overextension risk |
| Testability | Can the claim produce an observable task or evaluation condition? | Untestable claims may remain background knowledge |
| Failure condition | What would make translation unsafe, invalid, or misleading? | Missing failure conditions weaken governance |
| Autonomy boundary | Would the claim require autonomous action, coordination, or escalation? | Autonomy expansion triggers heightened review or rejection |
| Human ownership | Can a human reviewer accept responsibility for the decision? | Unowned decisions should stop |

Screening produces one of five practical outcomes:

| Outcome | Meaning |
|---|---|
| Retain | The claim can proceed to task derivation |
| Narrow | The claim may proceed after scope or evidence boundaries are tightened |
| Hold | The claim is useful background material, with insufficient basis for task translation |
| Restrict | The claim has safety, misuse, legal, security, or governance concerns requiring constrained handling |
| Reject | The claim exceeds the system boundary or lacks enough evidence for operational use |

---

## Stage 5: Task Derivation

Task derivation converts a screened claim into a bounded operational task. This is the most consequential step in the method because it determines what the system will allow the model or reviewer to do.

A valid task must define the following elements:

| Task Element | Purpose |
|---|---|
| Task ID | Gives the task a stable reference for traceability |
| Source or claim link | Binds the task back to source evidence through `from_claim_id` |
| Inputs | Specifies what the system may inspect |
| Outputs | Specifies what the system may produce |
| Constraints | Limits the task boundary before execution |
| Metrics | Defines how outputs will be judged |
| Abstention conditions | Specifies when the system should stop or decline |
| Restriction conditions | Specifies when the source or task requires constrained handling |
| Human gate point | Names where human authorization is required |
| Evidence linkage | Connects the task back to the source claim and intake boundary |

The output lives in:

```text
packs/<pack_id>/tasks.json
```

Task derivation follows one central rule: the task must be smaller than the claim. A research claim often has broader implications than the system should operationalize. The task selects a bounded portion that can be run, reviewed, and reconstructed.

---

## Stage 6: Evaluation Plan

The evaluation plan defines what would count as sufficient evidence for a task to proceed. This prevents the system from treating model output as self-validating.

The output lives in:

```text
packs/<pack_id>/eval_plan.json
```

A strong evaluation plan should identify:

| Evaluation Component | Governance Function |
|---|---|
| Success criteria | Defines what acceptable output means for the bounded task |
| Failure criteria | Defines when the task fails or requires rejection |
| Abstention triggers | Defines conditions under which the system should withhold output |
| Restriction triggers | Defines when the source, claim, or output requires constrained handling |
| Human review criteria | Defines what the reviewer must inspect before approval |
| Evidence requirements | Defines what artifacts must exist before a decision can be recorded |
| Residual uncertainty | Names what the evaluation cannot settle |

The method treats evaluation design as a decision artifact. A task without evaluation criteria is an ungoverned prompt.

---

## Stage 7: Translation Verdict

The translation verdict determines whether the source claim can enter a governed run, remain outside execution, or stop. It is the method’s main control point.

| Verdict | Meaning | Typical Use |
|---|---|---|
| `translation_positive` | The claim can become a bounded task with defined evidence and review conditions | Reliance calibration, workflow monitoring, classification, discrepancy review |
| `translation_positive_with_conditions` | The claim can proceed only under additional constraints | Higher-risk review, narrow source basis, elevated uncertainty |
| `evaluation_only` | The source should inform evaluation design without becoming an operational task | Benchmarks, measurement methods, safety evals |
| `policy_mapping_only` | The source should inform governance reasoning without execution | Legal texts, standards, structural risk, multi-agent autonomy analysis |
| `restricted` | The source or claim requires constrained handling | Dual-use, security-sensitive, legal, or model-weight sources |
| `human_review_required` | The source or task cannot proceed without designated expert review | AI safety, legal, security, governance, or domain authority required |
| `translation_negative` | The claim remains relevant to research, while operational translation exceeds the current system boundary | Autonomous coordination, unbounded agentic behavior, unsupported generalization |
| `reject_translation` | The source or claim should stop as an operational pathway | Source weakness, missing evidence, unacceptable autonomy, irreconstructable task boundary |
| `abstain` | Evidence is insufficient to classify or translate responsibly | Version ambiguity, unresolved source status, missing implementation detail |

The method preserves rejection and abstention as successful governance outcomes. A rejected translation means the system identified a boundary and recorded the reason.

---

## Stage 8: Governed Execution or Manual Review

Governed execution happens only after task boundaries and evaluation criteria are fixed. Some sources should never reach execution; they may instead remain in policy mapping, evaluation design, restricted review, or rejection. That is still a valid method outcome.

The execution layer is organized under:

```text
runloop/
```

A governed run should produce an artifact trail like this:

```text
run_input.json
candidate outputs
proposed.json
human_gate.json
final.json
decision_summary.json
```

The execution model separates candidate generation from authorization.

| Run Artifact | Role in the Method |
|---|---|
| `run_input.json` | Captures the specific inputs used for execution |
| Candidate outputs | Preserve raw model-generated material for inspection |
| `proposed.json` | Records schema-valid proposed output |
| `human_gate.json` | Records accept, override, reject, abstain, or escalate decision |
| `final.json` | Stores the human-authorized output |
| `decision_summary.json` | Records the final decision path |

The model may produce candidate evidence. It cannot promote its own output into a final institutional decision.

---

## Stage 9: Human Gate

The human gate is the authorization point. It records whether a reviewer accepts, overrides, rejects, abstains from, or escalates the proposed output.

| Gate Action | Meaning | Decision Record Requirement |
|---|---|---|
| Accept | The reviewer approves the proposed output under the task boundary | Reviewer identity, timestamp, rationale, accepted artifact |
| Override | The reviewer modifies or replaces the proposed output | Reviewer identity, override rationale, final artifact |
| Reject | The reviewer withholds authorization | Reviewer identity, rejection rationale, risk or evidence basis |
| Abstain | The reviewer declines to decide under current evidence | Missing evidence, uncertainty, required next review |
| Escalate | The reviewer routes the decision to stronger authority | Escalation target, unresolved issue, required authority |

The human gate exists because institutional accountability cannot be delegated to a model output. The decision record must show who carried authority at the point where evidence became action.

---

## Stage 10: Decision Summary

The decision summary is the final audit artifact. It records the source, safety-policy intake where applicable, claim, task, evidence, verdict, human decision, and residual uncertainty.

The output lives in:

```text
packs/<pack_id>/decision_summary.json
```

or, for runloop-generated demonstrations:

```text
docs/demo-runs/<run_id>/decision_summary.json
```

A decision summary should answer:

| Question | Expected Evidence |
|---|---|
| Which source informed the decision? | Source path, captured text, or citation metadata |
| What safety-policy classification applied? | Intake verdict, domain, risk screen, required review, and translation boundary |
| Which claim was translated? | Claim ID and claim text |
| What task was derived? | Task ID and bounded task definition |
| What evidence was produced? | Run artifacts, evaluation result, validation status |
| What did the human reviewer decide? | Accept, override, reject, abstain, escalation, or conditional approval |
| What remains unresolved? | Stated uncertainty, limitation, residual risk, or deferred review item |

The decision summary is deliberately structured. It should read as an audit record, not as a persuasive essay.

---

## Artifact Chain

The method’s integrity depends on the complete artifact chain.

```text
Source material
  → safety_policy_intake.json, where applicable
  → claims.json
  → tasks.json
  → eval_plan.json
  → run_input.json or reviewer notes
  → proposed.json
  → human_gate.json
  → final.json
  → decision_summary.json
```

| Link | Failure Prevented |
|---|---|
| Source → intake | Prevents safety-relevant material from entering task design before classification |
| Source → claims | Prevents unsupported paraphrase and whole-source adoption |
| Intake → claims | Prevents risk-domain and review-boundary loss |
| Claims → tasks | Prevents broad claims from becoming unbounded work |
| Tasks → eval plan | Prevents execution without evidence criteria |
| Eval plan → run input | Prevents input drift and unrecorded task expansion |
| Run input → proposed output | Preserves the model evidence trail |
| Proposed output → human gate | Prevents raw model output from becoming final authority |
| Human gate → final output | Assigns authorization to a reviewer |
| Final output → decision summary | Makes the full path reconstructable |

---

## Translation Criteria

A research claim should proceed only when the following criteria are satisfied.

| Criterion | Pass Condition | Fail Condition |
|---|---|---|
| Provenance | Source material is captured and reviewable | Source state cannot be reconstructed |
| Safety-policy classification | Intake exists and validates when AI safety or policy relevance is present | Risk domain, review authority, or translation boundary is missing |
| Claim clarity | Claim is discrete, scoped, and linked to evidence | Claim is broad, ambiguous, or unsupported |
| Operational boundedness | Task has fixed inputs, outputs, constraints, and review points | Task requires open-ended autonomy or undefined downstream action |
| Evaluation basis | Evaluation plan defines success, failure, restriction, and abstention | Output quality would be judged informally after execution |
| Schema compatibility | Artifacts can be validated against repository schemas | Required fields or artifact types are absent |
| Human ownership | Reviewer authority is explicit | Decision responsibility is diffuse or implied |
| Audit trail | Artifact sequence can be reconstructed | Final result lacks source-to-decision traceability |
| Residual risk | Uncertainty is recorded in the decision artifact | Uncertainty is hidden in prose or omitted |

---

## Negative, Restricted, and Abstention Logic

Negative translation is part of the method. A research artifact can be valuable while still unsuitable for operational translation.

A restrictive, abstention, or negative verdict is appropriate when one or more conditions hold:

| Condition | Reason for Restriction, Rejection, or Deferral |
|---|---|
| Autonomous coordination required | The task requires agents to plan, coordinate, escalate, or act beyond a bounded review surface |
| Safety-policy intake is missing | Risk domain, reviewer authority, and translation boundary have not been assigned |
| Dual-use exposure is material | Operationalization may lower barriers to harmful use |
| Source assumptions cannot be preserved | The deployment setting differs materially from the research condition |
| Evidence basis is too thin | The source provides insufficient support for the derived task |
| Human review cannot inspect the output adequately | The reviewer lacks a clear basis for acceptance or override |
| Audit chain breaks | The decision cannot be reconstructed from artifacts |
| Task expands during execution | The system would need to change scope after seeing model output |
| Failure conditions are undefined | The system lacks a principled stopping rule |

The negative multi-agent pack illustrates this principle. The research contribution may be important, yet translation may still fail because autonomous multi-agent behavior creates an accountability surface that the current runloop should not absorb.

---

## Method Applied to Example Packs

| Pack | Source Question | Method Outcome | Governance Reason |
|---|---|---|---|
| `haic_reliance_review_59e257ff` | Can human-AI reliance be assessed through structured review behavior? | Translation-positive | Reliance can be instrumented through accept, override, and confidence-stratified review signals |
| `measuring_agents_in_production_a98e2ca8` | Can production agent behavior be measured through workflow-level monitoring? | Translation-positive candidate | Monitoring can be bounded through metrics, drift detection, and reviewable evidence artifacts |
| `multi_agent_failure_modes_e0228882` | Can autonomous multi-agent failure-mode research become a bounded task? | Safety-policy classified, translation-negative | The intake classifies loss-of-control and structural-risk relevance, and the claim points toward coordination behavior beyond the bounded runloop surface |
| `t_c02` | Can operational triage proceed under a fixed taxonomy and human gate? | Approve with conditions | Classification stays within a constrained input-output format and requires review |
| `t_c04` | Can document discrepancy review proceed under bounded comparison logic? | Approve with conditions | Output remains inspectable and final authorization stays with the reviewer |

---

## Method Boundaries

The method supports governed translation. It does not claim to solve every research or deployment problem.

| Boundary | Meaning |
|---|---|
| No autonomous deployment authority | The system does not execute downstream institutional actions |
| No automatic proof of source validity | A captured paper, report, or repository still requires scholarly and technical review |
| No replacement for domain expertise | The method structures evidence; it does not supply subject-matter authority by itself |
| No automated safety certification | Safety-policy intake classifies risk for review; it does not certify safety |
| No universal benchmark claim | Example packs demonstrate method behavior, not cross-domain performance guarantees |
| No hidden model authorization | Model output remains candidate evidence until the human gate records a decision |

These boundaries strengthen the method because they make the claim auditable. The system governs the translation path. It does not pretend that translation alone establishes truth, safety, or deployability.

---

## Review Protocol

A reviewer can evaluate a pack by following this sequence:

| Step | Review Action | File |
|---:|---|---|
| 1 | Inspect source material | `sources/paper_text.txt` |
| 2 | Inspect safety-policy intake where applicable | `safety_policy_intake.json` |
| 3 | Compare extracted claims against source material | `claims.json` |
| 4 | Check whether each task preserves claim scope and intake boundary | `tasks.json` |
| 5 | Evaluate success, failure, restriction, and abstention criteria | `eval_plan.json` |
| 6 | Inspect translation verdict and rationale | `decision_summary.json` |
| 7 | For executed runs, inspect run input and proposed output | `run_input.json`, `proposed.json` |
| 8 | Inspect human gate decision | `human_gate.json` |
| 9 | Reconstruct final authorization path | `final.json`, `decision_summary.json` |

A pack passes review when the reviewer can move from source material to final decision without relying on unstated assumptions.

---

## Research Use

Researchers can use this method to study several questions in applied AI governance, AI safety, and AI policy.

| Research Question | Repository Surface |
|---|---|
| How should research findings be converted into bounded operational tasks? | `claims.json`, `tasks.json`, `TRANSLATION-METHOD.md` |
| How should AI safety and policy sources be classified before translation? | `safety_policy_intake.json`, `docs/governance/safety-policy-intake.md` |
| When should translation stop? | Negative translation packs and decision summaries |
| What artifacts are required for audit reconstruction? | `TRACEABILITY.md`, run manifests, decision summaries |
| How can human oversight be represented as a structured decision record? | `human_gate.py`, `human_gate.json`, final artifacts |
| How should schema validation function as a governance control? | `schemas/`, validation scripts |
| How can institutions use AI output as evidence while preserving human authority? | Governed runloop and deterministic decision summary |
| How can safety-relevant research remain useful without becoming an unsafe task? | Restricted, evaluation-only, policy-mapping-only, and rejection verdicts |

---

## Implementation Standard

A new mature translation pack should meet this minimum standard before release:

```text
packs/<pack_id>/
├── safety_policy_intake.json
├── agent_spec.json
├── claims.json
├── tasks.json
├── eval_plan.json
├── decision_summary.json
└── sources/
    └── paper_text.txt
```

For packs without AI safety or policy relevance, `safety_policy_intake.json` may be omitted, but the pack should then be described as outside the safety-policy intake path or as below safety-policy classified maturity.

Minimum acceptance criteria:

| Requirement | Acceptance Standard |
|---|---|
| Source preserved | Source material used for extraction appears in `sources/` |
| Intake completed where applicable | Safety-policy relevance, review authority, and translation boundary are recorded |
| Claims extracted | Claims are discrete and linked to evidence |
| Tasks bounded | Inputs, outputs, constraints, and review points are explicit |
| Evaluation stated | Success, failure, restriction, and abstention conditions are defined |
| Verdict recorded | Translation status and rationale are present |
| Human decision visible | Final authorization, override, rejection, abstention, escalation, or condition is recorded |
| Schema validation complete | Required files validate against the relevant schemas |

---

## Versioning Implications

Translation artifacts should be versioned because the source, model behavior, schemas, reviewer expectations, and institutional standards may change.

| Versioned Object | Why It Requires Versioning |
|---|---|
| Source artifact | Web pages, repositories, reports, and preprints can change after review |
| Safety-policy intake | Risk classifications and translation boundaries may change as evidence or policy changes |
| Claims | Later reviewers may extract different claims from the same source |
| Tasks | Task boundaries may tighten as risks become clearer |
| Schemas | Governance contracts may evolve as required evidence changes |
| Run artifacts | Model output may vary across model versions and execution settings |
| Decision summaries | Institutional approvals may expire, narrow, or be superseded |

A release should identify which translation method, schema set, intake schema, and pack state were used.

---

## Method Claim

The Applied AI Research Translator method advances one claim: research-to-decision translation can be governed when the repository treats source capture, safety-policy intake, interpretation, task design, model execution, human authorization, and audit reconstruction as separate artifacts.

That separation is the method.
