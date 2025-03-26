# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.
# Return the shortest such subarray and output its length.

# Example 1:
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 0

# Example 3:
# Input: nums = [1]
# Output: 0


from typing import List
import heapq
from functools import lru_cache
from collections import Counter, deque


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        leftBoundary , rightBoundary = 0, -1

        leftMax = nums[0]
        for i in range(1, len(nums)):
            if leftMax > nums[i]:
                rightBoundary = i
            else:
                leftMax = nums[i]

        rightMin = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if rightMin < nums[i]:
                leftBoundary = i
            else:
                rightMin = nums[i]

        return rightBoundary - leftBoundary + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findUnsortedSubarray([2,6,4,8,10,9,15]))
    print(sol.findUnsortedSubarray([1, 2, 3, 4]))
    print(sol.findUnsortedSubarray([0]))
    print(sol.findUnsortedSubarray([2,1]))
