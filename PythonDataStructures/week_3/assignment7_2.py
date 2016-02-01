'''
Created on Jan 31, 2016

@author: mike
'''

import re

if __name__ == '__main__':
    file_name = raw_input("Enter the file name: ")
    if len(file_name) == 0:
        file_name = "mbox-short.txt"
    file_handle = open(file_name)
    count = 0
    value_sum = 0.0
    for line in file_handle:
        if not line.startswith("X-DSPAM-Confidence:") : continue
        #print line.strip()
        count +=1
        value_list = re.findall('\d\.\d+',line)
        value_sum += float(value_list[0])
    print "Average spam confidence:",  value_sum/count
