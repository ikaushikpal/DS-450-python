# Given a binary tree. The task is to find the maximum GCD of the siblings of this tree. You have to return the value of the node whose two immediate children has the maximum gcd.
# If there are multiple such nodes, return the node which has the maximum value.

# Siblings: Nodes with the same parent are called siblings.

# GCD (Greatest Common Divisor) of two positive integers is the largest positive integer that divides both numbers without a remainder.

# Note:
# Return 0 if input tree is empty i.e level of tree is -1.
# Consider those nodes which have a sibling.
# Return 0 if no such pair of siblings found.
 

# Example 1:
# Input:
#               4
#             /   \
#            5     2
#                 /  \
#                3    1
#               /  \
#              6   12

# Output: 3
# Explanation: For the above tree, the maximum
# GCD for the siblings is formed for nodes 6 and 12
# for the children of node 3.
 

# Example 2:
# Input: 
#             1
#           /   \
#         3      5
#       /  \    /  \
#      6    9  4    8

# Output: 5
# Explanation: For the above tree, the maximum
# GCD for the siblings is formed for nodes 4 and 8
# for the children of node 5.



# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.data)

class Solution:
    def gcd(self, x, y):
        if x == 0:
            return y
        return self.gcd(y%x, x)
        
    def dfs(self, root):
        if not root:
            return
        
        if root.left and root.right:
            temp = self.gcd(root.left.data, root.right.data)
            
            if temp > self.maxGcd:
                self.maxGcd = temp
                self.nodeVal = root.data
                
            elif temp == self.maxGcd:
                self.nodeVal = max(self.nodeVal, root.data)
            
        self.dfs(root.left)
        self.dfs(root.right)
        
    def maxGCD(self, root):
        if not root:
            return 0
        
        self.maxGcd, self.nodeVal = float('-inf'), 0
        self.dfs(root)
        return self.nodeVal
# Time Complexity: O(NlogN)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    root = Node(1)
    root.left = Node(3)
    root.right = Node(5)
    root.left.left = Node(6)
    root.left.right = Node(9)
    root.right.left = Node(4)
    root.right.right = Node(8)
    print(sol.maxGCD(root))