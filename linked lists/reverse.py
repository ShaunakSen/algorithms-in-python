class Singly_list(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None


def reverse(head):
    current = head
    previous = None
    nextnode = None

    while current:

        nextnode = current.nextNode
        current.nextNode = previous
        previous = current
        current = nextnode
    return previous


a = Singly_list(1)
b = Singly_list(2)
c = Singly_list(3)
d = Singly_list(4)
e = Singly_list(5)

a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e

print reverse(a)

print e.nextNode.value
