# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 4 - Lists, dictionaries, tuples and sets


# ---------------- Warm-up: Shopping list (list) ----------------
def shopping_list():
    print("\n--- Warm-up: Shopping list ---")
    items = ["milk", "bread", "eggs"]
    items.append("tea")        # add to the end
    items.remove("bread")      # remove by value
    items.sort()               # alphabetical, changes the list in place
    for number, item in enumerate(items, start=1):
        print(f"{number}. {item}")

    # A tuple is used for data that should never change, e.g. a GPS point
    shop_location = (34.0151, 71.5249)
    print("Shop location (lat, lon):", shop_location)


# ---------------- Build: Phone book (dict) ----------------
def phone_book():
    print("\n--- Build: Phone book ---")
    contacts = {
        "Ali": "0300-1111111",
        "Sara": "0311-2222222",
        "Hamza": "0321-3333333",
        "Ayesha": "0333-4444444",
        "Bilal": "0345-5555555",
    }

    while True:
        print("\n1) Add  2) Search  3) Delete  4) Show all  5) Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Name: ").strip().title()
            number = input("Number: ").strip()
            if not name or not number:
                print("Name and number cannot be empty.")
            elif name in contacts:
                contacts[name] = number
                print(f"{name} already existed - number updated.")
            else:
                contacts[name] = number
                print(f"Saved {name}.")
        elif choice == "2":
            name = input("Search name: ").strip().title()
            print(contacts.get(name, "Not found"))   # .get() never crashes
        elif choice == "3":
            name = input("Delete name: ").strip().title()
            if name in contacts:
                del contacts[name]
                print(f"Deleted {name}.")
            else:
                print("Not found")
        elif choice == "4":
            for name in sorted(contacts):
                print(f"{name:<10} {contacts[name]}")
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Please choose 1-5.")


# ---------------- Challenge: Class result sheet ----------------
RESULTS = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Hamza": [35, 60, 42],
    "Ayesha": [70, 38, 85],
    "Bilal": [20, 29, 30],
}
PASS_MARK = 40


def result_sheet():
    print("\n--- Challenge: Class result sheet ---")
    print(f"{'Name':<8}{'Total':>7}{'Average':>9}")
    for name, marks in RESULTS.items():
        total = sum(marks)
        print(f"{name:<8}{total:>7}{total / len(marks):>9.1f}")

    # max() with key= compares students by their total marks
    topper = max(RESULTS, key=lambda name: sum(RESULTS[name]))
    print("Class topper:", topper)

    weak = set()                       # a set keeps each name only once
    for name, marks in RESULTS.items():
        for m in marks:
            if m < PASS_MARK:
                weak.add(name)
    print("Scored below 40 in any subject:", weak)


if __name__ == "__main__":
    shopping_list()
    phone_book()
    result_sheet()
