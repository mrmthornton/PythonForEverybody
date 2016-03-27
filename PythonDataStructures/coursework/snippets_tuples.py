'''
Created on Mar 27, 2016

@author: mike
'''
aDict = {'d':4, 'c':3, 'a':1, 'b':2, 'f':4}

for k, v in  sorted(aDict.items()):
    print k, v
    

temp = list()
for k,v in aDict.items():
    temp.append( (v, k) )
temp.sort(reverse=True)
print temp