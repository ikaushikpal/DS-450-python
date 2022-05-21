# Given a Binary Tree, write a function to populate next pointer for all nodes. The next pointer for every node should be set to point to inorder successor.

# Example 1:

# Input:
#            10
#        /  \
#       8    12
#      /
#     3
  

# Output: 3->8 8->10 10->12 12->-1
# Explanation: The inorder of the above tree is :
# 3 8 10 12. So the next pointer of node 3 is 
# pointing to 8 , next pointer of 8 is pointing
# to 10 and so on.And next pointer of 12 is
# pointing to -1 as there is no inorder successor 
# of 12.
# Example 2:

# Input:
#            1
#       /   \
#      2     3
# Output: 2->1 1->3 3->-1 


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None


class Solution:
    def populateNext(self, root):
        if root is None:
            return None
        
        currentNode = root
        lastNode = None

        while currentNode:
            # case 1
            if currentNode.left is None:
                lastNode = currentNode
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
                    # visit root
                    lastNode = currentNode
                    # go left
                    currentNode = currentNode.left
        if lastNode:
            lastNode.next = Node(-1)

        return root