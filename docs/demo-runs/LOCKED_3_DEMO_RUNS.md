# Locked 3 Demonstration Runs (No Drift)

System architecture is locked. No new abstractions or features are allowed.

Goal: produce three clean runs and Decision Summaries that demonstrate:
A) explicit abstention, B) human override, and C) swarm disagreement leading to abstention — then stop.

## Shared constraints (apply to A/B/C)
- Same pipeline path each time: ingest → analysis → decision packaging → decision summary.
- No code changes except swapping inputs (evidence + run config) and supplying a human override payload where applicable.
- Each run must produce:
  1) schema-valid decision-log JSON
  2) decision-summary (human readable) using the same section template
  3) run-manifest.json recording inputs/outputs/policy refs for repeatability

## Folder layout
runs/
  run-A-explicit-abstention/
  run-B-human-override/
  run-C-swarm-disagreement/

Each run folder contains:
- run-manifest.json
- decision-context.json (or equivalent existing input)
- policy-config.json (or existing policy ref)
- evidence/ (bundle)
- outputs/
  - decision-log.json
  - decision-summary.md

## Decision Summary template (identical structure across runs)
1. Decision (final: go/conditional-go/no-go/defer/abstain)
2. Confidence + posture (e.g., “Not decision-ready”)
3. Why this decision was reached (3–6 bullets)
4. Key evidence used (IDs/links)
5. Risks & assumptions (explicit)
6. Governance events (abstention trigger / override / escalation)
7. Next actions
8. Audit notes (run_id, policy ref, timestamps, approver(s))

## Run A — Explicit abstention (refusal)
### Intent
Demonstrate: system refuses to recommend a gate decision when minimum evidence requirements are not met, and produces actionable next steps.

### Inputs
- Evidence bundle incomplete by design (missing required evidence type OR below quality threshold).
- No override payload.

### Expected outputs
- decision-log: final_decision=abstain; abstention=true; abstention reasons tied to policy; required_next_evidence populated.
- decision-summary: ABSTAIN (Not decision-ready) + 3+ concrete evidence acquisition actions.

### Stopping criteria
- Schema-valid decision log.
- Intended abstention rule triggered.
- Summary includes 3+ concrete next actions.
- No override.

## Run B — Human override
### Intent
Demonstrate: system recommends X; human overrides to Y; record captures who accepted what risk and why.

### Inputs
- Evidence supports a non-abstain recommendation (e.g., conditional-go or defer).
- Provide override payload with: override_by, timestamp, original_recommendation, new_decision, justification, risk acceptance, conditions.

### Expected outputs
- decision-log: system_recommendation=X; final_decision=Y; override_applied=true; override justification + accountability fields populated.
- decision-summary: “System recommended X; Human override to Y” + explicit risk acceptance + conditions/monitoring.

### Stopping criteria
- Schema-valid.
- Override recorded as a first-class governance event.
- Summary includes original, override, justification, risk owner/acceptance.

## Run C — Swarm disagreement → escalation → abstention
### Intent
Demonstrate: swarm disagreement beyond threshold triggers escalation and results in abstention (not forced averaging).

### Inputs
- Evidence includes an explicit conflict or ambiguity that drives disagreement.
- Swarm settings fixed (n_agents, disagreement_threshold, aggregation method) per existing policy.

### Expected outputs
- decision-log: per-agent outputs recorded; disagreement metric recorded; escalation_triggered=true; final_decision=abstain; escalation path recorded.
- decision-summary: “Disagreement exceeded threshold → Escalation → ABSTAIN” + 2–3 disagreement drivers + next actions to resolve conflict.

### Stopping criteria
- Schema-valid.
- Disagreement metric above threshold and shown.
- Escalation event present.
- Final is abstain (or your defined escalate+abstain state), not majority vote.

## Global stop condition (hard)
Stop immediately when all are true:
1) Three run manifests exist with unique run_ids and complete input/output pointers.
2) Three decision logs validate against the same schema version.
3) Three decision summaries follow the same template and are readable by a non-builder.
4) Each run demonstrates exactly one behavior:
   - A: abstention by evidence/policy
   - B: override with accountable governance record
   - C: swarm disagreement → escalation → abstention
5) No run contains “bonus” behavior that muddies the demo.

## Expected state matrix
- Run A: abstain=true, override=false, escalation=false
- Run B: abstain=false, override=true, escalation=false
- Run C: abstain=true, override=false, escalation=true
