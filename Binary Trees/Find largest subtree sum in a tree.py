class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    
    def largestSubTreeSumUtil(self, root):
        if root is None:
            return 0
        
        left = self.largestSubTreeSumUtil(root.left)
        right = self.largestSubTreeSumUtil(root.right)

        total = left + right + root.data
        self.maxx = max(self.maxx, total)

        return total


    def largestSubTreeSum(self, root):
        self.maxx = float('-inf')
        self.largestSubTreeSumUtil(root)

        return self.maxx



if __name__ == '__main__':
    # Input :   1
    #         /   \
    #        2      3
    #       / \    / \
    #      4   5  6   7
    # Output : 28

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(Solution().largestSubTreeSum(root))

    # Input :     1
    #           /    \
    #         -2      3
    #         / \    /  \
    #         4   5  -6   2
    # Output : 7
    # Subtree with largest sum is: -2
    #                             /  \ 
    #                             4    5
    # Also, entire tree sum is also 7
    
    root = Node(1)
    root.left = Node(-2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(-6)
    root.right.right = Node(2)

    print(Solution().largestSubTreeSum(root))

    # Time Complexity: O(n), where n is number of nodes. 
    # Auxiliary Space: O(n), function call stack size.

