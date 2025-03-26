from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row = [0] * n
        col = [0] * n
        increased_height = 0

        for i in range(n):
            for j in range(n):
                row[i] = max(row[i], grid[i][j])
                col[j] = max(col[j], grid[i][j])
        
        for i in range(n):
            for j in range(n):
                increased_height += min(row[i], col[j]) - grid[i][j]
        
        return increased_height


if __name__ == '__main__':
    grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

    print(Solution().maxIncreaseKeepingSkyline(grid))
        
