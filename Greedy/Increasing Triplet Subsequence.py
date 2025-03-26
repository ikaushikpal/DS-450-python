# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 
# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.

# Example 2:
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.

# Example 3:
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # idea is to maintain two smallest value from left side
        # if any number is grater than 2nd smallest then we found a triplet
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
# Time Complexity: O(n)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.increasingTriplet([1, 2, 3, 4, 5]))
    print(sol.increasingTriplet([5, 4, 3, 2, 1]))
    print(sol.increasingTriplet([2, 1, 5, 0, 4, 6]))