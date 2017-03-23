import datetime
from datetime import date 
FIRST_DAY_OF_YEAR = date(2017, 1, 1)



def numberofdays():
    today = date(2017, 3, 22) #yeah, obviously I need to figure out what this really is
    delta = (today) - (FIRST_DAY_OF_YEAR)
    return delta.days
