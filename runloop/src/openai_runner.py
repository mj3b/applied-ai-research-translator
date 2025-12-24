from __future__ import annotations

from typing import List, Type

from openai import OpenAI
from pydantic import BaseModel


class OpenAIClassifier:
    """Bounded classifier using OpenAI Responses API with structured parsing."""

    def __init__(self, *, model: str, reasoning_effort: str = "low") -> None:
        self.client = OpenAI()
        self.model = model
        self.reasoning_effort = reasoning_effort

    def classify(
        self,
        *,
        system_instructions: str,
        user_content: str,
        text_format: Type[BaseModel],
    ) -> BaseModel:
        response = self.client.responses.parse(
            model=self.model,
            
            input=[
                {"role": "system", "content": system_instructions},
                {"role": "user", "content": user_content},
            ],
            text_format=text_format,
        )
        return response.output_parsed


def build_user_payload(*, artifact: str, taxonomy: List[str]) -> str:
    tax = "\n".join(f"- {t}" for t in taxonomy)
    return (
        "You are given an operational artifact and a taxonomy. "
        "Classify the artifact into exactly one taxonomy category, or abstain.\n\n"
        "TAXONOMY (choose one):\n"
        f"{tax}\n\n"
        "ARTIFACT:\n"
        f"{artifact}\n"
    )
