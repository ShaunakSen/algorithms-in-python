def is_unique(str1):
    mySet = set()

    for letter in str1:
        if letter in mySet:
            return False
        else:
            mySet.add(letter)
    return True


print is_unique('asfd')
