from collections import defaultdict
from dataclasses import dataclass

@dataclass
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
        child = 0

        for neighbour in self.graph[currentVertex]:
            if parentVertex == neighbour:
                continue # just a edge to its parent

            if visited[neighbour] == False:
                child += 1
                self.dfs(neighbour, currentVertex, visited, info, articulationPoints)
                info[currentVertex].lowTime = min(info[currentVertex].lowTime, info[neighbour].lowTime)

                if parentVertex is None and child > 1:
                    articulationPoints.add(currentVertex)
                
                if parentVertex is not None and info[neighbour].lowTime >= info[currentVertex].inTime:
                    articulationPoints.add(currentVertex)
            
            else:
                info[currentVertex].lowTime = min(info[currentVertex].lowTime, info[neighbour].inTime)


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
        articulationPoints = set()

        for vertex in list(self.graph):
            if visited[vertex] == False:
                self.dfs(vertex, None, visited, info, articulationPoints)
        
        self.printArticulationPoints(articulationPoints)


if __name__ == "__main__":
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    g.addEdge(5, 7)
    g.addEdge(6, 7)
    g.addEdge(6, 8)

    g.findArticulationPoints()