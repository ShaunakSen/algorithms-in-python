# INHERITANCE

class Animal(object):
    def __init__(self, birthType="Unknown", appearance="Unknown", blooded="Unknown"):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded

    # GETTERS AND SETTERS
    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    # STRING MAGIC METHOD: CAST OBJECT AS STRING

    def __str__(self):
        return "An {} is {} it is {} it is {}". \
            format(type(self).__name__, self.birthType, self.appearance, self.blooded)


class Mammal(Animal):
    def __init__(self, birthType="Born Alive", appearance="hair or fur", blooded="warm blooded", nurseYoung=True):
        Animal.__init__(self, birthType, appearance, blooded)
        self.__nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    # OVERWRITE
    def __str__(self):
        return super(Mammal, self).__str__() + "and it is {} that they nurse their young".format(self.nurseYoung)


class Reptile(Animal):
    def __init__(self, birthType="Born in Egg or Born Alive",
                 appearance="dry scales", blooded="cold blooded"):
        Animal.__init__(self, birthType, appearance, blooded)

    def sumAll(self, *args):
        sum = 0
        for i in args:
            sum += i
        return sum


def getBirthType(theObject):
    print "the {} is {}".format(type(theObject).__name__, theObject.birthType)


def main():
    animal1 = Animal("born alive")
    print animal1.birthType
    print animal1
    mamal1 = Mammal()
    print mamal1.birthType
    print mamal1.appearance
    print mamal1.blooded
    print mamal1.nurseYoung
    print mamal1

    reptile1 = Reptile()
    print reptile1.birthType
    print reptile1

    print reptile1.sumAll(1, 2, 3, 4)

    getBirthType(mamal1)
    getBirthType(reptile1)


main()
