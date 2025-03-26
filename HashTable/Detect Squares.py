# You are given a stream of points on the X-Y plane. Design an algorithm that:

# Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
# Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
# An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

# Implement the DetectSquares class:

# DetectSquares() Initializes the object with an empty data structure.
# void add(int[] point) Adds a new point point = [x, y] to the data structure.
# int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.
 

# Example 1:


# Input
# ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
# [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
# Output
# [null, null, null, null, 1, 0, null, 2]

# Explanation
# DetectSquares detectSquares = new DetectSquares();
# detectSquares.add([3, 10]);
# detectSquares.add([11, 2]);
# detectSquares.add([3, 2]);
# detectSquares.count([11, 10]); // return 1. You can choose:
#                                //   - The first, second, and third points
# detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
# detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
# detectSquares.count([11, 10]); // return 2. You can choose:
#                                //   - The first, second, and third points
#                                //   - The first, third, and fourth points


from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.xMapMap = defaultdict(dict)
        self.xMapSet = defaultdict(set)
        
        self.yMapMap = defaultdict(dict)
        self.yMapSet = defaultdict(set)
        
    def add(self, point: List[int]) -> None:
        x, y = point
        
        self.xMapSet[x].add(y)
        if y not in self.xMapMap[x]:
            self.xMapMap[x][y] = 0
        self.xMapMap[x][y] += 1
        
        self.yMapSet[y].add(x)
        if x not in self.yMapMap[y]:
            self.yMapMap[y][x] = 0
        self.yMapMap[y][x] += 1
        
    def count(self, point: List[int]) -> int:
        ans = 0
        x, y = point

        XSet = set()
        for newX in self.xMapSet[x]:
            if y - newX > 0:
                XSet.add(y - newX)
        
        YSet = set()
        for newY in self.yMapMap[y]:
            if x - newY > 0:
                YSet.add(x - newY)

        commonPoints = XSet.intersection(YSet)
        for diff in commonPoints:
            pointA = (x, y-diff)
            pointB = (x-diff, y)
            
            pointAFreq = self.xMapMap[pointA[0]][pointA[1]]
            pointBFreq = self.yMapMap[pointB[1]][pointB[0]]
            
            pointC = (x-diff, y-diff)
            pointCFreq = 0
            
            if pointC[1] in self.xMapSet[pointC[0]]:
                pointCFreq = self.xMapMap[pointC[0]][pointC[1]]
            
            ans += pointAFreq * pointBFreq * pointCFreq
        return ans
    
    

if __name__ == '__main__':
    detectSquares = DetectSquares()
    detectSquares.add([3, 10])
    detectSquares.add([11, 2])
    detectSquares.add([3, 2])
    print(detectSquares.count([11, 10])) # return 1. You can choose:
    print(detectSquares.count([14, 8]))  # return 0. The query point cannot form a square with any points in the data structure.
    detectSquares.add([11, 2])    # Adding duplicate points is allowed.
    print(detectSquares.count([11, 10])) # return 2. You can choose:
    #                                //   - The first, second, and third points
    #                                //   - The first, third, and fourth points
