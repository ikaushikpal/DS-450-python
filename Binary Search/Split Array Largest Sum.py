# Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

# Write an algorithm to minimize the largest sum among these m subarrays.


# Example 1:
# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.

# Example 2:
# Input: nums = [1,2,3,4,5], m = 2
# Output: 9

# Example 3:
# Input: nums = [1,4,4], m = 3
# Output: 4


from typing import List

# this problem is very similar to minimum allocation books[GOOGLE]
class Solution:
    def isValid(self, nums, m, maxSum):
        total = 0

        for num in nums:
            total += num
            # if total exceeds maxSum
            # that means we need to split array here
            if total > maxSum:
                m -= 1
                total = num
            
            # if we splited array more than its allowed then
            # simply return False meaning we can not form split
            if m <= 0:
                return False

        # we can split array in to m parts
        return True
    
    def findMaxSum(self, nums):
        total, maxValue = 0, float('-inf')
        for num in nums:
            total += num
            maxValue = max(maxValue, num)
        
        return (maxValue, total)

    def splitArray(self, nums: List[int], m: int) -> int:
        # edge case
        if m > len(nums):
            return -1
        
        maxValue, total = self.findMaxSum(nums)

        if m == len(nums):
            return maxValue

        if m == 1:
            return total

        low, high = maxValue, total
        ans = -1

        while low <= high:
            mid = (low + high) >> 1

            # if we can split array into m parts
            # with mid as maxSum then go left for more minimum ans
            if self.isValid(nums, m, mid):
                ans = mid
                high = mid - 1
            else:
                # could not split into m with current mid, go right
                low = mid + 1
        
        return ans
# Time Complexity : O(NlogK)
# where N = len(nums) and K is diff between total(nums) - max(nums)

# Space Complexity : O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.splitArray(nums = [7,2,5,10,8], m = 2))
    print(sol.splitArray(nums = [1,2,3,4,5], m = 2))
    print(sol.splitArray(nums = [1,4,4], m = 3))