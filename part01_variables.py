# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 1 - Variables, data types, input and output


def read_float(prompt, minimum=None):
    """Keep asking until the user types a valid number (decimal allowed).
    If minimum is given, numbers below it are refused too."""
    while True:
        text = input(prompt)
        try:
            value = float(text)
        except ValueError:
            print("  Please enter a number, e.g. 12.5")
            continue
        if minimum is not None and value < minimum:
            print(f"  The number cannot be less than {minimum}.")
            continue
        return value


def read_int(prompt, minimum=0):
    """Keep asking until the user types a whole number that is at least 'minimum'."""
    while True:
        text = input(prompt).strip()
        if text.isdigit() and int(text) >= minimum:   # isdigit() is False for "-5" and "abc"
            return int(text)
        print(f"  Please enter a whole number of at least {minimum}.")


# ---------------- Warm-up: Student ID card ----------------
def student_card():
    print("\n--- Warm-up: Student ID card ---")
    name = input("Name : ").strip()          # str
    age = read_int("Age  : ")                # int
    student_class = input("Class: ").strip() # str ("class" is a Python keyword)
    city = input("City : ").strip()          # str

    print("\n======== STUDENT CARD ========")
    print(f"Name : {name}")
    print(f"Age  : {age}")
    print(f"Class: {student_class}")
    print(f"City : {city}")
    print("==============================")

    # type() tells us what kind of value each variable holds
    print("Types:", type(name), type(age), type(student_class), type(city))


# ---------------- Build: Shop bill ----------------
DISCOUNT_RATE = 0.05   # 5% discount
TAX_RATE = 0.17        # 17% tax, applied AFTER the discount


def shop_bill():
    print("\n--- Build: Shop bill ---")
    item = input("Item name: ").strip()
    price = read_float("Price (Rs): ", minimum=0)     # a price cannot be negative
    quantity = read_int("Quantity: ", minimum=1)      # must buy at least one

    subtotal = price * quantity
    discount = subtotal * DISCOUNT_RATE
    after_discount = subtotal - discount
    tax = after_discount * TAX_RATE
    total = after_discount + tax

    print("\n----------- BILL -----------")
    print(f"Item      : {item} x {quantity}")
    print(f"Subtotal  : Rs {subtotal:10.2f}")
    print(f"Discount  : Rs {discount:10.2f}  (5%)")
    print(f"Tax       : Rs {tax:10.2f}  (17%)")
    print(f"TOTAL     : Rs {total:10.2f}")
    print("----------------------------")


# ---------------- Challenge: Unit converter ----------------
def unit_converter():
    print("\n--- Challenge: Unit converter ---")
    celsius = read_float("Temperature in Celsius: ", minimum=-273.15)  # absolute zero
    km = read_float("Distance in kilometres: ", minimum=0)

    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15
    miles = km * 0.621371
    metres = km * 1000

    print(f"{celsius:.1f} °C = {fahrenheit:.1f} °F = {kelvin:.1f} K")
    print(f"{km:.1f} km = {miles:.1f} miles = {metres:.1f} m")


if __name__ == "__main__":
    student_card()
    shop_bill()
    unit_converter()
