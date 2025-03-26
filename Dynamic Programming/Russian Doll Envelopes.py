# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.
# One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.
# Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

# Note: You cannot rotate an envelope.



# Example 1:
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).



# Example 2:
# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1


from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # every envelope is a pair of (width, height)
        # exactly same question as Maximum Non-Overlapping Bridges
        # Sort the list of pairs in increasing order of width 
        envelopes.sort(key = lambda x: x[0])

        dp = [1] * len(envelopes)
        maxLength = 1

        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            maxLength = max(maxLength, dp[i])

        return maxLength
# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Optimal approach should be using LIS binary approach
# to convert O(n^2) to O(nlog(n))
# otherwise it will accept on leetcode


if __name__ == '__main__':
    sol = Solution()
    envelopes = [[5,4],[6,4],[6,7],[2,3]]
    print(sol.maxEnvelopes(envelopes))
    envelopes = [[1,1],[1,1],[1,1]]
    print(sol.maxEnvelopes(envelopes))