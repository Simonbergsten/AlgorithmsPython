"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following
 the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
  Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.


Example 1:
Input: head=[3,2,0,-4], pos = 1
output: true

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hashCycle(self, head):
        hare = head
        turtle = head

        while turtle and hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next
            if (turtle == hare):
                return True

        return False

s = Solution()
node_1 = ListNode(1)
node_5 = ListNode(5)
node_11 = ListNode(11)
node_8 = ListNode(8)
node_9 = ListNode(9)

node_1.next = node_5
node_5.next = node_11
node_11.next = node_8
node_8.next = node_9
node_9.next = node_5

answer = s.hashCycle(node_1)
print(answer)
