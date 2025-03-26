from collections import defaultdict, deque
import heapq


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append((v, 0))
        self.graph[v].append((u, 1))
    
    def findMinCost(self, source, destination):
        priorityQueue = []
        heapq.heappush(priorityQueue, (0, source))

        dist = defaultdict(lambda: float('inf'))
        visited = defaultdict(bool)

        while len(priorityQueue):
            distance, vertex = heapq.heappop(priorityQueue)

            if vertex == destination:
                return distance

            if visited[vertex]:
                continue
                
            visited[vertex] = True
            dist[vertex] = distance

            for neighbour, cost in self.graph[vertex]:
                if not visited[neighbour]:
                    oldCost = dist[neighbour]
                    newCost = distance + cost
                    if newCost < oldCost:
                        dist[neighbour] = newCost
                        heapq.heappush(priorityQueue, (newCost, neighbour))
        
        return -1


class Solution():
    def minCost(self, v, src, dst, edges):
        graph = Graph(v)

        for u, v in edges:
            graph.addEdge(u, v)

        return graph.findMinCost(src, dst)
# Time Complexity: O(VlogE)
# Space Complexity: O(V + E)
# using dijkstra algo

# btw it can be done O(V + E) using 0-1 BFS


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCost(7, 0, 6, [[0, 1], [2, 1], [2, 3], [5, 1],[4, 5], [6, 4], [6, 3]]))