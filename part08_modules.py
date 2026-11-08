# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 8 - Modules, packages and projects
# Warm-up is in this file. Build + Challenge are in the part08_project/ folder.

import datetime
import math
import random
import statistics


def standard_library_tour():
    print("--- Warm-up: Standard library tour ---")

    # math
    print("Square root of 144:", math.sqrt(144))

    # random
    students = ["Ali", "Sara", "Hamza", "Ayesha", "Bilal"]
    print("Random student:", random.choice(students))

    # datetime - days left until 31 December of this year
    today = datetime.date.today()
    year_end = datetime.date(today.year, 12, 31)
    print(f"Days left until 31 December: {(year_end - today).days}")

    # statistics
    marks = [78, 92, 65, 88, 70]
    print("Marks:", marks)
    print("Mean  :", statistics.mean(marks))
    print("Median:", statistics.median(marks))


if __name__ == "__main__":
    standard_library_tour()
