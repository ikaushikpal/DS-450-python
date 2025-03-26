# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5


# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4


import random
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return heapq.heappop(minHeap)
# Time Complexity: O(NlogK)
# Space Complexity: O(K)

from random import randint



# Quick Select Algorithm
class Solution:
    def search(self, nums, k):
        # converting k-largest to k-smallest
        targetPos = len(nums) - k
        return self.searchUtil(0, len(nums)-1, targetPos, nums)

    def partition(self, left, right, index, arr):
        pivotValue = arr[index]
        arr[index], arr[right] = arr[right], arr[index]
        storeIndex = left

        for i in range(left, right):
            if arr[i] < pivotValue:
                arr[i], arr[storeIndex] = arr[storeIndex], arr[i]
                storeIndex += 1

        arr[storeIndex], arr[right] = arr[right], arr[storeIndex]
        return storeIndex

    def searchUtil(self, left, right, targetPos, arr):
        randIndex = randint(left, right)
        pivotIndex = self.partition(left, right, randIndex, arr)

        if pivotIndex == targetPos:
            return arr[pivotIndex]
        elif pivotIndex < targetPos:
            return self.searchUtil(pivotIndex + 1, right, targetPos, arr)
        else:
            return self.searchUtil(left, pivotIndex - 1, targetPos, arr)
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.search(nums, k)
# Time Complexity: avg=>O(N) and worst=>O(N^2)
# Space Complexity: O(1)

class Solution:
    def findPartition(self, nums, low, high):
        index = random.randint(low, high)
        pivotVal = nums[index]
        
        nums[index], nums[high] = nums[high], nums[index]
        i = low - 1
        
        for j in range(low, high + 1):
            if nums[j] < pivotVal:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        
        i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i
    
    def quickSelect(self, nums, k, low, high):
        pivotIndex = self.findPartition(nums, low, high)
        
        if pivotIndex == k:
            return nums[pivotIndex]
        
        elif pivotIndex > k:
            return self.quickSelect(nums, k, low, pivotIndex - 1)
        
        else:
            return self.quickSelect(nums, k, pivotIndex + 1, high)
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, len(nums) - k, 0, len(nums) - 1)
if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthLargest(nums = [3,2,1,5,6,4], k = 2))
    print(sol.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))