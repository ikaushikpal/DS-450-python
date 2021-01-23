import heapq
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Info:
    visited : bool=False
    distance : int=999999
    

class Graph:
    INF = 999999
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def printShortestDist(self, source, info):
        for item in info:
            print(f"distance from {source} to {item} = {info[item].distance}")

    # not necessary, only adding for output purpose
    def initializeDist(self, info):
        for pair in self.graph:
            info[pair] = Info()

    def dijkstraAlgo(self, source):
        priorityQueue = []
        heapq.heappush(priorityQueue, (0, source))
        info = defaultdict(Info)
        self.initializeDist(info)

        info[source] = Info(False, 0)

        while len(priorityQueue):
            distance, vertex = heapq.heappop(priorityQueue)

            if info[vertex].visited: #if already visited meaning already optimal
                continue
            info[vertex].visited = True

            # if distance > info[vertex].distance: #if it already optimized
            #     continue #then continue meaning run loop again

            for neighbour, currentDist in self.graph[vertex]:
                if info[neighbour].visited == False:
                    newDistance = distance + currentDist
                    if newDistance < info[neighbour].distance:
                        info[neighbour].distance = newDistance
                        newTuple = (newDistance, neighbour)
                        heapq.heappush(priorityQueue, newTuple)
        
        self.printShortestDist(source, info)


if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1, 4)
    g.addEdge(0, 2, 1)
    g.addEdge(2, 1, 2)
    g.addEdge(2, 3, 5)
    g.addEdge(1, 3, 1)
    g.addEdge(3, 4, 3)

    source = 0
    g.dijkstraAlgo(source)
    