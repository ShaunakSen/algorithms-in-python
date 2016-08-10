# STATIC METHOD.. ALLOWS ACCESS WITHOUT NEED TO CREATE OBJECT
# UTILITY FUNCTIONS

import derek_eleventh_2
from derek_eleventh_2 import getSum


class Dog(object):
    # STATIC VAR
    # VALUE IS SHARED BY EVERY OBJECT CREATED
    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name
        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print "There are currently {} no of dogs".format(Dog.num_of_dogs)


class Sum(object):
    @staticmethod
    def getSum(*args):
        mySum = 0
        for i in args:
            mySum += i
        return mySum


def main():
    print "Sum: ", Sum.getSum(2, 3, 4)
    print "Creating Dogs...."
    spot = Dog("Spot")
    timmy = Dog("Timmy")
    spot.getNumOfDogs()
    timmy.getNumOfDogs()
    print derek_eleventh_2.getSum(1, 2)
    print getSum(1, 2)


main()

# STATIC VARIABLE
