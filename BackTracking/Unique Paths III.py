# You are given an m x n integer array grid where grid[i][j] could be:

# 1 representing the starting square. There is exactly one starting square.
# 2 representing the ending square. There is exactly one ending square.
# 0 representing empty squares we can walk over.
# -1 representing obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 
# Example 1:
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)


# Example 2:
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)


# Example 3:
# Input: grid = [[0,1],[2,0]]
# Output: 0
# Explanation: There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.


from typing import List


class Solution:
    def isValid(self, i: int, j: int) -> bool:
        if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]):
            return False
        return self.grid[i][j] != -1
    
    def dfs(self, x, y, traveled):
        traveled += 1

        if (x, y) == self.end:
            if traveled == self.nonObstacle:
                return 1
            else:
                return 0
        
        # making visited
        self.grid[x][y] = -1
        res = 0
        for deltaX, deltaY in zip(self.dx, self.dy):
            nextX, nextY = x + deltaX, y + deltaY
            if self.isValid(nextX, nextY):
                res += self.dfs(nextX, nextY, traveled)
        
        # making un-visited
        self.grid[x][y] = 0
        return res

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        startX, startY = -1, -1
        self.end = (-1, -1)
        self.nonObstacle = M * N
        self.grid = grid
        self.dx = [0, 0, -1, 1]
        self.dy = [-1, 1, 0, 0]

        # -1 -> Visited
        # 0 -> Unvisited

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    startX, startY = i, j
                    grid[i][j] = 0

                elif grid[i][j] == 2:
                    self.end = (i, j)
                    grid[i][j] = 0

                elif grid[i][j] == -1:
                    self.nonObstacle -= 1

        return self.dfs(startX, startY, 0)
# Time Complexity: O(4**(M*N))
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.uniquePathsIII(grid=[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
    print(sol.uniquePathsIII(grid=[[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
    print(sol.uniquePathsIII(grid=[[0,1],[2,0]]))