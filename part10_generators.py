# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 10 - Iterators, generators and decorators

import random
import time
from functools import wraps

LOG_FILE = "server_log.txt"


# ---------------- Warm-up: Countdown generator ----------------
def countdown(n):
    while n > 0:
        yield n        # pause here, hand out n, continue from here next time
        n -= 1


def evens(limit):
    for n in range(0, limit + 1, 2):
        yield n


# ---------------- Build: Big file reader ----------------
def make_sample_log(path, lines=60):
    """Create a log file with 60 lines; some are ERROR lines."""
    random.seed(7)                        # same file every run, so results are repeatable
    levels = ["INFO", "INFO", "INFO", "WARNING", "ERROR"]
    with open(path, "w", encoding="utf-8") as f:
        for i in range(1, lines + 1):
            level = random.choice(levels)
            f.write(f"2026-11-06 10:{i:02d} {level} request #{i} handled\n")


def read_lines(path):
    """Yield one line at a time - the whole file is never in memory."""
    with open(path, encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")


def only_errors(lines):
    """Take any iterable of lines and yield only the ERROR ones."""
    for line in lines:
        if "ERROR" in line:
            yield line


# ---------------- Challenge: Your own decorators ----------------
def timer(func):
    @wraps(func)                          # keeps the original name and docstring
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timer] {func.__name__} took {elapsed:.4f} s")
        return result                     # must return, or the caller gets None
    return wrapper


def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[log] calling {func.__name__} with args={args} kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper


@timer
@log_calls
def sum_up_to(n):
    """Add 1 + 2 + ... + n with a loop."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def main():
    print("--- Warm-up ---")
    for n in countdown(5):
        print(n, end=" ")
    print("Lift off!")
    print(list(evens(10)))                # [0, 2, 4, 6, 8, 10]

    print("\n--- Build ---")
    make_sample_log(LOG_FILE)
    # sum(1 for ...) counts items one by one without building a list
    error_count = sum(1 for _ in only_errors(read_lines(LOG_FILE)))
    total_lines = sum(1 for _ in read_lines(LOG_FILE))
    print(f"{error_count} ERROR lines out of {total_lines} lines in {LOG_FILE}")

    print("\n--- Challenge ---")
    result = sum_up_to(1_000_000)
    print("Result:", result)              # 500000500000
    print("Function name kept by @wraps:", sum_up_to.__name__)


if __name__ == "__main__":
    main()
