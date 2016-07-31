F = list()
F.append(0)
F.append(1)

n = raw_input("")
n = int(n)
for i in range(2, n):
    F.append((F[i - 1] + F[i - 2]) % 10)
print F
print F[len(F) - 1]


def periodLength(mod):
    Fib = list()
    Fib.append(0)
    Fib.append(1)
    for x in range(2, 100):
        Fib.append((Fib[x - 1] + Fib[x - 2]) % mod)

    initial_period = 2
    for index in range(2, len(Fib)):
        index2 = index + 1
        if Fib[index] == 0 and Fib[index2] == 1:
            return initial_period
        else:
            initial_period += 1

print 'Period Length: ', periodLength(10)


def EuclidianGCD(a, b):
    if b == 0:
        return a
    rem = a % b
    return EuclidianGCD(b, rem)


def smartLCM(a, b):
    GCD = EuclidianGCD(a, b)
    LCM = a / GCD * b
    return LCM


print EuclidianGCD(28851538, 1183019)
print smartLCM(28851538, 1183019)
