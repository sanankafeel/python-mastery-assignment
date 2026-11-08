# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 2 - Conditions (if / elif / else)


def read_int(prompt):
    """Ask until the user types a whole number (negative allowed)."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Please enter a whole number.")


def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Please enter a number.")


# ---------------- Warm-up: Even, odd and sign ----------------
def even_odd_sign():
    print("\n--- Warm-up: Even, odd and sign ---")
    n = read_int("Enter a number: ")

    if n > 0:
        sign = "positive"
    elif n < 0:
        sign = "negative"
    else:
        sign = "zero"

    parity = "even" if n % 2 == 0 else "odd"   # remainder 0 means divisible by 2
    print(f"{n} is {sign} and {parity}.")


# ---------------- Build: Grade calculator ----------------
def get_grade(marks):
    """Return the grade for marks out of 100, or None if marks are invalid."""
    if marks < 0 or marks > 100:
        return None
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 33:
        return "D"
    else:
        return "Fail"


def grade_calculator():
    print("\n--- Build: Grade calculator ---")
    marks = read_float("Marks out of 100: ")
    grade = get_grade(marks)
    if grade is None:
        print("Invalid marks")
    else:
        print(f"Marks: {marks:g}  ->  Grade: {grade}")


# ---------------- Challenge: Electricity bill ----------------
FIXED_CHARGE = 50


def electricity_bill(units):
    """Slab billing: 1-100 @ Rs10, 101-200 @ Rs15, above 200 @ Rs20, + Rs50 fixed."""
    if units <= 100:
        energy = units * 10
    elif units <= 200:
        energy = 100 * 10 + (units - 100) * 15
    else:
        energy = 100 * 10 + 100 * 15 + (units - 200) * 20
    return energy + FIXED_CHARGE


def electricity_menu():
    print("\n--- Challenge: Electricity bill ---")
    units = read_int("Units used: ")
    if units < 0:
        print("Units cannot be negative.")
        return
    print(f"Total bill for {units} units: Rs {electricity_bill(units)}")

    # Boundary tests, as the assignment suggests (bugs hide at edges)
    print("Boundary check:")
    for u in [0, 100, 101, 200, 201, 250]:
        print(f"  {u:>3} units -> Rs {electricity_bill(u)}")


if __name__ == "__main__":
    even_odd_sign()
    grade_calculator()
    electricity_menu()
