# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example 1:

# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4

# Example 2:

# Input: matrix = [["0","1"],["1","0"]]
# Output: 1

# Example 3:

# Input: matrix = [["0"]]
# Output: 0


from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0]*COLS for _ in range(ROWS)]
        dx = [1, 0, 1]
        dy = [0, 1, 1]
        maxSide = 0
        
        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                if matrix[i][j] == '1':
                    dp[i][j] = float('inf')
                    for k in range(3):
                        x = i + dx[k]
                        y = j + dy[k]
                        
                        if 0<=x<ROWS and 0<=y<COLS:
                            dp[i][j] = min(dp[i][j], dp[x][y])
                        else:
                            dp[i][j] = 0
                            
                    dp[i][j] += 1
                    maxSide = max(maxSide, dp[i][j])

        return maxSide * maxSide
        

if __name__ == '__main__':
    sol = Solution()
    print(sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print(sol.maximalSquare([["0","1"],["1","0"]]))
    print(sol.maximalSquare([["0"]]))
    