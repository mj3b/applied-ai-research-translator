# Measuring Agents in Production Pack

This pack translates research on production AI agents into monitoring and evidence-design artifacts. The pack treats agent performance as a measurement problem: what happened in production, which task was being attempted, what evidence shows success or failure, and where the agent exceeded the reviewer’s ability to reconstruct behavior.

The pack currently contains claims, tasks, an agent specification, an evaluation plan, and source text. It does not include a final `decision_summary.json` in the current repository state, so it should be treated as an evaluation-ready scaffold rather than a decision-complete pack.

## What this pack evaluates

The pack focuses on production observability for agent workflows. Its core translation question is whether agent behavior can be represented through bounded metrics and reviewable artifacts without granting the agent operational authority.

The pack is organized around evidence such as production interaction logs, task definitions, outcome labels, error categories, and reviewer judgments. It supports tasks that measure success rate, error patterns, escalation gaps, and evidence coverage.

## Appropriate use

Use this pack when assessing deployed or pilot agent workflows where logs and task definitions exist. It is suitable for monitoring design, evidence completeness review, and task-success measurement.

Avoid using this pack when success criteria are undefined, ground truth is unavailable, logs are incomplete, or the agent can change state without a human gate.

## Governance boundary

The pack can support monitoring and evaluation design. It should not be described as deployment approval until a human-reviewed decision summary is added and the evaluation thresholds are completed.
