from collections import defaultdict
import heapq
from runTime import runTime
from DisjointSetData import Disjoint


class Graph:
    def __init__(self, totalVertices):
        self.graph = defaultdict(list)
        self.totalVertices = totalVertices

    def addEdge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def printMST(self, paths):
        total_cost = 0
        print("Generating paths for MST <Kruskal Method>")
        for item in paths:
            u, v, weight = item
            total_cost += weight
            print(f"{u} -> {v} = {weight}")
        print(f"total cost of MST = {total_cost}")

    @runTime
    def kruskalAlgorithm(self):
        heap = []
        paths = []
        disjointSet = Disjoint(self.totalVertices)

        for vertex in list(self.graph):
            for neighbour, weight in self.graph[vertex]:
                heapq.heappush(heap, (weight, vertex, neighbour))
        included_edges = 0

        while len(heap):
            if included_edges == self.totalVertices - 1:
                break
            weight, u, v = heapq.heappop(heap)
            myTuple = (u, v, weight)
            res = disjointSet.union(u, v)
            if res:
                paths.append(myTuple)
                included_edges += 1
        del heap
        self.printMST(paths)


if __name__ == "__main__":
    graph = Graph(8)
    graph.addEdge(1, 2, 28)
    graph.addEdge(1, 6, 10)
    graph.addEdge(3, 2, 16)
    graph.addEdge(3, 4, 12)
    graph.addEdge(2, 7, 14)
    graph.addEdge(7, 4, 18)
    graph.addEdge(7, 5, 24)
    graph.addEdge(4, 5, 22)
    graph.addEdge(6, 5, 25)

    graph.kruskalAlgorithm()
