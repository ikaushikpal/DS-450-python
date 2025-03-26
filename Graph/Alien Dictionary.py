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
        order = []

        for vertex in list(self.graph):
            if visited[vertex] == False:
                self.dfs(vertex, visited, order)
        
        return order

class Solution:
    def findOrder(self, words, N, K):
        g = Graph()
        
        for i in range(N-1):
            word1, word2 = words[i], words[i + 1]
            minLength = min(len(word1), len(word2))
            for j in range(minLength):
                if word1[j] != word2[j]:
                    g.addEdge(word1[j], word2[j])
                    break
        
        order = g.topologicalSort()
        return ''.join(order)[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findOrder(['baa', "abcd","abca","cab","cad"], 5, 4))