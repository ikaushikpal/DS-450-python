# You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

# You are also given a string s of length n, where s[i] is the character assigned to node i.

# Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.

 

# Example 1:
# Input: parent = [-1,0,0,1,1,2], s = "abacbe"
# Output: 3
# Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
# It can be proven that there is no longer path that satisfies the conditions. 


# Example 2:
# Input: parent = [-1,0,0,0], s = "aabc"
# Output: 3
# Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.



from typing import List
from collections import defaultdict


class Solution:
    def dfs(self, currentNode, tree, s):
        maxx1 = maxx2 = 0

        for child in tree[currentNode]:  
            length = self.dfs(child, tree, s)
            
            if s[currentNode] == s[child]:
                continue
                
            if length >= maxx1:
                maxx2 = maxx1
                maxx1 = length
            
            elif length > maxx2:
                maxx2 = length
        
        self.ans = max(self.ans, maxx1 + maxx2 + 1)
        return maxx1 + 1

    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        for u, v in enumerate(parent):
            if v == -1:
                continue
            tree[v].append(u)   
        
        self.ans = 0
        self.dfs(0, tree, s)
        return self.ans     
# Time Complexity: o(N)
# Space Complexity: o(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPath(parent = [-1,0,0,1,1,2], s = "abacbe"))
    print(sol.longestPath(parent = [-1,0,0,0], s = "aabc"))

