# Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.

# The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.

# A subarray is a contiguous part of an array.

 

# Example 1:
# Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
# Output: 20
# Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.


# Example 2:
# Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
# Output: 29
# Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.


# Example 3:
# Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
# Output: 31
# Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [0,3,8] with length 3.


from typing import List


class Solution:
    def findMaxSub(self, nums, low, high, k):
        if high - low + 1 < k:
            return -1, float('-inf')

        currWindow = 0
        for i in range(low, low + k):
            currWindow += nums[i]
        finalWindowSum, finalStart = currWindow, low
        
        for i in range(low + k, high+1):
            currWindow += nums[i] - nums[i - k]
            if currWindow > finalWindowSum:
                finalWindowSum = currWindow
                finalStart = i - k + 1

        return finalStart, finalWindowSum

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        s1, tot1 = self.findMaxSub(nums, 0, len(nums) - secondLen-1, firstLen)
        s2, tot2 = self.findMaxSub(nums, secondLen, len(nums)-1, firstLen)
        if s1 == s2:
            _, tot11 = self.findMaxSub(nums, 0, s1 - 1, secondLen)
            _, tot12 = self.findMaxSub(nums, s1 + firstLen, len(nums)-1, secondLen)
            return tot1 + max(tot11, tot12)
        else:
            _, tot11 = self.findMaxSub(nums, 0, s1 - 1, secondLen)
            _, tot12 = self.findMaxSub(nums, s1 + firstLen, len(nums)-1, secondLen)

            _, tot21 = self.findMaxSub(nums, 0, s2 - 1, secondLen)
            _, tot22 = self.findMaxSub(nums, s2 + firstLen, len(nums)-1, secondLen)

            return max(tot1 + max(tot11, tot12),
                    tot2 + max(tot21, tot22))


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1, 2))
    print(sol.maxSumTwoNoOverlap([3,8,1,3,2,1,8,9,0], 3, 2))
    print(sol.maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8], 4, 3))
