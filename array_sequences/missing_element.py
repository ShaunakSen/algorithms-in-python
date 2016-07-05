def missing_element(list1, list2):
    list1.sort()
    list2.sort()
    list3 = zip(list1, list2)
    print list1, list2
    print list3
    for i, j in list3:
        if i != j:
            return i
    return list1[-1]


def missing_element2(list1, list2):
    d = dict()
    for num in list2:
        d[num] = d.get(num, 0) + 1
    for num in list1:
        foundNum = d.get(num, -1)
        if foundNum == -1:
            return num


print missing_element([1, 2, 5, 4, 8, 6], [2, 4, 1, 6, 5])
print missing_element2([1, 2, 5, 4, 8, 6], [1, 4, 8, 6, 5])
