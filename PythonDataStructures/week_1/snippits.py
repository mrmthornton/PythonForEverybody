'''
Created on Jan 18, 2016

@author: mike
'''








if __name__ == '__main__':
    #pass
    
    fruit = 'banana'
    for letter in fruit:
        print letter
    
    # slicing 
    print fruit[:3]
    print fruit[3:80]
    print fruit[3:]
    print fruit[:]
    print fruit[:3] + fruit[3:]
    print fruit[:3] + " " + fruit[3:]
    print 'nn' in fruit
    print 'nan' in fruit
    
    print fruit.upper()
    print "hello, world!".capitalize()
    
    print dir(fruit)
    
    
    data = 'mike@thornton.net todays date'
    atpos = data.find('@')
    sppos = data.find(' ',atpos)
    print data[atpos+1:sppos]