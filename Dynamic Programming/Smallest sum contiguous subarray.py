# Given an array arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the minimum sum and return its sum.


# Example 1:
# Input: 
# arr[] = {3,-4, 2,-3,-1, 7,-5}
# Output: -6
# Explanation: sub-array which has smallest 
# sum among all the sub-array is {-4,2,-3,-1} = -6


# Example 2:
# Input:
# arr[] = {2, 6, 8, 1, 4}
# Output: 1
# Explanation: sub-array which has smallest
# sum among all the sub-array is {1} = 1


class Solution:
    def smallestSumSubarray(self, A, N):
        minSoFar, minTillNow = float('inf'), 0
        
        for i in range(N):
            minTillNow += A[i]
            minTillNow = min(minTillNow, A[i])
            minSoFar = min(minSoFar, minTillNow)
        return minSoFar
# Time Complexity: O(N)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestSumSubarray([3,-4, 2,-3,-1, 7,-5], 7))
    print(sol.smallestSumSubarray([2, 6, 8, 1, 4], 5))