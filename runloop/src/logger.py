from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class RunLogger:
    log_dir: Path

    def __post_init__(self) -> None:
        self.log_dir.mkdir(parents=True, exist_ok=True)

    def write_json(self, *, filename: str, payload: Dict[str, Any]) -> Path:
        path = self.log_dir / filename
        payload = {"_ts": utc_now_iso(), **payload}
        path.write_text(json.dumps(payload, indent=2, sort_keys=True))
        return path

    def append_jsonl(self, *, filename: str, payload: Dict[str, Any]) -> Path:
        path = self.log_dir / filename
        payload = {"_ts": utc_now_iso(), **payload}
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(payload, sort_keys=True) + "\n")
        return path
