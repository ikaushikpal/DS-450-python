# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
# A subarray is a contiguous subsequence of the array.


# Example 1:
# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58


# Example 2:
# Input: arr = [1,2]
# Output: 3
# Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.


# Example 3:
# Input: arr = [10,11,12]
# Output: 66


from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res, n = 0, len(arr)
        
        for i, val in enumerate(arr):
            # total occurrences of arr[i] of 1, 2, 3, ... n sized window
            occurrences = (i + 1) * (n - i) 
            # now here given alternating window then need to divide by 2
            # but if length of arr is odd then add 1 extra
            if n & 1:
                occurrences = (occurrences + 1) >> 1
            else:
                occurrences = occurrences >> 1
            res += val * occurrences
        
        return res
# Time Complexity: O(n)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.sumOddLengthSubarrays([1,4,2,5,3]))
    print(sol.sumOddLengthSubarrays([1,2]))
    print(sol.sumOddLengthSubarrays([10,11,12]))