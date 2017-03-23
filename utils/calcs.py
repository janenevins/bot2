from utils.datemaker import numberofdays

def location_of_death(result): #Getting the city
    bio = result['bio']
    import re
    regex = r"\bin\b (\w+)"
    matches = re.findall(regex, bio)
    for match in matches:
        return match

def sevtn_killed(jdata):#tells me the number of people murdered in 2017 - 7
    yrlist = []
    for row in jdata:
        if row['filters'][0] == '2017':
            yrlist.append(row)

    return len(yrlist)

def sixtn_killed(jdata):#tells me the number of people murdered in 2016 - 22
    yr16list = []
    for row in jdata:
        if row['filters'][0] == '2016':
            yr16list.append(row)

    return len(yr16list)

def average(jdata): #average number of days per death
    deaths = sevtn_killed(jdata)
    dayssofar = numberofdays()
    avg = (dayssofar)/(deaths)
    return round(avg)
