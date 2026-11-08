# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 8 Challenge - real project layout using a package and an installed library

import requests  # installed with pip inside the virtual environment

from school import attendance_percent, average, grade

marks = [80, 72, 91]
print(f"Average {average(marks):.1f} -> grade {grade(average(marks))}")
print(f"Attendance: {attendance_percent(42, 48):.1f}%")
print("requests version installed in venv:", requests.__version__)
