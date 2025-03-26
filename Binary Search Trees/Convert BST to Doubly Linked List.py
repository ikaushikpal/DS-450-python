# Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be the same as in Inorder for the given Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL. 

from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:
    def dfs(self, root: Node) -> None:
        if root is None:
            return
        
        self.dfs(root.left)
        
        if self.head is None:
            self.head = self.tail = root
        else:
            self.tail.right = root
            root.left = self.tail
            self.tail = root
        
        self.dfs(root.right)

    def convertToDLL(self, root: Optional[Node]) -> Node:
        self.head = self.tail = None
        self.dfs(root)
        return self.head

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
