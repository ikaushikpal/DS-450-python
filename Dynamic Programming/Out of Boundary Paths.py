# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

 

# Example 1:
# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6


# Example 2:
# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12


# Memoization Solution:
class Solution:
    def isOutOfBound(self, x, y):
        if 0<=x<self.m and 0<=y<self.n:
            return False
        return True
    
    def dfs(self, x, y, maxMove):
        if self.isOutOfBound(x, y):
            return 1
        
        if maxMove == 0:
            return 0
        
        if (x, y, maxMove) in self.dp:
            return self.dp[(x, y, maxMove)]
        
        res = 0
        for delX, delY in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            newX = delX + x
            newY = delY + y
            res += self.dfs(newX, newY, maxMove - 1)
            
        self.dp[(x, y, maxMove)] = res
        return res
        
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.m, self.n = m, n
        self.dp = {}
        return self.dfs(startRow, startColumn, maxMove) % 1_000_000_007
# Time Complexity: O(m * n * maxMove)
# Space Complexity : O(1)
#  The above implementation, although may use more space than dynamic allocation doesn't depend on input size and hence it's constant space complexity.
#  The space complexity of dynamic allocation implementation will be O(m * n * maxMove).

# Tabulation Solution:
class Solution:
    def isOutOfBound(self, x, y, m, n):
        if 0<=x<m and 0<=y<n:
            return False
        return True

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[0]*n for _ in range(m)] for _ in range(maxMove + 1)]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        MOD = 1_000_000_007

        for move in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    for delX, delY in zip(dx, dy):
                        newX = i + delX
                        newY = j + delY

                        if self.isOutOfBound(newX, newY, m, n):
                            dp[move][i][j] += 1
                        else:
                            dp[move][i][j] = (dp[move][i][j] + dp[move - 1][newX][newY]) % MOD
                            
        return dp[maxMove][startRow][startColumn] % MOD
# Time Complexity : O(m * n * maxMove)
# Space Complexity : O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPaths(2, 2, 2, 0, 0))
    print(sol.findPaths(1, 3, 3, 0, 1))