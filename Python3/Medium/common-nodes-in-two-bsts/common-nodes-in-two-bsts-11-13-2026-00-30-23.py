'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        stack1 = []
        stack2 = []

        ans = []

        while True:

            # Push all left nodes of BST 1
            while r1:
                stack1.append(r1)
                r1 = r1.left

            # Push all left nodes of BST 2
            while r2:
                stack2.append(r2)
                r2 = r2.left

            # If either stack is empty, traversal is complete
            if not stack1 or not stack2:
                break

            node1 = stack1[-1]
            node2 = stack2[-1]

            if node1.data == node2.data:
                ans.append(node1.data)

                r1 = stack1.pop().right
                r2 = stack2.pop().right

            elif node1.data < node2.data:
                r1 = stack1.pop().right

            else:
                r2 = stack2.pop().right

        return ans
