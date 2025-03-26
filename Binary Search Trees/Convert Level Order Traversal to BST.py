class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

from collections import deque

class NodeInfo:
    def __init__(self, parentNode=None, minRange=float('-inf'), maxRange=float('inf')):
        self.parentNode = parentNode
        self.minRange = minRange
        self.maxRange = maxRange

class Solution:

    def buildTree(self, levelOrder):
        if len(levelOrder) == 0:
            return None

        start, end = 1, len(levelOrder)-1
        queue = deque()
        root = Node(levelOrder[0])

        queue.append(NodeInfo(root, float('-inf'), root.data))
        queue.append(NodeInfo(root, root.data, float('inf')))

        while len(queue) and start<=end:
            nodeInfo = queue.popleft()
            val = levelOrder[start]

            if val < nodeInfo.minRange or val > nodeInfo.maxRange:
                continue


            if nodeInfo.minRange < val < nodeInfo.maxRange:
                start += 1
                newNode = Node(val)

                if val > nodeInfo.parentNode.data:
                    nodeInfo.parentNode.right = newNode
                else:
                    nodeInfo.parentNode.left = newNode

                queue.append(NodeInfo(newNode, nodeInfo.minRange, val))
                queue.append(NodeInfo(newNode, val, nodeInfo.maxRange))

            
        return root


def constructBst(arr,n):
    #Your code here
    return Solution().buildTree(arr)    

constructBst([50, 17, 72, 12, 23, 54, 76, 9, 14, 19, 67], 11)