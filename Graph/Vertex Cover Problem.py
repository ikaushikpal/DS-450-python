from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def buildEdgeSet(self):
        for u in list(self.graph):
            for v in self.graph[u]:
                self.edgeSet.add((u, v))

    def removeEdgesUtil(self, u):
        for v in self.graph[u]:
            x = (u, v)
            y = (v, u)

            if x in self.edgeSet:
                self.edgeSet.remove(x)

            if y in self.edgeSet:
                self.edgeSet.remove(y)

    def addEdgesUtil(self, u):
        for v in self.graph[u]:
            x = (u, v)
            y = (v, u)
            self.edgeSet.add(x)
            self.edgeSet.add(y)

    def vertexCoverDecisionUtil(self, u, k):
        if len(self.edgeSet) == 0:
            return True
        
        if k == 0:
            return False

        self.removeEdgesUtil(u)
        self.visited[u] = True

        for v in self.graph[u]:
            if self.visited[v] == False:
                if self.vertexCoverDecisionUtil(v, k-1):
                    return True

        self.addEdgesUtil(u)
        self.visited[u] = False

        return False

    def vertexCoverDecision(self, k):
        if k >= self.vertices:
            return True

        if k < 0:
            return False

        self.visited = defaultdict(lambda:False)
        self.edgeSet = set()
        self.buildEdgeSet()

        if len(self.edgeSet) == 0:
            return True

        for vertex in list(self.graph):
            if self.visited[vertex]==False:
                if self.vertexCoverDecisionUtil(vertex, k):
                    return True

        return False

if __name__ == '__main__':
    graph = Graph(5)
    graph.addEdge(0, 1)
    graph.addEdge(0, 3)
    graph.addEdge(1, 2)
    graph.addEdge(4, 1)
    graph.addEdge(4, 2)
    graph.addEdge(3, 2)

    print(graph.vertexCover(5))
