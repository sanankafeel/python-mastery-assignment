# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
"""Save and load students to/from a JSON file."""

import json
import logging
from dataclasses import asdict
from pathlib import Path

from school.models import Student

logger = logging.getLogger(__name__)

DEFAULT_FILE = "school.json"


def save_students(students: list[Student], path: str = DEFAULT_FILE) -> None:
    data = [asdict(s) for s in students]
    Path(path).write_text(json.dumps(data, indent=2), encoding="utf-8")
    logger.info("Saved %d students to %s", len(students), path)


def load_students(path: str = DEFAULT_FILE) -> list[Student]:
    """Load students. A missing or damaged file gives an empty list, never a crash."""
    file = Path(path)
    if not file.exists():
        logger.info("%s not found, starting with no students", path)
        return []
    try:
        data = json.loads(file.read_text(encoding="utf-8"))
        return [Student(**item) for item in data]
    # OSError: file can't be opened; JSONDecodeError (a ValueError): not valid JSON;
    # TypeError/ValueError: valid JSON but not a list of proper students.
    except (OSError, TypeError, ValueError) as error:
        logger.warning("Could not read %s (%s); starting fresh", path, error)
        return []
