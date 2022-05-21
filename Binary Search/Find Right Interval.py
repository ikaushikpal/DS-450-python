# You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

# The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

# Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

 

# Example 1:
# Input: intervals = [[1,2]]
# Output: [-1]
# Explanation: There is only one interval in the collection, so it outputs -1.


# Example 2:
# Input: intervals = [[3,4],[2,3],[1,2]]
# Output: [-1,0,1]
# Explanation: There is no right interval for [3,4].
# The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
# The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.


# Example 3:
# Input: intervals = [[1,4],[2,3],[3,4]]
# Output: [-1,2,-1]
# Explanation: There is no right interval for [1,4] and [3,4].
# The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.


from typing import List


class Solution:
    def findCeil(self, arr,  key):
        if key > arr[-1][0]:
            return -1

        low, high = 0, len(arr)-1
        res = -1

        while low <= high:
            mid = (low+high)//2

            if arr[mid][0] == key:
                return arr[mid][1]
            elif arr[mid][0] < key:
                low = mid + 1       
            else:
                res = arr[mid][1]
                high = mid - 1

        return res
    
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = [(interval[0], i) for i, interval in enumerate(intervals)]
        starts.sort()
        
        ans = []
        for _, end in intervals:
            minimumStart = self.findCeil(starts, end)
            ans.append(minimumStart)
        
        return ans


if __name__ == "__main__":
    intervals = [[1,4],[2,3],[3,4]]
    print(Solution().findRightInterval(intervals))
    intervals = [[1,2]]
    print(Solution().findRightInterval(intervals))
    intervals = [[3,4],[2,3],[1,2]]
    print(Solution().findRightInterval(intervals))