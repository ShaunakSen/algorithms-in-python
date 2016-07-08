class Singly_list(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None


a = Singly_list(1)
b = Singly_list(2)
c = Singly_list(3)

a.nextNode = b
b.nextNode = c

print a.value
a.value = 'start'
print a.value
print a.nextNode.value
print a.nextNode.nextNode.value
