def karatsuba(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        quot = n / 2

        a = x / 10 ** (quot)
        b = x % 10 ** (quot)
        c = y / 10 ** (quot)
        d = y % 10 ** (quot)

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
        final_prod = ac * 10 ** (2 * quot) + (ad_plus_bc * 10 ** quot) + bd

        return final_prod


def naive_mult(x, y):
    x_List = list(str(x))
    y_List = list(str(y))
    for i in range(len(x_List)):
        x_List[i] = int(x_List[i])
    for i in range(len(y_List)):
        y_List[i] = int(y_List[i])
        # print y_List
    to_mult = 1
    finalList = list()
    for num in range(len(y_List) - 1, -1, -1):
        # print "num is", y_List[num]
        prod = y_List[num] * x
        prod = prod * to_mult
        # print "prod is", prod
        to_mult *= 10
        finalList.append(prod)
    final_prod = 0
    for item in finalList:
        final_prod += item

        # print final_prod
    return final_prod


print "Naive method: ", naive_mult(5678, 1234)
print "Karatsuba: ", karatsuba(5678, 1234)
