# THINGS TO FIND OUT: Print line + Output no of words per line + ave word length

with open("data.txt") as myFile:
    lineNum = 1
    sumOfWords = 0
    while True:
        line = myFile.readline()
        if not line:
            break
        wordsArray = line.split()
        noOfWords = len(wordsArray)
        sumOfWords += noOfWords
        wordsLength = [len(word) for word in wordsArray]
        aveWordLength = float(sum(wordsLength)) / len(wordsLength)
        print "Line No: ", lineNum, line, "No of Words: ", noOfWords, "Ave word length: ", aveWordLength
        lineNum += 1
    print lineNum
    print "Ave no of Words per line: ", (float(sumOfWords) / (lineNum - 1))

myFile.close()

# TUPLES

# SAME AS LIST EXCEPT THAT THEIR VALUES CANNOT BE CHANGED
myTuple = (1, 2, 3, 4)

print myTuple[1]
print myTuple[:3]
print len(myTuple)

moreNums = myTuple + (5, 6, 7)
print moreNums
print 32 in moreNums

aList = [123, 345]
aTuple = tuple(aList)
aList = list(aTuple)
print aList
print aTuple