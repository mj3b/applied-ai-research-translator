from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import List, Optional

from src.schemas import ClassificationOutput
from src.openai_runner import OpenAIClassifier, build_user_payload
from src.logger import RunLogger
from src.human_gate import prompt_human_gate


SYSTEM_INSTRUCTIONS = (
    "You are a bounded classifier. You must follow the provided schema exactly. "
    "You must either select exactly one taxonomy category or abstain. "
    "If you abstain, set abstain=true and category=null. "
    "Your rationale must be brief and grounded only in the artifact text."
)


def load_taxonomy(path: Path) -> List[str]:
    items = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(items, list) or not all(isinstance(x, str) for x in items):
        raise ValueError("taxonomy must be a JSON list of strings")
    return items


def agree_or_abstain(candidates: List[ClassificationOutput]) -> ClassificationOutput:
    """Swarm aggregation rule (locked):
    - If all non-abstaining candidates agree on category, accept.
    - Any disagreement => abstain.
    """
    # If any candidate abstains, treat as uncertainty.
    if any(c.abstain for c in candidates):
        return ClassificationOutput(category=None, confidence=0.0, rationale="Swarm disagreement/abstention", abstain=True)

    cats = {c.category for c in candidates}
    if len(cats) != 1:
        return ClassificationOutput(category=None, confidence=0.0, rationale="Swarm disagreement", abstain=True)

    # All agree. Use minimum confidence to avoid optimism.
    conf = min(c.confidence for c in candidates)
    rationale = " | ".join(c.rationale.strip() for c in candidates)
    return ClassificationOutput(category=candidates[0].category, confidence=conf, rationale=rationale, abstain=False)


def main() -> int:
    ap = argparse.ArgumentParser(description="t_c02 Run loop (contract-preserving)")
    ap.add_argument("--artifact", required=True, help="Path to artifact text file")
    ap.add_argument("--taxonomy", required=True, help="Path to taxonomy JSON file")
    ap.add_argument("--model", default="gpt-4o-2024-08-06", help="OpenAI model")
    ap.add_argument("--reasoning_effort", default="low", choices=["low", "medium", "high"], help="Reasoning effort")
    ap.add_argument("--swarm", type=int, default=1, help="Number of independent calls (1 = no swarm)")
    ap.add_argument("--run_id", required=True, help="Run identifier")
    ap.add_argument("--log_dir", default="./logs", help="Log directory")

    args = ap.parse_args()

    artifact_text = Path(args.artifact).read_text(encoding="utf-8")
    taxonomy = load_taxonomy(Path(args.taxonomy))

    logger = RunLogger(Path(args.log_dir) / args.run_id)

    classifier = OpenAIClassifier(model=args.model, reasoning_effort=args.reasoning_effort)
    user_payload = build_user_payload(artifact=artifact_text, taxonomy=taxonomy)

    # 1) Model candidates (single or swarm)
    candidates: List[ClassificationOutput] = []
    for i in range(max(1, int(args.swarm))):
        out = classifier.classify(
            system_instructions=SYSTEM_INSTRUCTIONS,
            user_content=user_payload,
            text_format=ClassificationOutput,
        )
        candidates.append(out)
        logger.append_jsonl(
            filename="candidates.jsonl",
            payload={"i": i, "candidate": out.model_dump()},
        )

    # 2) Aggregate per locked rule
    proposed = candidates[0] if len(candidates) == 1 else agree_or_abstain(candidates)

    logger.write_json(filename="proposed.json", payload={"proposed": proposed.model_dump()})

    # 3) Mandatory human gate
    human = prompt_human_gate(proposed_category=proposed.category, rationale=proposed.rationale)
    logger.write_json(
        filename="human_gate.json",
        payload={"human": {"decision": human.decision, "approved_category": human.approved_category, "notes": human.notes}},
    )

    # 4) Final outcome (no autonomy)
    final_category: Optional[str] = None
    if human.decision == "accept":
        final_category = human.approved_category
    elif human.decision == "override":
        final_category = human.approved_category
    elif human.decision == "reject":
        final_category = None

    logger.write_json(
        filename="final.json",
        payload={
            "run_id": args.run_id,
            "model": args.model,
            "swarm": args.swarm,
            "proposed": proposed.model_dump(),
            "final": {"category": final_category, "human_decision": human.decision},
        },
    )

    print("\n--- RUN COMPLETE ---")
    print(f"Run ID: {args.run_id}")
    print(f"Final category: {final_category}")
    print(f"Logs: {logger.log_dir.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
