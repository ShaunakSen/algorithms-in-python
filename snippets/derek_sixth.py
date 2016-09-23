# LISTS

import random
import math

oneToTen = list(range(10))
print oneToTen

for i in oneToTen:
    print "{} : {}".format(oneToTen.index(i), i)
randomList = []
for count in range(5):
    random_no = random.randrange(1, 10)
    randomList.append(random_no)

print randomList

# BUBBLE SORT

i = len(randomList) - 1

while i > 1:
    j = 0
    while j < i:
        print "\nIs {} > {}".format(randomList[j], randomList[j + 1])
        if randomList[j] > randomList[j + 1]:
            print "Switch"
            temp = randomList[j]
            randomList[j] = randomList[j + 1]
            randomList[j + 1] = temp
        else:
            print "Dont Switch"
        j += 1
        for k in randomList:
            print k,
        print
    print "END OF ROUND"
    i -= 1

print randomList

# UTILITY FUNCTIONS

randomList.insert(4, 9)  # DOES NOT REPLACE
randomList.remove(9)  # REMOVE BY VALUE
randomList.pop(1)  # REMOVE BY INDEX
print randomList

# LIST COMPREHENSIONS

# COOL WAY TO GENERATE LISTS
evenValuesList = [i * 2 for i in range(10)]
print evenValuesList

# MULTIPLE CALCULATIONS TO GENERATE LIST

sampleList = [1, 2, 3, 4, 5]

powerList = [[math.pow(m, 1), math.pow(m, 2), math.pow(m, 3)]
             for m in sampleList]

print "Power List is: ", powerList
for power in powerList:
    print power

# CREATE 10x10 LIST

multiDList = [[0] * 10 for i in range(10)]

for row in multiDList:
    print row

print
# multiDList[0][3] = 2
# for row in multiDList:
#     print row


# MULTIPLICATION TABLE

multiplicationTable = [[0] * 9 for i in range(9)]

for row in multiplicationTable:
    print row

print

for i in range(9):
    for j in range(9):
        multiplicationTable[i][j] = "{} * {} = {}".format(i+1, j+1, (i + 1) * (j + 1))

for row in multiplicationTable:
    print row


