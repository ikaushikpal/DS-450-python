class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# your task is to complete this function
# function should return a list containing the boundary view of the binary tree

class Solution:
    def printBoundaryView(self, root):
        if root is None:
            return []
            
        self.leftBound = []
        self.rightBound = []
        self.leafs = []
        result = [root.data]

        self.leftBoundary(root.left)
        self.leafNodes(root)
        self.rightBoundary(root.right)

        result += self.leftBound[:-1]       
        result += self.leafs
        
        self.rightBound.reverse()

        if len(self.rightBound) > 1:
            result += self.rightBound[1:]

        return result


    def leftBoundary(self, root):
        if root is None:
            return None
        
        self.leftBound.append(root.data)

        left = self.leftBoundary(root.left)
        if left is None:
            right = self.leftBoundary(root.right)
        
        return root
        
    def rightBoundary(self, root):
        if root is None:
            return None
        
        self.rightBound.append(root.data)

        right = self.rightBoundary(root.right)
        if right is None:
            left = self.rightBoundary(root.left)
        
        return root
    
    def leafNodes(self, root):
        if root is None:
            return
        
        if root.left is None and root.right is None:
            self.leafs.append(root.data)
        
        self.leafNodes(root.left)
        self.leafNodes(root.right)


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)

    print(Solution().printBoundaryView(root))

