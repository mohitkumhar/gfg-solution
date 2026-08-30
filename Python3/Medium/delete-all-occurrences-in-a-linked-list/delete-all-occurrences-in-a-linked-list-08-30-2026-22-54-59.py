"""Structure of a linked list node

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""
class Solution:

    def deleteAllOccurances(self, head, x):

        dummy = Node(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:

            if curr.data == x:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next
