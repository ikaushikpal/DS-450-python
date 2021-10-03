from typing import Optional


class Node:
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class Solution:
    def maxPathSumUtil(self, root):
        if root is None:
            return 0
        
        left = self.maxPathSumUtil(root.left)
        right = self.maxPathSumUtil(root.right)

        include_root = left + right + root.data

        self.maxSum = max(self.maxSum, include_root)

        return max(left, right) + root.data


    def maxPathSum(self, root: Optional[Node]) -> int:
        if root is None:
            return 0

        self.maxSum = float('-inf')
        self.maxPathSumUtil(root)

        return self.maxSum


if __name__ == '__main__':
    # Driver program to test above function
    root = Node(-15)
    root.left = Node(5)
    root.right = Node(6)
    root.left.left = Node(-8)
    root.left.right = Node(1)
    root.left.left.left = Node(2)
    root.left.left.right = Node(6)
    root.right.left = Node(3)
    root.right.right = Node(9)
    root.right.right.right = Node(0)
    root.right.right.right.left = Node(4)
    root.right.right.right.right = Node(-1)
    root.right.right.right.right.left = Node(10)

    print(Solution().maxPathSum(root))

