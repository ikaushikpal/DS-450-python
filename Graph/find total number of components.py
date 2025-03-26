from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, starting_vertex, end_vertex):
        self.graph[starting_vertex].append(end_vertex)

    def totalComponents(self):
        visitedVertices = defaultdict(bool)
        no_components = defaultdict(list)
        count = 0

        for u in list(self.graph):
            if visitedVertices[u] == False:
                count += 1
                self.__totalComponentsUtil(u, visitedVertices, no_components[count])

        return no_components

    def __totalComponentsUtil(self, starting_vertex, visitedVertices, array):
        visitedVertices[starting_vertex] = True
        array.append(starting_vertex)

        for vertex in self.graph[starting_vertex]:
            if visitedVertices[vertex] == False:
                self.__totalComponentsUtil(vertex, visitedVertices, array)


g = Graph()
g.addEdge("A", "B")
g.addEdge("B", "D")
g.addEdge("A", "C")
g.addEdge("C", "D")
g.addEdge("D", "E")
g.addEdge("E", "F")
g.graph["G"] = []
g.graph["I"] = []
g.graph["X"] = []

res = g.totalComponents()
print(res)
