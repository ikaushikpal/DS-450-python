from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def KDistance(self, root, k, blockerNode):
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

                if currentNode.left and currentNode.left != blockerNode:
                    outerQueue.append(currentNode.left)
                
                if currentNode.right and currentNode.right != blockerNode:
                    outerQueue.append(currentNode.right)

            level += 1
            
        return res
    

    def nodeToRootPath(self, root, targetVal):
        if root is None:
            return []
        
        if root.data == targetVal:
            return [root]

        left = self.nodeToRootPath(root.left, targetVal)
        if len(left) > 0:
            left.append(root)
            return left

        right = self.nodeToRootPath(root.right, targetVal)
        if len(right) > 0:
            right.append(root)
            return right
        
        return []


    def KDistanceNodes(self, root,target,k):
        # code here
        # return the sorted list all nodes at k distance from target
        path = self.nodeToRootPath(root, target)
        output = []
        prevNode = None

        for i in range(len(path)):
            if i > k:
                break

            currentNode = path[i]
            k_dist_nodes = self.KDistance(currentNode, k-i, prevNode)

            output.extend(k_dist_nodes)
            prevNode = currentNode

        output.sort()
        return output


if __name__ == '__main__':
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    root.right.right.right = Node(4)
    root.right.right.right.right = Node(5)


    sol = Solution()
    print(sol.KDistanceNodes(root, 5, 1))

    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    root.right.right.right = Node(4)
    root.right.right.right.left = Node(5)


    sol = Solution()
    print(sol.KDistanceNodes(root, 5, 4))