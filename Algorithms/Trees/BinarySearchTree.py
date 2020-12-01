"""
[X] A node can can have at most 2 leaves
[X] If node Y is larger than node X, then it has to be on the right of node X.
[X] If node Y is smaller than node X, then it has to be on the left of node X.

Three cases of deletion:
1. Deletion of a lead node - Just remove the leaf
2. Deletion of a node with one child - Delete the node and connect it's parent to it's child
3. Deletion of a node with two childs - Set the new node to the minimum of right side
"""
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def insert(root, node):
    if (root is None):
        root = node
        return

    if (root.data < node.data):
        if (root.right is None):
            root.right = node
        else:
            insert(root.right, node)
    else:
        if (root.left is None):
            root.left = node
        else:
            insert(root.left, node)

def search(node, key):
    print("Current node is: ",node.data)
    if (node is None):
        print("No node found")
        return None
    if (node.data == key):
        print("Node found!")
        return node

    if (node.data < key):
        return search(node.right, key)
    return search(node.left, key)

def preorder(node):
    if (node is not None):
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def deleteNode(node, key):
    if (node is None):
        return node

    if key < node.data:
        node.left = deleteNode(node.left, key)
    elif key > node.data:
        node.right = deleteNode(node.right, key)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        temp = minimumValue(node.right)
        node.data = temp.data
        node.right = deleteNode(node.right, temp.data)
    return node

def minimumValue(node):
    while(node.left is not None):
        node = node.left
    return node



# Create a tree
tree = Node(5)
insert(tree, Node(3))
insert(tree, Node(2))
insert(tree, Node(4))
insert(tree, Node(7))
insert(tree, Node(6))
insert(tree, Node(8))

preorder(tree)
search(tree, 2)