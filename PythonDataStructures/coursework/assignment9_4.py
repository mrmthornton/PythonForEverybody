'''
Created on Feb 1, 2016

@author: mike
'''

if __name__ == '__main__':
    file_name = raw_input("Enter the file name: ")
    if len(file_name) == 0:
        file_name = "mbox-short.txt"
    file_handle = open(file_name, 'r')
    
    emailAddr = dict()
    count=0
    for line in file_handle:
        line = line.strip()
        if not line.startswith('From '): continue
        second_word = line.split()[1]
        emailAddr[second_word] = emailAddr.get(second_word,0) + 1
    
    #print emailAddr.items()
    
    addr = None
    count = None
    for key,value in emailAddr.items():
        if count is None or value > count:
            addr = key
            count = value
            
    print addr, count
