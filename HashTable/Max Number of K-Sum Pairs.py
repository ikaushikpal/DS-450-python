# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

 

# Example 1:
# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.



# Example 2:
# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.


from collections import Counter
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        ans = 0
        
        for key in list(freq):
            req = k - key

            if req == key:
                minmumFreq = freq[key] // 2
            else:
                minmumFreq = min(freq[req], freq[key])
                freq[req] -= minmumFreq

            freq[key] -= minmumFreq
            ans += minmumFreq
        
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxOperations([1,2,3,4], 5))
    print(s.maxOperations([3,1,3,4,3], 6))
    print(s.maxOperations([1,1,1,1,1], 2))