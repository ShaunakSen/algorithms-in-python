N = raw_input("").split()

number = N[0]
T = raw_input("").split()
cases = int(T[0])

for i in range(cases):
    left, right = raw_input("").split()
    left = int(left)
    right = int(right)
    left -= 1
    subStr = number[left:right]
    subNo = int(subStr)
    if subNo % 7 == 0:
        print "YES"
    else:
        print "NO"
