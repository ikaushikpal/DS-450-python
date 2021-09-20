from collections import deque


class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def merge(self, result, array, reverse=False):
        if reverse == False:
            while len(array):
                node = array.popleft()
                result.append(node.data)

        else:
            while len(array):
                node = array.pop()
                result.append(node.data)
        
        return result
            
    def zigZagTraversal(self, root):
        outerQueue = deque([root])
        innerQueue = deque([])
        level = 0
        result = []

        while len(outerQueue):
            innerQueue = outerQueue.copy()

            if level % 2 == 0:
                result = self.merge(result, outerQueue)

            else:
                result = self.merge(result, outerQueue, True)


            while len(innerQueue):
                node = innerQueue.popleft()

                if node.left:
                    outerQueue.append(node.left)
                
                if node.right:
                    outerQueue.append(node.right)
            
            level += 1
                    
        return result
            