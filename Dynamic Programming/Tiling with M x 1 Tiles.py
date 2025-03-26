class Recursive:
    def tilingMatch(self, m, n):
        if n == 0:
            return 1

        # perform vertical alignment
        verticalWays = self.tilingMatch(m, n-1)
        horizontalWays = 0

        # perform horizontal alignment if space is available
        if n >= m:
            horizontalWays = self.tilingMatch(m, n-m)

        return verticalWays + horizontalWays


class Solution:
    def tilingMatch(self, m, n):
        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(1, n+1):
            if n>=m:
                dp[i] = dp[i-1] + dp[i-m]
            else:
                dp[i] = dp[i-1]
        
        return dp[n]

if __name__ == '__main__':
    m, n = 3, 5
    print(Recursive().tilingMatch(m, n))
    print(Solution().tilingMatch(m, n))
