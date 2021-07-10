from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v, capacity):
        self.graph[u].append([v, capacity])
        self.graph[v].append([u, 0])

    def networkFlow(self, source, sink):
        parent = defaultdict()
        maxFlow = 0

        while self.bfs(source, parent, sink):
            currentVertex = sink
            bottleNeckFlow = 10**9

            while currentVertex != source:
                parentVertex = parent[currentVertex]

                for vertex, RC in self.graph[parentVertex]:
                    if vertex == currentVertex:
                        bottleNeckFlow = min(bottleNeckFlow, RC)
                        break

                currentVertex = parentVertex
            
            maxFlow += bottleNeckFlow
            currentVertex = sink

            while currentVertex != source:
                parentVertex = parent[currentVertex]
                

                for item in self.graph[parentVertex]:
                    if item[0] == currentVertex:
                        item[1] -= bottleNeckFlow
                        break

                for item in self.graph[currentVertex]:
                    if item[0] == parentVertex:
                        item[1] += bottleNeckFlow
                        break

                currentVertex = parentVertex
        
        return maxFlow

    def bfs(self, u, parent, sink):
        visited = defaultdict(bool)
        queue = deque()
        queue.append(u)
        visited[u] = True

        while len(queue):
            currentNode = queue.popleft()

            for neighbour, RC in self.graph[currentNode]:
                if visited[neighbour] == False and RC > 0:
                    queue.append(neighbour)
                    parent[neighbour] = currentNode
                    visited[neighbour] = True
                    if neighbour == sink:
                        return True
        
        return False

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 5)
    g.addEdge(1, 2, 15)
    g.addEdge(1, 3, 5)
    g.addEdge(2, 3, 10)
    
    print(g.networkFlow(0, 3))
