# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

# Example 1:
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

# Example 2:
# Input: s = "eccbbbbdec"
# Output: [10]


# Constraints:
# 1 <= s.length <= 500
# s consists of lowercase English letters.

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # converted this problem to intervals one
        locs = {}

        for i, char in enumerate(s):
            if char not in locs:
                locs[char] = [i, i]
            else:
                start, end = locs[char]
                locs[char] = [start, i]

        intervals = [tuple(interval) for interval in locs.values()]

        ans = []
        prev_start = prev_end = -1

        for start, end in intervals:
            if start > prev_end:
                ans.append(prev_end - prev_start + 1)
                prev_start, prev_end = start, end
            else:
                prev_start = min(start, prev_start)
                prev_end = max(end, prev_end)
        ans.append(prev_end - prev_start + 1)

        return ans[1:]


# Time complexity: O(N)
# Space Complexity: O(N)


if __name__ == "__main__":
    sol = Solution()
    print(sol.partitionLabels("ababcbacadefegdehijhklij"))
    print(sol.partitionLabels("eccbbbbdec"))
