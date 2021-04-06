class BottomUp():
    def equal_sum(self, arr, n):
        total = sum(arr)
        if total % 2:
            return False

        self.dp = [[False]*(total+1) for x in range(len(arr) + 1)]

        for i in range(0, n+1):
            self.dp[0][i] = True

        return self.equal_sum_util(arr, n, total // 2)
    
    def equal_sum_util(self, arr, n, sum):
        for i in range(1, n+1):
            for j in range(1, sum+1):
                if j >= arr[i - 1]:
                    self.dp[i][j] = self.dp[i-1][j-arr[i-1]] or self.dp[i-1][j]
                else:
                    self.dp[i][j] = self.dp[i-1][j]

        return self.dp[n][sum]


if __name__=='__main__':
    arr = [2, 3, 8, 7, 10]
    n = len(arr)

    t = BottomUp()
    result = t.equal_sum(arr, n)
    print(result)
