class BottomUp():
    def minimum_subset_sum(self, arr):
        n = len(arr)
        total = sum(arr)
        self.dp = [[False]*(total+1) for x in range(n + 1)]

        for i in range(0, n + 1):
            self.dp[i][0] = True

        self.minimum_subset_sum_util(arr, n, total)

        for i in range(1, total//2 + 1):
            if self.dp[n][i]:
                return i
    
    def minimum_subset_sum_util(self, arr, n, sum):
        for i in range(1, n+1):
            for j in range(1, sum+1):
                if j >= arr[i - 1]:
                    self.dp[i][j] = self.dp[i-1][j-arr[i-1]] or self.dp[i-1][j]
                else:
                    self.dp[i][j] = self.dp[i-1][j]

        return self.dp[n][sum]


if __name__=='__main__':
    arr = [1,6,5,11]

    t = BottomUp()
    result = t.minimum_subset_sum(arr)
    print(result)
