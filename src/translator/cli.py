import argparse
import json
import os
import re
import shutil
import subprocess
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

def iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text[:60] if text else "pack"

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def write_json(path: str, obj: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write("\n")

def require_cmd(cmd: str) -> None:
    if shutil.which(cmd) is None:
        raise SystemExit(f"Missing '{cmd}'. Install with: brew install poppler")

def copy_pdf_into_pack(pdf_path: str, sources_dir: str) -> str:
    src = Path(pdf_path).expanduser().resolve()
    if not src.exists() or src.suffix.lower() != ".pdf":
        raise SystemExit(f"--pdf must be an existing .pdf file. Got: {src}")
    ensure_dir(sources_dir)
    dst = Path(sources_dir) / "paper.pdf"
    shutil.copyfile(src, dst)
    return str(dst)

def extract_text_pdftotext(pdf_in_pack: str, out_txt: str) -> None:
    require_cmd("pdftotext")
    cmd = ["pdftotext", "-layout", "-nopgbrk", pdf_in_pack, out_txt]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise SystemExit(f"pdftotext failed:\n{p.stderr.strip()}")

def make_pack(title: str, out_dir: str, pdf: Optional[str]) -> str:
    pack_id = f"{slugify(title)}_{uuid.uuid4().hex[:8]}"
    pack_path = os.path.join(out_dir, pack_id)
    sources_dir = os.path.join(pack_path, "sources")
    ensure_dir(sources_dir)

    now = iso_now()
    spec_id = f"spec_{uuid.uuid4()}"

    pdf_in_pack = None
    paper_text_path = None
    if pdf:
        pdf_in_pack = copy_pdf_into_pack(pdf, sources_dir)
        paper_text_path = os.path.join(sources_dir, "paper_text.txt")
        extract_text_pdftotext(pdf_in_pack, paper_text_path)

    agent_spec = {
        "spec_version": "0.1.0",
        "spec_id": spec_id,
        "created_at": now,
        "updated_at": now,
        "status": "draft",
        "provenance": {
            "paper": {
                "title": title,
                "authors": [],
                "venue": None,
                "year": None,
                "url": None,
                "pdf_path": pdf_in_pack,
                "paper_text_path": paper_text_path,
                "claim_extraction_notes": None
            }
        },
        "decision": {
            "name": "paper_to_agent_spec_translation",
            "user": {
                "persona": "Applied AI Builder",
                "primary_goal": "Translate a research paper into a deployable agent specification with evaluation and governance.",
                "environment": "non-regulated"
            },
            "decision_statement": "Decide whether a paper's approach can be translated into a bounded, testable agent behavior under real operating constraints.",
            "scope": {"included": ["Task definition"], "excluded": ["Production deployment"]},
            "failure_cost": {
                "severity": "high",
                "harms": ["Build a brittle agent that fails under real inputs"],
                "reversibility": "partially_reversible"
            },
            "success_criteria": ["Schema-valid outputs"]
        },
        "inputs": {
            "modalities": ["pdf", "text"],
            "required_fields": [
                {
                    "name": "paper_text",
                    "type": "string",
                    "description": "Extracted paper text stored in the pack.",
                    "constraints": {"allowed_values": None, "regex": None, "min": None, "max": None},
                    "required": True,
                    "example": "packs/<id>/sources/paper_text.txt"
                }
            ],
            "optional_fields": [],
            "data_quality_assumptions": ["Paper content may omit assumptions."],
            "redaction_rules": []
        },
        "outputs": {
            "primary_output_schema": {"type": "object"},
            "evidence_requirements": {"citations_required": True, "citation_format": "source:chunk:span", "min_evidence_items": 3},
            "confidence_labeling": {"required": True, "scale": "low", "calibration_notes": "Be conservative."},
            "abstention": {"required": True, "triggers": [], "fallback_action": "escalate_to_human", "message_template": "Abstaining."}
        },
        "evaluation": {"eval_plan_ref": f"{pack_path}/eval_plan.json", "target_metrics": [], "acceptance_thresholds": []},
        "governance": {
            "human_in_loop": {"required": True, "checkpoints": []},
            "decision_log": {"schema_ref": "schemas/decision_log.schema.json", "required_fields": []},
            "change_control": {"versioning": "semver", "retrain_or_update_triggers": [], "rollback_plan": "Revert."}
        }
    }

    eval_plan = {
        "eval_version": "0.1.0",
        "eval_id": f"eval_{uuid.uuid4()}",
        "spec_id": spec_id,
        "created_at": now,
        "datasets": [],
        "metrics": [],
        "graders": [],
        "reporting": {"report_formats": ["json"], "decision_summary_template": "Spec validation + evidence coverage summary."}
    }

    write_json(os.path.join(pack_path, "agent_spec.json"), agent_spec)
    write_json(os.path.join(pack_path, "eval_plan.json"), eval_plan)

    return pack_path

def main():
    parser = argparse.ArgumentParser(prog="translator")
    sub = parser.add_subparsers(dest="cmd", required=True)

    mk = sub.add_parser("make-pack", help="Create a new pack folder with stubbed artifacts")
    mk.add_argument("--title", required=True, help="Paper title (or working title)")
    mk.add_argument("--out", default="packs", help="Output directory (default: packs)")
    mk.add_argument("--pdf", default=None, help="Path to a PDF to store + extract into the pack")

    args = parser.parse_args()
    if args.cmd == "make-pack":
        pack_path = make_pack(args.title, args.out, args.pdf)
        print(f"✅ Created pack: {pack_path}")

if __name__ == "__main__":
    main()
