# A Clique is a subgraph of graph such that all vertices in subgraph are completely connected with each other. Given a Graph, find if it can be divided into two Cliques.


# Examples:
# Input : G[][] =   {{0, 1, 1, 0, 0},
#                   {1, 0, 1, 1, 0},
#                   {1, 1, 0, 0, 0},
#                   {0, 1, 0, 0, 1},
#                   {0, 0, 0, 1, 0}};
# Output : Yes
# graph divided in two cliques

# AS {0, 1, 2} and {3, 4}

# This problem looks tricky at first, but has a simple and interesting solution. A graph can be divided in two cliques if its complement graph is Bipartitite


class Graph:
    def __init__(self, V, graph):
        self.adjMat = graph
        self.V = V
    
    def complementGraph(self):
        compAgjMat = [[0]*self.V for _ in range(self.V)]

        for i in range(self.V):
            for j in range(self.V):
                if i != j and self.adjMat[i][j] == 0:
                    compAgjMat[i][j] = 1

        return Graph(self.V, compAgjMat)

    def dfs(self, u, color, colors):
        colors[u] = color
        self.coloredVertices += 1
        compColor = 0 if color == 1 else 1
    
        for v in range(self.V):
            if u != v and self.adjMat[u][v]:
                if colors[v] is None:
                    return self.dfs(v, compColor, colors)

                elif colors[v] == color:
                    return False
        
        return True

    def isBipartite(self):
        colors = [None] * self.V
        self.coloredVertices = 0
        
        for u in range(self.V):
            if colors[u] is None:
                if not self.dfs(u, 0, colors):
                    return False

            if self.coloredVertices == self.V:
                break

        return True

    def checkTwoClique(self):
        gT = self.complementGraph()
        return gT.isBipartite()


if __name__ == '__main__':
    g = Graph(5,[[0, 1, 1, 1, 0],
                [1, 0, 1, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 1, 0]])
    print(g.checkTwoClique())
