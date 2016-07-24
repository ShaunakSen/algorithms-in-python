A node is a fundamental part of a tree. It can have a name which we call key
A node may have addnl info which we call payload

An edge connects 2 nodes to show that there exists relationship b/w them

Root is only node with no incoming edges
The level of a node "n" is the no of edges on the path from root node to n

ht = maxm level

If each node has a maxm of 2 children its a binary tree

Recursive Defn : A tree is either empty or consists of a root and zero or more subtrees, each of which
is also a tree

Binary Search Trees
_______________________

BST is a way to map from a key to a value

They allow fast lookup, addition and removal of items, and can be used to implement
either dynamic sets of items, or lookup tables that allow finding an item by its key
(e.g., finding the phone number of a person by name).

See wikipedia article

BST property: keys less than parent are found in left subtree.
keys > parent are found in right subtree
