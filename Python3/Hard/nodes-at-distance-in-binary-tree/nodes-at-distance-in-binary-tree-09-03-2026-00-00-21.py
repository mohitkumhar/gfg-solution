'''
Structure of Binary Tree Node
 class Node:
     def __init__(self, val):
         self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def kDistanceNodes(self, root, target, k):
        # Store parent of every node
        parent = {}

        target_node = None

        def build_parent(node, par):
            nonlocal target_node

            if node is None:
                return

            if node.data == target:
                target_node = node

            if par:
                parent[node] = par

            build_parent(node.left, node)
            build_parent(node.right, node)

        build_parent(root, None)

        # BFS from target
        q = deque([(target_node, 0)])
        visited = {target_node}

        ans = []

        while q:
            node, dist = q.popleft()

            if dist == k:
                ans.append(node.data)
                continue

            # Left child
            if node.left and node.left not in visited:
                visited.add(node.left)
                q.append((node.left, dist + 1))

            # Right child
            if node.right and node.right not in visited:
                visited.add(node.right)
                q.append((node.right, dist + 1))

            # Parent
            if node in parent and parent[node] not in visited:
                visited.add(parent[node])
                q.append((parent[node], dist + 1))

        return sorted(ans)