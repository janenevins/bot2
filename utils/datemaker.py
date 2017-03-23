import datetime
FIRST_DAY_OF_YEAR = date(2017, 1, 1)



def numberofdays():
    today = date(2017, 3, 22) #yeah, obviously I need to figure out what this really is
    delta = (today) - (FIRST_DAY_OF_YEAR)
    return delta.days

#I can't quite get this working tonight.

"""
def today():
    today = datetime.datetime.now()
    stoday = todaysdate.strftime('%Y-%m-%d')
    return stoday

datestring = today()

def fix_date_string(datestring):  #this function transforms the date string into something that can be correctly sorted
    """
    datestring change from '04/05/1984' to
    '1984-05-04'
    """
    ds = datestring.split('-')
    return (','.join([ds[2], ds[0], ds[1]]))

fixdate = fix_date_string(datestring)

#datetime.datetime(2017, 3, 22, 21, 54, 0, 916534)
"""
