# Given a Directed Graph, find a Mother Vertex in the Graph (if present). 
# A Mother Vertex is a vertex through which we can reach all the other vertices of the Graph.
 

# Example 1:
# Input: 
# Output: 0
# Explanation: According to the given edges, all 
# nodes can be reaced from nodes from 0, 1 and 2. 
# But, since 0 is minimum among 0,1 and 3, so 0 
# is the output.



# Example 2:
# Input: 
# Output: -1
# Explanation: According to the given edges, 
# no vertices are there from where we can 
# reach all vertices. So, output is -1.

#NOTE:
# How to find mother vertex? 

# Case 1:- Undirected Connected Graph : In this case, all the vertices are mother vertices as we can reach to all the other nodes in the graph.
# Case 2:- Undirected/Directed Disconnected Graph : In this case, there is no mother vertices as we cannot reach to all the other nodes in the graph.
# Case 3:- Directed Connected Graph : In this case, we have to find a vertex -v in the graph such that we can reach to all the other nodes in the graph through a directed path.


from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortUtil(self, node, visited, order):
        visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.topologicalSortUtil(neighbor, visited, order)
        order.append(node)

    def topologicalSort(self):
        order = deque()
        visited = set()
        for node in self.graph:
            if node not in visited:
                self.topologicalSortUtil(node, visited, order)
        return order

    def dfs(self, node, visited):
        visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def findMother(self):
        order = self.topologicalSort()
        possibleMotherVertex = order.pop()
        visited = set()
        self.dfs(possibleMotherVertex, visited)
        return possibleMotherVertex if len(visited) == len(self.graph) else -1
# Time Complexity : O(V+E)
# Space Complexity : O(V)


class Solution:
    def findMotherVertex(self, V, adj):   
        graph = Graph()
        for i in range(V):
            graph.graph[i] = adj[i]

        return graph.findMother()


if __name__ == "__main__":
    V = 4
    adj = [[1, 2], [2, 3], [3, 0], [0, 1]]
    print(Solution().findMotherVertex(V, adj))

    V = 5
    adj = [[1, 2], [2, 3], [3, 4], [4, 0], [0, 1]]
    print(Solution().findMotherVertex(V, adj))