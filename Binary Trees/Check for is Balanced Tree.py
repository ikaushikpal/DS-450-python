class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None


#Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalancedUtil(self, root):
        if root is None:
            return 0

        left = self.isBalancedUtil(root.left)
        right = self.isBalancedUtil(root.right)
        
        self.FLAG = self.FLAG & (abs(left - right) <= 1)

        return max(left, right) + 1

    def isBalanced(self, root):
        self.FLAG = True
        self.isBalancedUtil(root)
        
        return self.FLAG


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(10)
    root.right = Node(10)
    root.left.left = Node(10)
    # root = Node(10)
    # root = Node(10)

    print(Solution().isBalanced(root))