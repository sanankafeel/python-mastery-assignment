# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 5 - Functions and comprehensions
# (Type hints added for Part 11 - checked with mypy.)

import math


# ---------------- Warm-up: Small helpers ----------------
def area_of_circle(r: float) -> float:
    """Area = pi * r^2. Radius cannot be negative."""
    if r < 0:
        raise ValueError("radius cannot be negative")
    return math.pi * r ** 2


def is_even(n: int) -> bool:
    return n % 2 == 0


def greet(name: str, lang: str = "en") -> str:
    """Greet in English ("en") or Urdu ("ur"). Unknown languages fall back to English."""
    if lang == "ur":
        return f"Salaam, {name}!"
    return f"Hello, {name}!"


# ---------------- Build: Marks toolkit ----------------
def average(marks: list[float]) -> float:
    if not marks:                      # avoid dividing by zero on an empty list
        return 0.0
    return sum(marks) / len(marks)


def grade(avg: float) -> str:
    """Same table as Part 2."""
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
    """One-line result that reuses average() and grade()."""
    avg = average(marks)
    return f"{name}: average {avg:.1f}, grade {grade(avg)}"


# Same result sheet as Part 4
RESULTS: dict[str, list[float]] = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Hamza": [35, 60, 42],
    "Ayesha": [70, 38, 85],
    "Bilal": [20, 29, 30],
}


def main() -> None:
    print("--- Warm-up ---")
    for r in [1, 2.5, 10]:
        print(f"Area of circle r={r}: {area_of_circle(r):.2f}")
    for n in [4, 7, 0]:
        print(f"is_even({n}) -> {is_even(n)}")
    print(greet("Ali"))
    print(greet("Sara", "ur"))
    print(greet("Hamza", lang="en"))

    print("\n--- Build ---")
    for name in ["Ali", "Hamza", "Bilal"]:
        print(report(name, RESULTS[name]))

    print("\n--- Challenge: comprehensions ---")
    squares = [n * n for n in range(1, 11)]
    names = ["Ali", "Sara", "Hamza", "Ayesha", "Bilal", "Zain"]
    long_names = [n for n in names if len(n) > 4]
    averages = {name: round(average(marks), 1) for name, marks in RESULTS.items()}
    passing = {name: avg for name, avg in averages.items() if avg >= 33}

    print("Squares:", squares)
    print("Names longer than 4 letters:", long_names)
    print("Averages:", averages)
    print("Passing students:", passing)


if __name__ == "__main__":
    main()
