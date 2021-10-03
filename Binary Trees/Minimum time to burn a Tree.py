import sys


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def nodeToRootPath(self, root, targetVal):
        if root is None:
            return []
        
        if root.data == targetVal:
            return [root]

        left = self.nodeToRootPath(root.left, targetVal)
        if len(left) > 0:
            left.append(root)
            return left

        right = self.nodeToRootPath(root.right, targetVal)
        if len(right) > 0:
            right.append(root)
            return right
        
        return []
    
    def height(self, root, blockerNode):
        if root is None:
            return 0
        
        left = right = 0

        if root.left and root.left != blockerNode:
            left = self.height(root.left, blockerNode)
        
        if root.right and root.right != blockerNode:
            right = self.height(root.right, blockerNode)
        
        return max(left, right) + 1
    
    def burnTree(self, root, targetVal):
        sys.setrecursionlimit(10**4)
        path = self.nodeToRootPath(root, targetVal)
        maxTime = 0
        prevNode = None

        for i in range(len(path)):
            time = i + self.height(path[i], prevNode)
            prevNode = path[i]

            maxTime = max(maxTime, time)
        
        if maxTime > 0:
            return maxTime - 1
        else:
            return maxTime


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.left.left.left = Node(8)
    root.left.right.left = Node(9)
    root.left.right.right = Node(10)
    root.left.right.left.left = Node(11)
 
    print(Solution().burnTree(root, 11))