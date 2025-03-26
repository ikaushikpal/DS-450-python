# You are given two positive integer arrays nums1 and nums2, both of length n.

# The absolute sum difference of arrays nums1 and nums2 is defined as the sum of |nums1[i] - nums2[i]| for each 0 <= i < n (0-indexed).

# You can replace at most one element of nums1 with any other element in nums1 to minimize the absolute sum difference.

# Return the minimum absolute sum difference after replacing at most one element in the array nums1. Since the answer may be large, return it modulo 109 + 7.

# |x| is defined as:

# x if x >= 0, or
# -x if x < 0.
 

# Example 1:

# Input: nums1 = [1,7,5], nums2 = [2,3,5]
# Output: 3
# Explanation: There are two possible optimal solutions:
# - Replace the second element with the first: [1,7,5] => [1,1,5], or
# - Replace the second element with the third: [1,7,5] => [1,5,5].
# Both will yield an absolute sum difference of |1-2| + (|1-3| or |5-3|) + |5-5| = 3.

# Example 2:

# Input: nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
# Output: 0
# Explanation: nums1 is equal to nums2 so no replacement is needed. This will result in an 
# absolute sum difference of 0.

# Example 3:

# Input: nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
# Output: 20
# Explanation: Replace the first element with the second: [1,10,4,4,2,7] => [10,10,4,4,2,7].
# This yields an absolute sum difference of |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20


from typing import List


class Solution:
    def findCeil(self, arr, key):
        low, high = 0, len(arr)-1
        res = -1

        while low <= high:
            mid = (low+high)//2

            if arr[mid] == key:
                return mid
            
            elif arr[mid] < key:
                low = mid + 1       
            else:
                res = mid
                high = mid - 1

        return res

    def findFloor(self, arr, key):
        low, high = 0, len(arr)-1
        res = -1

        while low <= high:
            mid = (low+high)//2

            if arr[mid] == key:
                return mid
            
            elif arr[mid] < key:
                res = mid
                low = mid + 1       
            else:
                high = mid - 1

        return res

    def findClosestNumber(self, nums1, targetValue):
        ceilNumberPos = self.findCeil(nums1, targetValue)
        floowNumberPos = self.findFloor(nums1, targetValue)

        ceilNumber = nums1[ceilNumberPos] if ceilNumberPos != -1 else float('inf')
        floorNumber = nums1[floowNumberPos] if floowNumberPos != -1 else float('inf')

        ceilDiff = abs(ceilNumber - targetValue)
        floorDiff = abs(floorNumber - targetValue)

        if floorDiff < ceilDiff:
            return floorNumber
        return ceilNumber

    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_copy = nums1.copy()
        nums1_copy.sort()

        totalDiff = canLoseDiff = 0

        for i in range(len(nums1)):
            abs_diff = abs(nums1[i] - nums2[i])
            totalDiff += abs_diff

            if abs_diff == 0:
                continue
            
            closedNumber = self.findClosestNumber(nums1_copy, nums2[i])
            new_diff = abs(nums2[i] - closedNumber)
            canLoseDiff = max(canLoseDiff, abs(new_diff - abs_diff))

        return (totalDiff - canLoseDiff) % 1_000_000_007

        
# Time Complexity : O(nlogn)
# Space Complexity : O(n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minAbsoluteSumDiff([1,7,5], [2,3,5]))
    print(sol.minAbsoluteSumDiff([2,4,6,8,10], [2,4,6,8,10]))
    print(sol.minAbsoluteSumDiff([1,10,4,4,2,7], [9,3,5,1,7,4]))
    print(sol.minAbsoluteSumDiff([1,1,1], [1,1,1]))