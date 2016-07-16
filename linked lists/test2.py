mylist = [10, 3, 5, 7]

mylist.sort()

print mylist

mysum=0

index=0

for item in mylist[:len(mylist)-1]:
    mysum += item
    index += 1
    if mysum > mylist[len(mylist)-1]:
        break

print mysum, index-1