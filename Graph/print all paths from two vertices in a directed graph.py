from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, starting_vertex, end_vertex):
        self.graph[starting_vertex].append(end_vertex)

    def printAllPaths(self, starting_vertex, target_vertex):
        visitedVertices = defaultdict(bool)
        self.resultPaths = []

        self.dfsUtil(starting_vertex, visitedVertices, target_vertex, "")
        return self.resultPaths

    def dfsUtil(self, current_vertex, visitedVertices, target_vertex, output_string):
        visitedVertices[current_vertex] = True

        if output_string == "":
            output_string = current_vertex
        else:
            output_string = output_string + "->" + current_vertex

        if current_vertex == target_vertex:
            self.resultPaths.append(output_string)
            return

        for vertex in self.graph[current_vertex]:
            if visitedVertices[vertex] == False:
                self.dfsUtil(vertex, visitedVertices, target_vertex, output_string)
                visitedVertices[vertex] = False


if __name__ == "__main__":
    g = Graph()
    g.addEdge("A", "B")
    g.addEdge("B", "D")
    g.addEdge("A", "D")
    g.addEdge("C", "A")
    g.addEdge("C", "B")
    g.addEdge("A", "C")

    paths = g.printAllPaths("A", "B")
    print(paths)
