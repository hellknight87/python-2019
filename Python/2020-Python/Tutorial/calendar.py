# Displays the calendar.

import calendar

# Enter the month and year

yy = int(input("Enter the year: "))
mm = int(input("Enter the month: "))

# Display the calendar
print(calendar.month(yy,mm))