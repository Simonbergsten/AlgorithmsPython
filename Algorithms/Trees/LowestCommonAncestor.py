
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
         if root is None:
             return None
         if (root.val == p.val or root.val == q.val):
             return root

         left = self.lowestCommonAncestor(root.left, p, q)
         right = self.lowestCommonAncestor(root.right, p, q)

         if (left is None and right is None):
             return None
         if (left is not None and right is not None):
             return root
         if (left is None):
             return right
         return left
