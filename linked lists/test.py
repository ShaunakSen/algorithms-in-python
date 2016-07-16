import math

classes = int(raw_input("Enter no of classes: "))
cakes = int(raw_input("Enter no of cakes: "))

studentsList = []

for i in range(classes):
    students = raw_input("Enter no of students in class")
    studentsList.append(students)

total = 0

for item in studentsList:
    total += int(item)

print total

if total <= cakes:
    maximum = 0
else:

    if total % 2 == 0:
        maximum = int(math.ceil(float(total) / float(cakes)))

    else:
        maximum = int(math.ceil(float(total) / float(cakes)))

print maximum
