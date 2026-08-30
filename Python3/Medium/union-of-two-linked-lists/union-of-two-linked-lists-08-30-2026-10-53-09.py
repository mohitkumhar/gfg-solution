""" Linked List Node Structure
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

"""
class Solution:
    def makeUnion(self, head1, head2):
        # code here
        seen = set()

        dummy = Node(0)
        temp = dummy

        curr1 = head1

        while curr1:
            if curr1.data not in seen:
                seen.add(curr1.data)
                temp.next = Node(curr1.data)
                temp = temp.next
            curr1 = curr1.next

        curr2 = head2
        while curr2:
            if curr2.data not in seen:
                seen.add(curr2.data)
                temp.next = Node(curr2.data)
                temp = temp.next
            curr2 = curr2.next

        return dummy.next
