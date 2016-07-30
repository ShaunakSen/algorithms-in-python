import sys

myinput = sys.stdin.read()
print (myinput)
tokens = myinput.split()
a = int(tokens[0])
b = int(tokens[1])
print(a + b)