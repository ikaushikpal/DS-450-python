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
    def addOneRowUtil(self, root, depth, val):
        if depth == 1:
            return TreeNode(val, root)
        
        elif depth == 2:
            root.left = TreeNode(val, root.left)
            root.right = TreeNode(val, None, root.right)

        else:
            if root.left:
                self.addOneRowUtil(root.left, depth-1, val)
            
            if root.right:
                self.addOneRowUtil(root.right, depth-1, val)

        return root

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        return self.addOneRowUtil(root,depth, val)
        

if __name__ == '__main__':
#     Input: root = [4,2,6,3,1,5], val = 1, depth = 2
#       Output: [4,1,1,2,null,null,6,3,1,5]

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)

    Solution().addOneRow(root, 1, 2)
