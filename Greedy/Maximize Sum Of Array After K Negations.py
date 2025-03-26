# Given an integer array nums and an integer k, modify the array in the following way:

# choose an index i and replace nums[i] with -nums[i].
# You should apply this process exactly k times. You may choose the same index i multiple times.

# Return the largest possible sum of the array after modifying it in this way.

 

# Example 1:
# Input: nums = [4,2,3], k = 1
# Output: 5
# Explanation: Choose index 1 and nums becomes [4,-2,3].


# Example 2:
# Input: nums = [3,-1,0,2], k = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].


# Example 3:
# Input: nums = [2,-3,-1,5,-4], k = 2
# Output: 13
# Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].


from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if k == 0:
                break
                
            if nums[i] < 0:
                k -= 1
                nums[i] = -nums[i]
        
        if k & 1:
            return sum(nums) - 2*min(nums)
        return sum(nums)
# Time Complexity: O(nlogn)
# Space Complexity: O(1)


if __name__ == '__main__':
    nums = [4,2,3]
    k = 1
    print(Solution().largestSumAfterKNegations(nums, k))

    nums = [3,-1,0,2]
    k = 3
    print(Solution().largestSumAfterKNegations(nums, k))
