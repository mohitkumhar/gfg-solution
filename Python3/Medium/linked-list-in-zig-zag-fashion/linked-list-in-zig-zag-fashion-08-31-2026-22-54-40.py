''' Structure of link list Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

'''
class Solution:
    def zigZag(self, head):

        if not head or not head.next:
            return head

        curr = head
        flag = True

        while curr.next:

            if flag:
                # curr <= curr.next
                if curr.data > curr.next.data:
                    curr.data, curr.next.data = curr.next.data, curr.data

            else:
                # curr >= curr.next
                if curr.data < curr.next.data:
                    curr.data, curr.next.data = curr.next.data, curr.data

            flag = not flag
            curr = curr.next

        return head
