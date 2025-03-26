from collections import defaultdict
from email.policy import default
from typing import List

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v, w1, w2):
        self.graph[(u, w1)].append((v, w2))
        self.graph[(v, w2)].append((u, w1))
    
    def removeEdge(self, u, v, w1, w2):
        self.graph[(u, w1)].remove((v, w2))
        self.graph[(v, w2)].remove((u, w1))
    
    def dfs(self, u, w1, visited):
        visited[u] = True
        xor = w1
        for v, w2 in self.graph[(u, w1)]:
            if not visited[v]:
                xor = xor ^ self.dfs(v, w2, visited)
        return xor

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        graph = Graph()
        for u, v in edges:
            graph.addEdge(u, v, nums[u], nums[v])
        finalScore = float('inf')
        for e1 in edges:
            for e2 in edges:
                if e1 == e2:
                    continue
                u1, v1, w11, w12 = e1[0], e1[1], nums[e1[0]], nums[e1[1]]
                u2, v2, w21, w22 = e2[0], e2[1], nums[e2[0]], nums[e2[1]]
                graph.removeEdge(u1, v1, w11, w12)
                graph.removeEdge(u2, v2, w21, w22)
                visited = [False] * len(nums)
                minXor, maxXor = float('inf'), float('-inf')
                for v in range(len(nums)):
                    if not visited[v]:
                        xor = graph.dfs(v, nums[v], visited)
                        minXor = min(minXor, xor)
                        maxXor = max(maxXor, xor)
                
                finalScore = min(finalScore, maxXor - minXor)
                graph.addEdge(u1, v1, w11, w12)
                graph.addEdge(u2, v2, w21, w22)
    
        return finalScore


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumScore(nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]))
    print(sol.minimumScore(nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]))