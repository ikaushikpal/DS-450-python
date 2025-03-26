# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and space is marked as 1 and 0 respectively in the grid.

# Example 1:

# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2

# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right


class Solution:
    def uniquePathsWithObstacles(self, obstacleGridL) -> int:
        m = len(obstacleGridL)    # rows
        n = len(obstacleGridL[0]) # columns

        grid = [[0]*n for _ in range(m)]
        destX, destY = m-1, n-1
        grid[0][0] = 1   # initialize dp
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0: # (x,y) loc is a obstacle then no need to anything just skip
                    continue

                # go down
                x_down, y_down = x+1, y
                if 0<=x_down<=destX and 0<=y_down<=destY and \
                obstacleGridL[x_down][y_down] != 1: # only add ways if destLoc is not obstacle
                    grid[x_down][y_down] += grid[x][y]
                
                # go right
                x_right, y_right = x, y+1
                if 0<=x_right<=destX and 0<=y_right<=destY and \
                obstacleGridL[x_right][y_right] != 1:
                    grid[x_right][y_right] += grid[x][y]
        
        return grid[destX][destY]


if __name__ == '__main__':
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))