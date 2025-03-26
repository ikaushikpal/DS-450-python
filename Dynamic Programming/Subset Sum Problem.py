# recursive solution
# time complexity : O(2^n)
# space complexity : O(1)

def subset_sum(arr, n,sum):
    if n == 0: # if array is empty then there is no way make sum equals to zero
        return False

    if sum == 0: # if sum is zero means we found a subset whose sum is equal to sum(argument)
        return True
    
    if sum >= arr[n - 1]:
        return subset_sum(arr, n-1, sum-arr[n-1]) or subset_sum(arr, n-1, sum)
    else:
        return subset_sum(arr, n-1, sum)


# memoization solution
# time complexity : O(n*sum)
# space complexity : O(n*sum)

class Memoization():
    def subset_sum(self, arr, n, sum):
        self.dp = [[-1]*(sum+1) for x in range(len(arr) + 1)]
        return self.subset_sum_util(arr, n, sum)
    
    def subset_sum_util(self, arr, n, sum):
        if n == 0:
            return False

        if sum == 0:
            return True

        if self.dp[n][sum] != -1:
            return self.dp[n][sum]

        if sum >= arr[n - 1]:
            self.dp[n][sum] = self.subset_sum_util(arr, n-1, sum-arr[n-1]) or self.subset_sum_util(arr, n-1, sum)
            return self.dp[n][sum] 
        else:
            self.dp[n][sum] = self.subset_sum_util(arr, n-1, sum)
            return self.dp[n][sum]


# Top-Down(real DP) solution
# time complexity : O(n*sum)
# space complexity : O(n*sum)

class Topdown():
    def subset_sum(self, arr, n, sum):
        self.dp = [[True]*(sum+1) for x in range(len(arr) + 1)]

        for i in range(0, max(len(arr), sum) + 1):
            if i <= sum:
                self.dp[0][i] = False

            if i <= len(arr):
                self.dp[i][0] = True

        return self.subset_sum_util(arr, n, sum)
    
    def subset_sum_util(self, arr, n, sum):
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
    sum = 10

    t = Topdown()
    result = t.subset_sum(arr, n, sum)
    print(f"Can we form {sum} from array, {result}")
