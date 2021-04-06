# recursive solution
# time complexity : O(2^n)
# space complexity : O(1)


def coin_change(arr, m, n):
    if m == 0:
        return 1
    if n == 0:
        return 0

    if m >= arr[n - 1]:
        return coin_change(arr, m - arr[n - 1], n) + coin_change(arr, m, n - 1)
    else:
        return coin_change(arr, m, n - 1)


# memoization solution
# time complexity : O(n*sum)
# space complexity : O(n*sum)


class Memoization:
    def coin_change(self, coin, n, sum):
        self.dp = [[-1] * (sum + 1) for x in range(n + 1)]
        return self.coin_change_util(coin, n, sum)

    def coin_change_util(self, coin, n, sum):
        if n == 0 or sum == 0:
            return 0

        if self.dp[n][sum] != -1:
            return self.dp[n][sum]

        if sum >= coin[n - 1]:
            self.dp[n][sum] = self.coin_change_util(
                coin, n, sum - coin[n - 1]
            ) + self.coin_change_util(coin, n - 1, sum)
            return self.dp[n][sum]
        else:
            self.dp[n][sum] = self.coin_change_util(coin, n - 1, sum)
            return self.dp[n][sum]


# Top-Down(real DP) solution
# time complexity : O(n*sum)
# space complexity : O(n*sum)


class Topdown:
    def coin_change(self, coin, n, sum):
        self.dp = [[0] * (sum + 1) for x in range(n + 1)]

        for i in range(0, n + 1):
            self.dp[i][0] = 1

        return self.coin_change_util(coin, n, sum)

    def coin_change_util(self, coin, n, sum):
        for i in range(1, n + 1):
            for j in range(1, sum + 1):
                if j >= coin[i - 1]:
                    self.dp[i][j] = self.dp[i][j - coin[i - 1]] + self.dp[i - 1][j]
                else:
                    self.dp[i][j] = self.dp[i - 1][j]

        return self.dp[n][sum]


if __name__ == "__main__":
    coin = [1, 2, 3]
    sum = 5
    n = len(coin)

    t = Topdown()
    print(t.coin_change(coin, n, sum))
