# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

# Example 1:
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.


# Example 2:
# Input: nums = [1,2,3,4], k = 3
# Output: false


from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False

        subset_sum = nums_sum // k
        nums.sort(reverse=True)
        visited = [False] * len(nums)
        
        def can_partition(rest_k, cur_sum=0, next_index=0):
            if rest_k == 1:
                return True
            
            if cur_sum == subset_sum:
                return can_partition(rest_k - 1)
            
            for i in range(next_index, len(nums)):
                if not visited[i] and cur_sum + nums[i] <= subset_sum:
                    visited[i] = True
                    if can_partition(rest_k, cur_sum=cur_sum + nums[i], next_index=i + 1):
                        return True
                    visited[i] = False
            return False 
        
        return can_partition(k)


if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartitionKSubsets([4,3,2,3,5,2,1], 4))
    print(sol.canPartitionKSubsets([1,2,3,4], 3))
    print(sol.canPartitionKSubsets([2,2,2,2,3,4,5], 4))