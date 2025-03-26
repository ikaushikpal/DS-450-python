from collections import defaultdict
from dataclasses import dataclass
import sys


@dataclass
class Info():
    visited : bool = False
    weight:int = sys.maxsize
    parent:int = None


class Graph:
    def __init__(self, graph):
        self.graph = graph

    def setelectMinimumEdge(self, vertexInfo):
        minDist = sys.maxsize
        for vertex in vertexInfo:
            if vertexInfo[vertex].weight < minDist and vertexInfo[vertex].visited == False:
                minDist = vertexInfo[vertex].weight
                vertex_id = vertex
        return vertex_id

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

    def primsAlgorithm(self, source=0):
        vertexInfo = defaultdict(Info)
        vertexInfo[source].weight = 0
        total_vertices = len(self.graph)
        for i in range(total_vertices):
            min_vertex = self.setelectMinimumEdge(vertexInfo)
            vertexInfo[min_vertex].visited = True

            for j in range(total_vertices): 
                if self.graph[min_vertex][j] !=0 and not vertexInfo[j].visited and vertexInfo[j].weight > self.graph[min_vertex][j]:
                    vertexInfo[j].weight = self.graph[min_vertex][j]
                    vertexInfo[j].parent = min_vertex
        
        self.printMST(vertexInfo)



if __name__ == "__main__":
    mat = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 

    g = Graph(mat) 
    g.primsAlgorithm(4)