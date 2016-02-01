'''
Created on Nov 26, 2015

@author: mike
'''

import urllib
import json

def testAPI():
    while  True:
        address = raw_input('Enter Location: ')
        serviceUrl = 'http://python-data.dr-chuck.net/geojson?'
        #serviceUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'
        url = serviceUrl + urllib.urlencode( {'sensor':'false', 'address':address } )
        data = urllib.urlopen(url).read()
        try:
            info = json.loads(str(data))  #  the str() doesn't seem to matter
        except:
            info = None
        if 'status' not in info or info['status'] != 'OK':
            print  'Failure to retrieve data'
            print data
            continue
        
        #print json.dumps(info, indent=4)

        print info['results'][0]['place_id']
        print info['results'][0]['formatted_address']
        continue
    

def testJSON():
    url = raw_input('Enter - ')
    #url = ' http://python-data.dr-chuck.net/comments_42.json '
    #url = 'http://python-data.dr-chuck.net/comments_204730.json' 
    urlHandle = urllib.urlopen(url)
    data = urlHandle.read()
    info = json.loads(data)
    info['comments']
    print sum([int(dictionary['count']) for dictionary in info['comments']])


if __name__ == '__main__':
    testAPI()
    #testJSON()
    
