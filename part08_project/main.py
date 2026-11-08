# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 8 Build - uses functions imported from my own module

import school_tools
from school_tools import report, greet

print("main.py is running. __name__ of the module is:", school_tools.__name__)
print("(Notice the self-test text from school_tools.py did NOT print.)\n")

print(greet("Teacher", "ur"))
print(f"Area of circle r=3: {school_tools.area_of_circle(3):.2f}")
print(report("Ali", [80, 72, 91]))
print(report("Sara", [95, 88, 90]))
print(report("Bilal", [20, 29, 30]))
