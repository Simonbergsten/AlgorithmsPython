""""
Example:
    Input: [1,2,3,4,5]
    Output: [5,4,3,2,1]
"""
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        node = None
        while (head is not None):
            next = head.next
            head.next = node
            node = head
            head = next
        return node


s = Solution()
node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(5)

# Connect
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

print(s.reverseList(node_1.val))
