# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
"""Averages, grades, report cards, ranking and rule-based teacher comments."""

from school.models import Student


def average(marks: list[float]) -> float:
    """Average of a list of marks; 0.0 for an empty list (no crash)."""
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def grade(avg: float) -> str:
    """Grade table from Part 2. Raises ValueError outside 0-100."""
    if avg < 0 or avg > 100:
        raise ValueError(f"average must be 0-100, got {avg}")
    if avg >= 80:
        return "A"
    if avg >= 70:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= 33:
        return "D"
    return "Fail"


def report_card(student: Student) -> str:
    """Build the report card text for one student."""
    lines = [
        "=" * 32,
        f" REPORT CARD - {student.name} (Roll {student.roll_no})",
        "=" * 32,
    ]
    if not student.marks:
        lines.append(" No marks entered yet.")
    else:
        for number, mark in enumerate(student.marks, start=1):
            lines.append(f" Subject {number:<3}: {mark:>6.1f}")
        avg = average(student.marks)
        lines.append("-" * 32)
        lines.append(f" Average    : {avg:>6.1f}")
        lines.append(f" Grade      : {grade(avg):>6}")
    lines.append("=" * 32)
    return "\n".join(lines)


def rank_students(students: list[Student]) -> list[Student]:
    """Students with marks, highest average first. Ties are broken by roll number."""
    with_marks = [s for s in students if s.marks]
    return sorted(with_marks, key=lambda s: (-average(s.marks), s.roll_no))


def make_comment(student: Student) -> str:
    """Short teacher comment from simple rules (AI bonus, rule-based version)."""
    if not student.marks:
        return "No marks yet, so no comment can be written."
    avg = average(student.marks)
    lowest = min(student.marks)
    if avg >= 80 and lowest >= 70:
        return "Excellent in all subjects, keep it up."
    if avg >= 80:
        return "Excellent overall, but give a little more time to your weakest subject."
    if avg >= 60:
        return "Good work. Steady practice can take you to the top grade."
    if avg >= 33:
        return "You have passed, but regular revision is needed to improve."
    return "Needs serious improvement. Please meet your teacher for extra help."
