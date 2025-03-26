# Given N nodes of a tree and a list of edges. Find the minimum number of nodes to be selected to light up all the edges of the tree.
# An edge lights up when at least one node at the end of the edge is selected.


# Example 1:
# Input:
# N = 6
# edges[] = {(1,2), (1,3), (2,4), (3,5), (3,6)}
# Output: 2
# Explanation: Selecting nodes 2 and 3 lights
# up all the edges.


# Example 2:
# Input:
# N = 3
# arr[] = {(1,2), (1,3)}
# Output: 1
# Explanation: Selecting Node 1 
# lights up all the edges.


class Solution:
    def builtTree(self, edges, N):
        tree = {i:[] for i in range(1, N+1)}
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        return tree
    
    def dfs(self, currNode, seen, tree):
        if currNode in seen:
            return (0, 0)
        
        seen.add(currNode)
        
        prevLight = prevNotLight = 0
        for child in tree[currNode]:
            res = self.dfs(child, seen, tree)
            prevLight += res[0]
            prevNotLight += min(res)
        
        return (prevNotLight+1, prevLight)
        
    def countVertex(self, N, edges):
        tree = self.builtTree(edges, N)
        seen = set()
        return min(self.dfs(1, seen, tree))
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countVertex([(1,2), (1,3), (2,4), (3,5), (3,6)], 6))
    print(sol.countVertex([(1,2), (1,3)], 3))