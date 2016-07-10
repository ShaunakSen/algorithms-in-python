def sum_of_digits(num):
    if num / 10 == 0:
        return num
    else:
        temp = num % 10
        return temp + sum_of_digits(num / 10)


print sum_of_digits(10157)
