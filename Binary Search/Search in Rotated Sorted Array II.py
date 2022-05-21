# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.

# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true

# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1

        while low <= high:
            mid = (low + high) >> 1

            # found targetValue
            if nums[mid] == target:
                return True
            
            # if both low and high same
            # that means we don't know where to go
            # so increment and decrement low and high respectively
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1

            # if left half is sorted
            elif nums[low] <= nums[mid]:
                # if target value in between low and mid
                if nums[low] <= target and nums[mid] > target:
                    high = mid - 1
                # else target value in between mid and high
                else:
                    low = mid + 1
            # else right half is sorted
            else:
                # if target value in between mid and high
                if nums[high] >= target and nums[mid] < target:
                    low = mid + 1
                # else target value in between low and mid
                else:
                    high = mid - 1

        # count not find target Value
        return False

# Time Complexity:
# Best/ Average Case : O(logn)
# Worst Case : O(n) [when all values are same]

#Space Complexity : O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.search(nums = [2,5,6,0,0,1,2], target = 3))
    print(sol.search([1], 1))
    print(sol.search([5,1,3], 3))
            