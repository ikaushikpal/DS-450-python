# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

# Example 1:
# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.


# Example 2:
# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.


# Example 3:
# Input: nums = [23,2,6,4,7], k = 13
# Output: false


from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        # storing reminder to index location map
        remainderMap = {0:-1} # initial for remainder 0
        tot = 0
        
        for i, num in enumerate(nums):
            tot += num
            rem = tot % k
            
            if rem in remainderMap:
                # checking if size of subarray is more than 1
                if i - remainderMap[rem] > 1:
                    return True
            else:
                remainderMap[rem] = i
        return False
# Time Complexity: O(N)
# Space Complexity: O(K)


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkSubarraySum([23,2,4,6,7], 6))
    print(sol.checkSubarraySum([23,2,6,4,7], 6))
    print(sol.checkSubarraySum([23,2,6,4,7], 13))