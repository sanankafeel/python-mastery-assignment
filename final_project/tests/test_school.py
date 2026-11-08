# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
"""Tests for the School Manager. Run from the final_project folder:  pytest -v"""

from collections.abc import Iterator
from pathlib import Path

import pytest

from school.ai_comment import get_ai_comment, retry
from school.grading import average, grade, make_comment, rank_students, report_card
from school.models import Student
from school.storage import load_students, save_students


@pytest.fixture
def students() -> list[Student]:
    return [
        Student("Ali", 1, [80, 72, 91]),
        Student("Sara", 2, [95, 88, 90]),
        Student("Bilal", 3, [20, 29, 30]),
        Student("Zain", 4),                 # no marks yet
    ]


# ----- dataclass / validation -----
def test_student_gets_own_marks_list() -> None:
    a, b = Student("A", 10), Student("B", 11)
    a.add_mark(50)
    assert b.marks == []


@pytest.mark.parametrize("bad", [-1, 101])
def test_add_mark_rejects_out_of_range(bad: float) -> None:
    with pytest.raises(ValueError):
        Student("Ali", 1).add_mark(bad)


def test_empty_name_rejected() -> None:
    with pytest.raises(ValueError):
        Student("   ", 5)


# ----- grading -----
@pytest.mark.parametrize("avg, expected", [
    (100, "A"), (80, "A"), (79.9, "B"), (70, "B"), (60, "C"),
    (59, "D"), (33, "D"), (32.9, "Fail"), (0, "Fail"),
])
def test_grade_boundaries(avg: float, expected: str) -> None:
    assert grade(avg) == expected


def test_grade_out_of_range_raises() -> None:
    with pytest.raises(ValueError):
        grade(101)


def test_average_empty_is_zero() -> None:
    assert average([]) == 0.0


def test_report_card_contains_average_and_grade(students: list[Student]) -> None:
    card = report_card(students[0])
    assert "81.0" in card and "Grade" in card and " A" in card


# ----- ranking -----
def test_ranking_highest_first_and_skips_no_marks(students: list[Student]) -> None:
    ranked = rank_students(students)
    assert [s.name for s in ranked] == ["Sara", "Ali", "Bilal"]


# ----- storage -----
def test_save_and_load_round_trip(students: list[Student], tmp_path: Path) -> None:
    path = str(tmp_path / "school.json")
    save_students(students, path)
    assert load_students(path) == students


def test_load_missing_file_gives_empty_list(tmp_path: Path) -> None:
    assert load_students(str(tmp_path / "nope.json")) == []


def test_load_damaged_file_does_not_crash(tmp_path: Path) -> None:
    path = tmp_path / "school.json"
    path.write_text("{ this is not json")
    assert load_students(str(path)) == []


# ----- comments (AI bonus) -----
def test_rule_based_comment_excellent() -> None:
    assert make_comment(Student("Sara", 2, [95, 88, 90])) == "Excellent in all subjects, keep it up."


class FakeClient:
    """Mocked model: streams a fixed reply, no internet needed."""

    def __init__(self, fail_times: int = 0) -> None:
        self.fail_times = fail_times
        self.calls = 0
        self.last_prompt = ""

    def stream(self, prompt: str) -> Iterator[str]:
        self.calls += 1
        self.last_prompt = prompt
        if self.calls <= self.fail_times:
            raise ConnectionError("network down")
        yield from ["Great ", "work, ", "Sara!"]


def test_ai_comment_streams_pieces_with_mock(students: list[Student]) -> None:
    client = FakeClient()
    seen: list[str] = []
    text = get_ai_comment(students[1], client, on_piece=seen.append)
    assert text == "Great work, Sara!"
    assert seen == ["Great ", "work, ", "Sara!"]          # arrived piece by piece
    assert "Sara" in client.last_prompt


def test_ai_comment_retries_then_succeeds(students: list[Student],
                                          monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("school.ai_comment.time.sleep", lambda s: None)  # no real waiting
    client = FakeClient(fail_times=2)
    assert get_ai_comment(students[1], client) == "Great work, Sara!"
    assert client.calls == 3


def test_retry_gives_up_after_limit() -> None:
    calls: list[int] = []

    @retry(times=2, delay=0)
    def always_fails() -> None:
        calls.append(1)
        raise RuntimeError("boom")

    with pytest.raises(RuntimeError):
        always_fails()
    assert len(calls) == 2
