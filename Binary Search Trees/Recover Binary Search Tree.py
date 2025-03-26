# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

# Example 1:
# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.



# Example 2:
# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def storeInorder(self, root, order):
        if root is None:
            return

        self.storeInorder(root.left, order)
        order.append(root.val)
        self.storeInorder(root.right, order)

    def sortOrder(self, order):
        for j in range(len(order)-1, -1, -1):
            if order[j-1] > order[j]:
                break
        
        for i in range(0, len(order), 1):
            if order[i] > order[i+1]:
                break

        order[i], order[j] = order[j], order[i]

    def rebuildTree(self, root, order):
        if root is None:
            return

        self.rebuildTree(root.left, order)
        root.val = order.pop()
        self.rebuildTree(root.right, order)
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        order = []
        self.storeInorder(root, order)
        self.sortOrder(order)
        self.rebuildTree(root, order[::-1])
# This method 
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution: 
    def inorder(self, root):
        if root is None:
            return
        
        self.inorder(root.left)
        if self.prevNode.val > root.val:
            # first violation of condition
            if self.firstNode is None:
                self.firstNode = self.prevNode
                self.middleNode = root
            
            # second violation of condition
            else:
                self.lastNode = root
        
        self.prevNode = root
        self.inorder(root.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.firstNode = self.middleNode = self.lastNode = None
        self.prevNode = TreeNode(float('-inf'))

        
        # when those two are adjacent in BST then there wil be only one
        # violation of BST property
        # thats why we need to store firstNode, middleNode
        # but if they not adjacent then second violation will be there
        # that time firstNode and lastNode 
        self.inorder(root)

        if self.firstNode and self.lastNode:
            self.firstNode.val, self.lastNode.val = self.lastNode.val, self.firstNode.val

        elif self.firstNode and self.middleNode:
            self.firstNode.val, self.middleNode.val = self.middleNode.val, self.firstNode.val
# Time Complexity: O(n)
# Space Complexity: O(1)        
        