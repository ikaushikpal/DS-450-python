# You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

# Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

 

# Example 1:
# Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4


# Example 2:
# Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2


from collections import defaultdict
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # first separating points based on their y coordinates
        # why y coordinates? we can also use x coordinates to separate points
        # but y coordinates is like level of points, so if any level is not containing at-least two points, then we can't form a rectangle
        # mainly segPoints is used to check if certain value is exist or not
        segPoints = defaultdict(set)
        for x, y in points:
            segPoints[y].add(x)

        # now check for rectangle
        minArea = float('inf')
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]

                # checking (x1, y1) and (x2, y2) are in diagonal of rectangle
                if x1 == x2 or y1 == y2:
                    continue

                # if yes then (x1, y2) and (x2, y1) also should exist in points
                if x1 in segPoints[y2] and x2 in segPoints[y1]:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    minArea = min(minArea, area)
        
        return minArea if minArea != float('inf') else 0
# TIme Complexity: O(n^2)
# Space Complexity: O(n)  


if __name__ == '__main__':
    sol = Solution()
    points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
    print(sol.minAreaRect(points))
    points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
    print(sol.minAreaRect(points))
    points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3],[1,4],[3,4]]
    print(sol.minAreaRect(points))