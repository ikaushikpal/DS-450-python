# Given a Binary Tree. Check whether all of its nodes have the value equal to the sum of their child nodes.


# Example 1:

# Input:
#      10
#     /
#   10 
# Output: 1
# Explanation: Here, every node is sum of
# its left and right child.
# Example 2:

# Input:
#        1
#      /   \
#     4     3
#    /  \
#   5    N
# Output: 0
# Explanation: Here, 1 is the root node
# and 4, 3 are its child nodes. 4 + 3 =
# 7 which is not equal to the value of
# root node. Hence, this tree does not
# satisfy the given conditions.



'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        if root is None:
            return 1
        
        if not root.left and not root.right:
            return 1
            
        if self.isSumProperty(root.left) and self.isSumProperty(root.right):
            leftVal = root.left.data if root.left else 0
            rightVal = root.right.data if root.right else 0
            return int(leftVal+rightVal==root.data)
        else:
            return 0