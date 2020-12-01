""""
Maximum depth is the no.of nodes in the longest path from root to furthest leaf node
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


class Solution:
    def maxDepth(self, root):
        if (root is None):
            return 0
        if (root.left is None and root.right is None):
            return 1
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


# Create a tree
tree = Node(5)
insert(tree, Node(3))
insert(tree, Node(2))
insert(tree, Node(4))
insert(tree, Node(7))
insert(tree, Node(6))
insert(tree, Node(8))

s = Solution()
print(s.maxDepth(tree))