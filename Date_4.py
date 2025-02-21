from datetime import datetime

date1 = datetime(2025, 2, 10, 14, 30, 0)
date2 = datetime(2025, 2, 15, 18, 45, 30)

difference = (date2 - date1).total_seconds()

print("Difference in seconds:", difference)
