from collections import defaultdict
from dataclasses import dataclass
import sys
import heapq
from runTime import * 


@dataclass
class Info():
    visited : bool = False
    weight:int = sys.maxsize
    parent:int = None


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    # making undirected weighted graph
    def addEdge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def printMST(self, vertexInfo):
        total_cost = 0
        print("Generating paths fot MST")
        for vertex in vertexInfo:
            parentVertex = vertexInfo[vertex].parent
            if parentVertex is not None:
                currentVertex = vertex
                edgeWeight = vertexInfo[vertex].weight
                total_cost += edgeWeight
                print(f"{parentVertex} -> {currentVertex} = {edgeWeight}")
        print(f"total cost of MST = {total_cost}")

    @runTime
    def primsAlgorithm(self, source=0):
        heap = []
        vertexInfo = defaultdict(Info)
        
        vertexInfo[source].weight = 0
        heapq.heappush(heap, (0, source))
        while len(heap): 
            min_vertex = heapq.heappop(heap)[1]
            if vertexInfo[min_vertex].visited:
                continue

            vertexInfo[min_vertex].visited = True

            for neighbour, weight in self.graph[min_vertex]:
                if not vertexInfo[neighbour].visited and vertexInfo[neighbour].weight > weight:
                    vertexInfo[neighbour].weight = weight
                    vertexInfo[neighbour].parent = min_vertex
                    heapq.heappush(heap, (weight, neighbour))
            
        self.printMST(vertexInfo)


if __name__ == "__main__":
    graph = Graph() 
    graph.addEdge(0, 1, 4) 
    graph.addEdge(0, 7, 8) 
    graph.addEdge(1, 2, 8) 
    graph.addEdge(1, 7, 11) 
    graph.addEdge(2, 3, 7) 
    graph.addEdge(2, 8, 2) 
    graph.addEdge(2, 5, 4) 
    graph.addEdge(3, 4, 9) 
    graph.addEdge(3, 5, 14) 
    graph.addEdge(4, 5, 10) 
    graph.addEdge(5, 6, 2) 
    graph.addEdge(6, 7, 1) 
    graph.addEdge(6, 8, 6) 
    graph.addEdge(7, 8, 7) 

    graph.primsAlgorithm(2) 