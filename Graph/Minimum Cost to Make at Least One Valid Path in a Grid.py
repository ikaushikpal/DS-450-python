# Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:

# 1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
# 2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
# 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
# 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
# Notice that there could be some signs on the cells of the grid that point outside the grid.

# You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.

# You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

# Return the minimum cost to make the grid have at least one valid path.

 

# Example 1:


# Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
# Output: 3
# Explanation: You will start at point (0, 0).
# The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
# The total cost = 3.


# Example 2:
# Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
# Output: 0
# Explanation: You can follow the path from (0, 0) to (2, 2).


# Example 3:
# Input: grid = [[1,2],[4,3]]
# Output: 1


from typing import List
from collections import defaultdict, deque


# 0-1 BFS
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v, weight):
        self.graph[u].append((v, weight))
    
    def bfs(self, src):
        dist = defaultdict(lambda: float('inf'))
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


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        DX = [0, 0, 1, -1]
        DY = [1, -1, 0, 0]
        ROWS, COLS = len(grid), len(grid[0])
        g = Graph()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    targetX, targetY = i, j + 1
                elif grid[i][j] == 2:
                    targetX, targetY = i, j - 1
                elif grid[i][j] == 3:
                    targetX, targetY = i + 1, j
                else:
                    targetX, targetY = i - 1, j
                
                for x, y in zip(DX, DY):
                    newX = i + x
                    newY = j + y
                    if 0 <= newX < ROWS and 0 <= newY < COLS:
                        if newX == targetX and newY == targetY:
                            g.addEdge((i, j), (newX, newY), 0)
                        else:
                            g.addEdge((i, j), (newX, newY), 1)
        
        
        dist = g.bfs((0, 0))
        return dist[(ROWS-1, COLS-1)]

# Time Complexity : O(V + E)
# Space Complexity : O(V + E)


if __name__ == "__main__":
    s = Solution()
    print(s.minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))
    print(s.minCost([[1,1,3],[3,2,2],[1,1,4]]))
    print(s.minCost([[1,2],[4,3]]))