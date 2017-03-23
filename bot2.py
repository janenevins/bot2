from utils.micdata import parse_data
<<<<<<< HEAD
from utils.datemaker import numberofdays
from utils.mapmaker import make_locator_map
from utils.bot2story.py import make_story
=======
from utils.calcs import location_of_death
from utils.bot2story import make_story
>>>>>>> master

jdata = parse_data()

<<<<<<< HEAD
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
    for row in mylist:
        if row == '2017':
            yrlist.append(row)

    return len(yrlist)

def sixtn_killed():#tells me the number of people murdered in 2016 - 22
    yr16list = []
    for row in mylist:
        if row == '2016':
            yr16list.append(row)

    return len(yr16list)

def average():
    deaths = sevtn_killed()
    dayssofar = numberofdays()
    avg = (dayssofar)/(deaths)
    return round(avg)
=======
def bot2():
    jdata = parse_data()
    result = jdata[0]
    city = location_of_death(result)
    story = make_story(result)
    return final

def run_it():
    storymap = bot2()
    print(storymap)
>>>>>>> master
