# Given a Directed Acyclic Graph of V vertices from 0 to n-1 and a 2D Integer array(or vector) edges[ ][ ] of length E, where there is a directed edge from edge[i][0] to edge[i][1] with a distance of edge[i][2] for all i.

# Find the shortest path from src(0) vertex to all the vertices and if it is impossible to reach any vertex, then return -1 for that vertex.

# Examples :
# Input: V = 4, E = 2, edges = [[0,1,2], [0,2,1]]
# Output: [0, 2, 1, -1]
# Explanation: Shortest path from 0 to 1 is 0->1 with edge weight 2. Shortest path from 0 to 2 is 0->2 with edge weight 1. There is no way we can reach 3, so it's -1 for 3.

# Input: V = 6, E = 7, edges = [[0,1,2], [0,4,1], [4,5,4], [4,2,2], [1,2,3], [2,3,6], [5,3,1]]
# Output: [0, 2, 3, 6, 1, 5]
# Explanation: Shortest path from 0 to 1 is 0->1 with edge weight 2. Shortest path from 0 to 2 is 0->4->2 with edge weight 1+2=3. Shortest path from 0 to 3 is 0->4->5->3 with edge weight 1+4+1=6. Shortest path from 0 to 4 is 0->4 with edge weight 1.Shortest path from 0 to 5 is 0->4->5 with edge weight 1+4=5.

# Constraint:
# 1 <= V <= 100
# 1 <= E <= min((N*(N-1))/2,4000)
# 0 <= edgesi,0, edgesi,1 < n
# 0 <= edgei,2 <=10^5

from typing import List

class Graph:
    def __init__(self, V):
        self.graph = {i: [] for i in range(V)}
    
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))

    def dfs(self, vertex, visited, order):
        visited.add(vertex)
        
        for neighbour, weight in self.graph[vertex]:
            if neighbour not in visited:
                self.dfs(neighbour, visited, order)
                
        order.append(vertex)

    def topologicalSort(self):
        visited = set()
        order = []

        for vertex in self.graph:
            if vertex not in visited:
                self.dfs(vertex, visited, order)
        
        return order[::-1]
    

class Solution:

    def shortestPath(self, V: int, E: int, edges: List[List[int]]) -> List[int]:
        graph = Graph(V)

        for u, v, w in edges:
            graph.addEdge(u, v, w)

        order = graph.topologicalSort()
        dist = [float('inf')] * V
        dist[0] = 0

        for i in range(V - 1):
            node = order[i]

            for neighbour, weight in graph.graph[node]:
                currWeight = dist[neighbour]
                newWeight = dist[node] + weight

                if  currWeight > newWeight:
                    dist[neighbour] = newWeight
        
        for i in range(V):
            if dist[i] == float('inf'):
                dist[i] = -1
        return dist            
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)


if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestPath(4, 2, [[0,1,2], [0,2,1]]))
    print(sol.shortestPath(6, 7, [[0,1,2], [0,4,1], [4,5,4], [4,2,2], [1,2,3], [2,3,6], [5,3,1]]))
