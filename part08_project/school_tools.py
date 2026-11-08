# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 8 Build - my own module (functions moved here from Part 5)

import math


def area_of_circle(r: float) -> float:
    if r < 0:
        raise ValueError("radius cannot be negative")
    return math.pi * r ** 2


def is_even(n: int) -> bool:
    return n % 2 == 0


def greet(name: str, lang: str = "en") -> str:
    if lang == "ur":
        return f"Salaam, {name}!"
    return f"Hello, {name}!"


def average(marks: list[float]) -> float:
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def grade(avg: float) -> str:
    if avg < 0 or avg > 100:
        return "Invalid"
    if avg >= 80:
        return "A"
    if avg >= 70:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= 33:
        return "D"
    return "Fail"


def report(name: str, marks: list[float]) -> str:
    avg = average(marks)
    return f"{name}: average {avg:.1f}, grade {grade(avg)}"


# This block runs ONLY when this file is run directly (python school_tools.py).
# When main.py does "import school_tools", __name__ is "school_tools", not
# "__main__", so these self-tests are skipped.
if __name__ == "__main__":
    print("Running school_tools self-test...")
    assert is_even(4) and not is_even(7)
    assert grade(85) == "A" and grade(32) == "Fail"
    assert average([]) == 0.0
    print(report("Test", [70, 80, 90]))
    print("All self-tests passed.")
