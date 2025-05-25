# You are given an integer array nums and two integers minK and maxK.

# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.

# A subarray is a contiguous part of an array.


# Example 1:
# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

# Example 2:
# Input: nums = [1,1,1,1], minK = 1, maxK = 1
# Output: 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
 

# Constraints:
# 2 <= nums.length <= 10^5
# 1 <= nums[i], minK, maxK <= 10^6

from typing import List


class Solution:
    def splitArray(self, nums: List[int], minK: int, maxK: int) -> List[List[int]]:
        ans = []
        start = 0

        for end, num in enumerate(nums):
            if num < minK or num > maxK:
                if end - start - 1 > 0:
                    sub_array = nums[start : end]
                    ans.append(sub_array)
                start = end + 1

        sub_array = nums[start : end]
        ans.append(sub_array)
        return ans

    def countSubArraysHelper(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        min_indices = []
        max_indices = []

        for i, num in enumerate(nums):
            if num == minK:
                min_indices.append(i)
            
            if num == maxK:
                max_indices.append(i)
        
        seen = set()
        for i, min_index in enumerate(min_indices):
            for j, max_index in enumerate(max_indices):
                minn = min(min_index, max_index)
                maxx = max(min_index, max_index)

                if (minn, maxx) in seen:
                    continue

                left = minn
                right = len(nums) - maxx - 1

                ans += (left + 1) * (right + 1)
                seen.add((minn, maxx))
        return ans 
    
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        splits = self.splitArray(nums, minK, maxK)
        ans = 0

        for arr in splits:
            ans += self.countSubArraysHelper(arr, minK, maxK)
        return ans
    


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubarrays(nums = [1,3,5,2,7,5], minK = 1, maxK = 5))
    print(sol.countSubarrays(nums = [1,1,1,1], minK = 1, maxK = 1))