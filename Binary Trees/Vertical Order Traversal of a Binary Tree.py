# Definition for a binary tree node.
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class NodeInfo:
    def __init__(self, node, loc):
        self.node = node
        self.loc = loc


class Solution:
    def verticalTraversal(self, root): 
        if root is None:
            return []

        outerQueue = deque([NodeInfo(root, 0)])
        innerQueue = deque([])
        storedPos = {}
        minIndex = maxIndex = 0
        output_list = []

        while len(outerQueue):
            innerQueue, outerQueue = outerQueue, innerQueue
            storedPosTemp = {}

            while len(innerQueue):
                currNode = innerQueue.popleft()
     
                if currNode.loc not in storedPosTemp:
                    storedPosTemp[currNode.loc] = [currNode.node.val]
                else:
                    storedPosTemp[currNode.loc].append(currNode.node.val)


                if currNode.node.left:
                    newLoc =  currNode.loc-1
                    minIndex = min(newLoc, minIndex)
                    outerQueue.append(NodeInfo(currNode.node.left, newLoc))
                
                if currNode.node.right:
                    newLoc =  currNode.loc+1
                    maxIndex = max(newLoc, maxIndex)
                    outerQueue.append(NodeInfo(currNode.node.right, newLoc))

            for key in storedPosTemp:
                storedPosTemp[key].sort()
                
                if key not in storedPos:
                    storedPos[key] = storedPosTemp[key]
                else:
                    storedPos[key].extend(storedPosTemp[key])


        for i in range(minIndex, maxIndex+1):
            output_list.append(storedPos[i])
        
        return output_list