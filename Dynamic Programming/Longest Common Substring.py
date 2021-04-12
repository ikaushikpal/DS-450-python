def longestCommonSubstring(a, n, b, m, count):
    if m == 0 or n == 0:
        return count

    if a[n-1] == b[m-1]:
        count = max(longestCommonSubstring(a, n-1, b, m-1, count+1), count+1)
        return count
    else:
        return max(longestCommonSubstring(a, n-1, b, m, 0), longestCommonSubstring(a, n, b, m-1, 0))


class Memoization():
    def longestCommonSubstring(self, a, n, b, m):
        self.dp = [[None]*(m+1) for i in range(n+1)]
        count = 0
        return self.longestCommonSubstring_util(a, n, b, m, 0)

    def longestCommonSubstring_util(self, a, n, b, m, count):
        if n == 0 or m == 0:
            return 0

        if a[n-1] == b[m-1]:
            self.dp[n][m] = max(self.longestCommonSubstring_util(
                a, n-1, b, m-1, count+1), count+1)
            count = max(self.dp[n][m], count)
            return count

        else:
            self.dp[n][m] = max(self.longestCommonSubstring_util(
                a, n-1, b, m, 0), self.longestCommonSubstring_util(a, n, b, m-1, 0))
            return self.dp[n][m]


class TopDown():
    def longestCommonSubstring(self, a, n, b, m):
        dp = [[0]*(m+1) for i in range(n+1)]
        count = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    count = max(dp[i][j], count)
                else:
                    dp[i][j] = 0

        return count


if __name__ == '__main__':
    a = 'abcdxyz'
    b = 'xyzabcd'
    n = len(a)
    m = len(b)

    mem = Memoization()
    res = mem.longestCommonSubstring(a, n, b, m)
    print(res)

    top = TopDown()
    res = top.longestCommonSubstring(a, n, b, m)
    print(res)
