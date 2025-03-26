# Given an integer array arr and an integer k, modify the array by repeating it k times.

# For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

# Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

# As the answer can be very large, return the answer modulo 109 + 7.

 

# Example 1:
# Input: arr = [1,2], k = 3
# Output: 9



# Example 2:
# Input: arr = [1,-2,1], k = 5
# Output: 2



# Example 3:
# Input: arr = [-1,-2], k = 7
# Output: 0

# NOTE:
# introduce some pattern firstly,

# 1. all positive : [1,2,3], k = 3, array_sum = 6
#     return array_sum*3


# 2. all negative : [-1,-2], k = 2, array_sum = -3
#     return 0


# 3. hybrid, with array_sum <= 0, [2,1,-3], k = 4, array_sum = 0
#        [ 2,  1, -3, 2, 1, -3, 2, 1, -3, 2, 1, -3]
# max sum  2   3  0   2  3  0   2  3   0   2  3  0
# 	return max_subarray_sum between [2,1,-3,2,1,-3] which is twice of original array
# 	so, return max_subarray_sum = 3


# 4. hybrid, with array_sum > 0, [2,-6,5], k =4, array_sum = 1
#        [ 2, -6, 5, 2, -6, 5, 2, -6, 5, 2, -6, 5]
# max sum  2   0  5  7   1  6  8   2  7  9   3  8


# a. you can notice max subarray sum is getting bigger as k grows up.
# b. with first 2 array, we can get max subarray sum is 8.
# c. after that, with each new array, max_subarray_sum will increase by 1, which is array_sum
# ==>return (max_subarray_sum when k=2) + array_sum*(k-2)


# formula :
# return ((max_subarray_sum when k = 2) + (array_sum>0?array_sum*(k-2):0))%1000000007


from typing import List


class Solution:
    def kadaneAlgo(self, arr):
        currentBest = overallBest = 0
        
        for i in range(len(arr)):
            if currentBest + arr[i] >= arr[i]:
                currentBest += arr[i]
            else:
                currentBest = arr[i]
            overallBest = max(overallBest, currentBest)

        return overallBest

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 1_000_000_007

        if k == 1:
            return self.kadaneAlgo(arr) % MOD
        else:
            total = sum(arr)
            concatArr = arr + arr
            
            if total <= 0:
                return self.kadaneAlgo(concatArr) % MOD
            else:
                return (self.kadaneAlgo(concatArr) + total * (k - 2)) % MOD
# Time Complexity: O(N)
# Space Complexity: O(1)       


if __name__ == '__main__':
    print(Solution().kConcatenationMaxSum([-4, -2, 1, -3], 4))
    print(Solution().kConcatenationMaxSum([1, 2], 3))
    print(Solution().kConcatenationMaxSum([1, -2, 1], 5))
    print(Solution().kConcatenationMaxSum([-1, -2], 7))