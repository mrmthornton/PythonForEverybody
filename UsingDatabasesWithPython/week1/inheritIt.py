'''
Created on Dec 15, 2015

@author: mike
'''
from simpleObject import MyClass


class ChildOf(MyClass):


    def cubeIt(self):
        return self.squareIt() * self.squareIt()


if __name__ == "__main__":
    rubics = ChildOf(2)
    print rubics.squareIt()
    print rubics.cubeIt()