# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 
# Example 1:
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.

# Example 2:
# Input: nums = [-1,0]
# Output: [-1,0]

# Example 3:
# Input: nums = [0,1]
# Output: [1,0]
 

# Constraints:
# 2 <= nums.length <= 3 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# Each integer in nums will appear twice, only two integers will appear once.


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        total_xor = 0
        for num in nums:
            total_xor = total_xor ^ num
        
        right_most_set_bit = (~(total_xor & (total_xor - 1))) & total_xor
        bucket1 = bucket2 = 0

        for num in nums:
            if num & right_most_set_bit > 0:
                bucket1 = bucket1 ^ num
            else:
                bucket2 = bucket2 ^ num
        return [bucket1, bucket2]
# Time Complexity: O(N)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber(nums = [1,2,1,3,2,5]))
    print(sol.singleNumber(nums = [-1,0]))
    print(sol.singleNumber(nums = [0,1]))