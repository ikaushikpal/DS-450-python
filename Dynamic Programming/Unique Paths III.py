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

class Solution:
    def uniquePathsIII(self, grid) -> int:
        m, n = len(grid), len(grid[0]) # row & col
        # directly writting on given grid
        dp = [[0]*n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1: # staring loc
                    dp[x][y] = 1

                if dp[x][y] == 0: # (x,y) loc is a obstacle then no need to anything just skip
                    continue

                if grid[x][y] == 2: # destination loc
                    return dp[x][y]

                # go down
                x_down, y_down = x+1, y
                if 0<=x_down<m and 0<=y_down<n and \
                grid[x_down][y_down] != -1: # only add ways if destLoc is not 
                    if dp[x][y] > 2:
                        dp[x_down][y_down] += 1
                    else:
                        dp[x_down][y_down] += dp[x][y]
                
                # go right
                x_right, y_right = x, y+1
                if 0<=x_right<m and 0<=y_right<n and \
                grid[x_right][y_right] != -1:
                    if dp[x][y] > 2:
                        dp[x_right][y_right] += 1
                    else:
                        dp[x_right][y_right] += dp[x][y]
        
        
if __name__ == '__main__':
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    print(Solution().uniquePathsIII(grid))