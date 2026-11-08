# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 9 - OOP: classes and objects


# ---------------- Warm-up: Student class ----------------
class Student:
    def __init__(self, name, roll_no, marks=None):
        self.name = name
        self.roll_no = roll_no
        self.marks = list(marks) if marks else []   # own list per student (Part 6 lesson)

    def add_mark(self, mark):
        if not 0 <= mark <= 100:
            raise ValueError("mark must be between 0 and 100")
        self.marks.append(mark)

    def average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0.0

    def __str__(self):                     # used by print()
        return f"{self.name} (Roll {self.roll_no}): avg {self.average():.1f}"


# ---------------- Build: Bank account ----------------
class BankAccount:
    def __init__(self, owner, balance=0.0):
        if balance < 0:
            raise ValueError("opening balance cannot be negative")
        self.owner = owner
        self.balance = balance
        self.history = []                  # list of (type, amount, balance after)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self.balance += amount
        self.history.append(("deposit", amount, self.balance))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("insufficient balance")
        self.balance -= amount
        self.history.append(("withdraw", amount, self.balance))

    def print_history(self):
        print(f"History for {self.owner}:")
        for kind, amount, after in self.history:
            print(f"  {kind:<9} Rs {amount:>8.2f}   balance Rs {after:>8.2f}")


# ---------------- Challenge: Library system ----------------
class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        status = "available" if self.available else "borrowed"
        return f"'{self.title}' by {self.author} [{status}]"


class EBook(Book):                         # inheritance: an EBook IS a Book
    def __init__(self, title, author, file_size_mb):
        super().__init__(title, author)    # let Book set title/author/available
        self.file_size_mb = file_size_mb

    def __str__(self):                     # override Book's __str__
        return f"{super().__str__()} (eBook, {self.file_size_mb} MB)"


class Library:
    def __init__(self):
        self.books = []                    # composition: a Library HAS books

    def add_book(self, book):
        self.books.append(book)

    def _find(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow(self, title):
        book = self._find(title)
        if book is None:
            print(f"No book called '{title}'.")
        elif not book.available:
            print(f"'{book.title}' is already borrowed.")
        else:
            book.available = False
            print(f"You borrowed '{book.title}'.")

    def return_book(self, title):
        book = self._find(title)
        if book is None or book.available:
            print(f"'{title}' was not borrowed from this library.")
        else:
            book.available = True
            print(f"Returned '{book.title}'.")

    def available_books(self):
        return [b for b in self.books if b.available]


def main():
    print("--- Warm-up ---")
    ali = Student("Ali", 12, [80, 72])
    ali.add_mark(91)
    print(ali)                             # Ali (Roll 12): avg 81.0
    try:
        ali.add_mark(150)
    except ValueError as e:
        print("Error:", e)

    print("\n--- Build ---")
    acc = BankAccount("Sara", 1000)
    acc.deposit(500)
    acc.withdraw(300)
    for bad in [-50, 99999]:
        try:
            acc.withdraw(bad)
        except ValueError as e:
            print(f"Withdraw {bad} refused: {e}")
    try:
        acc.deposit(0)
    except ValueError as e:
        print("Deposit 0 refused:", e)
    acc.print_history()
    print(f"Final balance: Rs {acc.balance:.2f}")

    print("\n--- Challenge ---")
    lib = Library()
    lib.add_book(Book("Python Crash Course", "Eric Matthes"))
    lib.add_book(Book("Clean Code", "Robert Martin"))
    lib.add_book(EBook("Automate the Boring Stuff", "Al Sweigart", 12.5))
    lib.borrow("clean code")
    lib.borrow("Clean Code")               # already borrowed
    lib.borrow("Harry Potter")             # not in library
    print("Available now:")
    for b in lib.available_books():
        print("  ", b)
    lib.return_book("Clean Code")
    print("After return:", len(lib.available_books()), "books available")


if __name__ == "__main__":
    main()
