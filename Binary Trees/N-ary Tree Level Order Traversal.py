# Given an n-ary tree, return the level order traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 
# Example 1:
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]


# Example 2:
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]



# Definition for a Node.
from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque()
        res = []
        queue.append(root)
        
        while len(queue) > 0:
            temp = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                temp.append(curr.val)
                
                for child in curr.children:
                    queue.append(child)
            res.append(temp)
            
        return res
            

if __name__ == '__main__':
    sol = Solution()
    root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    print(sol.levelOrder(root))