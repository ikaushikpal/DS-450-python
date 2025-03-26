# Given a binary tree

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.


# Example 1:
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


# Example 2:
# Input: root = []
# Output: []


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # simple solution can be do bfs or level order traversal
        # and for each level link curr.next to next node of the queue
        # this approach will take O(n) time and O(n) space

        # but here we can do it in O(1) space. its tricky
        # maintain 3 variable parent, child and nextLevel
        # parent is direct parent Node of child Node
        # nextLevel denote the next level's first Node

        parentNode = root
        # traversing level by level
        while parentNode:
            # first creating a dummy node
            # for simplistic code
            childNode = nextLevel = Node(0)

            # traversing each node of same level
            while parentNode:
                if parentNode.left:
                    childNode.next = parentNode.left
                    childNode = childNode.next
                
                if parentNode.right:
                    childNode.next = parentNode.right
                    childNode = childNode.next

                # going to next node, how we can go to next node of same level ?
                # because we already made link using childNode on previous iteration
                parentNode = parentNode.next

            # going to next level
            parentNode = nextLevel.next

        return root
# Time Complexity : O(N)
# Space Complexity : O(1)