"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the
nodes of the first two lists.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def addToList(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode


def mergeLists(headA, headB):
    dummyNode = Node(0)

    # Tail stores the last node
    tail = dummyNode
    while True:

        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break

        # Compare the data of the lists and whichever is smaller
        # is appended to the last of the merged lists and the head is changed
        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next

        tail = tail.next

    return dummyNode.next


# Create two lists
listA = LinkedList()
listB = LinkedList()

listA.addToList(1)
listA.addToList(2)
listA.addToList(4)

listB.addToList(1)
listB.addToList(3)
listB.addToList(4)

listA.head = mergeLists(listA.head, listB.head)
print("Merged linked list: ")
listA.printList()
