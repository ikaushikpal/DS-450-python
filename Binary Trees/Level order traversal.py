from collections import deque 


class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self, root):
        res = []

        if root is None:
            return res
        
        queue =deque()
        queue.append(root)

        while len(queue):
            currentNode = queue.popleft()
            res.append(currentNode.data)

            if currentNode.left:
                queue.append(currentNode.left)
            
            if currentNode.right:
                queue.append(currentNode.right)


        return res