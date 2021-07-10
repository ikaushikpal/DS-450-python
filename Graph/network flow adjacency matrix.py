from collections import defaultdict, deque


class BuildAdjMat:

    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v, capacity):
        self.graph[u].append([v, capacity])

    def buildAdjMat(self, V):
        graph = [[0]*V for _ in range(V)]

        for u in self.graph:
            for v,capacity in self.graph[u]:
                graph[u][v]= capacity
        
        return graph
    

class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)


    def networkFlow(self, source, sink):
        parent = [None] * self.V
        maxFlow = 0

        while self.bfs(source, parent, sink):
            currentVertex = sink
            bottleNeckFlow = 10**9

            while currentVertex != source:
                parentVertex = parent[currentVertex]

                bottleNeckFlow = min(bottleNeckFlow, self.graph[parentVertex][currentVertex])

                currentVertex = parentVertex
            

            maxFlow += bottleNeckFlow
            currentVertex = sink


            while currentVertex != source:
                parentVertex = parent[currentVertex]
                
                self.graph[parentVertex][currentVertex] -= bottleNeckFlow
                self.graph[currentVertex][parentVertex] += bottleNeckFlow

                currentVertex = parentVertex
        
        return maxFlow

    def bfs(self, u, parent, sink):
        visited = [False] * self.V
        queue = deque([u])
        visited[u] = True

        while len(queue):
            currentNode = queue.popleft()

            for v in range(self.V):
                RC = self.graph[currentNode][v]

                if visited[v] == False and RC > 0:

                    queue.append(v)
                    parent[v] = currentNode
                    visited[v] = True

                    if v == sink:
                        return True
        
        return False

if __name__ == '__main__':
    buildGraph = BuildAdjMat()

    buildGraph.addEdge(0, 1, 11)
    buildGraph.addEdge(0, 2, 12)
    buildGraph.addEdge(2, 1, 1)
    buildGraph.addEdge(1, 3, 12)
    buildGraph.addEdge(2, 4, 11)  
    buildGraph.addEdge(4, 3, 7)  
    buildGraph.addEdge(3, 5, 19)  
    buildGraph.addEdge(4, 5, 4)  

    graph = buildGraph.buildAdjMat(6)
    g = Graph(graph)
    print(g.networkFlow(0, 5))
