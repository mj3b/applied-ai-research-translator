import json
from pathlib import Path
from datetime import datetime, timezone
import os

RUN_ID = "run_004"
LOG_DIR = Path("logs") / RUN_ID

def load_json(path: Path) -> dict:
    return json.loads(path.read_text())

def utc_to_local_str(utc_iso: str) -> str:
    # Uses your machine's local timezone automatically
    dt = datetime.fromisoformat(utc_iso.replace("Z", "+00:00"))
    local_dt = dt.astimezone()  # local tz
    return local_dt.isoformat()

def main():
    final_path = LOG_DIR / "final.json"
    gate_path  = LOG_DIR / "human_gate.json"
    prop_path  = LOG_DIR / "proposed.json"

    if not final_path.exists():
        raise SystemExit(f"Missing: {final_path}")
    if not gate_path.exists():
        raise SystemExit(f"Missing: {gate_path}")
    if not prop_path.exists():
        raise SystemExit(f"Missing: {prop_path}")

    final = load_json(final_path)
    gate  = load_json(gate_path)
    prop  = load_json(prop_path)

    # Extracts (contract-bound)
    run_id = final.get("run_id", RUN_ID)
    model  = final.get("model")
    swarm  = final.get("swarm")
    ts_utc = final.get("_ts") or gate.get("_ts") or datetime.now(timezone.utc).isoformat()

    proposed = final.get("proposed", {})
    final_out = final.get("final", {})
    human = gate.get("human", {})

    category = final_out.get("category")
    human_decision = final_out.get("human_decision")
    confidence = proposed.get("confidence")
    rationale = proposed.get("rationale")
    abstain = proposed.get("abstain")

    # Locked, static t_c04 definitions (do not let runtime change these)
    decision_id = "t_c04"
    pack_id = "t_c04"

    decision_summary = {
        "decision_id": decision_id,
        "pack_id": pack_id,
        "run_id": run_id,
        "timestamps": {
            "utc": ts_utc,
            "local": utc_to_local_str(ts_utc),
        },
        "decision_owner": "<FILL_DECISION_OWNER>",
        "prepared_by": "system",
        "section_1_decision_statement": {
            "proposed_action": "Approve use of LLM-assisted classification to support operational triage decisions, with mandatory human approval before downstream action.",
            "decision_scope": {
                "in_scope": [
                    "failure categorization and prioritization support"
                ],
                "out_of_scope": [
                    "autonomous remediation",
                    "customer-facing actions",
                    "irreversible system changes"
                ],
            },
            "authority": "phase-gate decision owner",
        },
        "section_2_context_trigger": {
            "triggering_condition": "Manual classification latency and inconsistency materially impact time-to-decision at gate reviews.",
            "operational_relevance": "Delays and variability increase release risk, inflate review cost, and degrade confidence in gate readiness.",
        },
        "section_3_claims_evaluated": [
            {
                "claim_id": "c04-01",
                "claim_statement": "LLM-assisted comparison can surface material discrepancies between two controlled documents faster than manual review without increasing false-positive risk, when outputs are schema-bounded and human-approved.",
                "source": "applied analysis",
                "status": "supported"
            }
        ],
        "section_4_task_definition": {
            "task_objective": "Classify operational artifacts into predefined categories to support triage and prioritization.",
            "inputs": [
                "structured operational artifact",
                "canonical taxonomy"
            ],
            "outputs": [
                "category assignment (or abstain)",
                "confidence indicator",
                "rationale text"
            ],
            "constraints": {
                "latency": "bounded for analyst workflow",
                "cost": "below manual baseline",
                "data_quality_assumptions": "noisy, incomplete inputs expected",
                "governance": "human approval required for use"
            },
            "human_oversight_points": [
                "review and approve each classification before it informs action"
            ]
        },
        "section_5_evidence_summary": {
            "evidence_sources": [
                "run artifacts: logs/{run_id}/(proposed.json, human_gate.json, final.json)".format(run_id=run_id)
            ],
            "key_results": {
                "proposed": {
                    "abstain": abstain,
                    "category": proposed.get("category"),
                    "confidence": confidence,
                    "rationale": rationale
                },
                "human_gate": {
                    "decision": human.get("decision"),
                    "approved_category": human.get("approved_category"),
                    "notes": human.get("notes")
                },
                "final": {
                    "category": category,
                    "human_decision": human_decision
                }
            }
        },
        "section_6_confidence_uncertainty": {
            "confidence_level": "medium-high (within tested scope)",
            "known_uncertainties": [
                "performance on novel edge cases",
                "long-term drift (requires monitoring)"
            ],
            "unknowns_explicitly_accepted": [
                "environmental drift effects until re-evaluation trigger"
            ]
        },
        "section_7_failure_abstention": {
            "invalid_if": [
                "sustained accuracy degradation on evaluation set",
                "override/abstention rates exceed threshold",
                "taxonomy mismatch or uncontrolled scope expansion"
            ],
            "abstention_triggers": [
                "low confidence",
                "out-of-taxonomy inputs",
                "schema violation"
            ],
            "escalation_path": "route to human analyst; log event; escalate to decision owner if recurring"
        },
        "section_8_governance_traceability": {
            "run_ids": [run_id],
            "model_version": model,
            "swarm": swarm,
            "evaluation_artifacts": [
                "proposed.json",
                "human_gate.json",
                "final.json",
                "candidates.jsonl"
            ],
            "human_approvals_recorded": True,
            "artifact_paths": {
                "log_dir": str(LOG_DIR.resolve())
            }
        },
        "section_9_decision_outcome": {
            "decision": "approve_with_conditions" if human_decision == "accept" else human_decision,
            "conditions": [
                "human approval mandatory",
                "periodic re-evaluation and drift monitoring"
            ],
            "next_review_point": "trigger-based (threshold breach, drift signal, or periodic cadence)"
        },
        "section_10_signoff": {
            "decision_owner": "<FILL_DECISION_OWNER>",
            "date": "<FILL_SIGNOFF_DATE>"
        }
    }

    out_path = LOG_DIR / "decision_summary.json"
    out_path.write_text(json.dumps(decision_summary, indent=2))
    print(f"Wrote: {out_path}")

if __name__ == "__main__":
    main()
