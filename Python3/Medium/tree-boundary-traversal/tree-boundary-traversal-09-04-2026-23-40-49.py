'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []

        ans = []

        def isLeaf(node):
            return node.left is None and node.right is None

        # Root
        if not isLeaf(root):
            ans.append(root.data)

        # Left boundary
        curr = root.left

        while curr:
            if not isLeaf(curr):
                ans.append(curr.data)

            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

        # Leaf nodes
        def addLeaves(node):
            if not node:
                return

            if isLeaf(node):
                ans.append(node.data)
                return

            addLeaves(node.left)
            addLeaves(node.right)

        addLeaves(root)

        # Right boundary
        curr = root.right
        temp = []

        while curr:
            if not isLeaf(curr):
                temp.append(curr.data)

            if curr.right:
                curr = curr.right
            else:
                curr = curr.left

        # Reverse right boundary
        ans.extend(temp[::-1])

        return ans