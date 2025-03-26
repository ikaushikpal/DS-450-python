# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 
# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0


from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        
        nums.sort()
        res = float('inf')
        for i in range(len(nums) - 2):
            j, k = i+1, len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if target == total:
                    return total
                
                elif abs(target - total) < abs(target - res):
                    res = total
                
                if total > target:
                    k -= 1
                else:
                    j += 1
        return res
# Time Complexity: O(NlogN + N^2) = O(N^2)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSumClosest([-1,2,1,-4], 1))
    print(sol.threeSumClosest([0,0,0], 1))