import argparse
import json
import uuid
from pathlib import Path
from datetime import datetime, timezone
from jsonschema import validate

def iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def write_json(path: Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def load_task(pack_dir: Path, task_id: str) -> dict:
    tasks = load_json(pack_dir / "tasks.json")["tasks"]
    for t in tasks:
        if t["task_id"] == task_id:
            return t
    raise SystemExit(f"Task not found: {task_id}")

def validate_against_schema(schema_path: Path, instance: dict) -> None:
    schema = load_json(schema_path)
    validate(instance=instance, schema=schema)


def _pct_drop(baseline: float, current: float) -> float:
    if baseline == 0:
        return 0.0
    return (baseline - current) / baseline

def exec_t_c04(inputs: dict) -> tuple[str, dict, list[str], str]:
    ts = inputs["production_metrics_timeseries"]
    baseline = inputs["baseline_metrics"]
    policy = inputs["drift_policy"]

    min_windows = int(policy.get("min_windows", 1))
    if len(ts) < min_windows:
        return ("abstained",
                {"reason": "insufficient_windows", "have": len(ts), "need": min_windows},
                [],
                "Not enough windows to evaluate drift policy.")

    base_success = float(baseline.get("task_success_rate"))
    base_override = float(baseline.get("override_rate"))

    drop_thresh = float(policy.get("task_success_drop_pct", 0.0))
    inc_thresh = float(policy.get("override_increase_pct", 0.0))

    drift_signals = []
    evidence = []

    # Evaluate last window (simple v1). Later we can do trend tests.
    last = ts[-1]
    cur_success = float(last.get("task_success_rate"))
    cur_override = float(last.get("override_rate"))

    success_drop = _pct_drop(base_success, cur_success)
    override_inc = _pct_drop(base_override, cur_override) * -1  # negative drop == increase

    evidence.append(
        f"baseline success={base_success:.2f}, override={base_override:.2f}"
    )
    evidence.append(
        f"last window {last.get('window_start')}..{last.get('window_end')}: "
        f"success={cur_success:.2f} (drop {success_drop:.2%}), "
        f"override={cur_override:.2f}"
    )

    drift = False
    if success_drop >= drop_thresh:
        drift = True
        drift_signals.append(f"task_success_rate drop {success_drop:.2%} >= {drop_thresh:.2%}")
    if (cur_override - base_override) / (base_override if base_override else 1.0) >= inc_thresh:
        drift = True
        drift_signals.append(
            f"override_rate increase {(cur_override-base_override):.2%} >= {inc_thresh:.2%}"
        )

    recommended_action = "no_action"
    if drift:
        recommended_action = "re_evaluate_agent_and_investigate_data_shift"

    result = {
        "drift_detected": drift,
        "drift_signals": drift_signals,
        "recommended_action": recommended_action,
        "notes": "v1 drift policy applied to last window vs baseline."
    }
    return ("ok", result, evidence, "Computed drift flags from metrics + policy.")

def simple_executor(task: dict, inputs: dict) -> tuple[str, dict, list[str], str]:
    """
    Non-LLM v0 executor:
    - checks required input keys exist (by name)
    - produces a structured summary output
    - abstains when key inputs missing
    """

    # Task-specific executor (v1)
    if task.get("task_id") == "t_c04":
        required = [f["name"] for f in task["inputs"]["required"]]
        missing = [k for k in required if k not in inputs]
        if missing:
            return ("abstained",
                    {"reason": "missing_required_inputs", "missing": missing},
                    [],
                    f"Missing required inputs: {missing}")
        return exec_t_c04(inputs)

    required_fields = [f["name"] for f in task["inputs"]["required"]]
    missing = [k for k in required_fields if k not in inputs]

    if missing:
        return (
            "abstained",
            {"reason": "missing_required_inputs", "missing": missing},
            [],
            f"Missing required inputs: {missing}"
        )

    # Placeholder execution: we just echo back what we'd use
    # Later we will replace this with real metric calculations or an LLM tool chain.
    evidence = []
    if "eval_artifacts" in inputs:
        evidence.append("eval_artifacts provided")
    if "production_metrics_timeseries" in inputs:
        evidence.append("production_metrics_timeseries provided")

    result = {
        "task_name": task["name"],
        "objective": task["objective"],
        "inputs_seen": list(inputs.keys()),
        "next_action": "Implement domain executor for this task (v1)."
    }
    return ("ok", result, evidence, "v0 executor produced a stubbed result")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pack", required=True, help="Pack directory, e.g. packs/measuring_agents_in_production_a98e2ca8")
    ap.add_argument("--task", required=True, help="Task id, e.g. t_c02")
    ap.add_argument("--run", default=None, help="Run id (optional). If omitted, a new one is created.")
    ap.add_argument("--input", required=True, help="Path to input.json for this run")
    args = ap.parse_args()

    pack_dir = Path(args.pack)
    if not pack_dir.exists():
        raise SystemExit(f"Pack dir not found: {pack_dir}")

    task = load_task(pack_dir, args.task)

    run_id = args.run or f"run_{uuid.uuid4().hex[:8]}"
    run_dir = Path("runs") / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    input_path = Path(args.input)
    run_input = load_json(input_path)

    # validate run input schema
    validate_against_schema(Path("schemas/run_input.schema.json"), run_input)

    # enforce that run_input matches requested pack/task
    if run_input["pack_id"] != pack_dir.name or run_input["task_id"] != args.task:
        raise SystemExit("run input pack_id/task_id does not match --pack/--task")

    status, result, evidence, notes = simple_executor(task, run_input["inputs"])

    run_output = {
        "run_id": run_input["run_id"],
        "pack_id": run_input["pack_id"],
        "task_id": run_input["task_id"],
        "created_at": iso_now(),
        "status": status,
        "result": result,
        "evidence": evidence,
        "notes": notes
    }

    # validate run output schema
    validate_against_schema(Path("schemas/run_output.schema.json"), run_output)

    write_json(run_dir / "output.json", run_output)

    # decision log (super minimal v0)
    decision_log = {
        "run_id": run_input["run_id"],
        "pack_id": run_input["pack_id"],
        "task_id": run_input["task_id"],
        "status": status,
        "created_at": run_output["created_at"],
        "input_path": str(input_path),
        "output_path": str(run_dir / "output.json")
    }
    write_json(run_dir / "decision_log.json", decision_log)

    print(f"✅ Wrote runs/{run_id}/output.json and decision_log.json")

if __name__ == "__main__":
    main()
