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
    
    def height(self, root, blockerNode, time):
        if root is None:
            return 0
        
        if time not in self.storedNodes:
            self.storedNodes[time] = [root.data]
        else:
            self.storedNodes[time].append(root.data)

        left = right = 0

        if root.left and root.left != blockerNode:
            left = self.height(root.left, blockerNode, time+1)
        
        if root.right and root.right != blockerNode:
            right = self.height(root.right, blockerNode, time+1)
        
        return max(left, right) + 1
    
    def burnTree(self, root, targetVal):
        sys.setrecursionlimit(10**4)
        path = self.nodeToRootPath(root, targetVal)
        prevNode = None
        self.storedNodes = {}

        for i in range(len(path)):
            time = i + self.height(path[i], prevNode, i)
            prevNode = path[i]
        
        return list(self.storedNodes.values())


if __name__ == '__main__':
    #     10
    #    /  \
    #   12  13
    #       / \
    #      14 15
    #     / \ / \
    #   21 22 23 24

    # Let us create Binary Tree as shown
 
    root = Node(10)
    root.left = Node(12)
    root.right = Node(13)
 
    root.right.left = Node(14)
    root.right.right = Node(15)
 
    root.right.left.left = Node(21)
    root.right.left.right = Node(22)
    root.right.right.left = Node(23)
    root.right.right.right = Node(24)
 
    print(Solution().burnTree(root, 14))