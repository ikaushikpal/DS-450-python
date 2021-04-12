def printLCS(a, n, b, m, output_string):
    if n == 0 or m == 0:
        return ''

    if a[n-1] != b[m-1]:
        x = printLCS(a, n-1, b, m, output_string)
        y = printLCS(a, n, b, m-1, output_string)
        if len(x) > len(y):
            return x
        else:
            return y
    else:
        return printLCS(a, n-1, b, m-1, output_string) + a[n-1]


class TopDown():
    def longestCommonSub(self, a, n, b, m):
        dp = [[0]*(m+1) for i in range(n+1)]
        output_string = ''

        for i in range(1, n+1):
            for j in range(1, m+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        i = n
        j = m

        while i and j:
            if a[i-1] == b[j-1]:
                output_string += a[i-1]
                i -= 1
                j -= 1
            else:
                if dp[i][j-1] > dp[i-1][j]:
                    j -= 1
                else:
                    i -= 1
        output_string = output_string[::-1]

        return output_string


if __name__ == "__main__":
    a = "AGGTAB"
    b = "GXTXAYB"
    n = len(a)
    m = len(b)

    print(printLCS(a, n, b, m, ''))

    top = TopDown()
    print(top.longestCommonSub(a, n, b, m))
