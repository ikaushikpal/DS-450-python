# Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

# A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

 

# Example 1:
# Input: nums = [10,2,-10,5,20], k = 2
# Output: 37
# Explanation: The subsequence is [10, 2, 5, 20].


# Example 2:
# Input: nums = [-1,-2,-3], k = 1
# Output: -1
# Explanation: The subsequence must be non-empty, so we choose the largest number.


# Example 3:
# Input: nums = [10,-2,-10,-5,20], k = 2
# Output: 23
# Explanation: The subsequence is [10, -2, -5, 20].


from typing import List


class Solution:
    def f(self, nums, k, i):
        if i >= len(nums):
            return float('-inf')
        

        ans1 = self.f(nums, k, i + 1)

        ans2 = float('-inf')
        for j in range(i+2, i+k+1):
            ans2 = max(ans2, self.f(nums, k, j + 1))

        return max(ans1, ans2, nums[i], ans1 + nums[i], ans2 + nums[i])
    
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        return self.f(nums, k, 0)
    


if __name__ == '__main__':
    sol = Solution()
    print(sol.constrainedSubsetSum(nums = [10,2,-10,5,20], k = 2))
    print(sol.constrainedSubsetSum(nums = [-1,-2,-3], k = 1))
    print(sol.constrainedSubsetSum(nums = [10,-2,-10,-5,20], k = 2))