t = raw_input("")

t = int(t)
stack = []
while t > 0:

    query = raw_input("").split()
    if int(query[0]) == 1:
        if len(stack) == 0:
            print "No Food"
        else:
            item = stack.pop()
            print item
    else:
        price = query[1]
        stack.append(price)

    t -= 1
