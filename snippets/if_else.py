n = int(raw_input().strip())

if n % 2 != 0:
    print 'Weird'
else:
    if 2 <= n <= 5:
        print 'Not Weird'
    elif 6 <= n <= 20:
        print 'Weird'
    elif n > 20:
        print 'Not Weird'

num1 = raw_input()
num1 = int(num1)

num2 = raw_input()
num2 = int(num2)

print num1 + num2
print num1 - num2
print num1 * num2
