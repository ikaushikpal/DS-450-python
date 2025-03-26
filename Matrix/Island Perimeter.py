from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        islands = neighbour = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    islands += 1
                    
                    # checking for down neighbour
                    if i+1 < row and grid[i+1][j] == 1:
                        neighbour += 1
                    
                    # checking for right neighbour
                    if j+1 < col and grid[i][j+1] == 1:
                        neighbour += 1
            
        return 4 * islands - 2 * neighbour


if __name__ == "__main__":
    sol = Solution()
    grid = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]
    print(sol.islandPerimeter(grid))

    grid = [[1]]
    print(sol.islandPerimeter(grid))

    grid = [[1,0]]
    print(sol.islandPerimeter(grid)) 