<<<<<<< HEAD
def make_story():
    storytemplate = """

    Every {average} days, a trangender person is killed in America this year.

    {thisyear} people were murdered this year. {lastyear} last year.

    The last person killed was {name}, aged {age}, from {city}.
=======
from utils.calcs import sevtn_killed
from utils.calcs import sixtn_killed
from utils.calcs import location_of_death
from utils.mapmaker import make_locator_map


def make_story(result):
    storytemplate = """

    Every {average} days, a transgender person is killed in America in 2017.

    {thisyear} people were murdered this year. {lastyear} last year.

    The last person killed was {name}, aged {age}, from {dcity}.
>>>>>>> master

    {mapurl}
    """

    story = storytemplate.format(
<<<<<<< HEAD
        name = jdata[0]['name'],
        age = jdata[0]['age'],
        city = location_of_death(),
        thisyear = sevtn_killed(),
        lastyear = sixtn_killed(),
        average = average(),
=======
        name = result['name'],
        age = result['age'],
        dcity = location_of_death(result),
        thisyear = sevtn_killed(jdata),
        lastyear = sixtn_killed(jdata),
        average = average(jdata),
>>>>>>> master
        mapurl = make_locator_map(city))


    return story
