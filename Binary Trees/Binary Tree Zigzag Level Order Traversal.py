# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).


# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]


# Example 2:
# Input: root = [1]
# Output: [[1]]


# Example 3:
# Input: root = []
# Output: []


# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        ans = []
        queue = deque([root])
        
        while queue:
            temp = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                temp.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
            
            if len(ans) & 1:
                temp = temp[::-1]
            ans.append(temp)
        return ans
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.zigzagLevelOrder([3,9,20,null,null,15,7]))
    print(sol.zigzagLevelOrder([1]))
    print(sol.zigzagLevelOrder([]))