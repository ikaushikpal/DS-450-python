from collections import deque


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    if root is None:
        return []
    
    result = []
    queue = deque()
    queueTemp = deque()

    queueTemp.append(root)

    while len(queueTemp):
        queue, queueTemp = queueTemp, queue
        FLAG = True

        while len(queue):
            currentNode = queue.popleft()
            if FLAG:
                result.append(currentNode.data)
                FLAG = False
            
            if currentNode.left:
                queueTemp.append(currentNode.left)
            
            if currentNode.right:
                queueTemp.append(currentNode.right)
            
    return result
