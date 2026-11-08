# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 7 - Exceptions and files
# The "second program" for the challenge is part07_read_results.py

import csv
import datetime
import json
import os

DIARY_FILE = "diary.txt"
CSV_FILE = "results.csv"
JSON_FILE = "results.json"


# ---------------- Warm-up: Safe division ----------------
def safe_division():
    print("\n--- Warm-up: Safe division ---")
    while True:
        try:
            a = float(input("First number : "))
            b = float(input("Second number: "))
            result = a / b
        except ValueError:
            print("  That is not a number. Try again.")
        except ZeroDivisionError:
            print("  Cannot divide by zero. Try again.")
        else:                               # runs only if no exception happened
            print(f"{a:g} / {b:g} = {result:.4g}")
            break


# ---------------- Build: Daily diary ----------------
def write_entry():
    note = input("Today's note: ").strip()
    if not note:
        print("Empty note not saved.")
        return
    today = datetime.date.today()
    # "a" = append mode: adds to the end, creates the file if it is missing
    with open(DIARY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{today}: {note}\n")
    print("Saved.")


def read_entries():
    try:
        with open(DIARY_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("No entries yet")
        return
    print(content if content else "No entries yet")


def diary_menu():
    print("\n--- Build: Daily diary ---")
    while True:
        choice = input("1) Write today's note  2) Read all  3) Back: ").strip()
        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            break
        else:
            print("Please choose 1, 2 or 3.")


# ---------------- Challenge: CSV + JSON result sheet ----------------
RESULTS = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Hamza": [35, 60, 42],
    "Ayesha": [70, 38, 85],
    "Bilal": [20, 29, 30],
}


def save_results():
    print("\n--- Challenge: save results ---")
    rows = []
    for name, marks in RESULTS.items():
        avg = round(sum(marks) / len(marks), 2)
        rows.append({"name": name, "mark1": marks[0], "mark2": marks[1],
                     "mark3": marks[2], "average": avg})

    # newline="" stops blank lines appearing between rows on Windows
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "mark1", "mark2", "mark3", "average"])
        writer.writeheader()
        writer.writerows(rows)

    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2)

    print(f"Saved {len(rows)} students to {os.path.abspath(CSV_FILE)} and {JSON_FILE}")
    print("Run part07_read_results.py to read them back.")


if __name__ == "__main__":
    safe_division()
    diary_menu()
    save_results()
