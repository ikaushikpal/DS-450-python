# Input: 
#         4        
#        / \       
#       2   5      
#      / \ / \     
#     7  1 2  3    
#       /
#      6
# Output: 13
# Explanation:
#         4        
#        / \       
#       2   5      
#      / \ / \     
#     7  1 2  3 
#       /
#      6

# The highlighted nodes (4, 2, 1, 6) above are 
# part of the longest root to leaf path having
# sum = (4 + 2 + 1 + 6) = 13

class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None


class Solution:
    def sumOfLongRootToLeafPathUtil(self, root, height, total):
        if root is None:
            return

        height += 1
        total += root.data

        if root.left is None and root.right is None: # leaf node

            if height > self.maxHeight:
                self.maxHeight = height
                self.total = total

            elif height == self.maxHeight:
                self.total = max(self.total, total)

        self.sumOfLongRootToLeafPathUtil(root.left, height, total)
        self.sumOfLongRootToLeafPathUtil(root.right, height, total)

        
    def sumOfLongRootToLeafPath(self, root):
        self.maxHeight = -1
        self.total = float('-inf')
        self.sumOfLongRootToLeafPathUtil(root, 0, 0)

        return self.total