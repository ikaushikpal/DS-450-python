# Given two binary trees, the task is to check if each of their levels are anagrams of each other or not. 


# Example 1:
# Input:
# Output: 1
# Explanation: 
# Tree 1:
# Level 0 : 1
# Level 1 : 3, 2
# Level 2 : 5, 4

# Tree 2:
# Level 0 : 1
# Level 1 : 2, 3
# Level 2 : 4, 5

# As we can clearly see all the levels of above two binary trees 
# are anagrams of each other, hence return true.



from typing import Optional
from collections import deque, defaultdict


# definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def areAnagrams(self, node1 : Optional['Node'], node2 : Optional['Node']) -> bool:
        if not node1 and not node2:
            return True
        
        if (node1 and not node2) or (not node1 and node2):
            return False
            
        queue1, queue2 = deque([node1]), deque([node2])
        while queue1 and queue2:
            if len(queue1) != len(queue2):
                return False
                
            mark1 = defaultdict(int)
            mark2 = defaultdict(int)
            
            for _ in range(len(queue1)):
                curr1 = queue1.popleft()
                curr2 = queue2.popleft()
                
                mark1[curr1.data] += 1
                mark2[curr2.data] += 1
                
                if curr1.left:
                    queue1.append(curr1.left)
                if curr1.right:
                    queue1.append(curr1.right)
                    
                if curr2.left:
                    queue2.append(curr2.left)
                if curr2.right:
                    queue2.append(curr2.right)
            
            if mark1 != mark2:
                return False
        return True
# Time Complexity: O(M + N)
# Space Complexity: O(M + N)