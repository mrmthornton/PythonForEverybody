'''
Created on Dec 15, 2015

@author: mike
'''

# class - a template, or cookie cutter,(exemplar).        example Dog
#
# method or message - a defined capability of a class.    example howl()
#
# field or attribute - a bit of data in a class.          example loudness
#
# object or instance - a particular instance of a class.  example Heidi = Dog()

class MyClass(object):

    x = 0

    def __init__(self, nmbr):
        print 'Constructor'
        self.x = nmbr
    
    def __del__(self):
        print "I'm melting, Ohhh, what a world, what a world!"
        
    def squareIt(self):
        return self.x * self.x

if __name__ == "__main__":
    first = MyClass(2)
    
    print first.squareIt()
    
    print dir(first)


    