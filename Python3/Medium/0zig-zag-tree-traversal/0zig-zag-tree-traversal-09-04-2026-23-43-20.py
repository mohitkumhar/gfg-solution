from collections import deque
''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def zigZagTraversal(self, root):

        if not root:
            return []

        q = deque([root])
        ans = []
        left_to_right = True

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.data)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if not left_to_right:
                level.reverse()

            ans.extend(level)

            left_to_right = not left_to_right

        return ans
