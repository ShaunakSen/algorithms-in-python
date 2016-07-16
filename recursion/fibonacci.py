lookup_table = {}


def fibo_dynamic(n):
    if n == 1 or n == 0:
        return n
    if n not in lookup_table:
        lookup_table[n] = fibo_dynamic(n - 1) + fibo_dynamic(n - 2)
    return lookup_table[n]


def fibo_iterative(n):
    a = 0
    b = 1
    for i in range(n):
        temp = a
        a = b
        b += temp
    return a


def fib_recursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


print fibo_dynamic(12)
print fibo_iterative(10)
print fib_recursive(10)
