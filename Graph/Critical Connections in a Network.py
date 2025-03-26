# There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

# A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

# Return all critical connections in the network in any order.

 
# Example 1:
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.


# Example 2:
# Input: n = 2, connections = [[0,1]]
# Output: [[0,1]]


from collections import defaultdict
from typing import List


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.clock = 1
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def findBridges(self, u, parent, visited, intime, lowtime, ans):
        visited[u] = True
        intime[u] = lowtime[u] = self.clock
        self.clock += 1
        
        for v in self.graph[u]:
            if v == parent:
                continue
            
            if visited[v]:
                lowtime[u] = min(lowtime[u], intime[v])
            else:
                self.findBridges(v, u, visited, intime, lowtime, ans)
                lowtime[u] = min(lowtime[u], lowtime[v])
                if intime[u] < lowtime[v]:
                    ans.append([u, v])
                
        
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = Graph()
        for u, v in connections:
            g.addEdge(u, v)
            g.addEdge(v, u)
            
        visited = [False] * n
        intime = [float('inf')] * n
        lowtime = [float('inf')] * n
        bridges = []
        
        for u in range(n):
            if not visited[u]:
                g.findBridges(u, None, visited, intime, lowtime, bridges)
        return bridges
# Time complexity : O(V+E)
# Space complexity : O(V+E)
# where V = number of vertices in the graph and E = number of edges in the graph.


if __name__ == "__main__":
    s = Solution()
    print(s.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))
    print(s.criticalConnections(2, [[0,1]]))