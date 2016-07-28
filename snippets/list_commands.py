n = raw_input()
n = int(n)

myList = []
for i in range(n):
    commands = raw_input("").split()
    method = commands[0]
    if method == "print":
        print myList
    elif method == "insert":
        index = int(commands[1])
        value = int(commands[2])
        myList.insert(index, value)
    elif method == "remove":
        element = int(commands[1])
        myList.remove(element)
    elif method == "append":
        append_val = int(commands[1])
        myList.append(append_val)
    elif method == "sort":
        myList.sort()
    elif method == "pop":
        myList.pop()
    elif method == "reverse":
        myList.reverse()
