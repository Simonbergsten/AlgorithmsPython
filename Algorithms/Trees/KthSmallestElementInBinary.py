"""
Solve by traversing, since the values are olready sorted in a binary tree.
"""
class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

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
    def kthSmallest(self, root, k):
        self.k = k
        self.res = None

        self.inorder(root)

        return self.res

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)

        self.k-= 1
        if self.k == 0:
            self.res == root.data
            return

        self.inorder(root.right)


tree = TreeNode(5)
insert(tree, TreeNode(3))
insert(tree, TreeNode(1))
insert(tree, TreeNode(4))
insert(tree, TreeNode(7))

s = Solution()
print(s.kthSmallest(tree, 3))

