def make_story():
    storytemplate = """

    Every {average} days, a trangender person is killed in America this year.

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
