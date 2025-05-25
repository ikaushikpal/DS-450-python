# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
            
        low = mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            val = nums[mid]
            if val == 0:
                swap(nums, low, mid)
                low += 1
                mid += 1
                
            elif val == 1:
                mid += 1
                
            else:
                swap(nums, high, mid)
                high -= 1
# Time Complexity: O(n)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortColors([2,0,2,1,1,0]))
    print(sol.sortColors([2,0,1]))