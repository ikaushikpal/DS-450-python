# https://cp-algorithms.com/graph/01_bfs.html
from collections import defaultdict, deque


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v, weight):
        self.graph[u].append((v, weight))
    
    def bfs(self, src):
        dist = [float('inf')] * self.V
        queue = deque()
        queue.append(src)
        dist[src] = 0

        while queue:
            u = queue.popleft()

            for v, weight in self.graph[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    if weight == 1:
                        queue.append(v)
                    else:
                        queue.appendleft(v)

        return dist
# Time Complexity : O(V+E)
# Space Complexity : O(V)
# where V is the number of vertices in the graph and E is the number of edges in the graph.
# 0-1 BFS can be useful when you want to find the shortest path between two vertices in a graph and there weight can be 0 or 1.

# further advance version s dial's algorithm
# where instead of maintaining a single queue, there we maintain k bucket of queues.
# where each weight can at most differ by k.  


if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(0, 1, 0)
    g.addEdge(0, 2, 1)
    g.addEdge(1, 2, 0)
    g.addEdge(1, 3, 1)
    g.addEdge(2, 3, 1)
    g.addEdge(3, 4, 1)
    print(g.bfs(0))
