from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def hasPathSumUtil(self, root, targetSum, currentSum):
        if root is None:
            return False
            
        if not root.left and not root.right:
            if currentSum + root.val == targetSum:
                return True
            else:
                return False
            
        left = self.hasPathSumUtil(root.left, targetSum, currentSum+root.val)
        right = self.hasPathSumUtil(root.right, targetSum, currentSum+root.val)
        
        return left|right
        

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        return self.hasPathSumUtil(root, targetSum, 0)