class Solution:
    def kAltReverse(self, head, k):
    
        if not head or k <= 1:
            return head
    
        dummy = Node(0)
        dummy.next = head
    
        prevGrpTail = dummy
        curr = head
        reverseFlag = True
    
        while curr:
    
            # Find the last node of current group
            groupTail = curr
            count = 1
    
            while count < k and groupTail.next:
                groupTail = groupTail.next
                count += 1
    
            nextGroup = groupTail.next
    
            if reverseFlag:
                # Reverse current group
                prev = nextGroup
                node = curr
    
                while node != nextGroup:
                    nxt = node.next
                    node.next = prev
                    prev = node
                    node = nxt
    
                # Connect previous group to reversed group
                prevGrpTail.next = groupTail
    
                # Old head becomes tail
                prevGrpTail = curr
    
            else:
                # Don't reverse
                prevGrpTail = groupTail
    
            # Move to next group
            curr = nextGroup
    
            reverseFlag = not reverseFlag
    
        return dummy.next