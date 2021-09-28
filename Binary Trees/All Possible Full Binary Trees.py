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
    def allPossibleFBTUtil(self, n):
        if n == 1:
            return deque([TreeNode(0)])  
        
        res = deque()
        
        if n in self.memo:
            return self.memo[n]
        
        for i in range(1, n, 2):
            left = self.allPossibleFBTUtil(i)
            right = self.allPossibleFBTUtil(n-i-1)
            
            for l,r in product(left, right):
                res.append(TreeNode(0, l, r))
        
        self.memo[n] = res
        return res
    
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        self.memo = {}
        return self.allPossibleFBTUtil(n)