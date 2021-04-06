class BottomUp():
    def minimum_subset_sum(self, arr, diff):
        n = len(arr)
        total = sum(arr)
        self.dp = [[0]*(total+1) for x in range(n + 1)]

        for i in range(0, n + 1):
            self.dp[i][0] = 1

        s1 = (total+diff)//2
        return self.minimum_subset_sum_util(arr, n, s1)

        for i in range(1, total//2 + 1):
            if self.dp[n][i]:
                return i
    
    def minimum_subset_sum_util(self, arr, n, sum):
        for i in range(1, n+1):
            for j in range(1, sum+1):
                if j >= arr[i - 1]:
                    self.dp[i][j] = self.dp[i-1][j-arr[i-1]] + self.dp[i-1][j]
                else:
                    self.dp[i][j] = self.dp[i-1][j]

        return self.dp[n][sum]


if __name__=='__main__':
    arr = [1,1,2,3]
    diff = 1

    t = BottomUp()
    result = t.minimum_subset_sum(arr, diff)
    print(result)
