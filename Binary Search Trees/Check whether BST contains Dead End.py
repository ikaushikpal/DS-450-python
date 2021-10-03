# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def getCount(root,low,high):
    if root is None:
        return 0
    
    curr = 0
    if low <= root.data and root.data <= high:
        curr = 1
    
    if root.data > low:
        curr += getCount(root.left, low, high)
    
    if root.data < high:
        curr += getCount(root.right, low, high)
        
    return curr

