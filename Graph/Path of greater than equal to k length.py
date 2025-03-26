from collections import defaultdict
from email.policy import default


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dfs(self, curr, k, visited):
        if k <= 0:
            return True
        
        visited[curr] = True

        for neighbor, weight in self.graph[curr]:
            if not visited[neighbor]:
                if self.dfs(neighbor, k - weight, visited):
                    return True

        visited[curr] = False
        return False

    def pathMoreThanK(self, src, k):
        visited = defaultdict(bool)
        return self.dfs(src, k, visited)


class Solution:
    def pathMoreThanK (self, V, E, K, A):
        g = Graph()
        for i in range(0, len(A), 3):
            g.addEdge(A[i], A[i + 1], A[i + 2])
        
        return g.pathMoreThanK(0, K)



if __name__ == '__main__':
    sol = Solution()
    print(sol.pathMoreThanK(9, 14, 60, [0, 1, 4, 0, 7, 8, 1, 2, 8, 1, 7, 
                                        11, 2, 3, 7, 2, 5, 4, 2, 8, 2, 3, 4, 9, 
                                        3, 5, 14, 4, 5, 10, 5, 6, 2, 6, 7, 1, 6, 
                                        8, 6, 7, 8, 7]))