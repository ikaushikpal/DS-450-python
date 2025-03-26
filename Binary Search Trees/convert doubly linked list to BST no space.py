# Given a Doubly Linked List which has data members sorted in ascending order. Construct a Balanced Binary Search Tree which has same data members as the given Doubly Linked List. The tree must be constructed in-place (No new node should be allocated for tree conversion) 

# Examples: 

# Input:  Doubly Linked List 1  2  3
# Output: A Balanced BST 
#      2   
#    /  \  
#   1    3 


# Input: Doubly Linked List 1  2 3  4 5  6  7
# Output: A Balanced BST
#         4
#       /   \
#      2     6
#    /  \   / \
#   1   3  5   7  

# Input: Doubly Linked List 1  2  3  4
# Output: A Balanced BST
#       3   
#     /  \  
#    2    4 
#  / 
# 1

# Input:  Doubly Linked List 1  2  3  4  5  6
# Output: A Balanced BST
#       4   
#     /   \  
#    2     6 
#  /  \   / 
# 1   3  5   

# NOTE:
# In this method, we construct from leaves to root. The idea is to insert nodes in BST in the same order as they appear in Doubly Linked List, so that the tree can be constructed in O(n) time complexity. We first count the number of nodes in the given Linked List. Let the count be n. After counting nodes, we take left n/2 nodes and recursively construct the left subtree. After left subtree is constructed, we assign middle node to root and link the left subtree with root. Finally, we recursively construct the right subtree and link it with root. 
# While constructing the BST, we also keep moving the list head pointer to next so that we have the appropriate pointer in each recursive call. 


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None

    def __repr__(self):
        return str(self.val)


class Solution:
    def countNodes(self, root: Node):
        count = 0
        while root:
            count += 1
            root = root.right
        return count

    def convertToBST_Util(self, n: int) -> Node:
        if n <= 0:
            return None

        leftCount = n >> 1
        rightCount = n - leftCount - 1

        leftChild = self.convertToBST_Util(leftCount)

        root = self.head
        root.left = leftChild

        # propagating head
        self.head = self.head.right

        root.right = self.convertToBST_Util(rightCount)
        return root

    def convertToBST(self, head: Node) -> Node:
        count = self.countNodes(head)
        self.head = head
        return self.convertToBST_Util(count)
# Time Complexity : O(N)
# Space Complexity: O(1)


# utility =====
def preorder(root):
    if root:
        print(root.val, end=', ')
        preorder(root.left)  
        preorder(root.right)


if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    a.right = b
    b.left = a
    b.right = c
    c.left = b
    c.right = d
    d.left = c
    d.right = e
    e.left = d

    sol = Solution()
    root = sol.convertToBST(a)
    preorder(root)
