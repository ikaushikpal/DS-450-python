# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    def binaryTreeToBST_Util(self, root):
        if root is None:
            return
        
        self.binaryTreeToBST_Util(root.left)

        self.values.append(root.data)
        self.nodesAddress.append(root)

        self.binaryTreeToBST_Util(root.right)


    def binaryTreeToBST(self, root):
        self.values = []
        self.nodesAddress = []

        self.binaryTreeToBST_Util(root)
        self.values.sort()

        for i in range(len(self.values)):
            node = self.nodesAddress[i]

            node.data = self.values[i]

        return root