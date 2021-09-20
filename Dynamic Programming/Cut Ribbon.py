import sys


class Topdown:
    def ribbon_cut(self, N, a, b, c):
        self.dp = [[-sys.maxsize] * (N+1) for x in range(4)]
        self.ribbons = [a, b, c]

        for i in range(0, 4):
            self.dp[i][0] = 0

        return self.ribbon_cut_util(self.ribbons, 3, N)

    def ribbon_cut_util(self, ribbons, n, N):
        for i in range(1, n+1):
            for j in range(1, N + 1):
                if j >= ribbons[i - 1]:
                    self.dp[i][j] = max(self.dp[i][j - ribbons[i - 1]] + 1, self.dp[i - 1][j])
                else:
                    self.dp[i][j] = self.dp[i - 1][j]

        return self.dp[n][N]

class Solution:
    def cutRibbon(self, ribbons:list, ribbonLength:int, n:int)->int:
        dp = [0] * (ribbonLength+1)
        dp[0] = 1

        for j in range(1, ribbonLength+1):
            for ribbon in ribbons:
                if j-ribbon >= 0:
                    dp[j] = max(dp[j], 1+dp[j-ribbon])

        return dp[ribbonLength]


if __name__ == '__main__':
    N = 16
    a, b, c = 7, 5, 3
    t = Topdown()
    print(Solution().cutRibbon([a,b,c], N, 3))

    print(t.ribbon_cut(N, a, b, c))
