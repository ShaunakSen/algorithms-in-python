# USE EXCEPTION HANDLING TO FORCE USER TO ENTER A NO
import random

while True:
    try:
        number = int(raw_input("Enter a no: "))
        break
    except ValueError:
        print "You Did Not enter a no"

    except:
        print "An unknown error occurred"

print "Thank you for entering a no"

# DO WHILE SIMULATION IN PYTHON
rand_num = random.randrange(1, 10)
print rand_num

while True:
    while True:
        try:
            user_number = int(raw_input("Enter a no between 1 and 9: "))
            if 1 <= user_number <= 9:
                break
            else:
                continue
        except ValueError:
            print "You Did Not enter a no"
        except:
            print "An unknown error occurred"

    if user_number == rand_num:
        print "U guessed right!!", user_number
        break
    else:
        continue

# STRINGS

myString = "Little Mini"

for i in range(0, len(myString) - 1, 2):
    print myString[i] + myString[i + 1]

print "A=", ord("A")
print "65=", chr(65)

strEncode = str(raw_input("Enter a string "))

strDecode = ""
helperList = list()
for char in strEncode:
    if 65 <= ord(char) <= 90:
        helperList.append(0)
    else:
        helperList.append(1)
    strDecode += str(ord(char))

print strDecode

print helperList

pointer = 0
reverseDecoded = ""
for helper_value in helperList:
    if helper_value == 0:
        extracted = strDecode[pointer:pointer + 2]
        # print extracted
        decodedValue = chr(int(strDecode[pointer:pointer + 2]))
        reverseDecoded += decodedValue
        pointer += 2
    else:
        if strDecode[pointer] == '1':
            extracted = strDecode[pointer:pointer + 3]
            # print extracted
            decodedValue = chr(int(strDecode[pointer:pointer + 3]))
            reverseDecoded += decodedValue
            pointer += 3
        else:
            extracted = strDecode[pointer:pointer + 2]
            # print extracted
            decodedValue = chr(int(strDecode[pointer:pointer + 2]))
            reverseDecoded += decodedValue
            pointer += 2
print reverseDecoded
# A-Z: 65-90
# a-z: 97-122
