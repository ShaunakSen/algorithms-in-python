str1 = raw_input("")


dictionary = dict()

for char in str1:
    dictionary[char] = dictionary.get(char, 0) + 1

templist = list()

for key, value in dictionary.items():
    templist.append((value, key))

templist.sort(reverse=True)

for k, v in templist[:1]:
    print v, k
