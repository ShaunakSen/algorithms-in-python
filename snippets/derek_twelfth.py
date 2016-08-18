# ASSIGN VAR TO A FUNCTION
def multiplyBy2(num):
    return num * 2


times2 = multiplyBy2
print "4*2 =", times2(4)


# PASS FUNCTION AS ARGUMENT

def do_math(func, num):
    return func(num)


print "8*2 =", do_math(multiplyBy2, 8)


# DYNAMICALLY CREATE A FUNCTION INSIDE A FUNCTION

def get_func_mult_by_num(num):
    def mult_by(value):
        return num * value

    return mult_by


generated_function = get_func_mult_by_num(5)

print "5 * 10 =", generated_function(10)

# EMBED FUNCTION INTO A DATA STRUCTURE

listOfFuncs = [times2, generated_function]
print "5 * 9 =", listOfFuncs[1](9)



