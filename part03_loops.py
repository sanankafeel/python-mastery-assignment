# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 3 - Loops (for / while)

import random


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Please enter a whole number.")


# ---------------- Warm-up: Times table ----------------
def times_table():
    print("\n--- Warm-up: Times table ---")
    n = read_int("Table of which number? ")
    for i in range(1, 11):              # for loop: we know it runs exactly 10 times
        print(f"{n} x {i} = {n * i}")


# ---------------- Build: ATM PIN check ----------------
CORRECT_PIN = "4321"   # kept as text so "04321" or "4321 " are not accepted by accident
MAX_TRIES = 3


def atm_pin_check():
    print("\n--- Build: ATM PIN check ---")
    tries_left = MAX_TRIES
    while tries_left > 0:               # while loop: repeat until success or no tries
        pin = input("Enter PIN: ").strip()
        if pin == CORRECT_PIN:
            print("Welcome")
            return
        tries_left -= 1
        if tries_left > 0:
            print(f"Wrong PIN. Tries left: {tries_left}")
    print("Card blocked")


# ---------------- Challenge: Number guessing game ----------------
def guessing_game():
    print("\n--- Challenge: Number guessing game ---")
    while True:                         # outer loop = one round per iteration
        secret = random.randint(1, 50)
        guesses = 0
        while True:                     # inner loop = guesses within a round
            guess = read_int("Guess (1-50): ")
            if guess < 1 or guess > 50:
                print("  Stay between 1 and 50.")
                continue                # does not count as a guess
            guesses += 1
            if guess > secret:
                print("Too high")
            elif guess < secret:
                print("Too low")
            else:
                print(f"Got it in {guesses} guesses!")
                break
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            break


# ---------------- Extra practice ----------------
def extra_practice():
    print("\n--- Extra: star triangle ---")
    for row in range(1, 6):             # nested loops: rows, then stars in each row
        line = ""
        for _ in range(row):
            line += "* "
        print(line)

    total = 0
    for n in range(2, 101, 2):          # step 2 gives only even numbers
        total += n
    print("Sum of even numbers 1-100:", total)   # 2550


if __name__ == "__main__":
    times_table()
    atm_pin_check()
    guessing_game()
    extra_practice()
