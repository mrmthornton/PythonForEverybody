'''
Created on Nov 27, 2015

@author: mike
'''

import urllib  

from twurl import augment

url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
              {'screen_name' : 'drchuck', 'count' : '2' } )
connection = urllib.urlopen(url)
data = connection.read()
print data
headers = connection.info().dict
print headers
