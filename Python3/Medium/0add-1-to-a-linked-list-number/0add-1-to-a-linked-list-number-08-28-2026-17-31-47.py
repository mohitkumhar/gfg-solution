''' structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def addOne(self, head):

        def reverse(head):
            prev = None

            while head:
                nextNode = head.next
                head.next = prev
                prev = head
                head = nextNode
            return prev

        head = reverse(head)

        curr = head
        carry = 1

        dummy = Node(0)
        node = dummy

        while curr or carry:
            val = curr.data if curr else 0

            currVal = val + carry

            carry = currVal // 10
            digit = currVal % 10

            node.next = Node(digit)
            node = node.next

            if curr:
                curr = curr.next

        return reverse(dummy.next)
