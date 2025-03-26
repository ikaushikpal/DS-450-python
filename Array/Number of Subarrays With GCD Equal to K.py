# Given an integer array nums and an integer k, return the number of subarrays of nums where the greatest common divisor of the subarray's elements is k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# The greatest common divisor of an array is the largest integer that evenly divides all the array elements.


# Example 1:
# Input: nums = [9,3,1,2,6,3], k = 3
# Output: 4
# Explanation: The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:
# - [9,3,1,2,6,3]
# - [9,3,1,2,6,3]
# - [9,3,1,2,6,3]
# - [9,3,1,2,6,3]


# Example 2:
# Input: nums = [4], k = 7
# Output: 0
# Explanation: There are no subarrays of nums where 7 is the greatest common divisor of all the subarray's elements.


from typing import List


class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a%b)
    
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        N = len(nums)
        
        for i in range(N):
            gcdVal = nums[i]
            for j in range(i, N):
                gcdVal = self.gcd(gcdVal, nums[j])
                
                if gcdVal == k:
                    ans += 1
                
                if gcdVal < k:
                    break
        return ans
# Time Complexity: O(N^2)
# Space Complexity: O(1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarrayGCD([9,3,1,2,6,3], 3))
    print(sol.subarrayGCD([4], 7))