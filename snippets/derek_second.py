import random

# Returns rand no bw 1 and 50
rand_num = random.randrange(1, 51)
print rand_num
i = 1
while i is not rand_num:
    i += 1

print rand_num

ht = raw_input("Enter ht: ")
ht = int(ht)

max_leaves = 1 + (ht - 1) * 2
myList = list()

for i in range(1, max_leaves+1, 2):
    myList.append(i)

print myList

count = 1

while count <= ht:
    no_of_leaves = myList[count-1]
    no_of_blanks = max_leaves - no_of_leaves
    for blank in range(no_of_blanks/2):
        print " ",
    for leaf in range(no_of_leaves):
        print "#",
    for blank2 in range(no_of_blanks / 2):
        print " ",
    print "\n"
    count += 1



