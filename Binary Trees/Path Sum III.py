# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

# Example 1:
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.


# Example 2:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root, currentSum, target):
        if root is None:
            return 0
        currentSum += root.val
        oldSum = currentSum - target
        self.ans += self.seen.get(oldSum, 0)
        self.seen[currentSum] = self.seen.get(currentSum, 0) + 1
        self.dfs(root.left, currentSum, target)
        self.dfs(root.right, currentSum, target)
        self.seen[currentSum] -= 1
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # approach
        # do preorder traversal
        # while doing so, keep track of the current sum
        # oldSum is the sum of the current sum minus the target sum
        # in other words oldSum is reqSum
        # then simple add freq[reqSum] to ans
        # then add 1 to freq[reqSum]
        # then do left and right subtrees
        # then subtract 1 from freq[reqSum]
        # why this is most important line. Because for a value it its freq will be > 0
        # only when it is in the same subtree
        # when we will do different branch then it will be 0 
        self.seen = {0:1}
        self.ans = 0
        self.dfs(root, 0, targetSum)
        
        return self.ans
# Time Complexity: O(N)
# N is the number of nodes in the tree.
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)
    print(sol.pathSum(root, 8))