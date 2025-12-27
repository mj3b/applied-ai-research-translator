from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field, field_validator


class ClassificationOutput(BaseModel):
    """Strict output for the t_c02 Task.

    Contract:
    - Outputs are limited to: category, confidence, rationale, abstain.
    - If abstain=True, category MUST be None.
    - confidence is bounded to [0.0, 1.0].
    """

    category: Optional[str] = Field(
        default=None,
        description="Chosen taxonomy category. Must be null when abstain=true.",
    )
    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Model confidence in the category assignment (0.0–1.0).",
    )
    rationale: str = Field(
        ...,
        min_length=1,
        description="Brief, bounded rationale grounded in the provided artifact.",
    )
    abstain: bool = Field(
        ...,
        description="True when the model cannot confidently classify within the taxonomy.",
    )

    @field_validator("category")
    @classmethod
    def category_required_unless_abstain(cls, v, info):
        abstain = info.data.get("abstain")
        if abstain is True and v is not None:
            raise ValueError("category must be null when abstain=true")
        if abstain is False and (v is None or not str(v).strip()):
            raise ValueError("category is required when abstain=false")
        return v
