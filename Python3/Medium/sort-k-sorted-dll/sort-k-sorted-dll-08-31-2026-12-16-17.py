import heapq

''' Structure of a Node of the Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''
class Solution:
    def sortKSortedDLL(self, head, k):

        if not head:
            return head

        heap = []
        curr = head
        count = 0

        # Put first k+1 nodes into heap
        for _ in range(k + 1):
            if curr:
                heapq.heappush(heap, (curr.data, count, curr))
                count += 1
                curr = curr.next

        newHead = None
        tail = None

        while heap:

            # Get smallest node
            _, _, node = heapq.heappop(heap)

            # Add node to result
            if newHead is None:
                newHead = node
                tail = node
                tail.prev = None
            else:
                tail.next = node
                node.prev = tail
                tail = node

            # Add next node
            if curr:
                heapq.heappush(heap, (curr.data, count, curr))
                count += 1
                curr = curr.next

        # End of DLL
        tail.next = None

        return newHead
        
        
        