# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
def attendance_percent(days_present: int, total_days: int) -> float:
    if total_days <= 0:
        raise ValueError("total_days must be positive")
    return days_present / total_days * 100
