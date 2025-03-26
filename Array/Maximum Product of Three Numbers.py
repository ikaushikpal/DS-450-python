# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

# Example 1:

# Input: nums = [1,2,3]
# Output: 6

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 24

# Example 3:
# Input: nums = [-1,-2,-3]
# Output: -6


from typing import List
import heapq
from functools import lru_cache
from collections import Counter, deque


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])

        
if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumProduct([1,2,3]))
    print(sol.maximumProduct([1,2,3,4]))
    print(sol.maximumProduct([-1,-2,-3]))
    print(sol.maximumProduct([-100,-98,-1,2,3,4]))