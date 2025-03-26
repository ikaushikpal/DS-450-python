# Given a binary tree in which each node element contains a number. Find the maximum possible path sum from one leaf node to another leaf node.

# Note: Here Leaf node is a node which is connected to exactly one different node.


# Example 1:
# Input:      
#            3                               
#          /    \                          
#        4       5                     
#       /  \      
#     -10   4                          
# Output: 16
# Explanation:
# Maximum Sum lies between leaf node 4 and 5.
# 4 + 4 + 3 + 5 = 16.


# Example 2:
# Input:    
#             -15                               
#          /      \                          
#         5         6                      
#       /  \       / \
#     -8    1     3   9
#    /  \              \
#   2   -3              0
#                      / \
#                     4  -1
#                        /
#                      10  
# Output:  27
# Explanation:
# The maximum possible sum from one leaf node 
# to another is (3 + 6 + 9 + 0 + -1 + 10 = 27)




'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    def dfs(self, root, mainRoot):
        if root is None:
            return -100_000_000
        
        if not root.left and not root.right:
            return root.data
            
        left = self.dfs(root.left, mainRoot)
        right = self.dfs(root.right, mainRoot)
        
        if left != -100_000_000 and right != -100_000_000:
            self.maxSum = max(self.maxSum, left + right + root.data)
        
        if not root.left and root.right and root == mainRoot:
            self.maxSum = max(self.maxSum, right + root.data)
        
        if root.left and not root.right and root == mainRoot:
            self.maxSum = max(self.maxSum, left + root.data)
            
        return max(left, right) + root.data
        
    def maxPathSum(self, root):
        self.maxSum = float('-inf')
        self.dfs(root, root)
        return self.maxSum
# Time Complexity: O(n)
# Space Complexity: O(h)