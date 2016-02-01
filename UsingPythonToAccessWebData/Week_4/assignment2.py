'''
Created on Nov 26, 2015

@author: mike
'''
import re
import urllib
from BeautifulSoup import BeautifulSoup 

#url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
#linkNum = 3
#loopCount = 4

url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Zachary.html'
linkNum = 18
loopCount = 7

print url
while loopCount > 0:
    tags = BeautifulSoup(urllib.urlopen(url).read())('a')
    url = re.findall('href="(.+)"', str(tags[linkNum-1]))[0]
    name = re.findall('>(.*)<', str(tags[linkNum-1]))[0]
    print name
    loopCount -= 1
