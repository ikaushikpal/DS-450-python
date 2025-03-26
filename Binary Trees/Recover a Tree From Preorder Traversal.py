# We run a preorder depth-first search (DFS) on the root of a binary tree.

# At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

# If a node has only one child, that child is guaranteed to be the left child.

# Given the output traversal of this traversal, recover the tree and return its root.

 

# Example 1:
# Input: traversal = "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]


# Example 2:
# Input: traversal = "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7]


# Example 3:
# Input: traversal = "1-401--349---90--88"
# Output: [1,401,null,349,88,90]


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0

        while i < len(traversal):
            depth = 0
            while i < len(traversal) and traversal[i] == '-':
                i += 1
                depth += 1
                
            nodeVal = 0
            while i < len(traversal) and traversal[i] != '-':
                nodeVal = nodeVal * 10 + int(traversal[i])
                i += 1
                
            newNode = TreeNode(nodeVal)
            while depth < len(stack):
                stack.pop()
            
            # not root of the tree
            if len(stack) > 0:
                parentNode = stack[-1]
                if parentNode.left is None:
                    parentNode.left = newNode
                else:
                    parentNode.right = newNode
            stack.append(newNode)   
        return stack[0]
# Time Complexity: O(n)
# Space Complexity: O(H)


if __name__ == '__main__':
    sol = Solution()
    print(sol.recoverFromPreorder("1-2--3--4-5--6--7"))
    print(sol.recoverFromPreorder("1-2--3---4-5--6---7"))
    print(sol.recoverFromPreorder("1-401--349---90--88"))