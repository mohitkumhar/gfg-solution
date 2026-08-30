'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    def sortedInsert(self, head, x):

        if not head:
            return None

        if x <= head.data:
            node = Node(x)
            node.next = head
            head.prev = node

            return node

        curr = head

        while curr.next and curr.next.data < x:
            curr = curr.next

        node = Node(x)

        node.next = curr.next
        node.prev = curr

        if curr.next:
            curr.next.prev = node

        curr.next = node

        return head
