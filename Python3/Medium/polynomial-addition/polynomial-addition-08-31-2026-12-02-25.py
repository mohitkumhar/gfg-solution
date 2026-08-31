# node class of the linked list
# class Node:
#     def __init__(self, c, p):
#         self.coeff = c
#         self.pow = p
#         self.next = None

class Solution:
    def addPolynomial(self, head1, head2):

        dummy = Node(0, 0)
        temp = dummy

        p1 = head1
        p2 = head2

        while p1 and p2:
            if p1.pow == p2.pow:

                coeff = p1.coeff + p2.coeff

                if coeff != 0:
                    temp.next = Node(coeff, p1.pow)
                    temp = temp.next

                p1 = p1.next
                p2 = p2.next

            elif p1.pow > p2.pow:
                temp.next = Node(p1.coeff, p1.pow)
                temp = temp.next

                p1 = p1.next

            else:
                temp.next = Node(p2.coeff, p2.pow)
                temp = temp.next

                p2 = p2.next

        while p1:
            temp.next = Node(p1.coeff, p1.pow)
            temp = temp.next

            p1 = p1.next

        while p2:
            temp.next = Node(p2.coeff, p2.pow)
            temp = temp.next

            p2 = p2.next

        return dummy.next
