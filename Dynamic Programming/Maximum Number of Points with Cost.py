# You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

# To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

# However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

# Return the maximum number of points you can achieve.

# abs(x) is defined as:

# x for x >= 0.
# -x for x < 0.
 

# Example 1:
# Input: points = [[1,2,3],[1,5,1],[3,1,1]]
# Output: 9
# Explanation:
# The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
# You add 3 + 5 + 3 = 11 to your score.
# However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
# Your final score is 11 - 2 = 9.


# Example 2:
# Input: points = [[1,5],[2,3],[4,2]]
# Output: 11
# Explanation:
# The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
# You add 5 + 3 + 4 = 12 to your score.
# However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
# Your final score is 12 - 1 = 11.


from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        M, N = len(points), len(points[0])
        
        currRow = points[-1]
        prevRow = [float('-inf')] * N
        
        for i in range(M-2, -1, -1):
            currRow, prevRow = prevRow, currRow
            
            for j in range(N - 1, -1, -1):
                currRow[j] = float('-inf')
                
                for k in range(N-1, -1, -1):
                    currRow[j] = max(currRow[j], prevRow[k] - abs(k - j))
                currRow[j] += points[i][j]
        return max(currRow)
# Time Complexity: O(M * N * N)
# Space Complexity: O(N)

# VISIT
# https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344888/C++-dp-from-O(m-*-n-*-n)-to-O(m-*-n)/1014241


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        M, N = len(points), len(points[0])
        
        currRow = points[-1].copy()
        prevRow = [float('-inf')] * N
        
        for i in range(M-2, -1, -1):
            prevRow = currRow

            # left to right
            left = [float('-inf')] * N
            left[0] = prevRow[0]
            for k in range(1, N):
                left[k] = max(prevRow[k], left[k - 1] - 1)
            
            # right to left
            right = [float('-inf')] * N
            right[-1] = prevRow[-1]
            for k in range(N-2, -1, -1):
                right[k] = max(prevRow[k], right[k + 1] - 1)

            for j in range(N):
                currRow[j] = max(left[j], right[j]) + points[i][j]
        return max(currRow)
# Time Complexity: O(M * N)
# Space Complexity: O(N)    


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxPoints(points = [[1,2,3],[1,5,1],[3,1,1]]))
    print(sol.maxPoints(points = [[1,5],[2,3],[4,2]]))