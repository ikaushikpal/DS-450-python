# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

# Example 1:
# Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.



# Example 2:
# Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
# Output: 4
# Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.


from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        # enqueuing all the land cells
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))
            
        # if there is no land, return -1
        if not queue:
            return -1
        
        # BFS
        distance = 0
        DX = [0, 0, 1, -1]
        DY = [1, -1, 0, 0]

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for x, y in zip(DX, DY):
                    newX = i + x
                    newY = j + y
                    if 0<=newX<ROWS and 0<=newY<COLS and (newX, newY) not in visited and grid[newX][newY] == 0:
                        queue.append((newX, newY))
                        visited.add((newX, newY))
            distance += 1
        
        if distance == 1:
            return -1
        return distance-1


if __name__ == '__main__':
    sol = Solution()
    grid = [[1,0,1],[0,0,0],[1,0,1]]
    print(sol.maxDistance(grid))
    
    print(Solution().maxDistance([[1,0,0],[0,0,0],[0,0,0]]))