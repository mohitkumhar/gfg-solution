'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
#Function to sort the given doubly linked list using Merge Sort.
    def mergeSort(self, head):
        # code hereclass Solution:
        if not head or not head.next:
            return head

        # Find middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Split into two lists
        right = slow.next
        slow.next = None

        if right:
            right.prev = None

        left = head

        # Sort both halves
        left = self.mergeSort(left)
        right = self.mergeSort(right)

        # Merge
        return self.merge(left, right)
    
    def merge(self, a, b):

        dummy = Node(0)
        tail = dummy

        while a and b:

            if a.data <= b.data:
                tail.next = a
                a.prev = tail
                a = a.next
            else:
                tail.next = b
                b.prev = tail
                b = b.next

            tail = tail.next

        # Attach remaining nodes
        if a:
            tail.next = a
            a.prev = tail

        if b:
            tail.next = b
            b.prev = tail

        # Remove dummy
        head = dummy.next

        if head:
            head.prev = None

        return head
