def compress(str1):
    count = {}
    for character in str1:
        if character in count:
            count[character] += 1
        else:
            count[character] = 1

    newStr = ""
    print count
    for item in count:
        newStr = newStr + item + str(count[item])
    return newStr




print compress('AAAABBBBBBB')
print compress('AAAAaaaabbbbAAAAAAAAAA')


