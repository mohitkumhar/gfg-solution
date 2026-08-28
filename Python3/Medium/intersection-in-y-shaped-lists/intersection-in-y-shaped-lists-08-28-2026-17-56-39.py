''' Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def intersectPoint(self, head1, head2):

        def findLength(head):
            length = 0
            while head:
                head = head.next
                length += 1
            return length

        curr1 = head1
        curr2 = head2

        len1 = findLength(head1)
        len2 = findLength(head2)

        while len1 > len2:
            head1 = head1.next
            len1 -= 1

        while len2 > len1:
            head2 = head2.next
            len2 -= 1

        while head1 and head2:

            if head1 == head2:
                return head1

            head1 = head1.next
            head2 = head2.next

        return None
