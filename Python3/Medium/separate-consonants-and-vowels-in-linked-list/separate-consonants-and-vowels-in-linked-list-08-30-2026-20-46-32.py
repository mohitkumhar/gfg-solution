"""
structure of a link list node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    def arrange(self, head):
        vowels = set('aeiou')

        vowelHead = vowelTail = None
        consHead = consTail = None
        curr = head

        while curr:
            nn = curr.next
            curr.next = None

            if curr.data in "aeiou":
                if not vowelHead:
                    vowelHead = curr
                    vowelTail = curr
                else:
                    vowelTail.next = curr
                    vowelTail = vowelTail.next

            else:
                if not consHead:
                    consHead = curr
                    consTail = curr
                else:
                    consTail.next = curr
                    consTail = consTail.next

            curr = nn

        if not vowelHead:
            return consHead
        if not consHead:
            return vowelHead

        vowelTail.next = consHead
        return vowelHead
