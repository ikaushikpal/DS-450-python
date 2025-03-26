class BottomUp():
    def knapsack_unbounded(self, weight, value, n, w):
        self.dp = [[0]*(w+1) for x in range(len(weight) + 1)]

        for i in range(0, max(len(weight), w) + 1):
            if i <= w:
                self.dp[0][i] = 0

            if i <= len(weight):
                self.dp[i][0] = 0

        return self.knapsack_unbounded_util(weight, value, n, w)
    
    def knapsack_unbounded_util(self, weight, value, n, w):
        for i in range(1, n+1):
            for j in range(1, w+1):
                if j >= weight[i - 1]:
                    self.dp[i][j] = max(value[i-1] + self.dp[i][j-weight[i-1]], self.dp[i-1][j])
                else:
                    self.dp[i][j] = self.dp[i-1][j]

        return self.dp[n][w]
    
    # Space : O(W)
    def knapSack(self, N, W, val, wt):
        dp = [0] * (W+1)
        for i in range(1, N+1):
            for j in range(1, W+1):
                if j - wt[i-1] >= 0:
                    dp[j] = max(dp[j], val[i-1] + dp[j - wt[i-1]])
        
        return dp[W]


if __name__=='__main__':
    weight = [1, 3, 4, 5]
    value = [1, 4, 5, 7]
    n = len(weight)
    w = 7

    t = BottomUp()
    result = t.knapsack_unbounded(weight, value, n, w)
    print(f"Maximum Profit we can form = {result}")