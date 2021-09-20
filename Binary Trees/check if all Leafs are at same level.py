from collections import deque


class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    def check(self, root):
        outerQueue = deque([root])
        innerQueue = deque([])
        result = []

        while len(outerQueue):
            count_leaf = 0
            innerQueue = outerQueue
            outerQueue = deque([])
            count = len(innerQueue)
            
            while len(innerQueue):
                node = innerQueue.popleft()

                
                if node.left ==None and node.right ==None:
                    count_leaf += 1

                if node.left:
                    outerQueue.append(node.left)
                
                if node.right:
                    outerQueue.append(node.right)
            
            if count_leaf > 0 and count != count_leaf:
                return False
                    
        return True