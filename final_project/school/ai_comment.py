# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
"""AI bonus: teacher comment from an AI model.

- API key is read from a .env file (never written in the code).
- The reply is streamed with a generator.
- A retry decorator tries again if the call fails.
- Tests use a fake (mocked) client, so they run offline.
"""

import logging
import os
import time
from collections.abc import Callable, Iterator
from functools import wraps
from pathlib import Path
from typing import Any, Protocol

from school.grading import average, grade
from school.models import Student

logger = logging.getLogger(__name__)

ENV_FILE = ".env"
API_KEY_NAME = "ANTHROPIC_API_KEY"
MODEL = "claude-haiku-5-5"


class ChatClient(Protocol):
    """Anything with a stream(prompt) method that yields text pieces."""

    def stream(self, prompt: str) -> Iterator[str]: ...


def load_env(path: str = ENV_FILE) -> None:
    """Read KEY=VALUE lines from .env into os.environ (tiny dotenv replacement)."""
    file = Path(path)
    if not file.exists():
        return
    for line in file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"'))


def retry(times: int = 3, delay: float = 1.0) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator: call the function again (up to 'times') if it raises an exception."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as error:  # any API/network error
                    logger.warning("%s failed (attempt %d/%d): %s",
                                   func.__name__, attempt, times, error)
                    if attempt == times:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator


def build_prompt(student: Student) -> str:
    avg = average(student.marks)
    return (
        "You are a kind school teacher. Write ONE short report-card comment "
        "(max 25 words) for this student.\n"
        f"Name: {student.name}\nMarks: {student.marks}\n"
        f"Average: {avg:.1f}\nGrade: {grade(avg)}"
    )


def stream_ai_comment(student: Student, client: ChatClient) -> Iterator[str]:
    """Generator: yields the comment piece by piece as the model sends it."""
    yield from client.stream(build_prompt(student))


@retry(times=3, delay=1.0)
def get_ai_comment(student: Student, client: ChatClient,
                   on_piece: Callable[[str], None] | None = None) -> str:
    """Collect the streamed pieces into one string, showing each piece as it arrives."""
    pieces: list[str] = []
    for piece in stream_ai_comment(student, client):
        if on_piece is not None:
            on_piece(piece)
        pieces.append(piece)
    return "".join(pieces).strip()


class AnthropicClient:
    """Real client. Needs: pip install anthropic, and ANTHROPIC_API_KEY in .env"""

    def __init__(self, api_key: str) -> None:
        import anthropic  # imported here so the app still runs without the library
        self._client = anthropic.Anthropic(api_key=api_key)

    def stream(self, prompt: str) -> Iterator[str]:
        with self._client.messages.stream(
            model=MODEL,
            max_tokens=100,
            messages=[{"role": "user", "content": prompt}],
        ) as response:
            yield from response.text_stream


def make_client() -> ChatClient | None:
    """Return a real AI client, or None if there is no key or no library."""
    load_env()
    api_key = os.environ.get(API_KEY_NAME)
    if not api_key:
        logger.info("No %s found; using rule-based comments", API_KEY_NAME)
        return None
    try:
        return AnthropicClient(api_key)
    except ImportError:
        logger.info("anthropic library not installed; using rule-based comments")
        return None
