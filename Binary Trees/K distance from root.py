#User function Template for python3
from collections import deque


class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None


def KDistance(root, k):
    '''
    :param root: root of given tree.
    :param k: distance k from root
    :return: Print all nodes that are at distance k from root, no need to print next line.
    '''
    res = []

    if root is None:
        return res
    
    outerQueue = deque([root])
    level = 0
    innerQueue = deque()

    while len(outerQueue):
        innerQueue, outerQueue = outerQueue, innerQueue
        
        if level == k:
            for node in innerQueue:
                res.append(node.data)

            return res

        while len(innerQueue):
            currentNode = innerQueue.popleft()
    
            if currentNode.left:
                outerQueue.append(currentNode.left)
            
            if currentNode.right:
                outerQueue.append(currentNode.right)

        level += 1
        
    return res

