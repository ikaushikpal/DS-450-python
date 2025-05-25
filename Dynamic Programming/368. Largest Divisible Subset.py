# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.

 
# Example 1:
# Input: nums = [1,2,3]
# Output: [1,2]
# Explanation: [1,3] is also accepted.

# Example 2:
# Input: nums = [1,2,4,8]
# Output: [1,2,4,8]
 

# Constraints:
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2 * 10^9
# All the integers in nums are unique.


from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)

        nums.sort()
        dp = [ [] for _ in range(N)]

        for i in range(N-1, -1, -1):
            ans = []
            for j in range(i + 1, N):
                if nums[j] % nums[i] == 0:
                    if len(ans) < len(dp[j]):
                        ans = dp[j]

            ans_cpy = ans[:]
            ans_cpy.append(nums[i])
            dp[i] = ans_cpy
        
        ans = []
        for i in range(N):
            if len(dp[i]) > len(ans):
                ans = dp[i]
        return ans
# Time Complexity: O(N^2)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestDivisibleSubset(nums = [1,2,3]))
    print(sol.largestDivisibleSubset(nums = [1,2,4,8]))