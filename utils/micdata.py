import requests
import json
from os.path import basename, exists, join
from os import makedirs


DEST_DIR = 'data-files'
DATA_URL = 'http://stash.compciv.org/2017/mic-unerased.json'


def fetch_and_save_url(url):
    """
    For a given URL, creates a filename to save to
    Checks to see if filename already exists; if not, download and save to that file name
    Return the filename as a string
    """
    makedirs(DEST_DIR, exist_ok=True)
    dest_filename = join(DEST_DIR, basename(url))
    if not exists(dest_filename):
        resp = requests.get(url)
        with open(dest_filename, 'wb') as f:
            f.write(resp.content)
    return dest_filename

def parse_data():
    fname = fetch_and_save_url(DATA_URL)
    thefile = open(fname, 'r')
    rawtxt = thefile.read()
    thefile.close()

    return json.loads(rawtxt)

jdata = parse_data
