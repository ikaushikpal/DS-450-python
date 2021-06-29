from collections import deque

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def reverseLevelOrder(root):
    if root is None:
        return []
    
    result = []
    queue = deque()
    queueTemp = deque()

    queueTemp.append(root)
    while len(queueTemp):
        temp = []
        queue, queueTemp = queueTemp, queue

        while len(queue):
            currentNode = queue.popleft()
            temp.append(currentNode.data)
            
            if currentNode.left:
                queueTemp.append(currentNode.left)
            
            if currentNode.right:
                queueTemp.append(currentNode.right)
            
        for i in range(len(temp)-1, -1, -1):
            result.append(temp[i])

        
    return result[::-1]
    