from collections import deque
from itertools import product
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def cloneTree(self, root):
        if root is None:
            return None
        
        newRoot = TreeNode(root.val)
        newRoot.left = self.cloneTree(root.left)
        newRoot.right = self.cloneTree(root.right)
        return newRoot
    
    def dfs(self, n):
        if n <= 0 or n%2 == 0:
            return []
        
        if n == 1:
            return [TreeNode(0)]
        
        if n in self.memo:
            return self.memo[n]
        
        ans = []
        for i in range(1, n, 2):
            leftTree = self.dfs(i)
            rightTree = self.dfs(n - i - 1)
            
            
            for j in range(len(leftTree)):
                for k in range(len(rightTree)):
                    root = TreeNode(0)
                    
                    root.left = self.cloneTree(leftTree[j])
                    root.right = self.cloneTree(rightTree[k])
                    
                    ans.append(root)
        self.memo[n] = ans
        return ans
        
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        self.memo = {}
        return self.dfs(n)