# A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

# Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

# You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

# You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

 
# Example 1:
# Input: mat = [[1,4],[3,2]]
# Output: [0,1]
# Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.


# Example 2:
# Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
# Output: [1,1]
# Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.


from typing import List


class Solution:
    def findMaxElement(self, arr):
        pos = 0
        for i in range(len(arr)):
            if arr[i] > arr[pos]:
                pos = i
        return pos
    
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        ROW, COLS = len(mat), len(mat[0])
        lowRow, highRow = 0, ROW - 1
        
        while lowRow <= highRow:
            midRow = (lowRow + highRow) // 2
            colPos = self.findMaxElement(mat[midRow])
            
            if ((midRow == 0 or mat[midRow][colPos] > mat[midRow-1][colPos])
                and 
                (midRow==ROW-1 or mat[midRow][colPos] > mat[midRow+1][colPos])):
                return (midRow, colPos)
            
            elif midRow > 0 and mat[midRow-1][colPos] > mat[midRow][colPos]:
                highRow = midRow - 1
            else:
                lowRow = midRow + 1
        
        # could not find peak
        return (-1, -1)


if __name__ == "__main__":
    mat = [[1,4],[3,2]]
    print(Solution().findPeakGrid(mat))
    mat = [[10,20,15],[21,30,14],[7,16,32]]
    print(Solution().findPeakGrid(mat))