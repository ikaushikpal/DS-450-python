# Given the root of a binary tree, return the maximum width of the given tree.

# The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

# It is guaranteed that the answer will in the range of a 32-bit signed integer.

 

# Example 1:
# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

# Example 2:
# Input: root = [1,3,2,5,null,null,9,6,null,7]
# Output: 7
# Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

# Example 3:
# Input: root = [1,3,2,5]
# Output: 2
# Explanation: The maximum width exists in the second level with length 2 (3,2).
 

# Constraints:
# The number of nodes in the tree is in the range [1, 3000].
# -100 <= Node.val <= 100
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, depth, pos):
        if root is None:
            return 
        
        if depth not in self.width:
            self.width[depth] = (pos, pos)

        left_pos = 2 * pos 
        right_pos = 2 * pos + 1
        
        self.dfs(root.left, depth + 1, left_pos)
        self.dfs(root.right, depth + 1, right_pos)

        minn, maxx = self.width[depth]
        minn = min(minn, pos)
        maxx = max(maxx, pos)

        current_width = maxx - minn + 1
        self.max_width = max(self.max_width, current_width)
        
        self.width[depth] = (minn, maxx)


    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.width = {}
        self.max_width = 0
        self.dfs(root, 0, 1)
        return self.max_width
# Time Complexity: O(N)
# Space Complexity: O(N)


# Helper function to build a binary tree from level-order list
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root


# === Test Cases ===
if __name__ == '__main__':
    sol = Solution()

    tree1 = build_tree([1, 3, 2, 5, 3, None, 9])
    print(sol.widthOfBinaryTree(tree1))  # Expected: 4

    tree2 = build_tree([1, 3, 2, 5, None, None, 9, 6, None, 7])
    print(sol.widthOfBinaryTree(tree2))  # Expected: 7

    tree3 = build_tree([1, 3, 2, 5])
    print(sol.widthOfBinaryTree(tree3))  # Expected: 2

    tree4 = build_tree([1])
    print(sol.widthOfBinaryTree(tree4))  # Expected: 1

    tree5 = build_tree([1, 2, None, 3, None, 4])
    print(sol.widthOfBinaryTree(tree5))  # Expected: 1
