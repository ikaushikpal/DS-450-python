# https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1#

'''class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None'''


#Function to check whether a binary tree is balanced or not.
result = True

def isBalanced(root):
    global result
    result = True
    isBalancedUtil(root)
    
    return result
    
def isBalancedUtil(root):
    if root is None:
        return 0
        
    global result
    
    leftHeight = isBalancedUtil(root.left)
    rightHeight = isBalancedUtil(root.right)
    
    if abs(leftHeight - rightHeight) >= 2:
        result = False
    
    return max(leftHeight , rightHeight) + 1