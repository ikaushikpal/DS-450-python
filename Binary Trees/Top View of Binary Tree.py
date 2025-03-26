class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class NodeInfo:
    def __init__(self, node, loc):
        self.node = node
        self.loc = loc


from collections import deque


class Solution:
    
    def topView(self, root): 
        # to find topview we must use level order because it is mandatory to maintain order
        # see vertical traversal first

        outerQueue = deque([NodeInfo(root, 0)])
        innerQueue = deque([])
        storedPos = {}
        minIndex = maxIndex = 0
        output_list = []

        while len(outerQueue):
            innerQueue, outerQueue = outerQueue, innerQueue
            
            while len(innerQueue):
                currNode = innerQueue.popleft()

                if currNode.loc not in storedPos:
                    storedPos[currNode.loc] = [currNode.node.data]
                else:
                    storedPos[currNode.loc].append(currNode.node.data)


                if currNode.node.left:
                    newLoc =  currNode.loc-1
                    minIndex = min(newLoc, minIndex)
                    outerQueue.append(NodeInfo(currNode.node.left, newLoc))
                
                if currNode.node.right:
                    newLoc =  currNode.loc+1
                    maxIndex = max(newLoc, maxIndex)
                    outerQueue.append(NodeInfo(currNode.node.right, newLoc))
        
        for i in range(minIndex, maxIndex+1):
            output_list.append(storedPos[i][0])
        
        return output_list


