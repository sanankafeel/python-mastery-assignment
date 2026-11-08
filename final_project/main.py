# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
"""School Manager - menu-driven program for a school office.

Run:  python main.py
"""

import logging

from school.ai_comment import get_ai_comment, make_client
from school.grading import average, grade, make_comment, rank_students, report_card
from school.models import Student
from school.storage import load_students, save_students

DATA_FILE = "school.json"
MENU = """
===== SCHOOL MANAGER =====
1. Add student
2. Add marks
3. Show report card
4. Class ranking
5. Write comment
6. Save and exit"""

logger = logging.getLogger("school_manager")


# ---------- small input helpers: they keep asking, so bad input never crashes ----------
def ask_text(prompt: str) -> str:
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("  This cannot be empty.")


def ask_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Please enter a whole number.")


def ask_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Please enter a number.")


def find_student(students: list[Student], roll_no: int) -> Student | None:
    for student in students:
        if student.roll_no == roll_no:
            return student
    return None


def pick_student(students: list[Student]) -> Student | None:
    if not students:
        print("No students yet. Add one first (option 1).")
        return None
    student = find_student(students, ask_int("Roll number: "))
    if student is None:
        print("No student with that roll number.")
    return student


# ---------- one function per menu option ----------
def add_student(students: list[Student]) -> None:
    name = ask_text("Name: ")
    roll_no = ask_int("Roll number: ")
    if find_student(students, roll_no) is not None:
        print(f"Roll number {roll_no} is already taken.")
        return
    try:
        students.append(Student(name=name, roll_no=roll_no))
    except ValueError as error:
        print(f"Could not add student: {error}")
        return
    logger.info("Added student %s (roll %d)", name, roll_no)
    print(f"Added {name}.")


def add_marks(students: list[Student]) -> None:
    student = pick_student(students)
    if student is None:
        return
    count = ask_int("How many subjects? ")
    if count <= 0:
        print("Number of subjects must be at least 1.")
        return
    for number in range(1, count + 1):
        while True:
            try:
                student.add_mark(ask_float(f"  Subject {number} mark (0-100): "))
                break
            except ValueError as error:
                print(f"  {error}")
    logger.info("Added %d marks for roll %d", count, student.roll_no)
    print(f"Marks saved for {student.name}.")


def show_report_card(students: list[Student]) -> None:
    student = pick_student(students)
    if student is not None:
        print(report_card(student))


def show_ranking(students: list[Student]) -> None:
    ranked = rank_students(students)
    if not ranked:
        print("No students with marks yet.")
        return
    print(f"\n{'Rank':<6}{'Roll':<6}{'Name':<15}{'Average':>8}  Grade")
    for position, student in enumerate(ranked, start=1):
        avg = average(student.marks)
        print(f"{position:<6}{student.roll_no:<6}{student.name:<15}{avg:>8.1f}  {grade(avg)}")


def write_comment(students: list[Student]) -> None:
    student = pick_student(students)
    if student is None:
        return
    if not student.marks:
        print(make_comment(student))
        return
    client = make_client()
    if client is None:
        print("Comment:", make_comment(student))
        return
    print("AI comment: ", end="", flush=True)
    try:
        get_ai_comment(student, client, on_piece=lambda p: print(p, end="", flush=True))
        print()
    except Exception as error:  # AI failed even after retries -> use the rules
        logger.warning("AI comment failed: %s", error)
        print(f"\n(AI unavailable) Comment: {make_comment(student)}")


def main() -> None:
    logging.basicConfig(filename="school.log", level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    students = load_students(DATA_FILE)
    print(f"Loaded {len(students)} students from {DATA_FILE}.")

    actions = {
        "1": add_student,
        "2": add_marks,
        "3": show_report_card,
        "4": show_ranking,
        "5": write_comment,
    }
    while True:
        print(MENU)
        choice = input("Choose: ").strip()
        if choice == "6":
            try:
                save_students(students, DATA_FILE)
            except OSError as error:  # e.g. folder is read-only or disk is full
                logger.error("Save failed: %s", error)
                print(f"Could not save: {error}. Your data is still here; try again.")
                continue
            print(f"Saved {len(students)} students. Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Please choose a number from 1 to 6.")
        else:
            action(students)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting without saving.")
