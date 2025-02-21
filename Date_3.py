from datetime import datetime

current_datetime = datetime.now()
datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Datetime with microseconds:", current_datetime)
print("Datetime without microseconds:", datetime_without_microseconds)
