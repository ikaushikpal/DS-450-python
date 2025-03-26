# You are given a tree rooted at node 1. The tree is given in form of an array P where Pi denotes the parent of node i, Also P1 = -1, as node 1 is the root node. Every node i has a value Ai associated with it. At first, you have to choose any node to start with, after that from a node you can go to any of its child nodes. You've to keep moving to a child node until you reach a leaf node. Every time you get to a new node, you write its value. Let us assume that the integer sequence in your path is B.
# Let us define a function f over B, which is defined as follows:
# f(B) = B1 - B2 + B3 - B4 + B5.... + (-1)(k-1)Bk.
# You have to find the maximum possible value of f(B).


# Example 1:
# Input:
# N = 3,
# A = { 1, 2, 3}
# P = {-1, 1, 1}
# Output:
# 3
# Explanation:
# The resulting tree is:
#         1(1)
#       /     \
#      2(2)   3(3)
# If we choose our starting node as 3, then the
# resulting sequence will be B = { 3 },
# which will give the maximum possible value.


# Example 2:
# Input:
# N = 3,
# A = { 3, 1, 2}
# P = {-1, 1, 2}
# Output:
# 4
# Explanation:
# The resulting tree is:
#   1(3)
#   |
#   2(1)
#   |
#   3(2)
# If we choose our starting node as 1, then the
# resulting sequence will be B = { 3 , 1 , 2 }.
# The value which we'll get is, 3-1+2 = 4, which
# is the maximum possible value.


from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.child = []


class Solution:
    def buildTree(self, A, P):
        N = len(A)
        treeMap = {}
        root = None
        
        for i in range(N):
            val = A[i]
            parent = P[i]
            node = TreeNode(val)

            if parent == -1:
                root = node
            else:
                treeMap[parent - 1].child.append(node)
            treeMap[i] = node
        return root
    
    def dfs(self, root):
        if len(root.child) == 0:
            self.ans = max(self.ans, root.val)
            return (root.val, -root.val)
        
        include = exclude = float('-inf')
        for child in root.child:
            res = self.dfs(child)
            include = max(include, res[1])
            exclude = max(exclude, res[0])
        
        include += root.val
        exclude -= root.val
        
        self.ans = max(self.ans, include)
        return (include, exclude)
        
    def bestNode(self, N : int, A : List[int], P : List[int]) -> int:
        root = self.buildTree(A, P)
        
        self.ans = float('-inf')
        self.dfs(root)
        return self.ans
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.bestNode(4, [16, -20, 3, -13], [-1, 1, 1, 1]))