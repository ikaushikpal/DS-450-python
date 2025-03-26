# An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

# Given the grid grid represented as a string array, return the number of regions.

# Note that backslash characters are escaped, so a '\' is represented as '\\'.

 

# Example 1:
# Input: grid = [" /",
#               "/ "]
# Output: 2


# Example 2:
# Input: grid = [" /",
#               "  "]
# Output: 1
# Example 3:


# Input: grid = ["/\\",
#               "\\/"]
# Output: 5
# Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.


from typing import List


class Disjoint:
    def __init__(self, n=0):
        self.n = n
        self.array = [-1] * self.n

    def add(self):
        self.array.append(-1)
        self.n += 1

    def find(self, n):
        if self.array[n] < 0:
            return (n,  -self.array[n])
        result = self.find(self.array[n])
        self.array[n] = result[0]
        return result
    
    def union(self, set1, set2):
        parent_of_set1, rank_of_set1 = self.find(set1)
        parent_of_set2, rank_of_set2 = self.find(set2)

        if parent_of_set1 == parent_of_set2:
            return False

        if rank_of_set1 > rank_of_set2:
            self.array[parent_of_set1] += self.array[parent_of_set2]
            self.array[parent_of_set2] = parent_of_set1
            
        else:
            self.array[parent_of_set2] += self.array[parent_of_set1]
            self.array[parent_of_set1] = parent_of_set2
        return True

class Solution:
    def indexMap(self, i, j, char, ROWS, COLS):
        if char == ' ':
            return None, None

        i += 1
        j += 1

        if char == '/':
            r = i * COLS + j - 1
            c = (i-1) * COLS + j
            return r, c
        else:
            r = (i - 1) * COLS + j - 1
            c = i * COLS + j
            return r, c

    def regionsBySlashes(self, grid: List[str]) -> int:
        ROWS = len(grid) + 1
        COLS = len(grid[0]) + 1
        d = Disjoint(ROWS * COLS)
        regions = 0

        # first row
        for i in range(COLS-1):
            if not d.union(i, i+ 1):
                regions += 1
            
        # last row
        for i in range((ROWS-1)*COLS, ROWS*COLS-1):
            if not d.union(i, i+1):
                regions += 1
            
        # left column
        for i in range(0,(ROWS-1)*COLS,COLS):
            if not d.union(i, i+COLS):
                regions += 1
            
        # right column
        for i in range(COLS-1, (ROWS-1)*COLS, COLS):
            if not d.union(i, i+COLS):
                regions += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == ' ':
                    continue

                u, v = self.indexMap(i, j, grid[i][j], ROWS, COLS)
                if not d.union(u, v):
                    regions += 1

        return regions
# Time Complexity : O(N * M)
# Space Complexity : o(N * M)
# where N and M are the rows and cols of grid
# really really HARD question
# fully solved by me
# if grid is of 2x2
# then
# 0 - 1 - 2
# |   |   |
# 3 - 4 - 5 
# |   |   |
# 6 - 7 - 8


if __name__ == '__main__':
    sol = Solution()
    print(sol.regionsBySlashes([" /", "/ "]))
    print(sol.regionsBySlashes([" /","  "]))
    print(sol.regionsBySlashes(["/\\","\\/"]))