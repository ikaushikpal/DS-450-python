# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

# Example 1:
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]


# Example 2:
# Input: root = []
# Output: []


# Example 3:
# Input: root = [0]
# Output: [0]


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def dfs(self, root):
        if root is None:
            return
        
        originalLeft, originalRight = root.left, root.right
        self.tail.right = root
        self.tail = root
        self.tail.left = None
        
        self.dfs(originalLeft)
        self.dfs(originalRight)
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.head = self.tail = TreeNode()
        self.dfs(root)
        return self.head.right
# Time Complexity: O(N)
# Space Complexity: O(H)

    # Diff approach
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if root is None:
            return None, None

        left = self.flatten(root.left)
        right = self.flatten(root.right)

        head = tail = root
        root.left = None
        
        if left[0]:
            tail.right = left[0]
            tail = left[1]
        
        if right[0]:
            tail.right = right[0]
            tail = right[1]
        
        return head, tail
# Time Complexity: O(N)
# Space Complexity: O(H)
        