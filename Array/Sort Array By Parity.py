# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.

# Example 1:
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]

# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Example 2:
# Input: nums = [0]
# Output: [0]


from typing import List
import heapq
from functools import lru_cache
from collections import Counter, deque


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # idea is j and i two pointers pointing to first odd number and first unsolved number
        # -------------------------------------------------
        # even numbers | odd numbers | unsolved numbers
        # -------------------------------------------------
        #              |              |
        #              j              i
        
        # from [0, j-1] = all even numbers
        # from [j, i-1] = all odd numbers
        # from [i, n-1] = unsolved numbers

        # now we need to check if arr[i] is odd, then simply i++
        # meaning incrementing odd number segment 
        
        # else, swap(arr[i], arr[j]), why? because arr[j] is first odd number 
        # and i++, meaning incrementing even number segment 
        # and j++, meaning incrementing odd number segment 

        j = 0

        for i in range(len(nums)):
            if nums[i]%2: # number is odd
                # then do nothing 
                continue
            
            else: # number is even
                # swaping nums[i] and nums[j]
                nums[j], nums[i] = nums[i], nums[j]
                j += i # shifting odd segment
        
        return nums


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortArrayByParity([3,1,2,4]))
    print(sol.sortArrayByParity([0]))