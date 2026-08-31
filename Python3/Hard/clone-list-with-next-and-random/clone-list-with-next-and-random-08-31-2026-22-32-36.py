''' Structure of Linked List Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None
'''        

class Solution:
    def cloneLinkedList(self, head):
        if not head:
            return None

        # Step 1: Create copy of every node
        # and insert it after the original node
        curr = head

        while curr:
            copy = Node(curr.data)

            copy.next = curr.next
            curr.next = copy

            curr = copy.next

        # Step 2: Set random pointers of copied nodes
        curr = head

        while curr:
            copy = curr.next

            if curr.random:
                copy.random = curr.random.next
            else:
                copy.random = None

            curr = copy.next

        # Step 3: Separate original and copied lists
        curr = head
        copyHead = head.next

        while curr:
            copy = curr.next

            # Restore original list
            curr.next = copy.next

            # Set copied list's next
            if copy.next:
                copy.next = copy.next.next

            curr = curr.next

        return copyHead