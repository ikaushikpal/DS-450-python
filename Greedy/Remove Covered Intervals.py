# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

# Return the number of remaining intervals.

# Example 1:

# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

# Example 2:

# Input: intervals = [[1,4],[2,3]]
# Output: 1


from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda key: (key[0], -key[1]))
        start, end = intervals[0]
        cntInBetween = 0
        
        for i in range(1, len(intervals)):
            newStart, newEnd = intervals[i] 
            if start<=newStart and newEnd<=end:
                cntInBetween += 1 
            else:
                start, end = newStart, newEnd
        
        return len(intervals) - cntInBetween


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeCoveredIntervals([[1,4],[3,6],[2,8]]))
    print(sol.removeCoveredIntervals([[1,4],[2,3]]))
    print(sol.removeCoveredIntervals([[1,4],[2,6],[3,5]]))