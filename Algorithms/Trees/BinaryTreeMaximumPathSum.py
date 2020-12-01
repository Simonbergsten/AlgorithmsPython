


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


tree = Node(10)
insert(tree, Node(4))
insert(tree, Node(-6))
insert(tree, Node(22))
insert(tree, Node(-30))
insert(tree, Node(-10))
insert(tree, Node(20))
insert(tree, Node(-28))
insert(tree, Node(2))
insert(tree, Node(7))

class Solution:
    ans = -float("inf")

    def solution(self, node):
        if (node is None):
            return 0
        left = self.solution(node.left)
        right = self.solution(node.right)

        mxSide = max(node.val, max(left, right)+node.val)
        mxTop = max(mxSide,left+right+node.val)
        self.ans = max(self.ans, mxTop)
        return mxSide

    def maxPathSum(self, root):
        self.solution(root)
        return self.ans

