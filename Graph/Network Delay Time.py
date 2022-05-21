# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2



# Example 2:
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1


# Example 3:
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1


from collections import defaultdict
import heapq
from typing import List


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def dijkstraAlgo(self, source):
        priorityQueue = []
        heapq.heappush(priorityQueue, (0, source))

        dist = defaultdict(lambda: float('inf'))
        visited = defaultdict(bool)

        while len(priorityQueue):
            distance, vertex = heapq.heappop(priorityQueue)

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
        
        return dist


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = Graph()
        for u, v, w in times:
            g.addEdge(u, v, w)
        
        dist = g.dijkstraAlgo(k)
        maxDelay = float('-inf')

        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return -1
            maxDelay = max(maxDelay, dist[i])
        return maxDelay


if __name__ == '__main__':
    print(Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
    print(Solution().networkDelayTime(times = [[1,2,1]], n = 2, k = 1))
    print(Solution().networkDelayTime(times = [[1,2,1]], n = 2, k = 2))
    print(Solution().networkDelayTime(times = [[1,2,1],[2,3,2],[1,3,4]], n=3, k=1))