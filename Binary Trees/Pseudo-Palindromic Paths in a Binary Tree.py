# Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.
# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.


# Example 1:
# Input: root = [2,3,1,3,1,null,1]
# Output: 2 
# Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).


# Example 2:
# Input: root = [2,1,1,1,3,null,null,null,null,null,1]
# Output: 1 
# Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).


# Example 3:
# Input: root = [9]
# Output: 1



# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def helper(self, root, evenFreq, oddFreq, freq):
        if root is None:
            return 0

        oldFreq = freq.get(root.val, 0)
        if oldFreq > 0 and oldFreq & 1:
            oddFreq -= 1

        elif oldFreq > 0 and not oldFreq & 1:
            evenFreq -= 1

        freq[root.val] = freq.get(root.val, 0) + 1
        if freq[root.val] & 1:
            oddFreq += 1
        else:
            evenFreq += 1

        retValue = 1 if not root.left and not root.right and oddFreq <= 1 else 0
        ans = self.helper(root.left, evenFreq, oddFreq, freq)
        ans += self.helper(root.right, evenFreq, oddFreq, freq)

        freq[root.val] -= 1
        return ans + retValue

    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0, 0, {})
# T.C. = O(N)
# S.C. = O(10 + H) = O(H)

