""" Node Structure
class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
"""
class Solution:

    def rearrange(self, head):

        oddHead = head
        evenHead = head.next
        even = evenHead
        odd = oddHead

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = None

        prev = None
        curr = evenHead

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        odd.next = prev
        return oddHead
