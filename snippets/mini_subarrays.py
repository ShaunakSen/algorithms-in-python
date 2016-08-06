T = int(raw_input(""))

while T:
    N = int(raw_input(""))
    arrayList = raw_input("").split()
    for i in range(len(arrayList)):
        arrayList[i] = int(arrayList[i])

    # print arrayList

    counDict = {}

    for i in range(len(arrayList) - 1):
        j = i + 1
        if arrayList[i] == arrayList[j]:
            counDict[arrayList[i]] = counDict.get(arrayList[i], 1) + 1
            j += 1
        else:
            counDict[arrayList[i]] = counDict.get(arrayList[i], 1) + 0

    print counDict

    # print counDict

    mainCount = 0

    for count in counDict.values():
        if count == 1:
            mainCount += 1
        elif count == 2:
            mainCount += 3
        else:
            totalWays = count * (count + 1) / 2
            mainCount += totalWays
    print mainCount
    arrayListLen = len(arrayList)
    sumOfValues = 0
    for value in counDict.values():
        sumOfValues += value
    diff = arrayListLen - sumOfValues

    if diff > 0:
        mainCount += diff

    print mainCount
    T -= 1
