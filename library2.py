# Activity 1

from datetime import date, time, datetime

today=date.today()
now=datetime.now()
print("Today's date is ", today)
print("\nCurrent date and time is ", now)

print("\nDate components", today.year, today.month, today.day)

# Activity 2

from datetime import date

month=int(input("Enter your birth month (MM): "))
day=int(input("Enter your birth day (DD): "))
year=int(input("Enter your birth year (YYYY): "))

today=date.today()

birthday_this_year = date(today.year, month, day)

if birthday_this_year < today:
    birthday_this_year = (today.year + 1, month, day)

days_left = (birthday_this_year - today).days

print(f"Your birthday is in {days_left} days!")

# Activity 3

from datetime import date

day_map = {
    "monday":0,
    "tuesday":1,
    "wednesday":2,
    "thursday":3,
    "friday":4,
    "saturday":5,
    "sunday":6
}
year=int(input("Enter a year: "))
day_name=input("Enter the day to count (e.g, sunday): ")

if day_name not in day_map:
    print("This is invalid")
else:
    target_day=day_map[day_name]
    count = 0

    for month in range (1,13):
        for day in range(1,32):
            try:
                current_date=date(year, month, day)
                if current_date.weekday() == target_day:
                    count += 1
            except ValueError:
                pass
    print(f"There are {count} {day_name}s in the year {year}.")


