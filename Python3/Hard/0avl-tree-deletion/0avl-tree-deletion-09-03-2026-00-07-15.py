''' Structure of AVL Tree Node
class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

'''
class Solution:
    def deleteNode(self,root, key):
        # Step 1: Normal BST deletion
        if root is None:
            return None

        if key < root.data:
            root.left = self.deleteNode(root.left, key)

        elif key > root.data:
            root.right = self.deleteNode(root.right, key)

        else:
            # No left child
            if root.left is None:
                return root.right

            # No right child
            if root.right is None:
                return root.left

            # Two children
            # Find inorder successor
            temp = root.right

            while temp.left:
                temp = temp.left

            root.data = temp.data

            root.right = self.deleteNode(root.right, temp.data)


        # Step 2: Update height
        root.height = 1 + max(
            self.height(root.left),
            self.height(root.right)
        )


        # Step 3: Get balance factor
        balance = self.height(root.left) - self.height(root.right)


        # Step 4: Rebalance

        # LL Case
        if balance > 1:
            if self.height(root.left.left) >= self.height(root.left.right):
                return self.rightRotate(root)

            # LR Case
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)


        # RR Case
        if balance < -1:
            if self.height(root.right.right) >= self.height(root.right.left):
                return self.leftRotate(root)

            # RL Case
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root


    def height(self, node):
        if node is None:
            return 0

        return node.height


    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(
            self.height(y.left),
            self.height(y.right)
        )

        x.height = 1 + max(
            self.height(x.left),
            self.height(x.right)
        )

        return x


    def leftRotate(self, x):
        y = x.right
        T2 = y.left

        x.right = T2
        y.left = x

        # Update heights
        x.height = 1 + max(
            self.height(x.left),
            self.height(x.right)
        )

        y.height = 1 + max(
            self.height(y.left),
            self.height(y.right)
        )

        return y