"""
i = 4
d = 4.0
s = "HackerRank "

myInt = raw_input()
myInt = int(myInt)

myFloat = raw_input()
myFloat = float(myFloat)

myStr = raw_input()

print myInt + i
print "{:.1f}".format(myFloat + d)
print s + myStr

mealCost = raw_input()
mealCost = float(mealCost)

tip = raw_input()
tip = int(tip)

tax = raw_input()
tax = int(tax)

cost = mealCost + ((tip/100.00) * mealCost) + ((tax/100.00) * mealCost)

print int(round(cost))

N = int(raw_input().strip())

if N % 2 != 0:
    print "Weird"
else:
    if 2 <= N <= 5:
        print "Not Weird"
    if 6 <= N <= 20:
        print "Weird"
    elif N > 20:
        print "Not Weird"

"""
