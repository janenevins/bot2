from utils.calcs import count_killed_in_year, location_of_death, average_deaths_in_2017
from utils.mapmaker import make_locator_map


STORY_TEMPLATE = """

Every {average_per_day} days, a transgender person is killed in America in {thisyear}.

{thisyear_count} were murdered in {thisyear}.
{lastyear_count} were murdered in {lastyear}.

The person most recently murdered was {name}, aged {age}, from {dcity}.

{mapurl}
"""


def make_story(result, data):

    thisyear = 2017
    lastyear = 2016
    city = location_of_death(result)

    story = STORY_TEMPLATE.format(
        name = result['name'],
        age = result['age'],
        dcity = location_of_death(result),
        thisyear = thisyear,
        thisyear_count = count_killed_in_year(data, thisyear),
        lastyear = lastyear,
        lastyear_count = count_killed_in_year(data, lastyear),
        average_per_day = average_deaths_in_2017(data),
        mapurl = make_locator_map(city)
    )


    return story
