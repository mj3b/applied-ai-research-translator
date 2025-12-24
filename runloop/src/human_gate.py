from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class HumanDecision:
    decision: str  # accept | override | reject
    approved_category: Optional[str] = None
    notes: str = ""


def prompt_human_gate(*, proposed_category: Optional[str], rationale: str) -> HumanDecision:
    print("\n--- HUMAN APPROVAL GATE (MANDATORY) ---")
    print(f"Proposed category: {proposed_category}")
    print(f"Rationale: {rationale}\n")

    while True:
        raw = input("Approve? [y]=accept, [o]=override, [n]=reject: ").strip().lower()
        if raw in {"y", "yes"}:
            notes = input("Notes (optional): ").strip()
            return HumanDecision(decision="accept", approved_category=proposed_category, notes=notes)
        if raw in {"o", "override"}:
            cat = input("Enter approved category: ").strip()
            notes = input("Notes (required): ").strip()
            return HumanDecision(decision="override", approved_category=cat, notes=notes)
        if raw in {"n", "no"}:
            notes = input("Reason (required): ").strip()
            return HumanDecision(decision="reject", approved_category=None, notes=notes)
        print("Invalid input. Use y, o, or n.")
