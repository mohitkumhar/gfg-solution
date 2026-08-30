""" Linked List Node
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None
"""

class Solution:
    def sortList(self, head: 'Node | None' = None) -> 'Node | None':
        if head is None or head.next is None:
            return head

        def findMid(head):
            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def merge(head1, head2):

            dummy = Node(0)
            temp = dummy

            curr1 = head1
            curr2 = head2

            while curr1 and curr2:
                if curr1.data <= curr2.data:
                    temp.next = curr1
                    curr1 = curr1.next
                else:
                    temp.next = curr2
                    curr2 = curr2.next
                temp = temp.next

            while curr1:
                temp.next = curr1
                curr1 = curr1.next
                temp = temp.next

            while curr2:
                temp.next = curr2
                curr2 = curr2.next
                temp = temp.next

            return dummy.next

        mid = findMid(head)

        left = head
        right = mid.next

        mid.next = None

        left = self.sortList(left)
        right = self.sortList(right)

        return merge(left, right)
