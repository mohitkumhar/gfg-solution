# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None

class Solution:
    def intersectPoint(self, head1, head2):

        def findLength(head):
            curr = head
            length = 0
            while curr:
                curr = curr.next
                length += 1
            return length

        len1 = findLength(head1)
        len2 = findLength(head2)

        while len1 > len2:
            head1 = head1.next
            len1 -= 1

        while len2 > len1:
            head2 = head2.next
            len2 -= 1

        while len1 >= 0:

            if head1 == head2:
                return head1

            head1 = head1.next
            head2 = head2.next

        return None
