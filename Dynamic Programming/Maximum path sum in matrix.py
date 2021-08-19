# also called Path with Maximum Gold

class Solution:
    def isValid(self, x, y, m, n):
        if 0<=x<m and 0<=y<n:
            return True
        else:
            return False

    def maximumPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        dx = [1, 1, 1]
        dy = [-1, 0, 1]

        for i in range(m-2, -1, -1):
            for j in range(n-1, -1, -1):
                maxGold = 0

                for k in range(len(dx)):
                    x, y = i+dx[k], j+dy[k]

                    if self.isValid(x, y, m, n):
                        maxGold = max(maxGold, grid[x][y])
                
                grid[i][j] += maxGold
        
        maxGold = 0
        for gold in grid[0]:
            maxGold = max(maxGold, gold)
        
        return maxGold


if __name__ == '__main__':
    grid = [[1,2,3],[9,8,7],[4,5,6]]
    s = Solution()

    print(s.maximumPath(grid))




