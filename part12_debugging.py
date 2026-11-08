# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 12 Warm-up - Fix 3 bugs
# Build and Challenge (pytest) are in the part12_testing/ folder.

# ORIGINAL (buggy) code - prints 23.33..., not 80.0:
#
# marks = [90, 25, 70]
# passing = []
# for m in range(len(marks) - 1):
#     if marks[m] > 33:
#         passing = [marks[m]]
# print(sum(passing) / len(marks))
#
# Bug 1 - range(len(marks) - 1) stops one item early, so 70 is never checked.
#         Kind: off-by-one / logic error in the loop range.
# Bug 2 - passing = [marks[m]] REPLACES the list each time instead of adding to it.
#         Kind: logic error (assignment used instead of .append()).
# Bug 3 - dividing by len(marks) (3 students) instead of len(passing) (2 passing).
#         Kind: logic error - wrong variable in the formula.
# Note: "> 33" was left as it is. By the grade table, 33 is a pass (D), so ">= 33"
# would be more correct, but it does not change the answer for these marks.
# None of these crash, which is why they are dangerous: the program runs but lies.
# Found by adding print(m, passing) inside the loop to watch each step.

marks = [90, 25, 70]
passing = []
for m in range(len(marks)):           # fix 1: check every mark
    if marks[m] > 33:
        passing.append(marks[m])      # fix 2: add, do not replace
print(sum(passing) / len(passing))    # fix 3: average of passing marks -> 80.0
