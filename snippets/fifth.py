length = raw_input("")
str1 = raw_input("")

myList = list()
for char in str1:
    myList.append(char)

max = 0
letter = myList[0]
index = 0
for i in range(len(myList)):
    if ord(myList[i]) > max:
        max = ord(myList[i])
        letter = myList[i]
        index = i


print "".join(myList[index:])