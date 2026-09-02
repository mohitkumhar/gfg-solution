# A binary tree node
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def findDist(self, root, a, b):
        # code here

        def lca(root, a, b):
            if root is None:
                return None

            if root.data == a or root.data == b:
                return root

            left = lca(root.left, a, b)
            right = lca(root.right, a, b)

            if left and right:
                return root

            return left if left else right

        def distance(root, target, dist):
            if root is None:
                return -1

            if root.data == target:
                return dist

            left = distance(root.left, target, dist + 1)

            if left != -1:
                return left

            return distance(root.right, target, dist + 1)

        common = lca(root, a, b)

        dist_a = distance(common, a, 0)
        dist_b = distance(common, b, 0)

        return dist_a + dist_b