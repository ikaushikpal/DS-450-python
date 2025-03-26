from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, starting_vertex, end_vertex):
        self.graph[starting_vertex].append(end_vertex)

    def isCyclic(self):
        visitedVertices = defaultdict(bool)

        FLAG = False

        for u in list(self.graph):
            if FLAG == True:
                return True

            if visitedVertices[u] == False:
                FLAG |= self.dfsUtil(u, visitedVertices, None)
        return False

    def dfsUtil(self, current_vertex, visitedVertices, parent_vertex):
        visitedVertices[current_vertex] = True

        for vertex in self.graph[current_vertex]:
            if visitedVertices[vertex] == False:
                if self.dfsUtil(vertex, visitedVertices, current_vertex) == True:
                    return True

            elif parent_vertex != vertex:
                return True
        return False


if __name__ == "__main__":
    g = Graph()

    g.addEdge("A", "F")
    g.addEdge("F", "A")
    g.addEdge("A", "B")
    g.addEdge("B", "A")
    g.addEdge("B", "C")
    g.addEdge("C", "B")
    g.addEdge("E", "B")
    g.addEdge("B", "E")
    g.addEdge("D", "C")
    g.addEdge("C", "D")
    g.addEdge("D", "E")
    g.addEdge("E", "D")

    res = g.isCyclic()
    print(f"Graph is cyclic ? {res}")
