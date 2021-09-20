# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        if n == 0: # empty array
            return [0]
        
        if n == 1: # sets say array is [100], so totalMul = 100
            return [1] # then 100/100 = 1 so return 1
        
        left = [0] * n  # cumulative multiplication from left to right (including i)
        right = [0] * n # cumulative multiplication from right to left (including i)
        left[0], right[-1] = nums[0], nums[-1]

        for i in range(1, n):
            left[i] = left[i-1] * nums[i]
            right[n-i-1] = right[n-i] * nums[n-i-1]

        res = [0] * n
        res[0], res[-1] = right[1], left[-2]

        for i in range(1, n-1):
            res[i] = left[i-1] * right[i+1]

        return res


if __name__ == '__main__':
    arr = [10, 3, 5, 6, 2]
    print(Solution().productExceptSelf(arr))