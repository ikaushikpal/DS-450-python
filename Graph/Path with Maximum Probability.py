# You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

# Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

# If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

 

# Example 1:
# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
# Output: 0.25000
# Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.


# Example 2:
# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
# Output: 0.30000


# Example 3:
# Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
# Output: 0.00000
# Explanation: There is no path between 0 and 2.


from collections import defaultdict
import heapq
from typing import List


class Solution:
    def builtGraph(self, n, edges, succProb):
        graph = defaultdict(list)

        for (u, v), proba in zip(edges, succProb):
            graph[u].append((v, -proba))
            graph[v].append((u, -proba))
        return graph
    
    def dijkstraAlgo(self, graph, start, end):
        maxHeap = [(-1, start)] # (-proba, node)
        distance = defaultdict(lambda : float('inf'))
        distance[start] = 0

        while maxHeap:
            proba, currNode = heapq.heappop(maxHeap)

            if currNode == end:
                return -proba

            for neighbour, neiProba in graph[currNode]:
                # only because python do not support maxHeap natively
                newProba = -abs(proba * neiProba)

                if distance[neighbour] > newProba:
                    distance[neighbour] = newProba
                    heapq.heappush(maxHeap, (newProba, neighbour))
        return 0
    
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = self.builtGraph(n, edges, succProb)
        return self.dijkstraAlgo(graph, start, end)
# Time Complexity: O((V+E)logV)
# Space Complexity : O(V + E)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2))
    print(sol.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2))
    print(sol.maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2))
