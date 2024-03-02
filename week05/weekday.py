# Weekly Task, 5. weekday.py
# The aim of this program is to output wether or not today is a weekday or the weekend.
# Author: Laura Lyons

from datetime import date # I searchted the internet on how generate what the current day is. 
# The datetime module provides classes for manipulating dates and times in Python.
# Reference: https://docs.python.org/3/library/datetime.html 
# Reference: https://www.w3schools.com/python/python_datetime.asp

current_day = date.today() # We use this code to get the current date.
day_of_week = current_day.weekday() # This code is used to tell us the specific day of the week,  (0 = Monday, 6 = Sunday)
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] # This is a list of the weekday names.

if day_of_week is weekdays[:5]: # The range is used to indicate which days are weekdays.
    print(f"Today is {weekdays[day_of_week]}.\nUnfortunately this is a weekday, go back to work!.")
else:
    print(f'Today is {weekdays[day_of_week]}.\nHurrah, go back to bed!')

