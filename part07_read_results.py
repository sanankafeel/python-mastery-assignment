# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 7 Challenge (second program) - read results.csv back and print the topper

import csv

CSV_FILE = "results.csv"


def main():
    try:
        with open(CSV_FILE, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))   # each row is a dict; all values are text
    except FileNotFoundError:
        print(f"{CSV_FILE} not found. Run part07_files.py first.")
        return

    if not rows:
        print("The file has no students.")
        return

    for row in rows:
        print(f"{row['name']:<8} {row['mark1']:>3} {row['mark2']:>3} {row['mark3']:>3}"
              f"  avg {row['average']}")

    # convert the text "88.33" to a number before comparing
    topper = max(rows, key=lambda row: float(row["average"]))
    print(f"\nTopper: {topper['name']} with average {topper['average']}")


if __name__ == "__main__":
    main()
