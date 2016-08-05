import math


# GLOBAL VARS

def change_name(name):
    name = "Shona"
    return name


name = "Mini"

change_name(name)

print name  # CANT CHANGE VALUE OF GLOBAL VAR

# ALTERNATIVE

name = change_name(name)
print name

# ACCESSING GLOBAL VARS FROM FUNCTION

global_var = "I am a global"


def change_var():
    global global_var
    global_var = "I am changed"


change_var()

print global_var


def equation_calculator(equation):
    equation = equation.strip()
    equation = equation.replace(" ", '')
    tokens = list(equation)
    op1 = int(tokens[4])
    op2 = int(tokens[2])
    result = op1 - op2
    print tokens
    return result


print equation_calculator("x + 9 = 6")


# RETURN MULTIPLE VALUES

def mult_div(num1, num2):
    return (num1 * num2), (num1 / num2)


print mult_div(35, 7)


# PRIME NO CODE

def isPrime(num):
    for i in range(2, num / 2):
        if num % i == 0:
            return False
    return True


def find_primes(limit):
    primeList = list()
    for i in range(2, limit + 1):
        if isPrime(i):
            primeList.append(i)
    return primeList


print find_primes(29)


# UNKNOWN NO OF ARGUMENTS  PASSED INTO FUNCTION

def sumAll(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print sumAll(1, 2, 3, 8)


# AREA CALCULATOR

def rectangle_area():
    length = float(raw_input("Enter length: "))
    width = float(raw_input("Enter width: "))
    area = length * width
    print "Area of rectangle is", area


def circle_area():
    radius = float(raw_input("Enter radius: "))
    area = math.pi * math.pow(radius, 2)
    print "Area of circle is {:.2f}".format(area)


def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print "Please enter rectangle or circle"


def main():
    shape_type = raw_input("What Shape: ")
    get_area(shape_type)


main()
