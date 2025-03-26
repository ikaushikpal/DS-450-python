from collections import defaultdict
import sys


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def countVertices(self):
        mySet = set()
        for vertex in self.graph:
            mySet.add(vertex)
            for neighbour, weight in self.graph[vertex]:
                mySet.add(neighbour)
        count = len(mySet)
        del mySet
        return count

    def relaxsation(self, distance):
        relaxsation_count = 0

        for vertex in self.graph:
            currentDistance = distance[vertex]
            for neighbour, weight in self.graph[vertex]:
                if distance[neighbour] > currentDistance + weight:
                    distance[neighbour] = currentDistance + weight
                    relaxsation_count += 1
        return relaxsation_count

    def printDistance(self, source, distance):
        count = 0
        for key in distance:
            print(f"distance from {source} to {key} = {distance[key]}")
            count += 1

        if count == 0:
            print(f"From {source} we can not reach to any vertex")

    def bellmanFordAlgorithm(self, source):
        total_no_vertices = self.countVertices()
        distance = defaultdict(lambda : sys.maxsize)
        distance[source] = 0
        FLAG = True

        for i in range(total_no_vertices-1):
            count = self.relaxsation(distance)
            if count == 0:
                FLAG = False
                break
        
        if FLAG:
            count = self.relaxsation(distance)
            if count > 0:
                print(f"Given Graph contain negative weight cycles, So no SSSP") 
        else:        
            self.printDistance(source, distance)


if __name__ == "__main__":
    g = Graph()
    g.addEdge('B','A', 7)
    g.addEdge('C', 'B', -9)
    g.addEdge('A', 'C', 4)
    g.addEdge('A', 'D', 5)
    g.addEdge('D', 'C', -3)
   
    g.bellmanFordAlgorithm('A')

