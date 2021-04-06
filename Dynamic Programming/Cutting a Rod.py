class BottomUp:
    def rod_cutting(self, price, n, N):
        self.dp = [[0] * (N+1) for x in range(n+1)]
        length = [x for x in range(1, n+1)]
        return self.rod_cutting_util(price, length, n, N)

    def rod_cutting_util(self, price, length, n, N):
        for i in range(1, n+1):
            for j in range(1, N + 1):
                if j >= length[i - 1]:
                    self.dp[i][j] = max(self.dp[i][j - length[i - 1]] + price[i-1], self.dp[i - 1][j])
                else:
                    self.dp[i][j] = self.dp[i - 1][j]

        return self.dp[n][N]

if __name__ == '__main__':
    price = [1,5,8,9,10,17,17,20]
    N = 8
    t = BottomUp()

    print(t.rod_cutting(price, len(price), N)) 
