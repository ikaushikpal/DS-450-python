# https://practice.geeksforgeeks.org/problems/diagonal-traversal-of-binary-tree/1

from collections import defaultdict

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#:param root: root of the given tree.
#return: print out the diagonal traversal,  no need to print new line
maxDiagonal = 0

def diagonal(root):
    global maxDiagonal
    maxDiagonal = 0

    hashMap = defaultdict(list)
    diagonalUtil(root, 0, hashMap)
    
    res = []
    
    for i in range(maxDiagonal+1):
        res.extend(hashMap[i])
    
    return res

def diagonalUtil(root, index, hashMap):
    if root is None:
        return
    global maxDiagonal

    hashMap[index].append(root.data)
    maxDiagonal = max(maxDiagonal, index)

    diagonalUtil(root.left, index+1, hashMap)
    diagonalUtil(root.right, index, hashMap)

# ====================================
# new code
# using vertical ordering

class NodeInfo:
    def __init__(self, node, loc):
        self.node = node
        self.loc = loc


from collections import deque


class Solution:
    
    #Function to find the vertical order traversal of Binary Tree.
    def diagonalClockWise(self, root): 
        if root is None:
            return []

        # to find vertical order we must use level order because it is mandatory to maintain order
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
                    newLoc =  currNode.loc
                    maxIndex = max(newLoc, maxIndex)
                    outerQueue.append(NodeInfo(currNode.node.right, newLoc))
        
        for i in range(maxIndex, minIndex-1, -1):
            output_list.extend(storedPos[i])
        
        return output_list


def diagonal(root):
    return Solution().diagonalClockWise(root)