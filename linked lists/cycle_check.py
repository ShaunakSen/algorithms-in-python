class Singly_list(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None


def cycle_check(node):
    visted_nodes = []
    while node not in visted_nodes:
        visted_nodes.append(node)
        print visted_nodes
        if node.nextNode is None:
            return False
        node = node.nextNode
    return True


def cycle_check2(node):
    marker1 = node
    marker2 = node

    while marker2 is not None and marker2.nextNode is not None:
        marker1 = marker1.nextNode
        marker2 = marker2.nextNode.nextNode

        if marker2 == marker1:
            return True

    return False


a = Singly_list(1)
b = Singly_list(2)
c = Singly_list(3)
d = Singly_list(4)
e = Singly_list(5)

a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e
e.nextNode = c

print cycle_check(a)
print cycle_check2(a)
