# Given the root of a binary tree, each node in the tree has a distinct value.

# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

# Return the roots of the trees in the remaining forest. You may return the result in any order.


# Example 1:
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]

# Example 2:
# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]


# Constraints:
# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, root, target_nodes):
        if root is None:
            return None

        root.left = self.dfs(root.left, target_nodes)
        root.right = self.dfs(root.right, target_nodes)

        if root.val in target_nodes:
            target_nodes.remove(root.val)

            if root.left: self.forest.append(root.left)
            if root.right: self.forest.append(root.right)

            return None
        return root

    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        target_nodes = set(to_delete)
        self.forest = []

        if self.dfs(root, target_nodes):
            self.forest.append(root)

        return self.forest
# Time Complexity: O(N)
# Space Complexity: O(H + N)
