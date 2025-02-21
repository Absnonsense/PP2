from datetime import datetime

date1_str = input("Enter first date and time (YYYY-MM-DD HH:MM:SS): ")
date2_str = input("Enter second date and time (YYYY-MM-DD HH:MM:SS): ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

difference = abs((date2 - date1).total_seconds())

print("Difference in seconds:", difference)
