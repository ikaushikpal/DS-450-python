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

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n<2:
            return n
        
        s1 = s
        s2 = s[::-1]
        lcs = self.longestCommonSub(s1, len(s1), s2, len(s2))

        return lcs


if __name__ == '__main__':
    s = "bbbab"
    print(Solution().longestPalindromeSubseq(s))