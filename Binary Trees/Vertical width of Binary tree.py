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

    def getLength(self, root): 
        # copied from vertical traversal of binary tree
        outerQueue = deque([NodeInfo(root, 0)])
        innerQueue = deque([])
        minIndex = maxIndex = 0

        while len(outerQueue):
            innerQueue, outerQueue = outerQueue, innerQueue
            
            while len(innerQueue):
                currNode = innerQueue.popleft()

                if currNode.node.left:
                    newLoc =  currNode.loc-1
                    minIndex = min(newLoc, minIndex)
                    outerQueue.append(NodeInfo(currNode.node.left, newLoc))
                
                if currNode.node.right:
                    newLoc =  currNode.loc+1
                    maxIndex = max(newLoc, maxIndex)
                    outerQueue.append(NodeInfo(currNode.node.right, newLoc))
        
        return maxIndex - minIndex + 1

if __name__ == '__main__':
    #     Input : 
    #              7
    #            /  \
    #           6    5
    #          / \  / \
    #         4   3 2  1 
    # Output :
    # 5

    root = Node(7) 
    root.left = Node(6) 
    root.right = Node(5) 
    root.left.left = Node(4) 
    root.left.right = Node(3) 
    root.right.left = Node(2) 
    root.right.right = Node(1) 
  
    print(Solution().getLength(root))
    
    # Input :
    #            1
    #          /    \
    #         2       3
    #        / \     / \
    #       4   5   6   7
    #                \   \ 
    #                 8   9 
    # Output :
    # 6