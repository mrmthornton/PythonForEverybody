'''
Created on Nov 26, 2015

@author: mike
'''

import urllib
import xml.etree.ElementTree as ET

def testXML():
    #url = raw_input('Enter - ')
    url = 'http://python-data.dr-chuck.net/comments_42.xml'
    #url = 'http://python-data.dr-chuck.net/comments_204726.xml' 
    pageData = urllib.urlopen(url).read()
    tree = ET.fromstring(pageData)
    print sum([int(count.text) for count in tree.findall('.//comments/comment/count')])


if __name__ == '__main__':
    testXML()
    
