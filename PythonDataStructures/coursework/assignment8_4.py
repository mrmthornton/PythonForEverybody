'''
Created on Feb 1, 2016

@author: mike
'''

if __name__ == '__main__':
    file_name = raw_input("Enter the file name: ")
    if len(file_name) == 0:
        file_name = "romeo.txt"
    file_handle = open(file_name)
    
    unique_words = []
    for line in file_handle:
        line_words = line.split()
        #print line_words
        for word in line_words:
            #print word
            if word in unique_words: continue
            unique_words.append(word)
    unique_words.sort()
    print unique_words
                
