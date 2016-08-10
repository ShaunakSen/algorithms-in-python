# EXCEPTION HANDLING

try:
    aList = [1, 2, 3]
    print aList[3]

except IndexError:
    print "Sorry.. That index does not exist"

except:
    print "Some error occured"


# CUSTOM EXCEPTIONS
class DogNameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


try:
    dogName = raw_input("What is you dog's name? ")
    for char in dogName:
        if char.isdigit():
            raise DogNameError

except DogNameError:
    print "Your dog's name cant have numbers"

num1, num2 = raw_input("Enter 2 values to divide: ").split()
try:
    quotient = int(num1) / int(num2)
    print "{} / {} = {}".format(num1, num2, quotient)
except ZeroDivisionError:
    print "Cant divide by 0"

else:
    print "You did not raise exception"

finally:
    print "END"

# PROBLEM

fname = raw_input("Enter File Name: ")
try:
    fh = open(fname)
except IOError as ex:
    print "Plz enter valid file name"
    print ex.args

else:
    while True:
        line = fh.readline()
        if not line:
            break
        print line
    fh.close()
finally:
    print "END"
