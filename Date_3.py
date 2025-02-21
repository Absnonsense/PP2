from datetime import datetime
user_input = input("Enter a datetime (YYYY-MM-DD HH:MM:SS.microseconds): ")
user_datetime = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S.%f")
datetime_without_microseconds = user_datetime.replace(microsecond=0)
print("Datetime without microseconds:", datetime_without_microseconds)
