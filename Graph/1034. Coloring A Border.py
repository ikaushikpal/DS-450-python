# You are given an m x n integer matrix grid, and three integers row, col, and color. Each value in the grid represents the color of the grid square at that location.

# Two squares are called adjacent if they are next to each other in any of the 4 directions.

# Two squares belong to the same connected component if they have the same color and they are adjacent.

# The border of a connected component is all the squares in the connected component that are either adjacent to (at least) a square not in the component, or on the boundary of the grid (the first or last row or column).

# You should color the border of the connected component that contains the square grid[row][col] with color.

# Return the final grid.

# Example 1:
# Input: grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
# Output: [[3,3],[3,2]]

# Example 2:
# Input: grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
# Output: [[1,3,3],[2,3,3]]

# Example 3:
# Input: grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
# Output: [[2,2,2],[2,1,2],[2,2,2]]
 

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j], color <= 1000
# 0 <= row < m
# 0 <= col < n


from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        visited = [[False] * N for _ in range(M)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        originalColor = grid[row][col]
        border_cells = []
        
        def dfs(x, y):
            visited[x][y] = True
            is_border = False
            
            # Check if this cell is on the border
            # A cell is on border if it's on grid boundary OR adjacent to different color/out of bounds
            for dx, dy in dirs:
                newX = x + dx
                newY = y + dy
                
                # If neighbor is out of bounds or has different color, current cell is border
                if (newX < 0 or newX >= M or newY < 0 or newY >= N or 
                    grid[newX][newY] != originalColor):
                    is_border = True
                # If neighbor is same color and not visited, continue DFS
                elif not visited[newX][newY]:
                    dfs(newX, newY)
            
            # If this cell is on border, add it to border_cells
            if is_border:
                border_cells.append((x, y))
        
        # Find all cells in the connected component and identify border cells
        dfs(row, col)
        
        # Color all border cells
        for x, y in border_cells:
            grid[x][y] = color
            
        return grid
# Time: O(M * N)
# Space: O(M * N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.colorBorder(grid = [[1,1],[1,2]], row = 0, col = 0, color = 3))
    print(sol.colorBorder(grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3))
    print(sol.colorBorder(grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2))