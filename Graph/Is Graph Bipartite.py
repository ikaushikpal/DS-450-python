# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

# Return true if and only if it is bipartite.

 

# Example 1:
# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.



# Example 2:
# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.


from collections import defaultdict, deque
from typing import List


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, starting_vertex, end_vertex):
        self.graph[starting_vertex].append(end_vertex)
    
    #coloring method
    def isBipartite(self):
        visitedVertices = defaultdict(int)
        queue = deque()

        for u in list(self.graph):
            if visitedVertices[u] == 0:
                visitedVertices[u] = 1
                queue.append(u)

                if not self.isBipartiteUtil(queue, visitedVertices):
                    return False

        return True

    def isBipartiteUtil(self, queue, visitedVertices):
        while queue:
            currentNode = queue.popleft()

            for neighbour in self.graph[currentNode]:
                # self loop is not allowed
                if neighbour == currentNode:
                    return False
                
                if visitedVertices[neighbour] == 0:
                    queue.append(neighbour)
                    # assigning opposite color to neighbour
                    if visitedVertices[currentNode]==1:
                        visitedVertices[neighbour] = 2
                    else:
                        visitedVertices[neighbour] = 1
                
                # if neighbour is already colored with same color as current node
                elif visitedVertices[neighbour] == visitedVertices[currentNode]:
                    return False

        return True
    
    
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        graphObj = Graph()
        
        for u in range(len(graph)):
            graphObj.graph[u] = graph[u]
                
        
        return graphObj.isBipartite()
# Time Complexity: O(V+E)
# Space Complexity: O(V+E)


if __name__ == '__main__':
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    print(Solution().isBipartite(graph))

    graph = [[1,3],[0,2],[1,3],[0,2]]
    print(Solution().isBipartite(graph))
