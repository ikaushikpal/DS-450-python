# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

# Example 1:
# Input: nums = [1,2,2,3]
# Output: true


# Example 2:
# Input: nums = [6,5,4,4]
# Output: true


# Example 3:
# Input: nums = [1,3,2]
# Output: false


from typing import List


class Solution:
    def checkMonotonicInc(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True
    
    def checkMonotonicDec(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                return False
        return True
    
    def isMonotonic(self, nums: List[int]) -> bool:
        return self.checkMonotonicInc(nums) or self.checkMonotonicDec(nums)
# Time Complexity: O(N)
# Space Complexity: O(1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMonotonic([1,2,2,3]))
    print(solution.isMonotonic([6,5,4,4]))
    print(solution.isMonotonic([1,3,2]))
