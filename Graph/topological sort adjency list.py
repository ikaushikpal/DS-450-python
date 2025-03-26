from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, vertex, visited, order):
        visited[vertex] = True
        for neighbour in self.graph[vertex]:
            if visited[neighbour] == False:
                self.dfs(neighbour, visited, order)
        order.append(vertex)

    def topologicalSort(self):
        visited = defaultdict(bool)
        order = deque()

        for vertex in list(self.graph):
            if visited[vertex] == False:
                self.dfs(vertex, visited, order)
        
        self.printOrder(order)
    
    def printOrder(self, order):
        print("topological ordering of the graph : ",end='')
        while len(order):
            print(order.pop(), end=' ')
        print()


if __name__ == "__main__":
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 6)
    g.addEdge(4, 7)
    g.addEdge(5, 7)
    g.addEdge(6, 5)
    g.addEdge(6, 7)

    g.topologicalSort()