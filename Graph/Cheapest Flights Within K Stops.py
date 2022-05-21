# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

# Example 1:
# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1

# Output: 700

# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.



# Example 2:
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1

# Output: 200

# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.



# Example 3:
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0

# Output: 500

# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.


from typing import List
from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V

    def addEdge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def relaxsation(self, prevDistance):
        relaxsationCount = 0
        newDistance = prevDistance.copy()

        for u in range(self.V):
            if prevDistance[u] == float('inf'):
                continue

            for v, cost in self.graph[u]:
                if prevDistance[u] + cost < newDistance[v]:
                    newDistance[v] = prevDistance[u] + cost
                    relaxsationCount += 1

        return relaxsationCount, newDistance

    def bellmanfordAlgo(self, src, dst, iterations):
        distance = [float('inf')] * self.V
        distance[src] = 0

        for _ in range(iterations):
            count, newDistance = self.relaxsation(distance)
            if count == 0:
                break
            distance = newDistance

        if distance[dst] == float('inf'):
            return -1
        return distance[dst]

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = Graph(n)
        for u, v, weight in flights:
            g.addEdge(u, v, weight)
        
        return g.bellmanfordAlgo(src, dst, k+1)


if __name__ == '__main__':
    s = Solution()
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1
    print(s.findCheapestPrice(n, flights, src, dst, k))
    print(s.findCheapestPrice(n = 11,
                            flights = [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]],
                            src = 0,
                            dst = 2,
                            k = 4))