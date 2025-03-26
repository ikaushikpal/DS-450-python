import heapq
from collections import defaultdict, deque
from dataclasses import dataclass


@dataclass
class Info:
    visited : bool = False
    distance : int = 999999
    parent : any = None

class Graph:
    INF = 999999
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def printShortestDist(self, source, end, info):
        queue = deque()
        currentVertex = end
        cost = info[currentVertex].distance

        while info[currentVertex].parent:
            queue.append(currentVertex)
            currentVertex = info[currentVertex].parent

        if len(queue) == 0:
            print(f"cost from {source} to {end} there is no path")
            return

        print(f"cost from {source} to {end} = {cost} and path : ",end='')

        while len(queue):
            if len(queue) == 1:
                print(queue.pop())
            else:
                print(queue.pop() ,end='-> ')
        
        
    # not necessary, only adding for output purpose
    def initializeDist(self, info):
        for pair in self.graph:
            info[pair] = Info()

    def dijkstraAlgo(self, source, end):
        priorityQueue = []
        heapq.heappush(priorityQueue, (0, source))
        info = defaultdict(Info)
        self.initializeDist(info)

        info[source] = Info(False, 0, None)

        while len(priorityQueue):
            distance, vertex = heapq.heappop(priorityQueue)

            if info[vertex].visited: #if already visited meaning already optimal
                continue
            info[vertex].visited = True

            if vertex == end:
                break

            for neighbour, currentDist in self.graph[vertex]:
                if info[neighbour].visited == False:
                    newDistance = distance + currentDist
                    if newDistance < info[neighbour].distance:
                        info[neighbour].distance = newDistance
                        info[neighbour].parent = vertex
                        newTuple = (newDistance, neighbour)
                        heapq.heappush(priorityQueue, newTuple)
            

        self.printShortestDist(source, end, info)


if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1, 4)
    g.addEdge(0, 2, 1)
    g.addEdge(2, 1, 2)
    g.addEdge(2, 3, 5)
    g.addEdge(1, 3, 1)
    g.addEdge(3, 4, 3)

    source = 2
    g.dijkstraAlgo(source, 0)
    