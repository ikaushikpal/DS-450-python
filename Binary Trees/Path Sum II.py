from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root, currentPath, currentSum, targetSum):
        if root is None:
            return

        currentPath.append(root.val)
        currentSum += root.val

        if not root.left and not root.right: # leaf node
            if currentSum == targetSum:
                self.ans.append(currentPath.copy())

        else:
            self.dfs(root.left, currentPath, currentSum, targetSum)
            self.dfs(root.right, currentPath, currentSum, targetSum)

        currentPath.pop()
        

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:        
        self.ans = []
        self.dfs(root, [], 0, targetSum)

        return self.ans
