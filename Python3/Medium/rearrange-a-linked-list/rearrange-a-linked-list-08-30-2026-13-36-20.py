""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def rearrangeEvenOdd(self, head):
        # code here

        oddHead = head
        evenHead = head.next

        odd = oddHead
        even = evenHead

        while even and even.next:

            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenHead

        return oddHead
