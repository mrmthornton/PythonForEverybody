'''
Created on Nov 22, 2015

@author: mike
'''
import re

fileHandle = open('regex_sum_204724.txt')
totalSum = 0
numberCount = 0
for line in fileHandle:
    aList = re.findall('([0-9]+)', line)
    for x in aList:
        totalSum += int(x)   
 
print totalSum