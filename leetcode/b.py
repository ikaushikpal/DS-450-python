# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def postOrder(self, root):
        if root is None:
            return (0, 0)
        
        left = self.postOrder(root.left)
        right = self.postOrder(root.right)

        totalSum = left[0] + right[0] + root.val
        totalCount = left[1] + right[1] + 1
        
        if totalSum // totalCount:
            self.count += 1

        return (totalSum, totalCount)
        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.postOrder(root)
        return self.count