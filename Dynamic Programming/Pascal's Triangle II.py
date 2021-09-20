class Solution:
    def getRow(self, rowIndex: int):
        rowIndex = rowIndex+1 #making 1 as starting

        dp = [0] * rowIndex
        dp[0] = dp[-1] = 1

        for i in range(1, rowIndex):
            dp[i] = 1
            tempDP = [0] * (i-1)

            for j in range(1, i):
                tempDP[j-1] = dp[j-1] + dp[j]

            dp[1:i] = tempDP
        return dp


if __name__ == '__main__':
    n = 5
    print(Solution().getRow(4))
        