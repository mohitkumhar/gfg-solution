''' Structure of a Linked List Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def sortLL(self, head):
        if head is None or head.next is None:
            return head

        def findMid(head):
            slow = head
            fast = head

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def merge(head1, head2):

            dummy = Node(0)
            temp = dummy

            while head1 and head2:
                if head1.data < head2.data:
                    temp.next = head1
                    head1 = head1.next
                else:
                    temp.next = head2
                    head2 = head2.next
                temp = temp.next

            while head1:
                temp.next = head1
                head1 = head1.next
                temp = temp.next

            while head2:
                temp.next = head2
                head2 = head2.next
                temp = temp.next

            temp = None

            return dummy.next

        mid = findMid(head)

        left = head
        right = mid.next

        mid.next = None

        left = self.sortLL(left)
        right = self.sortLL(right)

        return merge(left, right)
