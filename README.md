What does this bot do?
This bot takes in data and the current date to return a map url and text that says.
The text says: 
Every {average} days, a transgender person is killed in America in 2017.

{thisyear} people were murdered this year. {lastyear} last year.

The last person killed was {name}, aged {age}, from {city}.

{mapurl}


Fifteen years have passed since Gwen Araujo was violently murdered in Newark, Calif. The case made national headlines and started a new conversation in the United States about what it means to be a transgender person living in America.

In the years following Araujo's death, women like Laverne Cox  and Caitlyn Jenner have gained national celebrity. Mainstream TV shows like Transparent and Orange is the New Black have nuanced and complex transgender characters in leading roles.

The purpose of this bot is to highlight the murder rate for transgender women in America. While many queer millennial women benefit from the strides made by the LGBT and women’s rights movements, transgender women, especially poor women and people of color, remain extremely vulnerable to discrimination and violence.

Now, the Trump administration is rolling back legal protections for transgender people by rescinding an Obama era executive order requiring schools to allow transgender kids to use the bathroom that matches their identity.  Twelve states are considering bills that would require people to use the bathroom matching the sex on their birth certificate.

The data
The data set is from a Mic.com web app called “Database of transgender homicides, 2010-2017” that catalogs the murders of transgender people.
The original file is here: https://mic.com/unerased/db.json
A mirror is here:
http://stash.compciv.org/2017/mic-unerased.json

Challenges
[I can’t get the current date to work so I have a placeholder. ]
The first challenge was finding data. Thanks to Dan Nguyen for finding the data set at Mic.com.
I intended to have an app that told users, “It has been X days since a transgender person was killed in America” but I the dates are not consistently included or formatted in the data set. Second, I wanted to have a map that showed the cities where women were killed, but again the data set did not always include locations which caused errors.
Finally, there is a bigger question of what to count or track. Violence against transgender individuals was difficult to find and track. People may be misgendered in news reports. Hate crimes are generally under-reported.
Plus, research raised questions like, for 2016, do you include the people killed in the Ghostship fire in Oakland or the Pulse shooting in Orlando?

Inspirations
The idea that students have the tools to do data journalism. Counting things is like collecting a lot of anecdotes that give stories ammunition.  People forget the past, and reminding them has value.

The Intercept’s Officer Involved  https://theintercept.com/2015/06/09/officer-involved/
Officer down memorial page created by a college student: https://www.odmp.org/info/about-odmp
Is the L train fucked, an app with simple graphics but memorable impact http://www.istheltrainfucked.com/

Next steps
Posting this bot online and use bold, simple graphics and a map, similar to Is the L train.
Building on Mic.com’s work, I’d like to create an up to date, downloadable dataset that tracks the deaths of transgender people.
