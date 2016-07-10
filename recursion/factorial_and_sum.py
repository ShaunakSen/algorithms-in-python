def fact(n):
    if n == 0:
        print 'n=0 .. returns 1'
        return 1

    else:
        print "n=", n
        print "calling ", n, "*", n - 1, "!"
        return n * fact(n - 1)


def rec_sum(n):
    if n == 0:
        return 0
    else:
        print n
        return n + rec_sum(n - 1)


print fact(5)
print rec_sum(9)
