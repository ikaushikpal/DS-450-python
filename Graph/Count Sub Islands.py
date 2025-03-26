# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

# An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

# Return the number of islands in grid2 that are considered sub-islands.

 
# Example 1:
# Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.


# Example 2:
# Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# Output: 2 
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.


from typing import List


class Solution:
    DX = [1, -1, 0, 0]
    DY = [0, 0, 1, -1]

    def dfs(self, i, j, grid):
        grid[i][j] = 0

        for dx, dy in zip(self.DX, self.DY):
            newX = i + dx
            newY = j + dy
            if 0 > newX or newX >= len(grid) or 0 > newY or newY >= len(grid[0]):
                continue
        
            if grid[newX][newY] == 1:
                self.dfs(newX, newY, grid)

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        count = 0

        # removing all the non-common sub-islands
        for i in range(ROWS):
            for j in range(COLS):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    self.dfs(i, j, grid2)
        
        # counting the common sub-islands
        for i in range(ROWS):
            for j in range(COLS):
                if grid2[i][j] == 1:
                    count += 1
                    self.dfs(i, j, grid2)
        
        return count
# Runtime: O(ROWS * COLS)
# Space: O(ROWS * COLS)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubIslands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
                            [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))

    print(sol.countSubIslands([[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
                            [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]))