from utils.micdata import parse_data
from bot2.py import location_of_death
from bot2.py import location_of_death
from utils.datemaker import numberofdays
from utils.mapmaker import make_locator_map
jdata = parse_data()
city = location_of_death()

def make_story():
    storytemplate = """

    Every {average} days, a transgender person is killed in America in 2017.

    {thisyear} people were murdered this year. {lastyear} last year.

    The last person killed was {name}, aged {age}, from {city}.

    {mapurl}
    """

    story = storytemplate.format(
        name = jdata[0]['name'],
        age = jdata[0]['age'],
        city = location_of_death(),
        thisyear = sevtn_killed(),
        lastyear = sixtn_killed(),
        average = average(),
        mapurl = make_locator_map(city))


    return story
