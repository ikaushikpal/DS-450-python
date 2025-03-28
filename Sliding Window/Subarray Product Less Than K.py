# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.


# Example 1:
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.


# Example 2:
# Input: nums = [1,2,3], k = 0
# Output: 0


from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k < 1:
            return 0
        
        ans = i = 0
        currentProduct = 1
        
        for j in range(len(nums)):
            currentProduct *= nums[j]
            
            while i <= j and currentProduct >= k:
                currentProduct /= nums[i]
                i += 1
            
            ans += j - i + 1
        
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numSubarrayProductLessThanK([10,5,2,6], 100))