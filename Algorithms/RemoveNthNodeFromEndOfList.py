"""
n = 2
Linked List = [1, 2, 3, 4, 5]
Output: [1,2,3,5]
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        ans = ListNode(0)
        ans.next = head

        first = ans
        second = ans

        for i in range(1, n + 2):
            first = first.next

        while (first is not None):
            first = first.next
            second = second.next

        second.next = second.next.next
        return ans.next


s = Solution()
# 1 -> 3 -> 5 -> 7, n = 2
# 1 -> 3 -> 7

node_1 = ListNode(1)
node_3 = ListNode(3)
node_5 = ListNode(5)
node_7 = ListNode(7)

node_1.next = node_3
node_3.next = node_5
node_5.next = node_7

answer  = s.removeNthFromEnd(node_1, 2)
while(answer != None):
    print(answer.val)
    answer = answer.next




