'''
Created on Feb 1, 2016

@author: mike
'''

if __name__ == '__main__':
    file_name = raw_input("Enter the file name: ")
    if len(file_name) == 0:
        file_name = "mbox-short.txt"
    file_handle = open(file_name)
    
    count=0
    for line in file_handle:
        line = line.strip()
        if not line.startswith('From '): continue
        count +=1
        second_word = line.split()[1]
        print second_word
    
    print "There were", count, "lines in the file with From as the first word"
