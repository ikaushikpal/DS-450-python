class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    # Return the Kth smallest element in the given BST 
    def KthSmallestElement_Util(self, root, K):
        if root:
            self.KthSmallestElement_Util(root.left, K)

            self.count += 1
            if self.count == K:
                self.ans = root.data

            self.KthSmallestElement_Util(root.right, K)

    def KthSmallestElement(self, root, K): 
        self.count = 0
        self.ans = -1

        self.KthSmallestElement_Util(root, K)

        return self.ans

