class Solution:
    def subLinkedList(self, head1, head2):
    
        def removeLeadingZeros(head):
            while head and head.data == 0 and head.next:
                head = head.next
            return head
    
        def length(head):
            count = 0
            curr = head
            while curr:
                count += 1
                curr = curr.next
            return count
    
        def greater(a, b):
            # Compare two numbers represented by linked lists
            len1 = length(a)
            len2 = length(b)
    
            if len1 != len2:
                return len1 > len2
    
            while a and b:
                if a.data != b.data:
                    return a.data > b.data
                a = a.next
                b = b.next
    
            return True
    
        def reverse(head):
            prev = None
            curr = head
    
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
    
            return prev
    
        # Remove leading zeros first
        head1 = removeLeadingZeros(head1)
        head2 = removeLeadingZeros(head2)
    
        # Make sure head1 >= head2
        if not greater(head1, head2):
            head1, head2 = head2, head1
    
        # Reverse both lists
        head1 = reverse(head1)
        head2 = reverse(head2)
    
        borrow = 0
        dummy = Node(0)
        tail = dummy
    
        p = head1
        q = head2
    
        while p:
            a = p.data
            b = q.data if q else 0
    
            diff = a - b - borrow
    
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
    
            tail.next = Node(diff)
            tail = tail.next
    
            p = p.next
            if q:
                q = q.next
    
        # Reverse result
        result = reverse(dummy.next)
    
        # Remove leading zeros
        result = removeLeadingZeros(result)
    
        return result