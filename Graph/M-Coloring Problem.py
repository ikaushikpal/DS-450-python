# Given an undirected graph and an integer M. The task is to determine if the graph can be colored with at most M colors such that no two adjacent vertices of the graph are colored with the same color. Here coloring of a graph means the assignment of colors to all vertices. Print 1 if it is possible to colour vertices and 0 otherwise.

# Example 1:

# Input:
# N = 4
# M = 3
# E = 5
# Edges[] = {(0,1),(1,2),(2,3),(3,0),(0,2)}
# Output: 1
# Explanation: It is possible to colour the
# given graph using 3 colours.
# Example 2:

# Input:
# N = 3
# M = 2
# E = 3
# Edges[] = {(0,1),(1,2),(0,2)}
# Output: 0
# Your Task:
# Your task is to complete the function graphColoring() which takes the 2d-array graph[], the number of colours and the number of nodes as inputs and returns true if answer exists otherwise false. 1 is printed if the returned value is true, 0 otherwise. The printing is done by the driver's code.
# Note: In Example there are Edges not the graph.Graph will be like, if there is an edge between vertex X and vertex Y graph[] will contain 1 at graph[X-1][Y-1], else 0. In 2d-array graph[ ], nodes are 0-based indexed, i.e. from 0 to N-1.Function will be contain 2-D graph not the edges.

# Expected Time Complexity: O(MN).
# Expected Auxiliary Space: O(N).


class Graph:
    def __init__(self, graph, V, M):
        self.graph = graph
        self.V = V
        self.M = M

    def colorGraph(self):
        # -1 means not visited yet
        colors = [-1] * len(self.graph)

        for i in range(self.M):
            colors[0] = i
            if self.dfs(0, self.V-1, colors):
                return True
        return False

    def isValid(self, u, c, colors):
        for v in range(self.V):
            if self.graph[u][v] and u!=v and colors[v] == c:
                return True
        return False

    def dfs(self, u, dest, colors):
        if u == dest:
            return True

        for c in range(self.M):
            if self.isValid(u, c, colors):
                continue

            colors[u] = c
            if self.dfs(u+1, dest, colors):
                return True
            colors[u] = -1 
            
        return False
        

#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, m, V):
    g = Graph(graph, V, m)
    return g.colorGraph()


if __name__ == '__main__':
    graph = [[0, 1, 0, 1],
             [1, 0, 1, 1],
             [0, 1, 0, 1],
             [1, 1, 1, 0]]
    V = 4
    m = 3
    print(graphColoring(graph, m, V))