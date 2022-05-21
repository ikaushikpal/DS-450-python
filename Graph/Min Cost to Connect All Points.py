# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

# Example 1:
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 

# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.


# Example 2:

# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18

# For better understanding,visit
# https://leetcode.com/problems/min-cost-to-connect-all-points/
# https://www.youtube.com/watch?v=f7JOBJIC-NA


from collections import defaultdict
from dataclasses import dataclass
import sys
from typing import List


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

    def getTotalWeight(self, vertexInfo):
        total_cost = 0

        for vertex in vertexInfo:
            parentVertex = vertexInfo[vertex].parent
            if parentVertex is not None:
                edgeWeight = vertexInfo[vertex].weight
                total_cost += edgeWeight

        return total_cost

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
        
        return self.getTotalWeight(vertexInfo)


class Solution:
    def manhattenDistance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        # generate adjacency matrix
        matrix = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i != j:
                    matrix[i][j] = self.manhattenDistance(points[i], points[j])
        
        graph = Graph(matrix)
        return graph.primsAlgorithm()