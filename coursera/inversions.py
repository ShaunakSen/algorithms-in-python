inversions = 0


def mergeSort(myList):
    if len(myList) < 2:
        return myList
    else:
        length = len(myList) / 2
        return merge(mergeSort(myList[:length]), mergeSort(myList[length:]))


def merge(left, right):
    i = 0
    j = 0
    global inversions
    result = list()
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            inversions += len(left) - i
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


print "Enter The Elements One By One"

myList = list()

myList = raw_input("Enter the elements: ").split()

for i in range(len(myList)):
    myList[i] = int(myList[i])

print mergeSort(myList)

print inversions
