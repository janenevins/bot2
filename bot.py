from utils.micdata import parse_data
from utils.bot2story import make_story

def bot():
    jdata = parse_data()
    result = jdata[0]
    story = make_story(result, jdata)

    return story


if __name__ == '__main__':
    txt = bot()
    print(txt)
