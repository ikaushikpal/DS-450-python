def count_subset_sum(arr, n,sum):
    if sum == 0: # if sum is zero means we found a subset whose sum is equal to sum(argument)
        return 1

    if n == 0: # if array is empty then there is no way make sum equals to zero
        return 0
    
    if sum >= arr[n - 1]:
        return count_subset_sum(arr, n-1, sum-arr[n-1]) + count_subset_sum(arr, n-1, sum)
    else:
        return count_subset_sum(arr, n-1, sum)

class Solution:
    def countSubsetSum(self, arr, n, targetSum):
        dp = [[0] * (targetSum+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(1, n+1):
            for j in range(1, targetSum+1):
                if j - arr[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][targetSum]

arr = [2, 3, 5, 4, 1]
n = len(arr)
sum = 5
print(count_subset_sum(arr, n, sum))
print(Solution().countSubsetSum(arr, n, sum))