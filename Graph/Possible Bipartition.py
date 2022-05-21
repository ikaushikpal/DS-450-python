# We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

# Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

 
# Example 1:
# Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4] and group2 [2,3].


# Example 2:
# Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false


# Example 3:
# Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false


from collections import deque, defaultdict
from typing import List


class Graph:
    NOT_VISITED, BLACK, WHITE = range(0, 3)

    def __init__(self, V):
        self.V = V
        self.graph = [[] for _ in range(V+1)]
    
    def addEdge(self, starting_vertex, end_vertex):
        self.graph[starting_vertex].append(end_vertex)
    
    #coloring method
    def isBipartite(self):
        color = defaultdict(int)
        queue = deque()

        for u in range(1, self.V+1):
            if color[u] == self.NOT_VISITED:
                color[u] = self.BLACK
                queue.append(u)
                if not self.isBipartiteUtil(queue, color):
                    return False
        return True

    def isBipartiteUtil(self, queue, color):
        while queue:
            currentNode = queue.popleft()

            for neighbour in self.graph[currentNode]:
                if color[neighbour] == self.NOT_VISITED:
                    if color[currentNode] == self.BLACK:
                        color[neighbour] = self.WHITE
                    else:
                        color[neighbour] = self.BLACK
                    queue.append(neighbour)
                
                elif color[neighbour] == color[currentNode]:
                    return False
        return True    

        
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = Graph(n)
        # NOTE: its undirected graph
        for u, v in dislikes:
            g.addEdge(u, v)
            g.addEdge(v, u)
        
        return g.isBipartite()
# Time Complexity : O(V + E)
# Space Complexity: O(V + E)
# where V is the total number of persons
# E is the dislike person pi to pj and pj to pi


if __name__ == '__main__':
    sol = Solution()
    print(sol.possibleBipartition(10, [[5,9],[5,10],[5,6],[5,7],[1,5],[4,5],[2,5],[5,8],[3,5]]))