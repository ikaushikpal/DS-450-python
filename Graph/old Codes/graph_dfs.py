from collections import defaultdict
import time
from queueMod import Queue
from stackMod import Stack



class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def addEdge(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u].append(v)

    def DFSUtil(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=' ')

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.DFSUtil(neighbor, visited)

    def DFS(self, startVartex):
        visited = defaultdict(bool)
        self.DFSUtil(startVartex, visited)
        

    def BFS(self, startVartex):
        visited = defaultdict(bool)
        queue = Queue()

        queue.enqueue(startVartex)
        visited[startVartex] = True

        while not queue.isEmpty():
            currentVertex = queue.dequeue()
            print(currentVertex, end=' -> ')
            
            for vertices in self.graph[currentVertex]:
                if not visited[vertices]:
                    queue.enqueue(vertices)
                    visited[vertices] = True
        print('\n')

    def topologicalSort(self):
        stack = Stack()
        visited = defaultdict(bool)

        tempVertices = list(self.vertices)

        for vertex in tempVertices:
            if not visited[vertex]:
                self.topologicalSortUtil(vertex, visited, stack)
        
        while not stack.isEmpty():
            print(f"{stack.pop()}", end='->')
        print()

    def topologicalSortUtil(self, currentVertex, visited, stack):
        visited[currentVertex] = True

        for vertex in self.graph[currentVertex]:
            if not visited[vertex]:
                self.topologicalSortUtil(vertex, visited, stack)

        stack.push(currentVertex)


if __name__ == '__main__':
    g = Graph()
    g.addEdge('A', 'C')
    g.addEdge('B', 'C')
    g.addEdge('C', 'E')
    g.addEdge('B', 'D')
    g.addEdge('E', 'H')
    g.addEdge('E', 'F')
    g.addEdge('D', 'F')

    print("Following is DFS from (starting from vertex 0)")
    g.BFS('A')
    time_start = time.perf_counter()
    g.topologicalSort()
    time_elapsed = (time.perf_counter() - time_start) * 1000000
    # memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
    print("%5.2f microsecends" % (time_elapsed))