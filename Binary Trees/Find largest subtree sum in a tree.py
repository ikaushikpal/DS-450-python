class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 

class Solution:
    def findLargestSubtreeSumUtil(self, root):
        if root == None:
            return 0
        
        currSum = root.data + self.findLargestSubtreeSumUtil(root.left) + self.findLargestSubtreeSumUtil(root.right)
        self.maxSum = max(self.maxSum, currSum)

        return currSum
    

    def findLargestSubtreeSum(self, root):
        self.maxSum = float('-inf')
        self.findLargestSubtreeSumUtil(root)
    
        return self.maxSum
 

if __name__ == '__main__':
     
    #        1
    #      /   \
    #     /     \
    #   -2       3
    #   / \     /  \
    #  /   \   /    \
    # 4     5 -6     2

    # Output: 
    # 7
    
    root = Node(1)
    root.left = Node(-2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(-6)
    root.right.right = Node(2)
 
    print(Solution().findLargestSubtreeSum(root))
    
    # Time Complexity: O(n), where n is number of nodes. 
    # Auxiliary Space: O(n), function call stack size.