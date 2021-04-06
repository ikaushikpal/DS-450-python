class Topdown:
    def maximum_product_cut(self, N):
        self.dp = [[0] * (N+1) for x in range(N)]
        self.rope = [x for x in range(1, N)]

        for i in range(0, N):
            self.dp[i][0] = 1

        return self.maximum_product_cut_util(self.rope, N-1, N)

    def maximum_product_cut_util(self, rope, n, N):
        for i in range(1, n+1):
            for j in range(1, N + 1):
                if j >= rope[i - 1]:
                    self.dp[i][j] = max(rope[i-1] * self.dp[i][j - rope[i - 1]], self.dp[i - 1][j])
                else:
                    self.dp[i][j] = self.dp[i - 1][j]

        return self.dp[n][N]

if __name__ == '__main__':
    N = 10
    t = Topdown()
    print(t.maximum_product_cut(N))
