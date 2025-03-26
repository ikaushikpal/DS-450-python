# Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

# Example 1:
# Input:
# N = 5
# Arr[] = {1,2,3,-2,5}

# Output:
# 9

# Explanation:
# Max subarray sum is 9
# of elements (1, 2, 3, -2, 5) which 
# is a contiguous subarray.



# Example 2:
# Input:
# N = 4
# Arr[] = {-1,-2,-3,-4}

# Output:
# -1

# Explanation:
# Max subarray sum is -1 
# of element (-1)


class Solution:
    def maxSubArraySum(self, arr, size):
        currentBest, overallBest = 0, -10e7
        
        for val in arr:
            if val + currentBest >= val:
                currentBest += val
            else:
                currentBest = val
            
            overallBest = max(overallBest, currentBest)
        
        return overallBest


if __name__ == '__main__':
    sol = Solution()
    arr = [1,2,3,-2,5]
    size = len(arr)
    print(sol.maxSubArraySum(arr, size))
    arr = [-1,-2,-3,-4]
    size = len(arr)
    print(sol.maxSubArraySum(arr, size))