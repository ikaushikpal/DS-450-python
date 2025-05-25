# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

# Example 1:
# Input: intervals = [(0,40),(5,10),(15,20)]
# Output: 2
# Explanation:
# day1: (0,40)
# day2: (5,10),(15,20)

# Example 2:
# Input: intervals = [(4,9)]
# Output: 1
# Note:
# (0,8),(8,10) is not considered a conflict at 8

# Constraints:
# 0 <= intervals.length <= 500
# 0 <= intervals[i].start < intervals[i].end <= 1,000,000

# same as minimum no of platforms

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[int]) -> int:
        start = [interval[0] for interval in intervals]
        end = [interval[1] for interval in intervals]

        start.sort()
        end.sort()

        maximum_rooms = 0
        current = 0
        i = j = 0

        while i < len(start) and j < len(end):
            # if start is less than end then need one room
            # if room req then ++
            if start[i] < end[j]:
                i += 1
                current += 1
            else:
                # releasing room
                j += 1
                current -= 1
            maximum_rooms = max(maximum_rooms, current)
        return maximum_rooms
# Time Complexity: O(NlogN)
# Space Complexity: o(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minMeetingRooms(intervals = [(0,40),(5,10),(15,20)]))
    print(sol.minMeetingRooms(intervals = [(4,9)]))

            