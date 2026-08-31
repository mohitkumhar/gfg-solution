# Structure of linked list Node
# class Node:
#   def __init__(self, x):
#       self.data = x
#       self.next = None

class Solution:
    def partition(self, head, x):

        lessHead = lessTail = None
        equalHead = equalTail = None
        highHead = highTail = None

        curr = head

        while curr:
            nn = curr.next
            curr.next = None

            if curr.data < x:
                if not lessHead:
                    lessHead = curr
                    lessTail = curr
                else:
                    lessTail.next = curr
                    lessTail = lessTail.next

            elif curr.data == x:
                if not equalHead:
                    equalHead = curr
                    equalTail = curr
                else:
                    equalTail.next = curr
                    equalTail = equalTail.next

            elif curr.data > x:
                if not highHead:
                    highHead = curr
                    highTail = curr
                else:
                    highTail.next = curr
                    highTail = highTail.next

            curr = nn

        if lessTail:
            if equalHead:
                lessTail.next = equalHead
            else:
                lessTail.next = highHead
            
        if equalTail:
            equalTail.next = highHead

        if lessHead:
            return lessHead
        elif equalHead:
            return equalHead
        return highHead
