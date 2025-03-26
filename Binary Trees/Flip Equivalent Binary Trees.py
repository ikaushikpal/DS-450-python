# For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

# A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

# Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

 

# Example 1:
# Flipped Trees Diagram
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
# Explanation: We flipped at nodes with values 1, 3, and 5.


# Example 2:
# Input: root1 = [], root2 = []
# Output: true


# Example 3:
# Input: root1 = [], root2 = [1]
# Output: false


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        
        if root1 is None or root2 is None:
            return False
        
        if root1.val != root2.val:
            return False
        
        if self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right):
            return True
        
        if self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right):
            return True
        return False
# Worst case is perfect binary search tree (all same values except one leaf in one of the tree), so h = logN.
# 4 subproblem at each height, so time = 4^(h) = 4^(logN) (h=logN in worst case since worst case is perfect binary search tree) = 2^(2logN) = 2^(logN^2) = N^2.
# However, we are told that the numbers are unique so half of the recursive calls would fail, which makes time complexity
# 2 subproblem at each height, so time = 2^h = 2^logN = N.

# Space: O(h) (O(N) in the worst case of skewed trees!)