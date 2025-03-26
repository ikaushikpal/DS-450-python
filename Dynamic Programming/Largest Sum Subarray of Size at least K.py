# Given an array and a number k, find the largest sum of the subarray containing at least k numbers. It may be assumed that the size of array is at-least k.


# Example 1:

# Input : 
# n = 4
# arr[] = {-4, -2, 1, -3}
# k = 2

# Output : 
# -1

# Explanation :
# The sub array is {-2, 1}
 


# Example 2:
# Input :
# n = 6 
# arr[] = {1, 1, 1, 1, 1, 1}
# k = 2

# Output : 
# 6

# Explanation :
# The sub array is {1, 1, 1, 1, 1, 1}


class Solution:
    def kadaneAlgo(self, arr):
        dp = [0] * len(arr)
        currentBest = 0
        
        for i in range(len(arr)):
            if currentBest + arr[i] >= arr[i]:
                currentBest += arr[i]
            else:
                currentBest = arr[i]
            dp[i] = currentBest

        return dp
    
    def calcPrefixSum(self, arr):
        prefix = [0] * len(arr)

        for i, val in enumerate(arr):
            prefix[i] = prefix[i-1] + val

        return prefix

    def maxSumAtleastK(self, arr, k):
        if len(arr) == k:
            return sum(arr)
        
        dp = self.kadaneAlgo(arr)
        prefix = self.calcPrefixSum(arr)
        maxSum = prefix[k-1]

        for i in range(k, len(arr)):
            windowSum = prefix[i] - prefix[i-k]
            temp = max(windowSum, windowSum + dp[i-k])
            maxSum = max(temp, maxSum)
        
        return maxSum
# Time Complexity: O(n)
# Space Complexity: O(n)


def maxSumWithK(a, n, k):
    return Solution().maxSumAtleastK(a, k)


if __name__ == '__main__':
    print(maxSumWithK([-4, -2, 1, -3], 4, 2))
    print(maxSumWithK([1, 1, 1, 1, 1, 1], 6, 2))
    print(maxSumWithK([5, 7, -9, 3, -4, 2, 1, -8, 9, 10], 10, 5))