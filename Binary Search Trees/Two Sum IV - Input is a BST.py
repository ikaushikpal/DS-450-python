# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.


# Example 1:
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true


# Example 2:
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false


# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class BSTIterator:

    def __init__(self, root: Optional[TreeNode], reverse=False):
        self.stack = deque([root])
        self.reverse = reverse
        self.pushAll()
        
    def pushAll(self):
        ptr = self.stack[-1]

        if self.reverse == False:
            while ptr and ptr.left:
                ptr = ptr.left
                self.stack.append(ptr)
        else:
            while ptr and ptr.right:
                ptr = ptr.right
                self.stack.append(ptr)
            
    def next(self) -> int:
        currNode = self.stack.pop()
        
        if self.reverse == False:
            if currNode.right:
                self.stack.append(currNode.right)
                self.pushAll()
        else:
            if currNode.left:
                self.stack.append(currNode.left)
                self.pushAll()

        return currNode.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        
                
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        left = BSTIterator(root)
        right = BSTIterator(root, True)

        leftVal = left.next()
        rightVal = right.next()

        while leftVal < rightVal:
            if leftVal + rightVal == k:
                return True
            elif leftVal + rightVal < k:
                leftVal = left.next()
            else:
                rightVal = right.next()

        return False

class Solution1:
    def inorder(self, root, direction):
        if root is None:
            return
        
        left, right = (root.left, root.right)[::direction]
        yield from self.inorder(left, direction)
        yield root.val
        yield from self.inorder(right, direction)
            
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        leftGen, rightGen = self.inorder(root, 1), self.inorder(root, -1)
        ptr1, ptr2 = next(leftGen), next(rightGen)
        
        while ptr1 < ptr2:
            total = ptr1 + ptr2
            if total == k:
                return True
            elif total < k:
                ptr1 = next(leftGen)
            else:
                ptr2 = next(rightGen)
        return False
# Using Generators
# T.C. = O(n)
# S.C. = O(h)


if __name__ == "__main__":
    root =TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    print(Solution().findTarget(root, 1))

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    print(Solution().findTarget(root, 7))

    root = TreeNode(5)
    root.left = TreeNode(0)
    root.right = TreeNode(4)
    root.left.left = TreeNode(-2)
    root.right.left = TreeNode(3)
    print(Solution().findTarget(root, 7))