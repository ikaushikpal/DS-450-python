# You are given an adjacency list, adj of Undirected Graph having unit weight of the edges, find the shortest path from src to all the vertex and if it is unreachable to reach any vertex, then return -1 for that vertex.

# Examples :
# Input: adj[][] = [[1, 3], [0, 2], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [7, 6]], src=0
# Output: [0, 1, 2, 1, 2, 3, 3, 4, 4]
 
# Input: adj[][]= [[3], [3], [], [0, 1]], src=3
# Output: [1, 1, -1, 0]

# Input: adj[][]= [[], [], [], [4], [3], [], []], src=1
# Output: [-1, 0, -1, -1, -1, -1, -1] 

# Constraint:
# 1<=adj.size()<=10^4
# 0<=edges<=adj.size()-1


from collections import deque


class Solution:
    def shortestPath(self, adj, src):
        V = len(adj)
        graph = {i: edges for i, edges in enumerate(adj)}

        dist = [-1] * V
        queue = deque([(src, 0)])

        while queue:
            vertex, cost = queue.popleft()
            
            if dist[vertex] != -1:
                continue
            
            dist[vertex] = cost

            for neighbour in graph[vertex]:
                if dist[neighbour] == -1:
                    queue.append((neighbour, cost + 1))
        
        return dist
# Time Complexity: O(V+E)
# Space Complexity: O(V)


if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestPath([[1, 3], [0, 2], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [7, 6]], 0))
    print(sol.shortestPath([[3], [3], [], [0, 1]], 3))
    print(sol.shortestPath([[], [], [], [4], [3], [], []], 1))
        

