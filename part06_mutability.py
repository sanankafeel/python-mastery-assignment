# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 6 - References and mutability

import copy


# ---------------- Warm-up: Predict, then run ----------------
def predict_then_run():
    print("--- Warm-up: Predict, then run ---")
    a = [1, 2, 3]
    b = a              # b is NOT a new list; it is a second name for the same list
    b.append(4)
    print(a)           # prediction: [1, 2, 3, 4]  -> changing b changed a
    c = a.copy()       # c is a brand-new list with the same values
    c.append(5)
    print(a, c)        # prediction: [1, 2, 3, 4] [1, 2, 3, 4, 5]  -> a is untouched
    print(a is b, a is c, a == a[:])
    # prediction: True False True
    #   a is b   -> True  (same object in memory)
    #   a is c   -> False (different objects, even if values look alike)
    #   a == a[:] -> True (== compares VALUES; a[:] is a copy with equal values)
    # Surprise for most beginners: line 1 prints 4 even though we only appended to b.


# ---------------- Build: Fix the cart bug ----------------
def add_item_buggy(item, cart=[]):
    # BUG: the default list is created ONCE, when the function is defined,
    # so every call that uses the default shares the same list.
    cart.append(item)
    return cart


def add_item(item, cart=None):
    # FIX: use None as the default and make a fresh list inside the function.
    if cart is None:
        cart = []
    cart.append(item)
    return cart


def cart_bug_demo():
    print("\n--- Build: Fix the cart bug ---")
    customer1 = add_item_buggy("soap")
    customer2 = add_item_buggy("rice")
    print("Buggy  -> customer1:", customer1, "customer2:", customer2)
    print("         Both carts are the same list:", customer1 is customer2)

    customer1 = add_item("soap")
    customer2 = add_item("rice")
    print("Fixed  -> customer1:", customer1, "customer2:", customer2)


# ---------------- Challenge: Safe class copy ----------------
def safe_class_copy():
    print("\n--- Challenge: Shallow vs deep copy ---")
    classes = {"A": ["Ali", "Sara"]}
    shallow = classes.copy()        # new dict, but the inner list is SHARED
    deep = copy.deepcopy(classes)   # new dict AND new inner list

    shallow["A"].append("Hamza")    # changes the shared inner list -> original changes too
    deep["A"].append("Ayesha")      # changes only the deep copy's own list

    print("Original:", classes)     # {'A': ['Ali', 'Sara', 'Hamza']}
    print("Shallow :", shallow)     # {'A': ['Ali', 'Sara', 'Hamza']}
    print("Deep    :", deep)        # {'A': ['Ali', 'Sara', 'Ayesha']}


if __name__ == "__main__":
    predict_then_run()
    cart_bug_demo()
    safe_class_copy()
