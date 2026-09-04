''' Structure of binary tree Node 
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def diameter(self, root):

        diameter = 0

        def height(node):
            nonlocal diameter

            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            # Diameter through current node
            diameter = max(diameter, left + right)

            # Height of current node
            return 1 + max(left, right)

        height(root)

        return diameter
    