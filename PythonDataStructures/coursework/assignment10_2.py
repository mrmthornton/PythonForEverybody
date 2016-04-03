'''
Created on Mar 27, 2016

@author: mike
'''
'''
10.2 Write a program to read through the mbox-short.txt
figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by
 finding the time and then splitting the string a second time using a colon.
 
 ex:
      From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour,
 print out the counts, sorted by hour
'''
if __name__ == '__main__':
    file_name = raw_input("Enter the file name: ")
    if len(file_name) < 1: file_name = "mbox-short.txt"
    file_handle = open(file_name, 'r')
    
    histo = dict()
    count=0
    for line in file_handle:
        line = line.strip()
        if not line.startswith('From '): continue
        sixth_word = line.split()[5]
        hour = sixth_word.split(':')[0]
        histo[hour] = histo.get(hour,0) + 1
        
    for k,v in sorted( histo.items() ):
        print k, v
    