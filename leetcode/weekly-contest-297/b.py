from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[0]*N for _ in range(M)]
        for i in range(N):
            dp[M-1][i] = grid[M-1][i]
        
        for i in range(M-2, -1, -1):
            for j in range(N):
                minValue = float('inf')
                currentCellValue = grid[i][j]
                for k in range(N):
                    minValue = min(minValue, dp[i+1][k] + moveCost[currentCellValue][k])
                dp[i][j] = minValue + currentCellValue
        
        return min(dp[0])
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.minPathCost(grid = [[5,3],[4,0],[2,1]], moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]))
    print(sol.minPathCost(grid = [[5,1,2],[4,0,3]], moveCost = [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]]))