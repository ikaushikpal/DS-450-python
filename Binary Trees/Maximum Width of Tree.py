class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

from collections import deque


class Solution:
    
    def getMaxWidth(self, root):
        outerQueue = deque([root])
        innerQueue = deque([])
        storedPos = {}
        maxWidthLevelWise = 0

        while len(outerQueue):
            innerQueue, outerQueue = outerQueue, innerQueue
            maxWidthLevelWise = max(maxWidthLevelWise, len(innerQueue))

            while len(innerQueue):
                currNode = innerQueue.popleft()

                if currNode.left:
                    outerQueue.append(currNode.left)
                
                if currNode.right:

                    outerQueue.append(currNode.right)
        
        return maxWidthLevelWise


