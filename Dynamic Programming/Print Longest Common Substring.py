class Solution():
    def longestCommonSubstring(self, string1, string2, n1, n2):
        dp = [[0]*(n2+1) for i in range(n1+1)]
        count = 0
        outputString = ""

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if string1[i-1] == string2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] > count:
                        count = dp[i][j]
                        outputString = string1[i-count:i]
                else:
                    dp[i][j] = 0

        return outputString


if __name__ == '__main__':
    a = 'abcdxyz'
    b = 'xyzabcd'
    n = len(a)
    m = len(b)
    print(Solution().longestCommonSubstring(a, b, n, m))
