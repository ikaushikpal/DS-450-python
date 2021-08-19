from collections import defaultdict,deque


class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def calculateInDegrees(self):
        self.inDegrees = defaultdict(int)

        for u in self.graph:
            for v in self.graph[u]:
                self.inDegrees[v] += 1
        
    def topSort(self):
        self.calculateInDegrees()
        queue = deque()

        for u in range(self.V):
            if self.inDegrees[u] == 0:
                queue.append(u)
        
        countVertices = 0
        ordering = deque()

        while len(queue):
            x = queue.popleft()
            ordering.append(x)

            for v in self.graph[x]:
                self.inDegrees[v] -= 1
                if self.inDegrees[v] == 0:
                    queue.append(v)
            
            countVertices += 1
        
        if countVertices != self.V:
            print("Graph is not a DAG")
        else:
            while len(ordering):
                print(ordering.popleft(), end=' ')
            print()


if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    g.topSort()
    