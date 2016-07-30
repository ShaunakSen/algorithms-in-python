F = list()
F.append(0)
F.append(1)

n = raw_input("")
n = int(n)
for i in range(2, n):
    F.append(F[i - 1] + F[i - 2])

print F


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
