# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

# Example 1:
# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.



# Example 2:
# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.


from typing import List


class Solution:
    def dfs(self, i, j, grid):
        grid[i][j] = 0
        for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            newX = i + x
            newY = j + y
            if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]) and grid[newX][newY] == 1:
                self.dfs(newX, newY, grid)
        
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # first row
        for i in range(COLS):
            if grid[0][i] == 1:
                self.dfs(0, i, grid)
        
        # last row
        for i in range(COLS):
            if grid[-1][i] == 1:
                self.dfs(ROWS - 1, i, grid)
        
        # first col
        for i in range(ROWS):
            if grid[i][0] == 1:
                self.dfs(i, 0, grid)
            
        # last col
        for i in range(ROWS):
            if grid[i][-1] == 1:
                self.dfs(i, COLS - 1, grid)

        # count water surrounded land
        return sum(sum(row) for row in grid)



if __name__ == '__main__':
    sol = Solution()
    print(sol.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
    print(sol.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))