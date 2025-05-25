# Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

# A pair (i, j) is fair if:

# 0 <= i < j < n, and
# lower <= nums[i] + nums[j] <= upper
 
# Example 1:
# Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
# Output: 6
# Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

# Example 2:
# Input: nums = [1,7,9,2,5], lower = 11, upper = 11
# Output: 1
# Explanation: There is a single fair pair: (2,3).
 

# Constraints:
# 1 <= nums.length <= 10^5
# nums.length == n
# -109 <= nums[i] <= 10^9
# -109 <= lower <= upper <= 10^9



from typing import List


class Solution:
    def ceil(self, nums, low, high, target):
        ans = low

        while low <= high:
            mid = (low + high) >> 1

            if nums[mid] <= target:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
    
    def floor(self, nums, low, high, target):
        ans = high

        while low <= high:
            mid = (low + high) >> 1

            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        N = len(nums)
        ans = 0

        for i in range(N-1):
            min_index = self.floor(nums, i + 1, N - 1, lower-nums[i])
            max_index = self.ceil(nums, i + 1, N - 1, upper-nums[i])
            
            if nums[min_index] >= lower - nums[i] and nums[max_index] <= upper - nums[i]:
                ans += max_index - min_index + 1
        return ans
# Time Complexity: O(NlogN)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6))
    print(sol.countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11))