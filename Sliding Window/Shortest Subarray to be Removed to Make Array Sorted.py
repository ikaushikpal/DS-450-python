# Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.
# Return the length of the shortest subarray to remove.
# A subarray is a contiguous subsequence of the array.

 
# Example 1:
# Input: arr = [1,2,3,10,4,2,3,5]
# Output: 3
# Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
# Another correct solution is to remove the subarray [3,10,4].


# Example 2:
# Input: arr = [5,4,3,2,1]
# Output: 4
# Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].


# Example 3:
# Input: arr = [1,2,3]
# Output: 0
# Explanation: The array is already non-decreasing. We do not need to remove any elements.


from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        
        while left+1 < len(arr) and arr[left] <= arr[left + 1]:
            left += 1
        
        # in descending order
        if left == len(arr) - 1:
            return 0
        
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        
        window = min(len(arr)-left-1, right)
        i, j = 0, right
        
        while i<=left and j<len(arr):
            if arr[i] <= arr[j]:
                window = min(window, j-i-1)
                i += 1
            else:
                j += 1
        
        return window
        

if __name__ == '__main__':
    sol = Solution()
    arr = [1,2,3,10,4,2,3,5]
    print(sol.findLengthOfShortestSubarray(arr))
    
    arr = [5,4,3,2,1]
    print(sol.findLengthOfShortestSubarray(arr))
    
    arr = [1,2,3]
    print(sol.findLengthOfShortestSubarray(arr))