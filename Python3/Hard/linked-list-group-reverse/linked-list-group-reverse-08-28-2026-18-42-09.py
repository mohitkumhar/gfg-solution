""" Structure of linked list Node
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    def reverseKGroup(self, head, k):
        if not head or not head.next or k <= 1:
            return head

        curr = head
        newHead = None
        tail = None

        while curr:
            groupHead = curr
            prev = None
            nextNode = None
            count = 0

            while curr and count < k:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
                count += 1

            if not newHead:
                newHead = prev

            if tail:
                tail.next = prev

            tail = groupHead

        return newHead
