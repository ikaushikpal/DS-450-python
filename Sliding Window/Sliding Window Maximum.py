# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7


# Example 2:
# Input: nums = [1], k = 1
# Output: [1]


from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []
        
        for i in range(len(nums)):
            if queue and queue[0] <= i - k:
                queue.popleft()
            
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            
            queue.append(i)
            
            if i >= k - 1:
                ans.append(nums[queue[0]])
        return ans
# Time Complexity: O(N)
# Space Complexity: O(K)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
    print(sol.maxSlidingWindow(nums = [1], k = 1))