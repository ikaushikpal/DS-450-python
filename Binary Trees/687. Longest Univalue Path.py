# Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

# The length of the path between two nodes is represented by the number of edges between them.

 
# Example 1:
# Input: root = [5,4,5,1,1,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value (i.e. 5).

# Example 2:
# Input: root = [1,4,5,4,4,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value (i.e. 4).
 

# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000
# The depth of the tree will not exceed 1000.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root):
        if root is None:
            return None, 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        include_root = include_root_one_side = 1
        exclude_root = 0

        if left[0] == root.val:
            include_root += left[1]
            include_root_one_side = max(include_root_one_side, left[1] + 1)
        else:
            exclude_root = max(exclude_root, left[1])

        if right[0] == root.val:
            include_root += right[1]
            include_root_one_side = max(include_root_one_side, right[1] + 1)
        else:
            exclude_root = max(exclude_root, right[1])

        # print(root.val, include_root, exclude_root, include_root_one_side)
        self.ans = max(self.ans, include_root, exclude_root )
        return root.val, include_root_one_side
        

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root)
        return max(0, self.ans - 1)
# Time Complexity : O(N)
# Space Complexity : O(H)