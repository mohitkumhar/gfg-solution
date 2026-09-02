''' Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def serialize(self, root):

        if root is None:
            return []

        ans = []
        q = deque([root])

        while q:
            node = q.popleft()

            if node is None:
                ans.append(None)
                continue

            ans.append(node.data)

            q.append(node.left)
            q.append(node.right)

        return ans

    def deSerialize(self, arr):
        if not arr:
            return None

        root = Node(arr[0])
        q = deque([root])

        i = 1

        while q and i < len(arr):

            node = q.popleft()

            # Left child
            if arr[i] is not None:
                node.left = Node(arr[i])
                q.append(node.left)

            i += 1

            # Right child
            if i < len(arr) and arr[i] is not None:
                node.right = Node(arr[i])
                q.append(node.right)

            i += 1

        return root
