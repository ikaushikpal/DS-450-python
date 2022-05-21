# You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

# Example 1:
# Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].


# Example 2:
# Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
# Output: [1,1]


import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        K = len(nums)
        currentWindow = (-10**5, 10**5)
        minHeap = []
        maxRange = -10**5

        for i in range(K):
            maxRange = max(maxRange, nums[i][0])
            minHeap.append((nums[i][0], i, 0))
        heapq.heapify(minHeap)

        while len(minHeap) == K:
            value, i, j = heapq.heappop(minHeap)
            if currentWindow[1] - currentWindow[0] + 1 > maxRange - value + 1:
                currentWindow = (value, maxRange)
            
            if j + 1 < len(nums[i]):
                maxRange = max(maxRange, nums[i][j + 1])
                heapq.heappush(minHeap, (nums[i][j+1], i, j+1))
        
        return currentWindow
# Time Complexity : O(NKlogK)
# Space Complexity: O(K)


if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestRange(nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))