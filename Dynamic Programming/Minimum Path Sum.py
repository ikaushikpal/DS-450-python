# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.


# Example 1:
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.


# Example 2:
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12


from typing import List


class SolutionRec:
    def minPathSumRec(self, grid, cost, currentX, currentY, destX, destY):
        if currentX == destX and currentY == destY:
            return cost

        costDown = costRight = 10**9

        x = currentX + 1
        y = currentY
        if 0<=x<=destX and 0<=y<=destY:
            costDown = self.minPathSumRec(grid, cost+grid[x][y], x, y, destX, destY)
        
        x = currentX
        y = currentY + 1
        if 0<=x<=destX and 0<=y<=destY:
            costRight = self.minPathSumRec(grid, cost+grid[x][y], x, y, destX, destY)

        return min(costDown, costRight)


    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cost = grid[0][0]

        return self.minPathSumRec(grid, cost, 0,0, m-1, n-1)

class SolutionMem:
    def minPathSumMem(self, grid, cost, currentX, currentY, destX, destY):
        if currentX == destX and currentY == destY:
            return grid[destX][destY]

        if self.dp[currentX][currentY] != 10**9:
            return self.dp[currentX][currentY]

        costDown = costRight = 10**9

        x = currentX + 1
        y = currentY
        if 0<=x<=destX and 0<=y<=destY:
            costDown = self.minPathSumMem(grid, cost+grid[x][y], x, y, destX, destY)
        
        x = currentX
        y = currentY + 1
        if 0<=x<=destX and 0<=y<=destY:
            costRight = self.minPathSumMem(grid, cost+grid[x][y], x, y, destX, destY)

        minCost = min(costDown, costRight) + grid[currentX][currentY]
        self.dp[currentX][currentY] = minCost
        return minCost


    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cost = grid[0][0]
        self.dp = [[10**9]*n for _ in range(m)]

        return self.minPathSumMem(grid, cost, 0,0, m-1, n-1)

class Solution:
    def isValid(self, x, y, m, n):
        if 0<=x<m and 0<=y<n:
            return True
        return False

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MAX = 10**9
        # direct on given matrix

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                cost = grid[i][j]

                costDown = costRight = MAX
                x, y = i, j+1
                if self.isValid(x, y, m, n):
                    costRight = grid[x][y]

                x,y = i+1, j
                if self.isValid(x, y, m, n):
                    costDown = grid[x][y]

                if costDown != MAX or costRight != MAX:
                    grid[i][j] = min(costDown, costRight) + cost
        
        return grid[0][0]
                
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        currentRow = [0]*N
        prevRow = [0]*N
        
        for i in range(M-1, -1, -1):
            prevRow, currentRow = currentRow, prevRow

            for j in range(N-1, -1, -1):
                if i == M-1 and j == N-1:
                    currentRow[j] = grid[i][j]
                elif i == M-1:
                    currentRow[j] = currentRow[j+1] + grid[i][j]
                elif j == N-1:
                    currentRow[j] = prevRow[j] + grid[i][j]
                else:
                    currentRow[j] = min(currentRow[j+1], prevRow[j]) + grid[i][j]
        return currentRow[0]
# Time Complexity: O(M*N)
# Space Complexity: (N)


if __name__ == '__main__':
    grid = [[1,3,1],[1,5,1],[4,2,1]]

    s = Solution()
    print(s.minPathSum(grid))
    print(s.minPathSum([[1,2,3],[4,5,6]]))
    print(s.minPathSum([[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]))
