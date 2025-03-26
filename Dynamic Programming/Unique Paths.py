# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?


# Example 1:

# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]
        destX, destY = m-1, n-1
        grid[0][0] = 1   # initialize dp
        
        for x in range(m):
            for y in range(n):
                # go down
                x_down, y_down = x+1, y
                if 0<=x_down<=destX and 0<=y_down<=destY:
                    grid[x_down][y_down] += grid[x][y]
                
                # go right
                x_right, y_right = x, y+1
                if 0<=x_right<=destX and 0<=y_right<=destY:
                    grid[x_right][y_right] += grid[x][y]
        
        return grid[destX][destY]


if __name__ == '__main__':
    m = 3
    n = 7
    print(Solution().uniquePaths(m, n))