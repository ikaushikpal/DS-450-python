# The frequency of an element is the number of times it occurs in an array.

# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

# Return the maximum possible frequency of an element after performing at most k operations.


# Example 1:
# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
# 4 has a frequency of 3.

# Example 2:
# Input: nums = [1,4,8,13], k = 5
# Output: 2
# Explanation: There are multiple optimal solutions:
# - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
# - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
# - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

# Example 3:
# Input: nums = [3,9,6], k = 2
# Output: 1


from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        # sliding window approach
        maxWindowSize = 1
        i = totalSum = 0
        
        for j in range(len(nums)):
            totalSum += nums[j]
            # what this "nums[j] * (j - i + 1) > totalSum + k" means
            # nums[j] denote the right element for which we are trying to find its max
            # possible frequency
            # (j - i + 1) is current window size
            # totalSum + k means how much elements we can add to our window
            
            # e.g.
            # [1, 1, 1, 2, 2, 4], k = 2
            #  i     j 
            # here  nums[j] * (j - i + 1) = 1 * 3 = 3
            #       totalSum + k = 3 + 2 = 5
            # 3 <= 5, True so current Window is valid, because [1, 1, 1] all 1's 
            
            # but [1, 1, 1, 2, 2, 4]
            #      i        j
            # here  nums[j] * (j - i + 1) = 2 * 4 = 8
            #       totalSum + k = 5 + 2 = 7
            # 8 <= 7, False so we need to shrink our window from left side
            
            
            while nums[j] * (j - i + 1) > totalSum + k:
                totalSum -= nums[i]
                i += 1
            maxWindowSize = max(maxWindowSize, j-i+1)
            
        return maxWindowSize


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxFrequency([1, 1, 1, 2, 2, 4], 2))
    print(sol.maxFrequency([3,9,6], 2))
