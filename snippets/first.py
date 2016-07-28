num1, num2 = raw_input("Enter 2 nos: ").split()
num1 = int(num1)
num2 = int(num2)

print num1, num2

add = num1 + num2
diff = num1 - num2
prod = num1 * num2
div = num1 / num2

print "{} + {} = {}".format(num1, num2, add)

print "Simple Calculator.."

val1, operator, val2 = raw_input("").split()

val1 = int(val1)
val2 = int(val2)
if operator not in ['+', '*', '/', '-']:
    print "Sorry.. wrong command"

else:
    if operator == "+":
        print "{} + {} = {}".format(val1, val2, val1 + val2)
    if operator == "-":
        print "{} - {} = {}".format(val1, val2, val1 - val2)
    if operator == "*":
        print "{} * {} = {}".format(val1, val2, val1 * val2)
    if operator == "/":
        print "{} / {} = {}".format(val1, val2, val1 / val2)

my_float = raw_input("Enter a floating pt no: ")
my_float = float(my_float)

print "Rounded to 2 decimal places: {:.2f}".format(my_float)


