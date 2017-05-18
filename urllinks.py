# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter URL: ').strip()
count = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: '))

for c in range(count+1):
    html = urllib.urlopen(url).read()
    print url
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = soup('a')
    if c == count:
        print re.findall("known_by_(.+).html", url)
    else:
        url = tags[pos-1].get('href', None)