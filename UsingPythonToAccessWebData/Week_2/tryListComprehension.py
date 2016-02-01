'''
Created on Nov 22, 2015

@author: mike
'''
import re
#print sum([sum( [int(x) for x in re.findall('([0-9]+)', line)]) for line in open('regex_sum_204724.txt').readlines()])
print sum([int(x) for line in open('regex_sum_204724.txt').readlines() for x in re.findall('([0-9]+)', line)])
#assert(x == 513520)
