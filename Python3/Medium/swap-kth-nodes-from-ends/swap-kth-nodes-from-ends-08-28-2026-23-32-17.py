'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def swapKth(self, head, k):

        n = 0

        curr = head
        while curr:
            curr = curr.next
            n += 1

        if k > n:
            return head

        # both nodes are same
        if 2 * k - 1 == n:
            return head

        # kth node from beginning
        first = head
        for _ in range(k - 1):
            first = first.next

        # kth node from end
        second = head
        for _ in range(n - k):
            second = second.next

        first.data, second.data = second.data, first.data

        return head
