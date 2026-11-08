# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 12 Build - pytest tests for grade(), every boundary included

import pytest

from grades import grade


@pytest.mark.parametrize("marks, expected", [
    (0, "Fail"),
    (32, "Fail"),     # last Fail
    (33, "D"),        # first D
    (59, "D"),        # last D
    (60, "C"),        # first C
    (69, "C"),
    (70, "B"),
    (79, "B"),
    (80, "A"),
    (100, "A"),
])
def test_grade_boundaries(marks, expected):
    assert grade(marks) == expected


@pytest.mark.parametrize("bad_marks", [101, 150, -1])
def test_grade_rejects_out_of_range(bad_marks):
    with pytest.raises(ValueError):
        grade(bad_marks)
