n = raw_input("")

n = int(n)

myList = list(map(int, input().split()))



print myList

dictionary = dict()

for item in myList:
    newList = list(item)
    dictionary[item] = newList

print dictionary




new_big_list = list()
for key, value in dictionary.items():
    new_big_list.append(value)

print new_big_list

new_big_list.sort(reverse=True)

print new_big_list

final = ""
for item in new_big_list:
    for digit in item:
        final += digit

print final