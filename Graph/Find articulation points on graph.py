from collections import defaultdict
from dataclasses import dataclass


class Info():
    inTime:int=None
    lowTime:int=None

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.timer = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self, currentVertex, parentVertex, visited, info, articulationPoints):
        visited[currentVertex] = True
        info[currentVertex].inTime = info[currentVertex].lowTime = self.timer
        self.timer += 1

        for neighbour in self.graph[currentVertex]:
            if parentVertex == neighbour:
                continue # just a edge to its parent

            elif visited[neighbour]:# meaning it found a back edge
                info[currentVertex].lowTime = min(info[currentVertex].lowTime, info[neighbour].inTime)
                # update backedges property

            else: #forwards edge
                self.dfs(neighbour, currentVertex, visited, info, articulationPoints)
                if parentVertex is not None and info[currentVertex].inTime <= info[neighbour].lowTime:
                    # find bridge condition(<) and cycle(==)
                    articulationPoints.append(currentVertex)
                info[currentVertex].lowTime = min(info[currentVertex].lowTime, info[neighbour].lowTime)

        if parentVertex is None and len(self.graph[currentVertex]) > 1:
            articulationPoints.append(currentVertex)


    def  printArticulationPoints(self, articulationPoints):
        if len(articulationPoints) == 0:
            print("Graph do not contain any articulation Points")
            return
        print("Total number of articulation Points in graph are :",len(articulationPoints))
        print("Those vertices are : ",end='')
        for u in articulationPoints:
            print(u,end=', ')
        print()

    def findArticulationPoints(self):
        visited = defaultdict(bool)
        info = defaultdict(Info)
        articulationPoints = []

        for vertex in self.graph:
            if visited[vertex] == False:
                self.dfs(vertex, None, visited, info, articulationPoints)
        
        self.printArticulationPoints(articulationPoints)


if __name__ == "__main__":
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(3, 2)
    g.addEdge(4, 2)
    g.addEdge(3, 4)

    g.findArticulationPoints()