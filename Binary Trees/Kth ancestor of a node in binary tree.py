class Node:
    # Constructor to create a node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def kthAncestorUtil(self, root, targetVal, k):
        if root is None:
            return None

        if root.data == targetVal:
            self.k -= 1
            return None

        if self.k < k:
            self.k -= 1

        if self.k == 0:
            return root

        left = self.kthAncestorUtil(root.left, targetVal, k)
        if left:
            return left

        right = self.kthAncestorUtil(root.right, targetVal, k)
        if right:
            return right

        return None

    def kthAncestor(self, root, targetVal, k):
        self.k =k
        return self.kthAncestorUtil(root, targetVal, k)    
