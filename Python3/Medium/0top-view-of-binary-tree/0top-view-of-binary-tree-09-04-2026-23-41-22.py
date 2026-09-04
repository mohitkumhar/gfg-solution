'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        if not root:
            return []

        from collections import deque

        q = deque([(root, 0)])
        mp = {}

        while q:
            node, hd = q.popleft()

            # First node at this horizontal distance
            if hd not in mp:
                mp[hd] = node.data

            if node.left:
                q.append((node.left, hd - 1))

            if node.right:
                q.append((node.right, hd + 1))

        # Leftmost to rightmost
        return [mp[hd] for hd in sorted(mp)]