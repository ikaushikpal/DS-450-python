class Solution:
    def isValid(self, x, y, m, n):
        if 0<=x<m and 0<=y<n:
            return True
        else:
            return False

    def maximumGold(self, grid):
        m = len(grid)
        n = len(grid[0])

        dx = [-1, 0, 1]
        dy = [1, 1, 1]

        overallMAxGold = 0
        for i in range(1, n):
            for j in range(0,m):
                maxGold = 0

                for k in range(len(dx)):
                    x, y = j-dx[k], i-dy[k]

                    if self.isValid(x, y, m, n):
                        maxGold = max(maxGold, grid[x][y])
                
                grid[j][i] += maxGold
            
                if i == n-1:
                    overallMAxGold = max(overallMAxGold, grid[j][i])
        
        
        return overallMAxGold


if __name__ == '__main__':
    grid = [[2,1],[1,2]];
    s = Solution()

    print(s.maximumGold(grid))
