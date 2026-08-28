""" Structure of a Linked List Node
class Node:
    def __init__(self):
        self.data = None
        self.next = None
"""

class Solution:
    def divide(self, head):

        evenHead = None
        evenTail = None

        oddHead = None
        oddTail = None

        curr = head

        while curr:
            if curr.data % 2 == 0:
                if not evenHead:
                    evenHead = curr
                    evenTail = curr
                else:
                    evenTail.next = curr
                    evenTail = evenTail.next

            else:
                if not oddHead:
                    oddHead = curr
                    oddTail = curr
                else:
                    oddTail.next = curr
                    oddTail = oddTail.next
            curr = curr.next

        if evenHead is None:
            return oddHead

        evenTail.next = oddHead

        if oddTail:
            oddTail.next = None

        return evenHead
