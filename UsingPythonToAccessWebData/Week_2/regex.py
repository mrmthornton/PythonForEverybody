'''
Created on Nov 22, 2015

@author: mike
'''

'''
 ^  start of line
 $  end of line
 .  any character
 \s whitespace
 \S Non-whitespace
 *  repeat 0 or more
 *? repeat 0 or more - non greedy
 +  repeat 1 or more
 +? repeat 1 or more - non greedy
 [aeiou] match a single character from the list aeiou
 [^aeiou] match not in list
 [a-z] the match list is a range
 ( start string extraction
 ) end string extaction
'''

import re

if __name__ == '__main__':
    fileHandle = open('mailbox.txt')
    lines = []
    for line in fileHandle:
        line.strip()
        lines.append(line)

    for line in lines:
        if re.search('^From:', line): # returns True or False
            print '^FROM: ', line
            
    for line in lines:
        aList = re.findall('[0-9]+', line)
        if len(aList) != 0:
            print 'NUMBERS ', aList
        
    for line in lines:
        aList = re.findall('^F.+:', line)
        if len(aList) != 0:
            print 'greedy     ', aList[0]
        
    for line in lines:
        aList = re.findall('^F.+?:', line)
        if len(aList) != 0:
            print 'non greedy  ', aList[0]
        
    for line in lines:
        aList = re.findall('^From:\s+(\S+@\S+)', line)
        if len(aList) != 0:
            print 'extract  ', aList[0]
