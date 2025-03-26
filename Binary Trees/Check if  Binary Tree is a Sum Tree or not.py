
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# your task is to complete this function
# function should return True is Tree is SumTree else return False
class Solution:
    def isSumTreeUtil(self, root):
        if self.IS_SUM_TREE == False:
            return 0

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.data

        total_left = self.isSumTreeUtil(root.left)
        total_right = self.isSumTreeUtil(root.right)

        total = total_left + total_right
        if root.data != total:
            self.IS_SUM_TREE = False

        return root.data + total
        
    def isSumTree(self, root)->bool:
        self.IS_SUM_TREE = True
        self.isSumTreeUtil(root)

        return self.IS_SUM_TREE