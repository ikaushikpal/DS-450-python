from collections import deque
from itertools import product
from functools import lru_cache
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    @lru_cache(None)
    def generateTreesUtil(self, low, high):
        if low > high:
            return deque([None])
        
        elif low == high:
            return deque([TreeNode(low)])
        
        res = deque()
        
        for i in range(low, high+1):
            left = self.generateTreesUtil(low, i-1)
            right = self.generateTreesUtil(i+1, high)
            
            for l,r in product(left, right):
                res.append(TreeNode(i, l, r))
            
        return res
    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generateTreesUtil(1, n)