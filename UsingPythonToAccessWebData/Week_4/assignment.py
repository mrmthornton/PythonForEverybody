'''
Created on Nov 26, 2015

@author: mike
'''

import urllib
from BeautifulSoup import BeautifulSoup

#url = 'http://python-data.dr-chuck.net/comments_42.html'
url = 'http://python-data.dr-chuck.net/comments_204729.html' 
tags = BeautifulSoup(urllib.urlopen(url).read())('span')
print sum([int(tag.text) for tag in tags])
