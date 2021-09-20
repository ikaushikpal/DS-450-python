
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def toSumTreeUtil(self, root, total):
        if root is None:
            return 0

        total_left = self.toSumTreeUtil(root.left, total)
        total_right = self.toSumTreeUtil(root.right, total)

        total = total_left + total_right + root.data
        root.data = total_left + total_right

        return total


    def toSumTree(self, root):
        self.toSumTreeUtil(root, 0)
        return root
