import datetime

"""
  Gets the age of a person in years, months, days, and what day of the week they were born on.

  Args:
    birthday: The person's birthday as a datetime object.

  Returns:
    A tuple of (age in years, age in months, age in days, day of the week).
"""

birthday=input( "Enter your birthday in the format YYYY-MM-DD: ")
birthday=datetime.datetime.strptime(birthday, "%Y-%m-%d").date()

# Get the current date.
today_day = datetime.date.today()
today_month = datetime.date.today().month
today_year = datetime.date.today().year

# Calculate the difference between the birthday and the current date.
difference = today_day - birthday

# Get the age in years.
age_in_years = int((today_year - birthday.year)-1)

# Get the age in months.
age_in_months = int(today_month - birthday.month)

# Get the age in days.
#age_in_days = int(today_day - birthday.day)

# Get the day of the week on which the person was born.
day_of_week = birthday.strftime("%A")

# Return the age in years, months, days, and day of the week.
print([age_in_years, age_in_months, difference.days, day_of_week])
print(day_of_week)




