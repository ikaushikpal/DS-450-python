from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = []
        self.INF = 10**9

    def addEdge(self, u, v, weight):
        self.graph.append((u, v, weight))

    def relaxsation(self, dist):
        relaxsation_count = 0

        # how many edges are present in list is |E| no of
        # so this loop's time complexity is O(E)
        for u,v,weight in self.graph:
            if dist[u] != self.INF and dist[v] > dist[u] + weight:
                # just like dijkstra, relaxing all vertices
                dist[v] = dist[u] + weight
                relaxsation_count += 1

        return relaxsation_count


    def printDistance(self, source, dist):
        count = 0
        for key in dist:
            print(f"distance from {source} to {key} = {dist[key]}")
            count += 1

        if count == 0:
            print(f"From {source} we can not reach to any vertex")


    def bellmanFordAlgorithm(self, source):
        dist = defaultdict(lambda : self.INF)
        dist[source] = 0
        FLAG = True
        total_no_vertices = len(self.graph)

        # we are looping 0 to |V|-1, so loop will execute |V| times
        # outer loop time complexity is O(V)
        for i in range(total_no_vertices-1):
            count = self.relaxsation(dist)
            if count == 0:
                FLAG = False
                break
        # so total time complexity is O(VE)

        if FLAG:
            count = self.relaxsation(dist)
            if count > 0:
                print(f"Given Graph contain negative weight cycles, So no SSSP") 

        else:        
            self.printDistance(source, dist)


if __name__ == "__main__":
    g = Graph()
    g.addEdge('B','A', 7)
    g.addEdge('C', 'B', -9)
    g.addEdge('A', 'C', 4)
    g.addEdge('A', 'D', 5)
    g.addEdge('D', 'C', -3)
   
    g.bellmanFordAlgorithm('A')

