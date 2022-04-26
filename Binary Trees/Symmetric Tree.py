# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true


# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetricUtil(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        
        elif (root1 and root2 is None) or (root1 is None and root2):
            return False
        
        elif root1.val != root2.val:
            return False

        return self.isSymmetricUtil(root1.left, root2.right) & self.isSymmetricUtil(root1.right, root2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSymmetricUtil(root.left, root.right)