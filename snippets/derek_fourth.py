blaah = "     hi.. Little mini   "

blaah = blaah.strip()

print blaah

print blaah.capitalize()

print blaah.count(" ")

print "Where is String: ", blaah.find("hi")

long_form = str(raw_input("Enter String: "))

long_form = long_form.strip()

myList = long_form.split()
acronym = ""
for item in myList:
    acronym += item[0].upper()

print acronym

# USEFUL FUNCTIONS

print "ijskjds333".isalnum()  # CHECKS LETTERS AND NUMBERS
print "sdD2".isalpha()  # CHECKS LETTERS
print "687".isdigit()
print "sjkald".islower()
print "    ".isspace()


# CREATE isfloat() function

def isfloat(myStr):
    try:
        float(myStr)
        return True
    except ValueError:
        return False


print isfloat("3.14sd")


# 65-90 || 97-122

def CeasersCipher(myStr, key):
    finalString = ""
    if key > 26:
        key = 26

    for char in myStr:
        if char.islower():
            upperLimit = 122
            lowerLimit = 97
            intValue = int(ord(char))
            intValue += key
            if intValue > upperLimit:
                diff = intValue - upperLimit
                finalIntValue = lowerLimit + diff - 1
                stringEncode = chr(finalIntValue)
                finalString += stringEncode
            else:
                stringEncode = chr(intValue)
                finalString += stringEncode
        elif char.isupper():
            upperLimit = 90
            lowerLimit = 65
            intValue = int(ord(char))
            intValue += key
            if intValue > upperLimit:
                diff = intValue - upperLimit
                finalIntValue = lowerLimit + diff - 1
                stringEncode = chr(finalIntValue)
                finalString += stringEncode
            else:
                stringEncode = chr(intValue)
                finalString += stringEncode
        else:
            finalString += char

    return finalString



print CeasersCipher("Shaunak Sen", 1)
