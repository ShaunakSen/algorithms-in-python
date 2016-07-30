# Uses python3
n = int(raw_input())
a = [int(x) for x in raw_input().split()]

assert(len(a) == n)

max_index1 = 0

for i in range(0, n):
    if a[i] > a[max_index1]:
        max_index1 = i

max_index2 = -1
for x in range(0, n):
    if x != max_index1 and a[x] > a[max_index2]:
        max_index2 = x

result = a[max_index1] * a[max_index2]

print a[max_index1] * a[max_index2]