# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

# Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

# The test cases are generated so that there will be an answer.

# Example 1:
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 

# Example 2:
# Input: nums = [44,22,33,11,1], threshold = 5
# Output: 44


from math import ceil
from typing import List


class Solution:
    def isValidDivisor(self, nums, threshold, divisor):
        quotientSum = 0
        
        for num in nums:
            quotientSum += int(ceil(num / divisor))
            if quotientSum > threshold:
                return False
        return True
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)
        smallestDivisor = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.isValidDivisor(nums, threshold, mid):
                smallestDivisor = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return smallestDivisor


if __name__ == '__main__':
    s = Solution()
    print(s.smallestDivisor([1,2,5,9], 6))
    print(s.smallestDivisor([44,22,33,11,1], 5))
    print(s.smallestDivisor([1,2,5,9,12], 6))