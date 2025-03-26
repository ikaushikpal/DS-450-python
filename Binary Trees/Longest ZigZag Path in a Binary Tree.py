class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZagUtil(self, root, prevMove, count):
        # if prevMove = 0 meaning from its parent its left called
        # if prevMove = 1 meaning from its parent its right called
        # count nodes in current path
        if root is None:
            self.countMaxNodes = max(self.countMaxNodes, count)
            return

        if prevMove == 0:
            self.longestZigZagUtil(root.right, 1, count+1)
            self.longestZigZagUtil(root.left, 0, 1)
        
        elif prevMove == 1:
            self.longestZigZagUtil(root.left, 0, count+1)
            self.longestZigZagUtil(root.right, 1, 1)


    def longestZigZag(self, root) -> int:
        self.countMaxNodes = 0
        self.longestZigZagUtil(root, 0, 0)
        left = self.countMaxNodes

        self.countMaxNodes = 0
        self.longestZigZagUtil(root, 1, 0)
        right = self.countMaxNodes

        return max(left, right) - 1
        