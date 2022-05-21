# You are given an array Arr of size N. You have to find the K-th largest sum of contiguous subarray within the array elements.


# Example 1:
# Input:
# N = 3
# K = 2
# Arr = {3,2,1}
# Output:
# 5
# Explanation:
# The different subarray sums we can get from the array
# are = {6,5,3,2,1}. Where 5 is the 2nd largest.
 

# Example 2:
# Input:
# N = 4
# K = 3
# Arr = {2,6,4,1}
# Output:
# 11
# Explanation:
# The different subarray sums we can get from the array
# are = {13,12,11,10,8,6,5,4,2,1}. Where 11 is the 3rd largest.


from typing import List
from heapq import heappush, heappop


class Solution:
    def kthLargest(self, N : int, K : int, nums : List[int]) -> int:
        minHeap = []
        prefixSum = [0] * (N + 1)
        for i in range(N):
            prefixSum[i+1] = prefixSum[i] + nums[i]
        
        for i in range(1, N+1):
            for j in range(i, N+1):
                value = prefixSum[j] - prefixSum[i - 1]
                heappush(minHeap, value)

                if len(minHeap) > K:
                    heappop(minHeap)
        
        return heappop(minHeap)
# Time Complexity : O((N^2)logK)
# Space Complexity : O(K)


if __name__ == '__main__':
    sol = Solution()
    print(sol.kthLargest(3, 2, [3,2,1]))
    print(sol.kthLargest(4, 3, [2,6,4,1]))
    print(sol.kthLargest(3, 3, [20, -5, -1]))
