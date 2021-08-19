def lcs(a, n, b, m):
    if n == 0 or m == 0:
        return 0

    if a[n-1] != b[m-1]:
        return max(lcs(a, n-1, b, m), lcs(a, n, b, m-1))
    else:
        return lcs(a, n-1, b, m-1) + 1


class Memoization():
    def longestCommonSub(self, a, n, b, m):
        self.dp = [[None]*(m+1) for i in range(n+1)]
        return self.longestCommonSub_util(a, n, b, m)

    def longestCommonSub_util(self, a, n, b, m):
        if n == 0 or m == 0:
            return 0

        if self.dp[n][m]:
            return self.dp[n][m]

        elif a[n-1] == b[m-1]:
            self.dp[n][m] = self.longestCommonSub_util(a, n-1, b, m-1) + 1

        else:
            self.dp[n][m] = max(self.longestCommonSub_util(
                a, n-1, b, m), self.longestCommonSub_util(a, n, b, m-1))

        return self.dp[n][m]


class BottomUp():
    def longestCommonSub(self, a, n, b, m):
        dp = [[0]*(m+1) for i in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]


if __name__ == '__main__':
    a = "abcd"
    b = "abce"
    n = len(a)
    m = len(b)

    bottomUp = BottomUp()
    res = bottomUp.longestCommonSub(a, len(a), b, len(b))
    print(res)

    mem = Memoization()
    res = mem.longestCommonSub(a, n, b, m)
    print(res)
