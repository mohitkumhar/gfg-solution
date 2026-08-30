''' Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def sort(self, head):

        ascendingHead = Node(0)
        decendingHead = Node(0)

        curr = head
        flag = True

        ass = ascendingHead
        des = decendingHead

        while curr:
            if flag:
                ass.next = Node(curr.data)
                ass = ass.next
                flag = False

            else:
                des.next = Node(curr.data)
                des = des.next
                flag = True

            curr = curr.next

        decendingHead = decendingHead.next

        prev = None
        while decendingHead:
            nextNode = decendingHead.next
            decendingHead.next = prev
            prev = decendingHead
            decendingHead = nextNode

        curr1 = ascendingHead.next
        curr2 = prev

        ans = Node(0)
        temp = ans

        while curr1 and curr2:
            if curr1.data < curr2.data:
                temp.next = Node(curr1.data)
                curr1 = curr1.next
            else:
                temp.next = Node(curr2.data)
                curr2 = curr2.next
            temp = temp.next

        while curr1:
            temp.next = Node(curr1.data)
            curr1 = curr1.next
            temp = temp.next

        while curr2:
            temp.next = Node(curr2.data)
            curr2 = curr2.next
            temp = temp.next

        return ans.next
