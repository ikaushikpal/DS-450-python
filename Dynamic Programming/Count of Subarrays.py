# Given an array of N positive integers  Arr1, Arr2 ............ Arrn. The value of each contiguous subarray of given array is the maximum element present in that subarray. The task is to return the number of subarrays having value strictly greater than K.


# Example 1:
# Input:
# N = 3, K = 2
# Arr[] = {3, 2, 1}
# Output: 3
# Explanation: The subarrays having value
# strictly greater than K are: [3], [3, 2]
# and [3, 2, 1]. Thus there are 3 such
# sub-arrays.


# Example 2:
# Input:
# N = 4, K = 1
# Arr[] = {1, 2, 3, 4}
# Output: 9
# Explanation: There are 9 subarrays having
# value strictly greater than K.

class Solution:
    def countSubarray(self,arr, n, k):
        prev = ans = 0
        for i in range(n):
            if arr[i] > k:
                prev = i + 1
            ans += prev
        return ans
# Time Complexity: O(N)
# Auxiliary Space: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubarray([3, 2, 1], 3, 2))
    print(sol.countSubarray([1, 2, 3, 4], 4, 1))