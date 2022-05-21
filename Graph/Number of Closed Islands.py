# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

# Return the number of closed islands.

 

# Example 1:
# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water (group of 1s).


# Example 2:
# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1


# Example 3:
# Input: grid = [[1,1,1,1,1,1,1],
#                [1,0,0,0,0,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,1,0,1,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,0,0,0,0,1],
#                [1,1,1,1,1,1,1]]
# Output: 2


from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # 0 -> land
        # 1 -> water
        def dfs(i, j):
            grid[i][j] = 1

            for del_x, del_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = i + del_x, j + del_y
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
                    dfs(x, y)
            
        ROWS, COLS = len(grid), len(grid[0])
        for j in range(COLS):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[ROWS - 1][j] == 0:
                dfs(ROWS - 1, j)
        
        for i in range(ROWS):
            if grid[i][0] == 0:
                dfs(i, 0)
            
            if grid[i][COLS - 1] == 0:
                dfs(i, COLS - 1)

        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    count += 1
                    dfs(i, j)
        return count
# Time Complexity: O(ROWS * COLS)
# Space Complexity: O(1)


if __name__ == '__main__':
    s = Solution()
    grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    print(s.closedIsland(grid))

    grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
    print(s.closedIsland(grid))

    grid = [[1,1,1,1,1,1,1],
            [1,0,0,0,0,0,1],
            [1,0,1,1,1,0,1],
            [1,0,1,0,1,0,1],
            [1,0,1,1,1,0,1],
            [1,0,0,0,0,0,1],
            [1,1,1,1,1,1,1]]
    print(s.closedIsland(grid))
