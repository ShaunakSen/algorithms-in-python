# DICTIONARIES
import os

miniDict = {"fname": "Mini", "lname": "Sen",
            "address": "3/1 Bada bazar 284002"}
print miniDict["fname"]

miniDict["address"] = "89 Dum Dum Park"

print miniDict

miniDict["city"] = "Jhansi"

print "Is there a city: ", "city" in miniDict  # CHECK WHETHER KEY EXISTS

print miniDict.values()
print miniDict.keys()
print miniDict.items()

for key, value in miniDict.items():
    print key, value

print miniDict.get("mName", "N.A")

# DELETE

del miniDict["city"]
miniDict.clear()

print miniDict

# LISTS AND DICTIONARIES
employee = []
while True:
    try:
        fname, lname = raw_input("Enter name: ").split()
        employee.append({"fname": fname, "lname": lname})
        break
    except ValueError:
        print "Enter space separated name"

print employee

customers = []

while True:
    createEntry = raw_input("Enter customer(yes/no) ")
    createEntry = createEntry[0].lower()
    if createEntry == "n":
        break
    else:
        fname, lname = raw_input("Enter name: ").split()
        customers.append({"fname": fname, "lname": lname})

print customers

# FILE OPS
# with bcoz it ensures that if our program crashes file is closed
# w is for overwriting..use a for appending

with open("mydata.txt", mode="w") as myFile:
    myFile.write("Some random text\nSome random text")

# default is read mode

# read(), readline(), readlines() methods
# with open("mydata.txt") as myFile:
#     print myFile.read()

# print myFile.closed
#
# print myFile.name
#
# print myFile.mode

os.rename("mydata.txt", "data.txt")

# os.remove("file_name")
# os.mkdir("test_directory")
os.chdir("test_directory")
print "Current directory: ", os.getcwd()


# os.chdir("..")
# os.rmdir("test_directory")

# FIBONACCI

def fibo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        result = fibo(num - 1) + fibo(num - 2)
        return result

for i in range(1, 10):
    print fibo(i)

# READ ONE LINE AT A TIME

with open('readme.txt') as myFile:
    lineNum = 1
    while True:
        line = myFile.readline()
        if not line:
            break
        print "Line: ", lineNum, line
        lineNum += 1

