# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Example 2:
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

# Constraints:
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100



from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # similar to 0/1 Knapsack
        N = len(nums)
        total_sum = sum(nums)

        if total_sum & 1:
            return False
        
        target_sum = total_sum >> 1
        dp = [False] * (target_sum + 1)

        dp[0] = True
        
        for i in range(1, N + 1):
            new_dp = [False] * (target_sum + 1)
            new_dp[0] = True

            for j in range(1, target_sum + 1):
                new_dp[j] = dp[j]
                
                if j - nums[i - 1] >= 0:
                    new_dp[j] |= dp[j - nums[i - 1]]
            dp = new_dp
            
            # early exiting, if already one subset satisfy then no need more iteration
            if dp[target_sum]:
                return True
        return False
# Time Complexity: O(N^2)
# Space Complexity: O(N)



if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartition(nums = [1,2,5]))
    print(sol.canPartition(nums = [1,5,11,5]))
    print(sol.canPartition(nums = [1,2,3,5]))