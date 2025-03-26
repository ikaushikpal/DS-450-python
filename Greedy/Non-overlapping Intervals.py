# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.


# Example 1:
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.


# Example 2:
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.


# Example 3:
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intuition is sort by start
        # if found overlapping interval then delete the longest one
        # cause longest one can overlap with other interval
        # long interval meaning who's end is higher 

        intervals.sort()
        
        p_end = intervals[0][1]
        count_deletes = 0

        for start, end in intervals[1:]:
            # no overlapping
            if start >= p_end:
                p_end = end
            else:
                # taking shorter end, greedily 
                p_end = min(p_end, end)
                count_deletes += 1
        return count_deletes
# TIme Complexity: O(NlogN)
# Space Complexity: o(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))
    print(sol.eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]]))
    print(sol.eraseOverlapIntervals(intervals = [[1,2],[2,3]]))