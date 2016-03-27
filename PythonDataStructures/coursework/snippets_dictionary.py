'''
Created on Mar 26, 2016

@author: mike
'''

if __name__ == '__main__':
    inputLine = raw_input("Enter a line of text: ")
    if inputLine == "": 
        inputLine = "This is the default text input"
    words = inputLine.split()
    #print words
    
    counts = dict()
    for word in words:
        counts[word] = counts.get(word,0) + 1
    
    for key in counts:
        print key, counts[key]
    
    newList = list(counts)
    print newList
    print counts.keys()
    print counts.values()
    print counts.items()
    
    for key, value in counts.items():
        print key, value
        