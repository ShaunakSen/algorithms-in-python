class Singly_list(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None


def find_length(node):
    length = 1
    while node.nextNode is not None:
        node = node.nextNode
        length += 1

    return length


def nth_to_last(index, node):
    length = find_length(node)
    effextiveLength = length - index + 1
    i = 1
    while i != effextiveLength:
        node = node.nextNode
        i += 1
    return node.value


a = Singly_list(1)
b = Singly_list(2)
c = Singly_list(3)
d = Singly_list(4)
e = Singly_list(5)

a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e

print nth_to_last(3, a)
