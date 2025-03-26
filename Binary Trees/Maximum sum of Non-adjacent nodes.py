# Given a binary tree with a value associated with each node, we need to choose a subset of these nodes such that sum of chosen nodes is maximum under a constraint that no two chosen node in subset should be directly connected that is, if we have taken a node in our sum then we can’t take its any children or parents in consideration and vice versa.

                                        
# Example 1:
# Input:
#      11
#     /  \
#    1    2
# Output: 11
# Explanation: The maximum sum is sum of
# node 11.


# Example 2:
# Input:
#         1
#       /   \
#      2     3
#     /     /  \
#    4     5    6
# Output: 16
# Explanation: The maximum sum is sum of
# nodes 1 4 5 6 , i.e 16. These nodes are
# non adjacent.

# NOTE:
# all the nodes' values are in the range [0, 10^9].
# Exactly same problem as Clever Thief


'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to return the maximum sum of non-adjacent nodes.
    
    def dfs(self, root):
        if root is None:
            # (include_root, exclude_root)
            return 0, 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        # left.exclusion +  right.exclusion + root's value
        inclusion = left[1] + right[1] + root.data

        # max(left's inclusion and exclusion) + max(right's inclusion and exclusion)
        exclusion = max(left) + max(right)

        return (inclusion, exclusion)

    def getMaxSum(self, root) -> int:
        return max(self.dfs(root))
 