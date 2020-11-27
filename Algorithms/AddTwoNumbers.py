
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        ans = ListNode(None)
        pointer:ListNode = ans
        carry = 0
        sum = 0
        while(l1 != None or l2 != None):
            sum = carry
            if (l1!= None):
                sum += l1.val
                l1 = l1.next

            if (l2!= None):
                sum += l2.val
                l2 = l2.next

            carry = int(sum / 10)
            pointer.next = ListNode(sum % 10)
            pointer = pointer.next

        if (carry > 0):
            pointer.next = ListNode(carry)

        return ans.next

s = Solution()

# first list implementation
l1_node_2 = ListNode(2)
l1_node_4 = ListNode(4)
l1_node_3 = ListNode(3)

l1_node_2.next = l1_node_4
l1_node_4.next = l1_node_3


l2_node_5 = ListNode(5)
l2_node_6 = ListNode(6)
l2_node_4 = ListNode(4)

l2_node_5.next = l2_node_6
l2_node_6.next = l2_node_4

answer = s.addTwoNumbers(l1_node_2, l2_node_5)
while (answer != None):
    print(answer.val)
    answer = answer.next
