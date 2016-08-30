class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def preOrder(root):
    if root is None:
        return
    print root.data,
    preOrder(root.left)
    preOrder(root.right)


def height(root):
    if root is None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    maxHt = max(lh, rh)
    return maxHt + 1


def LevelOrder(root):
    ht = height(root)
    for i in range(1, ht + 1):
        printGivenLevel(root, i)
        print


def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print root.data,
        return
    if level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print "PRE ORDER ",
preOrder(root)
print
print "Level No 2:",
printGivenLevel(root, 2)
print
print "HEIGHT: ", height(root)
print "LEVEL ORDER:"
LevelOrder(root)




