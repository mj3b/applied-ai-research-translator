# Research Context

This repository applies a structured translation discipline to three applied AI research papers. The purpose is not to survey the literature but to demonstrate a governed method: converting research findings into falsifiable claims, bounded tasks, and human-authorized decision artifacts — or producing a documented rejection when that conversion is not possible without governance risk.

---

## Translation Criteria

A paper is translation-positive when its contributions can be converted into bounded, controllable tasks that satisfy four criteria:

1. **Testability** — claims can be evaluated against defined metrics with observable outputs
2. **Containment** — the task has defined failure and abstention conditions that prevent unbounded execution
3. **Human ownership** — a named human can authorize the output without depending on the AI's judgment
4. **Governance surface** — the accountability and audit requirements are proportional to the risk level

A paper is translation-negative when its primary contributions require autonomous coordination, exceed the acceptable governance surface for the deployment context, or cannot be evaluated without multi-agent execution. Translation-negative is a first-class outcome — not a failure.

---

## Paper 1: Human-AI Collaboration and Reliance Calibration

**Pack:** `haic_reliance_review_59e257ff`
**Verdict:** Translation-positive

**Core finding:** Mis-calibrated reliance — both over-reliance (automation bias) and under-reliance (algorithm aversion) — is the primary failure mode in human-AI decision systems, not model accuracy. The research establishes that reliance calibration is measurable via accept/override instrumentation and that human skill degrades predictably when AI dominates the workflow without periodic independent judgment checkpoints.

**Why it translates:** The claims operationalize directly into bounded measurement tasks. Override rate stratified by AI confidence is a deterministic metric requiring no autonomous execution. Periodic blind evaluation (human-only) is a governance mechanism, not an AI task. The accountability surface is explicitly human.

**Claims extracted:**

| Claim ID | Type | Operationalization | Testability |
|----------|------|--------------------|-------------|
| c01 | method | Decision-support workflow with bounded AI recommendations and human final authority | medium |
| c02 | measurement | Accept/override rate by AI confidence — over/under reliance detection | high |
| c03 | reliability | Periodic human-only evaluation to measure skill retention trend | medium |
| c04 | method | Audit-ready decision summary with evidence, rationale, and ownership per decision | high |

**Relevance to this system:** The human gate architecture directly addresses automation bias (c02): the gate makes rejection structurally equal to acceptance. The decision summary addresses c04: every run produces an audit-ready artifact assembled deterministically, not authored by the model.

---

## Paper 2: Measuring AI Agents in Production

**Pack:** `measuring_agents_in_production_a98e2ca8`
**Verdict:** Translation-positive

**Core finding:** Model-level metrics (accuracy on benchmark datasets) do not predict workflow-level outcomes. Production measurement requires end-to-end evaluation, drift detection across the full pipeline, and safety instrumentation at the workflow level — not the model level.

**Why it translates:** Production measurement is a bounded analytical task. Drift detection generates observable signals without autonomous action. Workflow-level safety can be instrumented through schema validation and abstention rules — both of which the governed runloop already enforces.

**Relevance to this system:** This paper grounds the design of the run artifact trail. `candidates.jsonl`, `proposed.json`, `human_gate.json`, `final.json`, and `decision_summary.json` together constitute end-to-end measurement of what the system actually produced — model output, human gate decision, and final authorized artifact. This is workflow-level observability, not model-level accuracy.

---

## Paper 3: Multi-Agent LLM Failure Modes

**Pack:** `multi_agent_failure_modes_e0228882`
**Verdict:** Translation-negative (explicit rejection)

**Core finding:** Multi-agent LLM coordination introduces failure modes that do not appear in single-agent deployments: cascading errors across agent boundaries, accountability gaps when no single agent owns an outcome, and audit trail fragmentation that makes post-hoc review structurally difficult.

**Why it does not translate:**

The paper's primary contribution is diagnostic — it characterizes failure modes of multi-agent autonomy. The natural application of this research would be to build a multi-agent system, observe the failure modes in practice, and measure mitigation effectiveness. That application requires:

- autonomous agent coordination (prohibited under the non-agentic constraint)
- an accountability surface that exceeds the governance boundary for this system
- inter-agent communication that is structurally incompatible with the single-gate, sequential approval model

Attempting to bound this into a controlled task would require either: (a) removing the multi-agent element, which eliminates the primary research contribution, or (b) permitting autonomous coordination, which violates the system's core governance constraint.

**Decision summary:**

```json
{
  "decision": "reject_translation",
  "confidence": "high",
  "rationale": [
    "Primary contributions are diagnostic failure modes of multi-agent autonomy rather than a bounded, controllable decision-support task.",
    "In regulated/phase-gated settings, the accountability and audit surface of multi-agent coordination exceeds acceptable governance risk for this system's scope."
  ]
}
```

**Why this rejection is the most important example in the repository:**

A translation system that never rejects is not evaluating governance risk — it is rationalizing adoption. The multi-agent pack demonstrates that the system applies genuine criteria. A team that adopted multi-agent coordination without passing through this kind of structured rejection analysis would be making an ungoverned adoption decision. The rejection is the correct governance outcome.

---

## What the Research Base Establishes

Taken together, the three papers establish three design principles that are directly encoded in this system's architecture:

**1. Measure reliance, not just accuracy.** Human-AI system quality is a function of calibrated reliance — the degree to which human reviewers accept AI output when it is correct and override it when it is not. The human gate instruments this directly: every accept and override is logged with rationale.

**2. Evaluate end-to-end, not model-only.** The decision summary is the evaluation artifact, not the model output. What the system produces is the full pipeline output: model candidate, human gate decision, and human-authorized final artifact. The pipeline is the unit of evaluation.

**3. Document rejections with the same rigor as approvals.** The multi-agent rejection demonstrates that a governed no-go is as valuable as a governed go. The translation-negative verdict produces a schema-validated decision summary with documented rationale — not a note in a Slack thread.

---

*Part of the Applied AI Research Translator system. Apache 2.0.*
*See also: [GDI v3.0](https://github.com/mj3b/governed-decision-intelligence) · [RGDS AI Governance](https://github.com/mj3b/rgds-ai-governance)*
