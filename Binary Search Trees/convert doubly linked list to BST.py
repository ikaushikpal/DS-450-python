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


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None

    def __repr__(self):
        return str(self.val)

class Solution:
    def middleNode(self, root: Node):
        slow = fast = root

        while fast and fast.right and fast.right.right:
            slow = slow.right
            fast = fast.right.right
        
        return slow    
    
    def countNodes(self, root: Node):
        count = 0
        while root:
            count += 1
            root = root.right
        return count

    def convertToBST_Util(self, head: Node, count) -> Node:
        if head is None:
            return None

        if count == 0:
            return None

        root = self.middleNode(head)

        head1, head2 = head, root.right
        prevNode, nextNode = root.left, root.right

        leftCount = (count - 1) >> 1
        rightCount = count - leftCount - 1

        if prevNode:
            prevNode.right = root.left = None
        
        if nextNode:
            nextNode.left = root.right = None
        
        root.left = self.convertToBST_Util(head1, leftCount)
        root.right = self.convertToBST_Util(head2, rightCount)

        return root
    def convertToBST(self, head: Node) -> Node:
        count = self.countNodes(head)
        return self.convertToBST_Util(head, count)

# Time Complexity : O(NlogN)
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