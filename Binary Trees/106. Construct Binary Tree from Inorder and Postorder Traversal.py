# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.


# Example 1:
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
 

# Constraints:
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def dfs(self, post_i, post_j, in_i, in_j, post, in_d):
        if post_i > post_j:
            return None
        
        if post_i == post_j:
            return TreeNode(post[post_j])

        root = TreeNode(post[post_j])
        in_idx = in_d[root.val]
        dist = in_idx - in_i

        root.left = self.dfs(post_i, post_i+dist-1,  in_i, in_idx - 1,  post, in_d)
        root.right = self.dfs(post_i+dist, post_j - 1, in_idx + 1, in_j, post, in_d)

        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        in_d = {val:i for i, val in enumerate(inorder)}
        return self.dfs(0, len(postorder)-1, 0, len(postorder)-1, postorder, in_d)
# Time Complexity: O(N)
# Space Complexity: O(N)



if __name__ == '__main__':
    sol = Solution()
    print(sol.buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]))
    print(sol.buildTree(inorder = [-1], postorder = [-1]))