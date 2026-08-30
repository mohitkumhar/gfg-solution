'''Structure for linked list Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''
class Solution:
    def mergeResult(self, head1, head2):

        dummy = Node(0)
        temp = dummy

        # merge the LL

        curr1 = head1
        curr2 = head2

        while curr1 and curr2:
            if curr1.data < curr2.data:
                temp.next = Node(curr1.data)
                curr1 = curr1.next
            else:
                temp.next = Node(curr2.data)
                curr2 = curr2.next
            temp = temp.next

        while curr1:
            temp.next = Node(curr1.data)
            curr1 = curr1.next
            temp = temp.next

        while curr2:
            temp.next = Node(curr2.data)
            curr2 = curr2.next
            temp = temp.next

        # reverse the LL

        prev = None

        curr = dummy.next
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev
