from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, starting_vertex, end_vertex):
        self.graph[starting_vertex].append(end_vertex)
    
    def bfs(self, starting_vertex):
        visitedVertices = defaultdict(bool)
        queue = deque()
        queue.append(starting_vertex)
        visitedVertices[starting_vertex] = True

        while len(queue):
            currentNode = queue.popleft()
            print(f"{currentNode}",end=', ')

            for neighbour in self.graph[currentNode]:
                if visitedVertices[neighbour] == False:
                    queue.append(neighbour)
                    visitedVertices[neighbour] = True


g = Graph()
g.addEdge('A','B')
g.addEdge('B','D')
g.addEdge('A','C')
g.addEdge('C','D')
g.addEdge('D','E')
g.addEdge('E','F')

g.bfs('A')