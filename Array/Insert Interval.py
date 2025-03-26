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


from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # there are 3 possiblities
        
        # one: if newInterval is before of some interval
        # in that case append newInterval to result array 
        # and extend rest of the intervals to the array indexing from i
        
        # two: if newInterval is end of some interval
        # in that case append interval and proceed with loop
        
        # three: overlap
        # here we need to take minimize of interval.start and newInterval.start
        # and maximize of interval.end and newInterval.end
        # store that to newIntreval
        
        
        result = []
        for i, interval in enumerate(intervals):
            start, end = interval
            
            if start > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i : ]
            
            elif end < newInterval[0]:
                result.append(interval)
                
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        
        # if never case one occurred 
        # then adding newInterval
        result.append(newInterval)
        return result
# Time Complexity: O(n)
# Space Complexity: O(n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.insert([[1,3],[6,9]], [2,5]))
    print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
    