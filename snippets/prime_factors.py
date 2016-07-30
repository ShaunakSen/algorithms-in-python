def primes(n):
    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac


T = raw_input("").split()
cases = int(T[0])
A = list()
for i in range(cases):
    size = raw_input("").split()
    N = int(size[0])
    X = int(size[1])
    Y = int(size[2])
    Z = int(size[3])
    A = raw_input("").split()

for x in range(0, len(A)):
    A[x] = int(A[x])

print A

big_array = []
for item in A:
    prime_array = primes(item)
    for inner_item in prime_array:
        if inner_item not in big_array:
            big_array.append(inner_item)

