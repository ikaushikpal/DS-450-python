# Given a Binary Search Tree, find median of it. 
# If no. of nodes are even: then median = ((n/2th node + (n+1)/2th node) /2 
# If no. of nodes are odd : then median = (n+1)/2th node.
# For example, median of below BST is 12. 
 

# More Examples: 
#  Given BST(with odd no. of nodes) is : 
#                     6
#                  /    \
#                 3       8
#               /   \    /  \
#              1     4  7    9

# Inorder of Given BST will be : 1, 3, 4, 6, 7, 8, 9
# So, here median will 6.

# Given BST(with even no. of nodes) is :  
#                     6
#                  /    \
#                 3       8
#               /   \    /  
#              1     4  7    

# Inorder of Given BST will be : 1, 3, 4, 6, 7, 8
# So, here median will  (4+6)/2 = 5.
# Asked in: Google

# optimal approach:
# The task is very simple if we are allowed to use extra space but Inorder traversal using recursion and stack both use Space which is not allowed here. So, the solution is to do Morris Inorder traversal as it doesn’t require any extra space.


import math


def count(root):
    if root is None: return 0

    return count(root.left) + count(root.right) + 1

def kthSmallest(root, k):
    if root is None:
        return None
    
    left = kthSmallest(root.left, k)
    if left:
        return left

    k[0] -= 1
    if k[0] == 0:
        return root

    right = kthSmallest(root.right, k)
    if right:
        return right
    
    return None

def findMedian(root):
    # code here
    # return the median
    noNodes = count(root)

    if noNodes % 2 == 1: # odd  no of nodes
        k = (noNodes+1) // 2
        return kthSmallest(root, [k]).data
        
    else:
        k1 = noNodes // 2
        k2 = math.ceil((noNodes+1) / 2)
        
        res = (kthSmallest(root, [k1]).data + kthSmallest(root, [k2]).data) / 2
        
        if res.is_integer():
            return int(res)
        else:
            return res

# Time Complexity: O(N)
# Space Complexity: O(H); Height of the tree.

# Optimal approach
class Solution:
    def countNodes(self, root):
        if root is None:
            return 0
        
        count = 0
        currentNode = root

        while currentNode:
            # case 1
            if currentNode.left is None:
                count += 1
                # go right
                currentNode = currentNode.right

            # case 2
            else:
                prevNode = currentNode.left
                while prevNode.right and prevNode.right != currentNode:
                    prevNode = prevNode.right
                
                # creating thread
                if prevNode.right is None:
                    prevNode.right = currentNode
                    # go left
                    currentNode = currentNode.left
                
                # deleting thread
                else:
                    prevNode.right = None
                    count += 1
                    # go right
                    currentNode = currentNode.right
        return count

    def kthSmallest(self, root, k):
        if root is None:
            return -1
        
        currentNode = root
        returnValue = None
        
        while currentNode:
            # case 1
            if currentNode.left is None:
                k -= 1
                if k == 0:
                    returnValue = currentNode.data
                # go right
                currentNode = currentNode.right

            # case 2
            else:
                prevNode = currentNode.left
                while prevNode.right and prevNode.right != currentNode:
                    prevNode = prevNode.right
                
                # creating thread
                if prevNode.right is None:
                    prevNode.right = currentNode
                    # go left
                    currentNode = currentNode.left
                
                # deleting thread
                else:
                    prevNode.right = None
                    k -= 1
                    if k == 0:
                        returnValue = currentNode.data
                    # go right
                    currentNode = currentNode.right

        return returnValue  

    def findMedian(self, root):
        # code here
        # return the median
        noNodes = self.countNodes(root)

        if noNodes % 2 == 1: # odd  no of nodes
            k = (noNodes+1) >> 1
            return self.kthSmallest(root, k)
        
        else:
            k1 = noNodes >> 1
            k2 = math.ceil((noNodes+1) / 2)
            
            res = (self.kthSmallest(root, k1) + self.kthSmallest(root, k2)) / 2
            
            if res.is_integer():
                return int(res)
            else:
                return res
# Time COmplexity: O(N)
# Space Complexity: O(1)