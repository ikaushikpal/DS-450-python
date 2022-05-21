# Given a binary tree. The task is to check whether the given tree follows the max heap property or not.
# Note: Properties of a tree to be a max heap - Completeness and Value of node greater than or equal to its child.


# Example 1:
# Input:
#       5
#     /  \
#    2    3
# Output: 1
# Explanation: The given tree follows max-heap property since 5,
# is root and it is greater than both its children.


# Example 2:
# Input:
#        10
#      /   \
#     20   30 
#   /   \
#  40   60
# Output: 0


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
    
    def maxHeapProp(self, root):
        if root is None:
            return float('-inf')
        
        if not self.complete:
            return float('inf')
            
        left = self.maxHeapProp(root.left)
        right = self.maxHeapProp(root.right)
        
        if root.data < max(left, right):
            self.complete = False
        
        return max(root.data, left, right)
        
    def isHeap(self, root):
        totalNodes = self.countNodes(root)
        if not self.isComplete(root, 1, totalNodes):
            return False
        
        self.complete = True
        self.maxHeapProp(root)
        return self.complete
        
# Time Complexity : O(N)
# Space Complexity : O(N)
