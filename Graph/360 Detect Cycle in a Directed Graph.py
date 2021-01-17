from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, starting_vertex, end_vertex):
        self.graph[starting_vertex].append(end_vertex)
    
    def isCyclic(self):
        visitedVertices = defaultdict(bool)
        recursionStack = defaultdict(bool)

        FLAG = False

        for u in list(self.graph):
            if FLAG == True:
                return True

            if visitedVertices[u] == False:
                FLAG |= self.dfsUtil(u, visitedVertices, recursionStack)  
        return False


    def dfsUtil(self, starting_vertex, visitedVertices, recursionStack):
        recursionStack[starting_vertex] = True
        visitedVertices[starting_vertex] = True


        for vertex in self.graph[starting_vertex]:
            if visitedVertices[vertex] == False:
                res = self.dfsUtil(vertex, visitedVertices, recursionStack)
                if res == True:
                    return True
                    
            if recursionStack[vertex] == True:
                return True
        
        recursionStack[starting_vertex] = False
        return False


g = Graph()
g.addEdge('A','B')
g.addEdge('B','C')
g.addEdge('A','C')
g.addEdge('B','D')
g.addEdge('D','E')
g.addEdge('E','B')

g.addEdge('B','A')
g.addEdge('C','B')
g.addEdge('C','A')
g.addEdge('D','B')
g.addEdge('E','D')
g.addEdge('B','E')

res = g.isCyclic()
print(res)