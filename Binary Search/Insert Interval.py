# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        starts = [start for start, _ in intervals]
        ends = [end for _, end in intervals]
        newStart, newEnd = newInterval

        left = bisect_left(ends, newInterval[0])
        right = bisect_right(starts, newInterval[1])
        print(left, right)

        startIndex, endIndex = len(intervals), -1
        for i in range(max(0, left), min(right, len(intervals)-1)):
            if newStart <= intervals[i][0] and intervals[i][1] <= newEnd:
                startIndex = min(startIndex, i)

            elif intervals[i][1] > newEnd:
                newEnd = intervals[i][1]
                endIndex = max(endIndex, i)
                startIndex = min(startIndex, i)

            elif newStart > intervals[i][0]:
                newStart = intervals[i][0]
                endIndex = max(endIndex, i)
                startIndex = min(startIndex, i)

        return intervals[:startIndex] + [[newStart, newEnd]] + intervals[endIndex+1:]


if __name__ == '__main__':
    sol = Solution()
    print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]))
    print(sol.insert([[1,3],[6,9]], [2,5]))
        