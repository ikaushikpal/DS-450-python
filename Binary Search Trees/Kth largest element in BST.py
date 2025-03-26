class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# return the Kth largest element in the given BST rooted at 'root'

class Solution:
    # Return the Kth smallest element in the given BST 
    def kthLargestUtil(self, root, K):
        if root:
            self.kthLargestUtil(root.right, K)

            self.count += 1
            if self.count == K:
                self.ans = root.data

            self.kthLargestUtil(root.left, K)

    def kthLargest(self, root, K): 
        self.count = 0
        self.ans = -1

        self.kthLargestUtil(root, K)

        return self.ans