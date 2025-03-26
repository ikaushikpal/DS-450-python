# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# A subarray is a contiguous subsequence of the array.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


from multiprocessing.dummy import current_process
from typing import List
import heapq
from functools import lru_cache
from collections import Counter, deque


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_product = 1
        ans = float('-inf')

        for val in nums:
            current_product *= val
            ans = max(ans, current_product)

            if current_product == 0:
                current_product = 1
        
        current_product = 1
        for val in nums[::-1]:
            current_product *= val
            ans = max(ans, current_product)

            if current_product == 0:
                current_product = 1

        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProduct([2,3,-2,4]))
    print(sol.maxProduct([-2,0,-1]))
    print(sol.maxProduct([-1,-2,-3,0]))
