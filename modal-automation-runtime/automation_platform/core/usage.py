from __future__ import annotations

from dataclasses import dataclass

from automation_platform.core.config import UsageLimits


@dataclass
class UsageCounter:
    documents_processed: int = 0
    ai_calls: int = 0
    messages_sent: int = 0
    ocr_pages: int = 0


class UsageLimitExceeded(RuntimeError):
    """Raised when a workflow would exceed a configured free-tier guardrail."""


def assert_within_limits(counter: UsageCounter, limits: UsageLimits) -> None:
    """Fail fast before a workflow overruns a free/included allowance."""

    if counter.documents_processed > limits.max_documents_per_batch:
        raise UsageLimitExceeded("document batch limit exceeded")
    if counter.ai_calls > limits.max_ai_calls_per_day:
        raise UsageLimitExceeded("daily AI call limit exceeded")
    if counter.messages_sent > limits.max_messages_per_day:
        raise UsageLimitExceeded("daily message limit exceeded")
    if counter.ocr_pages > limits.max_ocr_pages_per_batch:
        raise UsageLimitExceeded("OCR page batch limit exceeded")
