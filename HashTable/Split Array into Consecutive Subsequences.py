# You are given an integer array nums that is sorted in non-decreasing order.

# Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

# Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
# All subsequences have a length of 3 or more.
# Return true if you can split nums according to the above conditions, or false otherwise.

# A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

 
# Example 1:
# Input: nums = [1,2,3,3,4,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,5] --> 1, 2, 3
# [1,2,3,3,4,5] --> 3, 4, 5


# Example 2:
# Input: nums = [1,2,3,3,4,4,5,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
# [1,2,3,3,4,4,5,5] --> 3, 4, 5


# Example 3:
# Input: nums = [1,2,3,4,4,5]
# Output: false
# Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.


from collections import Counter, defaultdict
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # Approach
        # We iterate through the array once to get the frequency of all the elements in the array
        # We iterate through the array once more and for each element we either see if it can be appended to a previously constructed consecutive sequence or if it can be the start of a new consecutive sequence. If neither are true, then we return false.
        freqMap = Counter(nums)
        hypoMap = defaultdict(int)
        
        for num in nums:
            # no more num left for pairing
            if freqMap[num] == 0:
                continue
            
            # checking if num is already paired with some sequence
            elif hypoMap[num] > 0:
                hypoMap[num] -= 1
                freqMap[num] -= 1
                hypoMap[num + 1] += 1
            
            # checking if num can start a new sequence
            elif freqMap[num + 1] > 0 and freqMap[num + 2] > 0:
                freqMap[num] -= 1
                freqMap[num + 1] -= 1
                freqMap[num + 2] -= 1
                hypoMap[num + 3] += 1
                
            else:
                return False
        return True
# Time complexity: O(n)
# Space complexity: O(n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPossible([1,2,3,3,4,5]))
    print(sol.isPossible([1,2,3,3,4,4,5,5]))
    print(sol.isPossible([1,2,3,4,4,5]))