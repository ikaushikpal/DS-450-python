# Given the root of a binary tree, determine if it is a complete binary tree.

# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 
# Example 1:
# Input: root = [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.


# Example 2:
# Input: root = [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def countNodes(self, root):
        if root is None:
            return 0

        return self.countNodes(root.left) + self.countNodes(root.right) + 1
    
    def isComplete(self, root, index, totalNodes):
        if root is None:
            return True
        
        if index > totalNodes:
            return False
        
        left = self.isComplete(root.left, index<<1, totalNodes)
        right = self.isComplete(root.right, (index<<1) + 1, totalNodes)
        return left & right

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # to solve this problem we are going to use binary tree property
        # if a node i then its left child would be 2i and right child 2i + 1
        # for array representation with start index from 1 
        # here only need to check if currentIndex is grater than totalNodes
        # if yes that means tree is not complete
        # Need to Satisfy the Conditions:
        # - every level except is fully filled
        # - every node must have left child if its having a right child

        totalNodes = self.countNodes(root)
        return self.isComplete(root, 1, totalNodes)