from datetime import datetime
import re



def number_of_days_in_2017_so_far():
    startdate = datetime(2017, 1, 1)
    today = datetime.now()
    delta = (today) - (startdate)
    return delta.days



def location_of_death(result): #Getting the city
    bio = result['bio']
    regex = r"\bin\b (\w+)"
    matches = re.findall(regex, bio)
    if matches:
        return matches[0]

def count_killed_in_year(jdata, year):
    yrlist = []
    for row in jdata:
        if row['filters'][0] == str(year):
            yrlist.append(row)

    return len(yrlist)

def average_deaths_in_2017(jdata):
    deathcount = count_killed_in_year(jdata, 2017)
    days_so_far = number_of_days_in_2017_so_far()
    return round((days_so_far)/(deathcount))
