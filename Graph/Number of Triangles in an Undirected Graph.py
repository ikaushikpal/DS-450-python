# Given a Graph, count number of triangles in it. The graph is can be directed or undirected.

# Example: 

# Input: digraph[V][V] = { {0, 0, 1, 0},
#                         {1, 0, 0, 1},
#                         {0, 1, 0, 0},
#                         {0, 0, 1, 0}
#                       };
# Output: 2
# Give adjacency matrix represents following 
# directed graph.

# in an undirected graph, the triplet (i, j, k) can be permuted to give six combination (See previous post for details). Hence we divide the total count by 6 to get the actual number of triangles. 
# In case of directed graph, the number of permutation would be 3 (as order of nodes becomes relevant). Hence in this case the total number of triangles will be obtained by dividing total count by 3

from typing import List


class Graph:
    pass


class Solution:
    def findTriangles(self, graph: List[List[int]]) -> int:
        count = 0
        for i in range(len(graph)):
            for j in range(len(graph)):
                for k in range(len(graph)):
                    if i != j and i != k and j != k and graph[i][j] == 1 and graph[i][k] == 1 and graph[j][k] == 1:
                        count += 1
        
        return count // 3

    def findTrianglesAdjList(self, graph: Graph) -> int:
        count = 0
        for u in graph.graph:
            for v in graph.graph[u]:
                for w in graph.graph[v]:
                    if u != v and u != w and v != w and u in graph.graph[w]:
                        count += 1
        
        return count // 3
        
