from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, starting_vertex, end_vertex):
        self.graph[starting_vertex].append(end_vertex)
    
    #coloring method
    def isBipartite(self):
        visitedVertices = defaultdict(int)
        queue = deque()

        flag = True

        for u in list(self.graph):
            if visitedVertices[u] == 0:
                visitedVertices[u] = 1
                queue.append(u)
                flag = self.isBipartiteUtil(queue, visitedVertices)

                if flag == False:
                    return False
        return True

    def isBipartiteUtil(self, queue, visitedVertices):
        while len(queue):
            currentNode = queue.popleft()

            for neighbour in self.graph[currentNode]:
                if neighbour == currentNode:
                    return False
                
                if visitedVertices[neighbour] == 0:
                    queue.append(neighbour)
                    if visitedVertices[currentNode]==1:
                        visitedVertices[neighbour] = 2
                    else:
                        visitedVertices[neighbour] = 1
                
                elif visitedVertices[neighbour] == visitedVertices[currentNode]:
                    return False
        return True
    
    #using bipartite theory
    def isBipartite2(self):
        for u in list(self.graph):
            count = len(self.graph[u])
            if count %2:
                return False
            if u in self.graph[u]:
                return False
        return True

    
g = Graph()
g.addEdge('A','B')
# g.addEdge('A','D')
# g.addEdge('A','A')
g.addEdge('B','A')
g.addEdge('B','C')
g.addEdge('C','D')
g.addEdge('C','B')
g.addEdge('D','A')
g.addEdge('D','C')

print(g.isBipartite())