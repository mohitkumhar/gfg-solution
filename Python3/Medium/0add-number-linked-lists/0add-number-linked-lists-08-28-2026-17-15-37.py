'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def addTwoLists(self, head1, head2):

        def reverse(head):
            prev = None
            while head != None:
                nextNode = head.next
                head.next = prev
                prev = head
                head = nextNode

            return prev

        head1 = reverse(head1)
        head2 = reverse(head2)

        curr1 = head1
        curr2 = head2

        carry = 0

        dummy = Node(0)
        curr = dummy

        while curr1 != None or curr2 != None or carry:

            val1 = curr1.data if curr1 else 0
            val2 = curr2.data if curr2 else 0

            currVal = val1 + val2 + carry

            carry = currVal // 10
            digit = currVal % 10

            curr.next = Node(digit)
            curr = curr.next

            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next

        result = reverse(dummy.next)

        while result and result.next:
            if result.data != 0:
                break
            result = result.next

        return result
