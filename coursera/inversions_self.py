inversions = 0


def mergeSort(aList):
    if len(aList) < 2:
        return aList
    mid = len(aList) / 2
    firstHalf = aList[:mid]
    lastHalf = aList[mid:]

    return merge(mergeSort(firstHalf), mergeSort(lastHalf))


def merge(left, right):
    i = 0
    j = 0
    result = []
    global inversions
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


def main():
    myList = [5, 4, 3, 2]
    print mergeSort(myList)

    print inversions
main()