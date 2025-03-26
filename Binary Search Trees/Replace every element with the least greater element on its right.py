# Given an array of integers, replace every element with the least greater element on its right side in the array. If there are no greater elements on the right side, replace it with -1.

# Examples: 

# Input: [8, 58, 71, 18, 31, 32, 63, 92, 
#          43, 3, 91, 93, 25, 80, 28]
# Output: [18, 63, 80, 25, 32, 43, 80, 93, 
#          80, 25, 93, -1, 28, -1, -1]


class Node:
     
    def __init__(self, d):
         
        self.data = d
        self.left = None
        self.right = None
 
# A utility function to insert a new node with
# given data in BST and find its successor
def insert(node, data):
     
    global succ
     
    # If the tree is empty, return a new node
    root = node
 
    if (node == None):
        return Node(data)
 
    # If key is smaller than root's key, go to left
    # subtree and set successor as current node
    if (data < node.data):
         
        #print("1")
        succ = node
        root.left = insert(node.left, data)
 
    # Go to right subtree
    elif (data > node.data):
        root.right = insert(node.right, data)
         
    return root
 
# Function to replace every element with the
# least greater element on its right
def replace(arr, n):
     
    global succ
    root = None
 
    # Start from right to left
    for i in range(n - 1, -1, -1):
        succ = None
 
        # Insert current element into BST and
        # find its inorder successor
        root = insert(root, arr[i])
 
        # Replace element by its inorder
        # successor in BST
        if (succ):
            arr[i] = succ.data
         
        # No inorder successor
        else:  
            arr[i] = -1
             
    return arr
 
# Driver code
if __name__ == '__main__':
     
    arr = [ 8, 58, 71, 18, 31, 32, 63,
            92, 43, 3, 91, 93, 25, 80, 28 ]
    n = len(arr)
    succ = None
 
    arr = replace(arr, n)
 
    print(*arr)