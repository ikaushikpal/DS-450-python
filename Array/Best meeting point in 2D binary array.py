# You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in a group. And the group of two or more people wants to meet and minimize the total travel distance. They can meet anywhere means that there might be a home or not.

# The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x – p1.x| + |p2.y – p1.y|.
# Find the total distance that needs to be traveled to reach the best meeting point (Total distance traveled is minimum).

# Examples: 
 
# Input : grid[][] = [[1, 0, 0, 0, 1], 
#                    [0, 0, 0, 0, 0],
#                    [0, 0, 1, 0, 0]];
# Output : 6
# Best meeting point is (0, 2).
# Total distance traveled is 2 + 2 + 2 = 6

# Input : grid[3][5] = [[1, 0, 1, 0, 1],
#                      [0, 1, 0, 0, 0], 
#                      [0, 1, 1, 0, 0]];
# Output : 11



class Solution:
    def minTotalDistance(self, grid):
        xIndices, yIndices = [], []
        houseIndices = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # a house found
                    xIndices.append(i)
                    yIndices.append(j)
                    houseIndices.append((i, j))
        
        # finding median x, y
        xIndices.sort()
        yIndices.sort()

        mid = len(xIndices) // 2
        x, y = xIndices[mid], yIndices[mid]

        dist = 0
        for house in houseIndices:
            dist += abs(house[0] - x) + abs(house[1] - y)

        return dist


if __name__ == '__main__':
    sol = Solution()
    print(sol.minTotalDistance([[1, 0, 0, 0, 1], 
                                [0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 0]]))