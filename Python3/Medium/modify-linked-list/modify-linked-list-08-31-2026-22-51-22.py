''' Node Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def modifyTheList(self, head):
        
        if not head or not head.next:
            return head
        
        # Find middle
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # For odd length:
        # slow = middle
        # second half starts at slow.next
        #
        # For even length:
        # slow = last node of first half
        # second half starts at slow.next
        
        second = slow.next
        slow.next = None
        
        # Reverse second half
        prev = None
        curr = second
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # prev points to last node
        # Pair first half with reversed second half
        left = head
        right = prev
        
        while left and right:
            old_left = left.data
        
            left.data = right.data - old_left
            right.data = old_left
        
            left = left.next
            right = right.next
        
        # Restore second half
        curr = prev
        prev_restore = None
        
        while curr:
            nxt = curr.next
            curr.next = prev_restore
            prev_restore = curr
            curr = nxt
        
        # Connect halves
        slow.next = prev_restore
        
        return head