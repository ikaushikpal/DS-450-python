# Top-Down(real DP) solution
# time complexity : O(n*sum)
# space complexity : O(n*sum)
import sys


class Topdown:
    def coin_change_min(self, coin, n, sum):
        self.dp = [[sys.maxsize - 1] * (sum + 1) for x in range(n + 1)]

        for i in range(1, n + 1):
            self.dp[i][0] = 0

        res = self.coin_change_min_util(coin, n, sum)
        if res == sys.maxsize - 1:
            return -1
        else:
            return res

    def coin_change_min_util(self, coin, n, sum):
        for i in range(1, n + 1):
            for j in range(1, sum + 1):
                if j >= coin[i - 1]:
                    self.dp[i][j] = min(1 + self.dp[i][j - coin[i - 1]], self.dp[i - 1][j])
                else:
                    self.dp[i][j] = self.dp[i - 1][j]

        return self.dp[n][sum]


if __name__ == "__main__":
    coin = [4, 5, 6]
    sum = 2
    n = len(coin)

    t = Topdown()
    print(t.coin_change_min(coin, n, sum))