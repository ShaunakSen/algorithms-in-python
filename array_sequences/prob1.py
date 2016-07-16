def anagram(str1, str2):
    str1 = str1.replace(' ', '')
    str2 = str2.replace(' ', '')
    str1 = str1.lower()
    str2 = str2.lower()
    print str1, str2
    sortedList1 = sorted(str1)
    sortedList2 = sorted(str2)
    print sortedList1, sortedList2
    sortedStr1 = ''.join(sortedList1)
    sortedStr2 = ''.join(sortedList2)
    print sortedStr1, sortedStr2
    print sortedStr1 == sortedStr2


def anagram2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    #EDGE CASE CHECK

    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True

anagram('clint eastwood','old west action')

print anagram2('d o  g', 'go   D')
