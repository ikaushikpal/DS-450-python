# Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

# A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:
# Input: arr = [1,2,3,4], difference = 1
# Output: 4
# Explanation: The longest arithmetic subsequence is [1,2,3,4].


# Example 2:
# Input: arr = [1,3,5,7], difference = 1
# Output: 1
# Explanation: The longest arithmetic subsequence is any single element.


# Example 3:
# Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
# Output: 4
# Explanation: The longest arithmetic subsequence is [7,5,3,1].


from collections import defaultdict
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # the main idea is that
        # ! what is the AP longest subsequence ending at arr[i] !
        # it is the longest subsequence ending at arr[i] - difference + 1


        # NOTE: here mentioned only subsequence not entire array
        # so ordering matters

        dp = defaultdict(int)
        maxSeq = 0
        
        for val in arr:
            # if previous value exist that means we can add this value to the sequence
            # and make it longer by 1
            dp[val] = dp[val - difference] + 1
            maxSeq = max(dp[val], maxSeq)
        return maxSeq
# TIme Complexity: O(n)
# Space Complexity: O(n)


if __name__ == "__main__":
    sol=Solution()
    print(sol.longestSubsequence([1,2,3,4],1))
    print(sol.longestSubsequence([4, 3, 2, 1],1))
    print(sol.longestSubsequence([1,3,5,7],1))
    print(sol.longestSubsequence([1,5,7,8,5,3,4,2,1],2))