from collections import deque
'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        if not root:
            return []

        q = deque([(root, 0)])
        mp = {}

        while q:
            node, hd = q.popleft()

            # Always update
            mp[hd] = node.data

            if node.left:
                q.append((node.left, hd - 1))

            if node.right:
                q.append((node.right, hd + 1))

        # Leftmost to rightmost
        return [mp[hd] for hd in sorted(mp)]