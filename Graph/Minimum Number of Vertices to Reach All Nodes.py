# Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

# Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

# Notice that you can return the vertices in any order.

 
# Example 1:
# Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
# Output: [0,3]
# Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].


# Example 2:
# Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
# Output: [0,2,3]
# Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.


from typing import List

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
    
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topologicalSort(self) -> List[int]:
        visited = [False] * self.n
        stack = []

        for i in range(self.n):
            if not visited[i]:
                self.dfs(i, visited, stack)

        return stack[::-1]

    def dfs(self, u, visited, stack):
        visited[u] = True

        for v in self.graph[u]:
            if not visited[v]:
                self.dfs(v, visited, stack)

        if stack is not None:
            stack.append(u)

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        g = Graph(n)
        for u, v in edges:
            g.add_edge(u, v)

        order = g.topologicalSort()
        minimumVertices = []
        visited = [False] * n

        for u in order:
            if not visited[u]:
                g.dfs(u, visited, None) 
                minimumVertices.append(u)

        return minimumVertices
# Time Complexity : O(V + E)
# Space Complexity : O(V + E)


# Best Solution
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # only find 0 inDegree vertices
        inDegree = [0] * n
        for _, v in edges:
            inDegree[v] += 1
        
        return [i for i in range(n) if inDegree[i] == 0]
# Time Complexity : O(V + E)
# Space Complexity : O(V)


if __name__ == '__main__':
    s = Solution()
    print(s.findSmallestSetOfVertices(n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]))
    print(s.findSmallestSetOfVertices(n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]))
