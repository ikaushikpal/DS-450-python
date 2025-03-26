# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.


# Example 1:
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true


# Example 2:
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false


from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(2, len(coordinates)):
            x1, y1 = coordinates[i - 2] # first point
            x2, y2 = coordinates[i - 1] # second point
            x3, y3 = coordinates[i]     # third point
            
            # slope of the line
            # (x2-x1)    (x3-x2)
            # ------- == --------
            # (y2-y1)     (y3-y2)

            # => (x2-x1) * (y3-y2) == (x3-x2) * (y2-y1)

            if (x2-x1) * (y3-y2)  != (x3-x2) * (y2-y1):
                return False
        return True
# Time complexity: O(N)
# Space complexity: O(1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkStraightLine(coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
    print(sol.checkStraightLine(coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
            