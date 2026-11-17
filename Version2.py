# Version 2: Deadline and Date Formatter using datetime

from datetime import date, datetime

event_title = input("Enter the title of the event: ")
year = int(input("Enter the year of the event: ").strip())

month_input = input("Enter the month of the event: ").strip()
if month_input.isdigit():
    month = int(month_input)
else:
    month = datetime.strptime(month_input, "%B").month  # Convert month name to number

day = int(input("Enter the day of the event: ").strip())

event_date = date(year, month, day)

formatted_event = event_title.upper()  # Convert the event title to uppercase
month_name = event_date.strftime("%B")  # Extract the month
formatted_date = f"{month_name} {event_date.day}, {event_date.year}"  # Format full date
weekday_name = event_date.strftime("%A")  # Extract the weekday

print("\nFormatted Output:")
print(f"Event: {formatted_event}")
print(f"Date: {formatted_date}")
print(f"Year: {event_date.year}")
print(f"Month: {month_name}")
print(f"Day: {event_date.day}")
print(f"Weekday: {weekday_name}")
