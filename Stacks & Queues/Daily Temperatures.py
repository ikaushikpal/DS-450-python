# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
from typing import List
from collections import deque


class Solution:
    def nextGreaterRight(self, nums: List[int]) -> List[int]:
        # approach:
        # 1. use a stack to store the index of the last element that is greater than the current element
        # 2. if the stack is empty, then the current element is the last element that is greater than the current element
        # 3. pushing current index to stack
        # we are maintaining a monotonic decreasing stack

        ans = [0] * len(nums)
        stack = deque()

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)

        return ans

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return self.nextGreaterRight(temperatures)


if __name__ == '__main__':
    sol = Solution()
    print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(sol.dailyTemperatures([30, 40, 50, 60]))
    print(sol.dailyTemperatures([30, 60, 90]))