# You are given an array nums consisting of positive integers.

# We call a subarray of an array complete if the following condition is satisfied:

# The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
# Return the number of complete subarrays.

# A subarray is a contiguous non-empty part of an array.

 
# Example 1:
# Input: nums = [1,3,1,2,2]
# Output: 4
# Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].

# Example 2:
# Input: nums = [5,5,5,5]
# Output: 10
# Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
 

# Constraints:
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2000

from typing import List


class Solution:
    def atMostK(self, nums: List[int], K) -> int:
        ans = i = 0
        visited = {}

        for j, num in enumerate(nums):
            if num not in visited:
                visited[num] = 0
            
            visited[num] += 1

            while i < len(nums) and len(visited) > K:
                rem_num = nums[i]
                visited[rem_num] -= 1

                if visited[rem_num] == 0:
                    del visited[rem_num]
                
                i += 1
            ans += j - i + 1
        return ans

    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        K = len(unique_nums)

        return self.atMostK(nums, K) - self.atMostK(nums, K - 1)
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countCompleteSubarrays(nums = [1,3,1,2,2]))
    print(sol.countCompleteSubarrays(nums = [5,5,5,5]))