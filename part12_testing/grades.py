# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 12 - grade() changed to raise ValueError for marks outside 0-100


def grade(marks: float) -> str:
    if marks < 0 or marks > 100:
        raise ValueError(f"marks must be 0-100, got {marks}")
    if marks >= 80:
        return "A"
    if marks >= 70:
        return "B"
    if marks >= 60:
        return "C"
    if marks >= 33:
        return "D"
    return "Fail"
