# You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

# 0 means the cell is empty, so you can pass through,
# 1 means the cell contains a cherry that you can pick up and pass through, or
# -1 means the cell contains a thorn that blocks your way.
# Return the maximum number of cherries you can collect by following the rules below:

# Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
# After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
# When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
# If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.
 

# Example 1:
# Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
# Output: 5
# Explanation: The player started at (0, 0) and went down, down, right right to reach (2, 2).
# 4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
# Then, the player went left, up, up, left to return home, picking up one more cherry.
# The total number of cherries picked up is 5, and this is the maximum possible.


# Example 2:
# Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
# Output: 0



from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if -1 in (grid[0][0], grid[-1][-1]):
            return 0
        
        N = len(grid)
        
        dp = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if grid[i][j] == -1:
                    continue

                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + grid[i][j]
                
                grid[i][j] = 0
        
        if dp[-1][-1] == 0:
            return 0
        
        newDp = [[0]*N for _ in range(N)]
        for i in range(N-1, -1, -1):
            for j in range(N-1, -1, -1):
                if grid[i][j] == -1:
                    continue

                if i == N-1 and j == N-1:
                    newDp[i][j] = dp[-1][-1]
                elif i == N-1:
                    newDp[i][j] = newDp[i][j+1] + grid[i][j]
                elif j == N-1:
                    newDp[i][j] = newDp[i+1][j] + grid[i][j]
                else:
                    newDp[i][j] = max(newDp[i][j+1], newDp[i+1][j]) + grid[i][j]
                
                grid[i][j] = 0
        return newDp[-1][-1]
    


if __name__ == '__main__':
    sol = Solution()
    print(sol.cherryPickup(grid = [[0,1,-1],[1,0,-1],[1,1,1]]))
    print(sol.cherryPickup(grid = [[1,1,-1],[1,-1,1],[-1,1,1]]))