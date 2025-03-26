# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

# Return the maximum score you can get by erasing exactly one subarray.

# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 

# Example 1:
# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].


# Example 2:
# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window = set()
        maxSum = t = 0
        i = j = 0
        
        while j < len(nums):
            window.add(nums[j])
            t += nums[j]
            
            if len(window) != j-i+1:
                while nums[i] != nums[j]:
                    window.remove(nums[i])
                    t -= nums[i]
                    i += 1
                    
                t -= nums[i]
                i += 1
                
            maxSum = max(maxSum, t)
            j += 1
        return maxSum


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumUniqueSubarray([4,2,4,5,6]))
    print(sol.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))
    