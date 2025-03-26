class Solution:
    def longestCommonSub(self, a, n, b, m):
        dp = [[0]*(m+1) for i in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]

    def sequencePatternMatching(self, a:str, b:str)->bool:
        n = len(a)
        m = len(b)

        lcs = self.longestCommonSub(a, n,b,m)
        if lcs == n:
            return True
        else:
            return False


if __name__ == '__main__':
    a = "AXY"
    b = "ADXCPY"
    print(Solution().sequencePatternMatching(a, b))