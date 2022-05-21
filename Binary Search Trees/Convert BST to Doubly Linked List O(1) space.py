# Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be the same as in Inorder for the given Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL. 
from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:
    def convertToDLL(self, root: Optional[Node]) -> Node:
        if root is None:
            return None
        
        head = tail = None
        currentNode = root

        while currentNode:
            # case 1
            if currentNode.left is None:
                # visit root
                if head is None:
                    head = tail = currentNode
                else:
                    tail.right = currentNode
                    currentNode.left = tail
                    tail = currentNode

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

                    # visit root
                    tail.right = currentNode
                    currentNode.left = tail
                    tail = currentNode

                    # go right
                    currentNode = currentNode.right
        return head

# utility =======
def printNodes(root):
    while root:
        print(root.val, end=', ')
        root = root.right
    print()


if __name__ == '__main__':
    root = Node(10)
    
    root.left = Node(5)
    root.right = Node(15)
    
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.left = Node(12)
    root.right.right = Node(20)

    sol = Solution()
    head = sol.convertToDLL(root)
    printNodes(head)
