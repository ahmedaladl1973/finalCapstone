import datetime

def has_friday_13th(month, year):
  """
  Checks if the given month and year contain a Friday the 13th.

  Args:
    month: The month as a number, from 1 to 12.
    year: The four-digit year.

  Returns:
    True if the month contains a Friday the 13th, False otherwise.
  """

  # Create a datetime object for the first day of the month.
  first_day_of_month = datetime.date(year, month, 1)

  # Get the day of the week for the first day of the month.
  day_of_week = first_day_of_month.weekday()

  # If the day of the week is 4 (Friday), then the month contains a Friday the 13th.
  return day_of_week == 4