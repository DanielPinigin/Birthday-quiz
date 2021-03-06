"""
birthday.py
Author: Daniel
Credit: Mr. Dennison
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""

from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

name = input("Hello, what is your name? ")
month = input("Hi {0}, what was the name of the month you were born in? " .format(name))
year = input("And what year were you born in, {0}? " .format(name))
day = input("And the day? ")

month = month.lower()
winter = ["december", "january", "february"]
spring = ["march", "april", "may"]
summer = ["june", "july", "august"]
fall = ["september", "october", "november"]



if month in ["december", "january", "february"]:
    season = "winter"
elif month in ["march", "april", "may"]:
    season = "spring"
elif month in ["june", "july", "august"]:
    season = "summer"
else: 
    season = "fall"

if int(year) < 1980:
    timeperiod = "Stone Age"
elif year in ["1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989"]:
    timeperiod = "eighties"
elif year in ["1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999"]:
    timeperiod = "nineties"
else:
    timeperiod = "two thousands"

if month == month_name[todaymonth].lower() and int(day) == todaydate:
    print("Happy birthday!")
elif month in ["october",] and int(day) == 31:
    print("You were born on Halloween!")
else:
    print("{0}, you are a {1} baby of the {2}. " .format(name, season, timeperiod))