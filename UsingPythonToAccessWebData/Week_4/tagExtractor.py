'''
Created on Nov 26, 2015

@author: mike
'''
import urllib # treats url/s like files
from BeautifulSoup import *


url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve a list of the anchor tags
# Each   tag is like a dictionary of HTML atributes

tags = soup('a')

for tag in tags:
    print tag.get('href', None)
