class Solution():
    #def longestCommonSub(self,):
    def maxlen(cls, input1, input2):

        string1, string2 = input1, input2
        N, M = len(string1), len(string2)
        dp = [[0]*(M+1) for i in range(N+1)]

        for i in range(1, N+1):
            for j in range(1, M+1):
                if string1[i-1] == string2[j-1] and string1[i-1] in 'aeiou':
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[N][M]


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxlen('shabi', 'abcid'))