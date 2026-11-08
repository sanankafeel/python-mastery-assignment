# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
"""The Student dataclass."""

from dataclasses import dataclass, field

MIN_MARK = 0
MAX_MARK = 100


@dataclass
class Student:
    name: str
    roll_no: int
    marks: list[float] = field(default_factory=list)  # each student gets their own list

    def __post_init__(self) -> None:
        self.name = self.name.strip()
        if not self.name:
            raise ValueError("name cannot be empty")
        if self.roll_no <= 0:
            raise ValueError("roll number must be positive")
        for mark in self.marks:
            check_mark(mark)

    def add_mark(self, mark: float) -> None:
        check_mark(mark)
        self.marks.append(mark)


def check_mark(mark: float) -> None:
    """Raise ValueError if a mark is outside 0-100."""
    if not MIN_MARK <= mark <= MAX_MARK:
        raise ValueError(f"mark must be between {MIN_MARK} and {MAX_MARK}, got {mark}")
