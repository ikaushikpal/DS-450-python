# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4


# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


# Example 3:
# Input: nums = [1], target = 0
# Output: -1



from typing import List


class Solution:
    def findSplit(self, nums):
        """
        Find the index at which the array `nums` is split into two sorted subarrays.

        Args:
            nums (List[int]): The input array.

        Returns:
            int: The index at which the array is split. Returns -1 if no split is found.
        """
        N = len(nums)

        # Check if the array is already sorted
        if nums[0] < nums[N-1]:
            return 0

        low, high = 0, N-1

        while low <= high:
            # Check if the current subarray is sorted
            if nums[low] < nums[high]:
                return low

            mid = low + ((high-low) >> 1)
            
            mid_next = (mid+1) % N
            mid_prev = (mid-1+N) % N

            if nums[mid_prev] >= nums[mid] <= nums[mid_next]:
                return mid
                
            elif nums[low] <= nums[mid]:
                low = mid + 1

            elif nums[mid] <= nums[high]:
                high = mid - 1

        return -1
    
    def binarySearch(self, nums, target, start, end):
        """
        Perform binary search on a sorted list of numbers.

        Args:
            nums (List[int]): The sorted list of numbers.
            target (int): The number to search for.
            start (int): The starting index of the search range.
            end (int): The ending index of the search range.

        Returns:
            int: The index of the target number in the list, or -1 if not found.
        """
        while start <= end:
            mid = (start + end) >> 1
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        partIndex = self.findSplit(nums)
        
        start, end = 0, partIndex - 1
        res = self.binarySearch(nums, target, start, end)
        if res != -1:
            return res
        
        start, end = partIndex, len(nums) - 1
        res = self.binarySearch(nums, target, start, end)
        return res
    

if __name__ == '__main__':
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 0))
    print(s.search([4,5,6,7,0,1,2], 3))
    print(s.search([1], 0))
    print(s.search([6,7,1,2,3,4,5], 6))
    print(s.search([1], 1))