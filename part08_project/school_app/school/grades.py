# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
def average(marks: list[float]) -> float:
    return sum(marks) / len(marks) if marks else 0.0


def grade(avg: float) -> str:
    if avg >= 80:
        return "A"
    if avg >= 70:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= 33:
        return "D"
    return "Fail"
