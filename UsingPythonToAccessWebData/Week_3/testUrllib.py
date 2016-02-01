'''
Created on Nov 25, 2015

@author: mike
'''
import urllib # treats url/s like files

url = 'http://www.py4inf.com/code/romeo.txt'
urlHandle =  urllib.urlopen(url)
#for line in urlHandler:
#    print line.strip()
print urlHandle.read()