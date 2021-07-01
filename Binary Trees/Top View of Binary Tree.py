from collections import deque


class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self, root):
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
            
            if len(temp) == 1:
                result.append(temp[0])
            else:
                leftMostNode = temp[0]
                rightMostNode = temp[-1]

                result.append(rightMostNode)
                result.insert(0, leftMostNode)
            
        return result