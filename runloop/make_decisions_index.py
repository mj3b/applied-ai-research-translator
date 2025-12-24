import json
from pathlib import Path

LOGS_DIR = Path("logs")
OUT_FILE = Path("DECISIONS.md")

def main():
    entries = []

    for run_dir in sorted(LOGS_DIR.iterdir()):
        if not run_dir.is_dir():
            continue

        ds_path = run_dir / "decision_summary.json"
        if not ds_path.exists():
            continue

        data = json.loads(ds_path.read_text())

        decision_id = data.get("decision_id", "UNKNOWN")
        run_id = data.get("run_id", run_dir.name)
        outcome = data.get("section_9_decision_outcome", {}).get("decision", "UNKNOWN")

        entries.append({
            "decision_id": decision_id,
            "run_id": run_id,
            "path": str(ds_path),
            "outcome": outcome
        })

    lines = ["# Decision Index\n"]
    for e in entries:
        lines.append(f"## {e['decision_id']}")
        lines.append(f"- Run: `{e['run_id']}`")
        lines.append(f"- Artifact: `{e['path']}`")
        lines.append(f"- Outcome: `{e['outcome']}`\n")

    OUT_FILE.write_text("\n".join(lines))
    print(f"Wrote: {OUT_FILE}")

if __name__ == "__main__":
    main()
