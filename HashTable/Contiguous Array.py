# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.


# Example 1:
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.


# Example 2:
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


from typing import List


class Solution:
    def findMaxLengthSumZero(self, nums: List[int]) -> int:
        prefixMap = {}
        prefixMap[0] = -1
        maxLen = cumSum = 0

        for i, num in enumerate(nums):
            cumSum += num
            if cumSum in prefixMap:
                maxLen = max(maxLen, i - prefixMap[cumSum])
            else:
                prefixMap[cumSum] = i
        return maxLen

    def findMaxLength(self, nums: List[int]) -> int:
        # the trick is that map 0 to -1 and keep 1 to 1
        # then simply find maximum sub-array of sum == 0
        for i, num in enumerate(nums):
            if num == 0:
                nums[i] = -1
        return self.findMaxLengthSumZero(nums)
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxLength([0, 1]))
    print(sol.findMaxLength([0, 1, 0]))