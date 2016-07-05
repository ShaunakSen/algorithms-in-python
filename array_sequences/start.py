import sys

n = 50

data = []

for i in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print 'Length: ', a, 'Size: ', b
    data.append(n)
