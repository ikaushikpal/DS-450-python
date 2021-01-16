from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, starting_vertex, end_vertex):
        self.graph[starting_vertex].append(end_vertex)
    
    def dfs(self, starting_vertex):
        visitedVertices = defaultdict(bool)
        vertices = self.graph.keys()

        for u in list(self.graph):
            if visitedVertices[u] == False:
                self.dfsUtil(u, visitedVertices)  
    

    def dfsUtil(self, starting_vertex, visitedVertices):
        visitedVertices[starting_vertex] = True
        print(starting_vertex,end=', ')

        for vertex in self.graph[starting_vertex]:
            if visitedVertices[vertex] == False:
                self.dfsUtil(vertex, visitedVertices)



g = Graph()
g.addEdge('A','B')
g.addEdge('B','D')
g.addEdge('A','C')
g.addEdge('C','D')
# g.addEdge('D','E')
# g.addEdge('E','F')
g.graph['G'] = []
g.dfs('A')