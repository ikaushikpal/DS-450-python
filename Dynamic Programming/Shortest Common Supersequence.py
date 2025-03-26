class Solution:
    def longestCommonSub(self, a, n, b, m):
        dp = [[0]*(m+1) for i in range(n+1)]
        output_string = ''

        for i in range(1, n+1):
            for j in range(1, m+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[n][m]
        
    def shortestCommonSupersequence(self, X, Y, m, n):
        lcs = self.longestCommonSub(X,m,Y,n)
        return m+n-lcs


if __name__ == "__main__":
    # Input:
    X = "abcd"
    Y = "xycd"
    m = len(X)
    n = len(Y)

    # Output:
    print(Solution().shortestCommonSupersequence(X, Y, m, n))
    
    # Explanation: Shortest Common Supersequence
    # would be abxycd which is of length 6 and
    # has both the strings as its subsequences.