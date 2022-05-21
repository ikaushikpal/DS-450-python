# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

# Example 1:

# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].

# Example 2:

# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

# Example 3:

# Input: matrix = [[1]]
# Output: 1


from typing import List


class Solution:
    def dfs(self, matrix, i, j, ROWS, COLS, lip):
        if lip[i][j]:
            return lip[i][j]
        
        maxLength = 0
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x += i
            y += j
            if 0<=x<ROWS and 0<=y<COLS and matrix[x][y] > matrix[i][j]:
                maxLength = max(maxLength, self.dfs(matrix, x, y, ROWS, COLS, lip))
        
        lip[i][j] = maxLength + 1
        return lip[i][j]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        maxPath = 0
        ROWS, COLS = len(matrix), len(matrix[0])
        lip = [[0] * COLS for _ in range(ROWS)]

        for i in range(ROWS):
            for j in range(COLS):
                maxPath = max(maxPath, self.dfs(matrix, i, j, ROWS, COLS, lip))

        return maxPath


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
    print(sol.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
    print(sol.longestIncreasingPath([[1]]))
