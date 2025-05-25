# Given a Binary Tree, you need to find all the possible paths from the root node to all the leaf nodes of the binary tree.

# Note: The paths should be returned such that paths from the left subtree of any node are listed first, followed by paths from the right subtree.

# Examples:

# Example 1:
# Input: root[] = [1, 2, 3, 4, 5]
# ex-3
# Output: [[1, 2, 4], [1, 2, 5], [1, 3]] 
# Explanation: All possible paths: 1->2->4, 1->2->5 and 1->3

# Example 2:
# Input: root[] = [1, 2, 3]
#        1
#     /     \
#    2       3
# Output: [[1, 2], [1, 3]] 
# Explanation: All possible paths: 1->2 and 1->3

# Example 3:
# Input: root[] = [10, 20, 30, 40, 60]
#          10
#        /    \
#       20    30
#      /  \
#     40   60
# Output: [[10, 20, 40], [10, 20, 60], [10, 30]]
# Explanation: All possible paths: 10->20 ->40, 10->20->60 and 10->30

# Constraints:
# 1<=number of nodes<=10^4
# 1<=node->data<=10^4



from typing import Optional
from collections import deque

from typing import List



"""
definition of binary tree node.
"""
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None



class Solution:
    def dfs(self, root, path):
        if root is None:
            return True
            
        path.append(root.data)
        
        left = self.dfs(root.left, path)
        right = self.dfs(root.right, path)
        
        
        if left and right:
            self.ans.append(path[:])
            
        path.pop()
        return False
        
        
    def Paths(self, root):
        self.ans = []
        self.dfs(root, [])
        return self.ans
        