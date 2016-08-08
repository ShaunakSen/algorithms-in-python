with open("data.txt") as myFile:
    lineNum = 1
    while True:
        line = myFile.readline()
        if not line:
            break
        print "Line no: ", lineNum, line
        lineNum += 1

myFile.close()