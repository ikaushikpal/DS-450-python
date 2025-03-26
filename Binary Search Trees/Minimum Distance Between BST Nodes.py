# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

# Example 1:
# Input: root = [4,2,6,1,3]
# Output: 1


# Example 2:
# Input: root = [1,0,48,null,null,12,49]
# Output: 1


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, root):
        if root is None:
            return
        
        self.inorder(root.left)
        self.ans = min(self.ans, root.val - self.prevMax)
        self.prevMax = root.val
        self.inorder(root.right)
        
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.ans, self.prevMax = float('inf'), float('-inf')
        self.inorder(root)
        return self.ans
# Time Complexity: O(N)
# Space Complexity: O(H)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDiffInBST([4,2,6,1,3]))
    print(sol.minDiffInBST([1,0,48,null,null,12,49]))
            