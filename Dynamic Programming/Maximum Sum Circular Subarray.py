# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

# Example 1:
# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.


# Example 2:
# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.


# Example 3:
# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.

from typing import List


class Solution:
    def kadaneAlgo(self, nums):
        maxSoFar, maxEndingHere = float('-inf'), 0

        for num in nums:
            maxEndingHere += num
            
            if maxEndingHere > maxSoFar:
                maxSoFar = maxEndingHere
            
            if maxEndingHere < 0:
                maxEndingHere = 0

        return maxSoFar

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Intuition:
        # 1. If the array is non-circular, then the answer is simply the maximum subarray sum.
        # 2. If the array is circular, then the answer is the total sum minus the minimum subarray sum.

        # EDGE CASE: If all numbers are negative, return the largest number.

        nonCircularMaxSum = self.kadaneAlgo(nums)
        total = 0, float('-inf')
        anyPositiveNum = False

        for i in range(len(nums)):
            total += nums[i]
            maxNum = max(maxNum, nums[i])

            if nums[i] > 0:
                anyPositiveNum = True

            nums[i] = -nums[i]

        if not anyPositiveNum:
            return maxNum
        
        minimumSubarraySum = -self.kadaneAlgo(nums)
        CircularMaxSum = total - minimumSubarraySum
        
        return max(nonCircularMaxSum, CircularMaxSum)
# Time Complexity: O(n)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubarraySumCircular([1,-2,3,-2]))
    print(sol.maxSubarraySumCircular([5,-3,5]))
    print(sol.maxSubarraySumCircular([-3,-2,-3]))