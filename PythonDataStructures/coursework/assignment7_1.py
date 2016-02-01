'''
Created on Jan 31, 2016

@author: mike
'''

if __name__ == '__main__':
    file_name = raw_input("Enter the file name: ")
    file_handle = open(file_name)
    for line in file_handle:
        print line.strip().upper()