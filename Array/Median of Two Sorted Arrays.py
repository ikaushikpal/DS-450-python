# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


from typing import List



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        partition_size = total_length // 2

        # checking whether num2 is longer than num1
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        INF = 1000_000_007
        low, high = 0, len(nums1) - 1
        
        while True:
            mid = (low + high) >> 1
            i, j = mid, partition_size - mid -2

            left_nums1 = nums1[i] if i >= 0 else -INF
            right_nums1 = nums1[i + 1] if (i + 1) < len(nums1) else INF

            left_nums2 = nums2[j] if j >= 0 else -INF
            right_nums2 = nums2[j + 1] if (j + 1) < len(nums2) else INF

            if left_nums1 <= right_nums2 and left_nums2 <= right_nums1:
                if total_length & 1:
                    return min(right_nums1, right_nums2)
                else:
                    return (max(left_nums1, left_nums2) + min(right_nums1, right_nums2)) / 2
            
            elif left_nums1 > right_nums2:
                high = mid - 1
            
            elif left_nums2 > right_nums1:
                low = mid + 1
    
    