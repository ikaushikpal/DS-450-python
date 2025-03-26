# Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:

# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
# Return the length of left after such a partitioning.

# Test cases are generated such that partitioning exists.

 

# Example 1:

# Input: nums = [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
# Example 2:

# Input: nums = [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]


from typing import List
import heapq
from functools import lru_cache
from collections import Counter, deque

# Time: O(n)
# Space : O(n)
class Solution1:
    def generateRightMin(self, arr):
        rightMin = [float('inf')] * (len(arr) + 1)

        for i in range(len(arr)-1, -1, -1):
            rightMin[i] = min(rightMin[i + 1], arr[i])

        return rightMin
    
    def partitionDisjoint(self, nums: List[int]) -> int:
        maxSofar = float('-inf')
        
        rightMin = self.generateRightMin(nums)
        
        for i in range(len(nums)):
            maxSofar = max(maxSofar, nums[i])
            if maxSofar <= rightMin[i + 1]:
                return i + 1

        return 1


# Time: O(n)
# Space : O(1)
class Solution:  
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = greater = nums[0]
        ans = 0

        for i in range(1, len(nums)):
            if nums[i] > greater:
                greater = nums[i]
            
            elif nums[i] < left_max:
                left_max = greater
                ans = i
        
        return ans + 1

        
if __name__ == '__main__':
    sol = Solution()
    print(sol.partitionDisjoint([5,0,3,8,6]))
    print(sol.partitionDisjoint([1,1,1,0,6,12]))