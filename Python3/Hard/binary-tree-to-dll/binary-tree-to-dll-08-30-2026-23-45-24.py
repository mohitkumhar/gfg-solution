''' Structure for tree and linked list
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
'''
class Solution:
    def treeToDLL(self, root):

        head = None
        prev = None

        def inorder(node):
            nonlocal head, prev

            if not node:
                return None

            inorder(node.left)

            if not head:
                head = node
            else:
                prev.right = node
                node.left = prev

            prev = node

            inorder(node.right)

        inorder(root)

        if prev:
            prev.right = None

        return head
