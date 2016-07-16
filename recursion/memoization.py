def factorial_memoize(n):
    if n < 2:
        return 1
    lookup_table = {}
    if n not in lookup_table:
        lookup_table[n] = n * factorial_memoize(n - 1)
    return lookup_table[n]


print factorial_memoize(8)
