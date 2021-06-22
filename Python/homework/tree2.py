# Python3 program to check
# if a given tree is BST.
import math


# A binary tree node has data,
# pointer to left child and
# a pointer to right child
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBSTUtil(root, prev):
    # traverse the tree in inorder fashion
    # and keep track of prev node
    if root is not None:
        if isBSTUtil(root.left, prev):
            return False

        # Allows only distinct valued nodes
        if prev is not None and root.data <= prev.data:
            return False

        prev = root
        return isBSTUtil(root.right, prev)

    return True


def isBST(root):
    prev = None
    return isBSTUtil(root, prev)


# Driver Code
if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    #root.left.right.left = Node(9)

    if isBST(root) is not None:
        print("Not a BST")
    else:
        print("Is BST")

# This code is contributed by Srathore
