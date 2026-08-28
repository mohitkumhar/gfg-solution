''' Structure of a Linked List Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

'''
class Solution:
    def reverseBetween(self, a, b, head):

        def reverse(first, second):

            stop = second.next
            prev = None
            curr = first

            while curr != stop:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode

            return second, first

        count = 1
        startPrev = None
        curr = head

        while curr:
            if count == a:
                break
            startPrev = curr
            curr = curr.next
            count += 1

        first = curr

        curr = head
        count = 1
        while curr:
            if count == b:
                break

            curr = curr.next
            count += 1

        second = curr
        nextNode = curr.next

        newHead, newTail = reverse(first, second)

        if startPrev:
            startPrev.next = newHead
        else:
            head = newHead

        newTail.next = nextNode

        return head
