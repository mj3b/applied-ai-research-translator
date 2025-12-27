# Research Context (Public)

This repository demonstrates a **decision-discipline** method for translating applied AI research into
**auditable, decision-ready artifacts**.

It intentionally avoids autonomy and multi-agent execution. The goal is not to prove cleverness—
it is to prove **defensibility** under real operating constraints.

## How papers are used here

Papers fall into two categories:

- **Translation-positive**: the paper supports bounded decision-support tasks with measurable evaluation and clear human ownership.
- **Translation-negative**: the paper is useful, but its contributions do **not** translate into bounded, auditable tasks without introducing disallowed autonomy or unacceptable governance risk.

Both outcomes are valuable in regulated or high-stakes delivery.

## Included example packs

### Translation-positive

- `packs/measuring_agents_in_production_a98e2ca8/`
  - Production measurement and monitoring patterns.
  - Used to motivate end-to-end evaluation, drift detection, and workflow-level safety.

- `packs/haic_reliance_review_59e257ff/`
  - Human–AI collaboration and **reliance calibration** (over-/under-trust, override behavior, skill preservation).
  - Used to justify decision-support boundaries and measurable reliance/override instrumentation.

### Translation-negative

- `packs/multi_agent_failure_modes_e0228882/`
  - Multi-agent LLM failure modes.
  - Included as an explicit **rejection** example: the translator can produce a defensible *no-go* when bounded tasks are not available without autonomy.

## Why a negative example exists

In production, the most valuable decision is often **“No—do not proceed.”**

A credible decision-discipline method must be able to:
- identify when a paper’s claims cannot be bounded into controllable tasks,
- document why,
- and preserve ownership and accountability.
