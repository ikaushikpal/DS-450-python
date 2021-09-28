from typing import Optional



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # -1000 <= Node.val <= 1000
        self.left = left
        self.right = right

# single node value can be solution 
# meaning it is not necessary that path must contain more than 1 node
# if need to contain minmum 1

class Solution:
    def maxPathSumUtil(self, root):
        if root is None:
            return 0
        
        left = self.maxPathSumUtil(root.left)
        right = self.maxPathSumUtil(root.right)

        temp = max(max(left, right)+root.val, root.val)
        ans = max(temp, left+right+root.val)
        
        self.maxSum = max(self.maxSum, ans)
        
        return temp

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.maxSum = float('-inf')
        self.maxPathSumUtil(root)

        return self.maxSum