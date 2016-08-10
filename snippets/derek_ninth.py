# class Dog:
#     def __init__(self, name="", height=0, weigth=0):
#         self.name = name
#         self.height = height
#         self.weight = weigth
#
#     def run(self):
#         print "{} the dog is running".format(self.name)
#
#     def eat(self):
#         print "{} the dog eats".format(self.name)
#
#     def bark(self):
#         print "{} the dog barks".format(self.name)
#
#
# def main():
#     timmy = Dog("Timmy", 86, 46)
#     timmy.bark()
#
#
# main()


class Square(object):
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        print "retrieving the height"
        return self.__height

    @height.setter
    def height(self, value):
        if value:
            print "Setting the height..."
            self.__height = value
        else:
            print "Plz only enter nos"

    @property
    def width(self):
        print "retrieving the width"
        return self.__width

    @width.setter
    def width(self, value):
        if value:
            print "Setting the width..."
            self.__width = value
        else:
            print "Plz only enter nos"

    def area(self):
        return int(self.__width) * int(self.__height)


def main():
    miniSquare = Square()
    height = raw_input("Enter height: ")
    width = raw_input("Enter width: ")
    miniSquare.height = height
    miniSquare.width = width

    print "Height =", miniSquare.height
    print "Width =", miniSquare.width
    print "Area =", miniSquare.area()


main()
