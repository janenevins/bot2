from utils.micdata import parse_data
from utils.calcs import location_of_death
from utils.bot2story import make_story


def bot2():
    jdata = parse_data()
    result = jdata[0]
    city = location_of_death(result)
    story = make_story(result)
    return final

def run_it():
    storymap = bot2()
    print(storymap)
