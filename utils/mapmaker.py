import re
<<<<<<< HEAD

https://maps.googleapis.com/maps/api/staticmap?size=600x400&zoom=4&markers=NewOrleans

city = location_of_death()
=======
import requests
>>>>>>> master

def make_locator_map(city):
    base_endpoint = 'https://maps.googleapis.com/maps/api/staticmap?size=600x400&zoom=4&markers='
    myparams = {}
    # a list of markers; we could add more if we wanted...
    myparams['markers'] = []
    myparams['markers'].append('color:red|' + city)

    preq = requests.PreparedRequest()
    preq.prepare_url(base_endpoint, myparams)

    return preq.url

<<<<<<< HEAD
#ideally this woudl be all the cities for which I have data, bit some of the bios do not have cityies
#so I don't know how to deal with that 
=======
#ideally this woudl be all the cities for which I have data,
#but some of the bios do not have cities
#so I don't know how to deal with that
>>>>>>> master
