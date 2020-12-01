"""
Is a tree a mirror of itself?

           5
        /     \
       2      2
     /  \    /  \
    3    4  4   3

Ovanstående är exempelvis en mirror
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




class Solution:

    def isMirror(self, t1, t2):
        if (t1 is None and t2 is None):
            return True
        if (t1 is None or t2 is None):
            return False

        return (t1.val == t2.val) and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)

    def isSymmetric(self, root):
        return self.isMirror(root, root)


tree = TreeNode(5)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(3)

s = Solution()
print(s.isSymmetric(tree))
