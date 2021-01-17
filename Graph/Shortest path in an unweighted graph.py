from collections import defaultdict, deque, namedtuple
from dataclasses import dataclass


@dataclass
class Info:
    visited: bool = False
    distance: int = 0
    parentVertex: str = None


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, starting_vertex, end_vertex):
        self.graph[starting_vertex].append(end_vertex)

    def printDistance(self, starting_vertex, ending_vertex, vertexInfo):
        paths = deque()

        paths.append(ending_vertex)
        totalDistance = vertexInfo[ending_vertex].distance
        current = ending_vertex

        while vertexInfo[current].parentVertex:
            paths.append(vertexInfo[current].parentVertex)
            current = vertexInfo[current].parentVertex

        print(
            f"from {starting_vertex} to {ending_vertex}, there exist path and it cost = {totalDistance}"
        )
        print("Path : ",end='')

        while len(paths):
            if len(paths) == 1:
                print(paths.pop())
            else:
                print(paths.pop(), end="->")

    def shortestDistance(self, starting_vertex, ending_vertex):
        vertexInfo = defaultdict(Info)
        queue = deque()

        queue.append(starting_vertex)
        vertexInfo[starting_vertex] = Info(True, 0, None)
        FLAG = False

        while len(queue):
            currentVertex = queue.popleft()
            if currentVertex == ending_vertex:
                FLAG = True
                break

            for neighbour in self.graph[currentVertex]:
                if vertexInfo[neighbour].visited == False:
                    queue.append(neighbour)

                    currentDistance = vertexInfo[currentVertex].distance + 1
                    vertexInfo[neighbour] = Info(True, currentDistance, currentVertex)

        if FLAG:
            self.printDistance(starting_vertex, ending_vertex, vertexInfo)
        else:
            print(f"from {starting_vertex} to {ending_vertex}, there is no path")


g = Graph()
g.addEdge("A", "B")
g.addEdge("B", "C")
g.addEdge("A", "G")
g.addEdge("G", "H")
g.addEdge("H", "C")
g.addEdge("C", "D")
g.addEdge("H", "F")
g.addEdge("D", "E")

g.shortestDistance("A", "F")
