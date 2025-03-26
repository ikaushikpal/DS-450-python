# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

# Example 1:
# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.


# Example 2:
# Input: nums = [4,2,1]
# Output: false
# Explanation: You can't get a non-decreasing array by modify at most one element.


from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        countInversion = 0
        pos = -1
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                countInversion += 1
                pos = i
            
            if countInversion > 1:
                return False
            
        if countInversion == 0 or pos == 0 or pos >= len(nums) - 2:
            return True
        
        return nums[pos - 1] <= nums[pos + 1] or nums[pos] <= nums[pos + 2]
# Time Complexity: O(n)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkPossibility([4,2,3]))
    print(sol.checkPossibility([4,2,1]))
    print(sol.checkPossibility([3,4,2,3]))