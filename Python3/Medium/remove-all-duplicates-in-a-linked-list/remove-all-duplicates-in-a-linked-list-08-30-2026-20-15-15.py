''' Structure of linked list Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def removeDuplicates(self, head):
        freq = {}

        curr = head

        while curr:
            freq[curr.data] = freq.get(curr.data, 0) + 1
            curr = curr.next

        dummy = Node(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:

            if freq[curr.data] > 1:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next
