from utils.micdata import parse_data
from utils.datemaker import numberofdays
from utils.bot2story.py import make_story

jdata = parse_data()

story = make_story()
print(story)



#Getting the city

def location_of_death():

    bio = jdata[0]['bio']
    import re
    regex = r"\bin\b (\w+)"
    matches = re.findall(regex, bio)
    for match in matches:
        return match

def sevtn_killed():#tells me the number of people murdered in 2017 - 7
    yrlist = []
    for row in jdata:
        if row['filters'][0] == '2017':
            yrlist.append(row)

    return len(yrlist)

def sixtn_killed():#tells me the number of people murdered in 2016 - 22
    yr16list = []
    for row in jdata:
        if row['filters'][0] == '2016':
            yr16list.append(row)

    return len(yr16list)

def average():
    deaths = sevtn_killed()
    dayssofar = numberofdays()
    avg = (dayssofar)/(deaths)
    return round(avg)
