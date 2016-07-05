def reverse_sentence(str):
    str = str.rstrip()
    str = str.lstrip()
    myList = str.split(' ')
    myList.reverse()
    newStr = ' '.join(myList)
    return newStr


def reverse_sentence2(str):
    words = []
    length = len(str)

    index = 0

    while index < length:
        if str[index] != ' ':
            start = index
            while str[index] != ' ':
                index += 1
            end = index
            words.append(str[start:end])
        index += 1

    print " ".join(reversed(words))


# print reverse_sentence('   This is the Best  ')
reverse_sentence2('   This is the Best  ')
