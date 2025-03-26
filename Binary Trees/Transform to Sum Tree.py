# Given a Binary Tree of size N , where each node can have positive or negative values. Convert this to a tree where value of each node will be the sum of the values of all the nodes in left and right sub trees of the original tree. The values of leaf nodes are changed to 0.
# Note: You have to modify the given tree in-place.


# Example 1:


# Input:
#              10
#           /      \
#         -2        6
#        /   \     /  \
#       8    -4   7    5


# Output:
#             20
#           /     \
#         4        12
#        /  \     /  \
#      0     0   0    0


# Explanation:
#            (4-2+12+6)
#           /           \
#       (8-4)          (7+5)
#        /   \         /  \
#       0     0       0    0



# Example 2:

# Input:
#             10
#         /        \
#       -2           6
#      /   \        /  \
#     8    -4      7     5
#     / \   / \    / \   / \
#   2  -2 3  -5  9  -8 2   8


# Output:
#             29
#         /        \
#        2          23
#      /  \        /  \
#     0   -2      1    10
#    / \  / \    / \   / \
#    0  0 0   0  0   0 0   0


# Explanation:
#                  (-2+6+8-4+7+5+2-2+3-5+9-8+2+8)
#                /                                \
#           (8-4+2-2+3-5)                    (7+5+9-8+2+8)
#           /      \                            /      \       
#        (2-2)   (3-5)                        (9-8)    (2+8)
#         /     \  /    \                      /     \   /     \
#        0      0 0      0                   0        0 0       0



class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def toSumTree(self, root) :
        if not root:
            return 0
        
        leftVal = rightVal = 0
        temp = root.data

        leftVal += self.toSumTree(root.left)
        rightVal += self.toSumTree(root.right)
        
        if root.left:
            leftVal += root.left.data
        
        if root.right:
            rightVal += root.right.data
            
        root.data = leftVal + rightVal
        return temp
# Time Complexity: O(n)
# Space Complexity: O(n)
