from collections import deque


'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        if root is None:
            return []
        
        result = []
        queue = deque()
        queueTemp = deque()

        queueTemp.append(root)

        while len(queueTemp):
            queue, queueTemp = queueTemp, queue
            temp = []

            while len(queue):
                currentNode = queue.popleft()
                temp.append(currentNode.data)
                
                if currentNode.left:
                    queueTemp.append(currentNode.left)
                
                if currentNode.right:
                    queueTemp.append(currentNode.right)
            
            result.append(temp[-1])
            
        return result
